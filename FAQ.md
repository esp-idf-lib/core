# FAQ

* [How to debug I2C-based drivers?](#how-to-debug-i2c-based-drivers)
* [Why are semaphores (mutexes) used in i2cdev routines?](#why-are-semaphores-mutexes-used-in-i2cdev-routines)
* [How can I connect multiple I2C devices?](#how-can-i-connect-multiple-i2c-devices)
* [How do I use an i2cdev driver together with a third-party I2C driver?](#how-do-i-use-an-i2cdev-driver-together-with-a-third-party-i2c-driver)
* [When is the I2C bus created and destroyed?](#when-is-the-i2c-bus-created-and-destroyed)
* [Why does a driver return ESP_ERR_INVALID_STATE?](#why-does-a-driver-return-esp_err_invalid_state)
* [How can I change frequency of I2C clock? At default frequency my device is unstable or not working at all.](#how-can-i-change-frequency-of-i2c-clock-at-default-frequency-my-device-is-unstable-or-not-working-at-all)
* [Can I mix devices with different clock speeds or 10-bit addresses on one bus?](#can-i-mix-devices-with-different-clock-speeds-or-10-bit-addresses-on-one-bus)
* [How to use internal pull-up resistors](#how-to-use-internal-pull-up-resistors)
* [Can I use I2C device drivers from interrupts?](#can-i-use-i2c-device-drivers-from-interrupts)
* [Porting I2C libs to I2Cdev](#porting-i2c-libs-to-i2cdev)
* [My DHT sensor doesn't work well/doesn't work at all](#my-dht-sensor-doesnt-work-welldoesnt-work-at-all)
* [How can I include ets_sys.h in my code without complex macros and remain compatible with different targets?](#how-can-i-include-ets_sysh-in-my-code-without-complex-macros-and-remain-compatible-with-different-targets)

## How to debug I2C-based drivers?

Common causes of I2C issues are:

* wrong wiring
* wrong pull-up resistors
* wrong I2C address
* broken I2C module
* the driver has a bug

When any of I2C-based drivers does not work, follow the steps below.

Build an [_I2C scanner_
device](https://github.com/esp-idf-lib/i2cdev/tree/main/examples/default).
The device is not necessarily an ESP device. There are many examples for
various platforms. Search by keyword `i2c scanner`.

Connect the I2C module to the I2C scanner device. Make sure appropriate
pull-up resistors are connected to `SCL` and `SDA` lines.

Scan devices on the I2C bus. If the scanner does not find the I2C device, then
your wiring might have issues. If the scanner finds the I2C device, make sure
the address found is what the driver expects. If you have more than one same
I2C modules, try them all.

If the scanner finds the I2C device and you are sure that the wiring is
correct, see the signals on the wire using an oscilloscope. Most oscilloscopes
can decode I2C signals and display I2C transactions in human-readable way.

If the driver does not work after these steps, please [let us
know](https://github.com/esp-idf-lib/core/issues). If the problem is clearly
in one driver, open an issue in the repository of that component instead.

## Why are semaphores (mutexes) used in i2cdev routines?

i2cdev uses two kinds of mutexes.

The port mutex, one per I2C port number (`I2C_NUM_MAX` of them, which can be
two or three depending on the target), protects the bus lifecycle: creating the
bus, adding and removing device handles, and tearing the bus down in
`i2cdev_done()`. Actual transactions on the bus are serialised by the ESP-IDF
I2C driver itself, not by i2cdev.

The second kind is a per-device mutex created by `i2c_dev_create_mutex()`. It is
needed when the same device is used from several tasks, and it also protects
operations that require several transactions in a row (`i2c_dev_read_reg()`,
`i2c_dev_write_reg()` and driver-level sequences):

```C
static i2c_dev_t some_dev;

void task1(void *arg)
{
     // some_dev used here
}

void task2(void *arg)
{
     // and here some_dev used too
}

...

xTaskCreate(task1, "task1", ....);
xTaskCreate(task2, "task2", ....);
```

Wrap such sequences with `I2C_DEV_TAKE_MUTEX()` and `I2C_DEV_GIVE_MUTEX()`, and
create the mutex with `i2c_dev_create_mutex()` before the first operation.

With `CONFIG_I2CDEV_NOLOCK=y` the per-device mutexes are not created at all and
none of this is protected. The port mutex and the bus lifecycle still work.

## How can I connect multiple I2C devices?

With i2cdev, you can use both I2C ports of the chip, and any device on them.

For example, in the case of using SSD1306 and two MCP3428s, I would recommend
connecting them like this:

* 2 GPIO outputs on ESP32 for dedicated screen connection via I2C bus 0
* 2 GPIO outputs to the second I2C bus, to which 2 MCP3428 are connected with
  different addresses.

Unlike the legacy driver, the `i2c_master` based driver binds an I2C port to one
pair of pins, and this binding cannot be changed while the bus exists: an
attempt to use the same port with another pair of pins returns
`ESP_ERR_INVALID_STATE`. If you need more devices than free ports allow, use an
I2C multiplexer such as `tca9548` or `tca6424a`, or put the devices on separate
ports.

## How do I use an i2cdev driver together with a third-party I2C driver?

Both can share one bus. i2cdev owns the bus handle, and a third-party component
adds its own device to that bus with `i2cdev_get_shared_handle()`:

```C
#include <i2cdev.h>
#include <bmp180.h>
#include <esp_lcd_panel_io.h>
#include <esp_lcd_panel_io_i2c.h>

#define I2C_PORT    I2C_NUM_0
#define I2C_SDA     GPIO_NUM_21
#define I2C_SCL     GPIO_NUM_22

static i2c_dev_t bmp;

void app_main(void)
{
    i2c_master_bus_handle_t bus_handle = NULL;
    esp_lcd_panel_io_handle_t io_handle = NULL;
    esp_lcd_panel_io_i2c_config_t io_config = {
        .dev_addr = 0x3c,             // SSD1306
        .scl_speed_hz = 400000,
        .control_phase_bytes = 1,
        .dc_bit_offset = 6,
        .lcd_cmd_bits = 8,
        .lcd_param_bits = 8,
    };

    ESP_ERROR_CHECK(i2cdev_init());

    // Our driver on port 0
    ESP_ERROR_CHECK(bmp180_init_desc(&bmp, I2C_PORT, I2C_SDA, I2C_SCL));
    ESP_ERROR_CHECK(bmp180_init(&bmp));

    // The bus exists only after the first real transaction, so ask for the
    // handle after bmp180_init(), not right after i2cdev_init()
    ESP_ERROR_CHECK(i2cdev_get_shared_handle(I2C_PORT, (void **)&bus_handle));

    // Third-party device on the same bus
    ESP_ERROR_CHECK(esp_lcd_new_panel_io_i2c(bus_handle, &io_config, &io_handle));

    // ... both can be used from any task
    // ...

    // Cleanup in the reverse order: the external device first, because
    // i2cdev_done() cannot delete a bus with devices still attached
    ESP_ERROR_CHECK(esp_lcd_panel_io_del(io_handle));
    ESP_ERROR_CHECK(bmp180_free_desc(&bmp));
    ESP_ERROR_CHECK(i2cdev_done());
}
```

Add `esp_lcd` (and `esp_driver_i2c`) to the component requirements of your
project. The transaction-level lock of the ESP-IDF driver keeps the two devices
from colliding on the wire, but it does not protect a device handle from
concurrent use: take `I2C_DEV_TAKE_MUTEX()` around i2cdev devices used from
several tasks, and do the same for the third-party driver if it does not lock
internally. Note that i2cdev knows nothing about devices added by other
components, so removing them stays your job.

## When is the I2C bus created and destroyed?

Lazily. `i2cdev_init()` only creates the port mutexes; the bus itself is created
by the first operation on that port (a read, write or probe), and the device
handle is created on the first transaction with a particular device.

The bus lives until `i2cdev_done()`, even if all devices have been removed with
`i2c_dev_delete_mutex()`. This is deliberate: the bus handle may have been handed
out with `i2cdev_get_shared_handle()`, and i2cdev cannot see the devices added by
other components.

`i2cdev_done()` removes the devices it knows about and deletes the bus. If some
device is still attached or cannot be removed, the port is left as is and the
function returns an error, so a repeated call can retry the cleanup.

## Why does a driver return ESP_ERR_INVALID_STATE?

The usual reasons:

* `i2cdev_init()` has not been called, so the port mutex does not exist yet;
* the port already has a bus created with a different pair of pins, and the
  driver was given another pair;
* the device descriptor is used after `i2cdev_done()` or after
  `i2c_dev_delete_mutex()`.

`ESP_ERR_INVALID_ARG` usually means a bad argument: a port outside
`0 .. I2C_NUM_MAX-1`, a NULL pointer, or the same GPIO for SDA and SCL.

## How can I change frequency of I2C clock? At default frequency my device is unstable or not working at all.

You can change the frequency after initializing the device handler, like this:

```C
#include <ads111x.h>

...

ESP_ERROR_CHECK(ads111x_init_desc(&dev, addr, I2C_PORT, SDA_GPIO, SCL_GPIO));

dev.cfg.master.clk_speed = 100000; // Hz

ESP_ERROR_CHECK(ads111x_set_mode(&dev, ADS111X_MODE_CONTINUOUS));    // Continuous conversion mode
ESP_ERROR_CHECK(ads111x_set_data_rate(&dev, ADS111X_DATA_RATE_32)); // 32 samples per second
...
```

Set the speed before the first transaction with the device. `clk_speed` equal to
zero means 400 kHz, and the library prints a warning about it.

With the legacy driver the clock speed belongs to the whole bus. With the
`i2c_master` based driver it belongs to the device, so on one bus you can keep a
BMP180 at 1 MHz and a PCF8574 at 100 kHz.

## Can I mix devices with different clock speeds or 10-bit addresses on one bus?

Yes for clock speeds, see above. 10-bit addressing is supported only on targets
where `SOC_I2C_SUPPORT_10BIT_ADDR` is set; elsewhere `addr_bit_len` is forced to
7 bit and the library prints a warning. The legacy driver does not support 10-bit
addresses at all.

## How to use internal pull-up resistors

Enable them in `i2c_dev_t` config. For example:

```C
...

dev.cfg.scl_pullup_en = true;
dev.cfg.sda_pullup_en = true;
ESP_ERROR_CHECK(ads111x_init_desc(&dev, addr, I2C_PORT, SDA_GPIO, SCL_GPIO));

...
```

The pull-ups are applied when the bus is created, that is on the first operation
with any device on that port. You can enable just one of the two lines. With
`CONFIG_I2CDEV_AUTO_ENABLE_PULLUPS=y` they are enabled automatically when neither
is requested.

Keep in mind that the internal pull-ups are about 45 kOhm, which is too weak for
I2C in most cases: use external 4.7 kOhm resistors.

## Can I use I2C device drivers from interrupts?

No. The drivers are not ISR-safe, and `CONFIG_I2CDEV_NOLOCK` does not change
that: it removes only the per-device mutexes, while the port mutex, the bus setup
and the blocking ESP-IDF I2C calls remain.

If you need to react to an interrupt, notify a task with `xTaskNotifyFromISR()`
and do the I2C work there.

## Porting I2C libs to I2Cdev

Start from the
[`template-component`](https://github.com/esp-idf-lib/template-component)
repository and follow [CONTRIBUTING.md](CONTRIBUTING.md). The API of `i2cdev` is
documented in [its header](https://github.com/esp-idf-lib/i2cdev/blob/main/i2cdev.h).

## My DHT sensor doesn't work well/doesn't work at all

1. Check if the sensor is connected correctly.
2. Use an external 4k7 pullup resistor! With an internal pullup resistor, operation will be unstable, if at all. The `dht` example has `CONFIG_EXAMPLE_INTERNAL_PULLUP=n` by default for this reason.
3. Shorten the wires that connect the sensor.
4. Use 5V for powering the sensor, not 3.3V. ESP chips are 5V tolerant.
5. Use shielded wires where the shield is connected to the GND.

This is about the bit-banging `dht` driver, not about `i2cdev`.

## How can I include ets_sys.h in my code without complex macros and remain compatible with different targets?

Add the `esp_idf_lib_helpers` component to the list of required ones, and after
that you can simply write `#include <ets_sys.h>` in your code. See, for example,
the source code of the `scd30` component.

`ets_delay_us()` is a legacy ROM symbol: IDF documents `esp_rom_delay_us()` from
`<esp_rom_sys.h>` instead, and since `esp_idf_lib_helpers` 1.4.2 the shim maps
`ets_delay_us()` to it. New code should call `esp_rom_delay_us()` directly.
