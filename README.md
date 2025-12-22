# The core repository of `esp-idf-lib`

This is the core repository of [esp-idf-lib](https://github.com/esp-idf-lib/). The organization is the successor of [UncleRus/esp-idf-lib](https://github.com/UncleRus/esp-idf-lib).

> [!NOTE]
>
> When migrating from [UncleRus/esp-idf-lib](https://github.com/UncleRus/esp-idf-lib) do not add this repository as a dependency.
> Instead, add individual components as [ESP-IDF components](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-component-manager.html) in your `idf_component.yml`.
> You can find all components on the [ESP Component Registry](https://components.espressif.com/components?q=namespace%3Aesp-idf-lib).

## Supported versions of frameworks and devices

| Chip     | Framework        | Versions                                                                                                                                         |
| -------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| ESP32-xx | ESP-IDF          | All officially supported versions (see [Support Period Policy](https://github.com/espressif/esp-idf/blob/master/SUPPORT_POLICY.md)) and `master` |

## Purpose

The purpose of [esp-idf-lib/core](https://github.com/esp-idf-lib/core) is:

* Documenting common policies and rules
* Discussions about our components
* Linking all the components and their [status](https://esp-idf-lib.github.io/core/status.html)

## Reporting issues in our component

When the issue is bug in the component, please open an Issue in the component
repository.

## Questions or discussions

For questions or discussions, use [discussions](https://github.com/esp-idf-lib/core/discussions) in this
repository.

## Documentation

- [How to contribute to `esp-idf-lib`](https://github.com/esp-idf-lib/core/blob/main/CONTRIBUTING.md)
- [Frequently asked questions](https://github.com/esp-idf-lib/core/blob/main/FAQ.md)

## Requesting new driver

TBW

## Components

Components for Espressif ESP32 [ESP-IDF framework](https://github.com/espressif/esp-idf)
and [ESP8266 RTOS SDK](https://github.com/espressif/ESP8266_RTOS_SDK).

Part of them ported from [esp-open-rtos](https://github.com/SuperHouse/esp-open-rtos).

### ADC/DAC libraries

| Name | Description |
|------|-------------|
| [ads111x](https://github.com/esp-idf-lib/ads111x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ads111x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ads111x) | Driver for ADS1113/ADS1114/ADS1115 and ADS1013/ADS1014/ADS1015 I2C ADC ([Documentation](https://esp-idf-lib.github.io/ads111x)) |
| [ads130e08](https://github.com/esp-idf-lib/ads130e08) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ads130e08/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ads130e08) | Driver for ADS130E08 ADC ([Documentation](https://esp-idf-lib.github.io/ads130e08)) |
| [hx711](https://github.com/esp-idf-lib/hx711) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/hx711/badge.svg)](https://components.espressif.com/components/esp-idf-lib/hx711) | Driver for HX711 24-bit ADC for weigh scales ([Documentation](https://esp-idf-lib.github.io/hx711)) |
| [mcp342x](https://github.com/esp-idf-lib/mcp342x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/mcp342x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/mcp342x) | Driver for 18-Bit, delta-sigma ADC MCP3426/MCP3427/MCP3428 ([Documentation](https://esp-idf-lib.github.io/mcp342x)) |
| [mcp4725](https://github.com/esp-idf-lib/mcp4725) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/mcp4725/badge.svg)](https://components.espressif.com/components/esp-idf-lib/mcp4725) | Driver for 12-bit DAC MCP4725 ([Documentation](https://esp-idf-lib.github.io/mcp4725)) |
| [pcf8591](https://github.com/esp-idf-lib/pcf8591) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/pcf8591/badge.svg)](https://components.espressif.com/components/esp-idf-lib/pcf8591) | Driver for 8-bit ADC and an 8-bit DAC PCF8591 ([Documentation](https://esp-idf-lib.github.io/pcf8591)) |
| [sgm58031](https://github.com/esp-idf-lib/sgm58031) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/sgm58031/badge.svg)](https://components.espressif.com/components/esp-idf-lib/sgm58031) | Driver for SGM58031 16-bit I2C ADC ([Documentation](https://esp-idf-lib.github.io/sgm58031)) |

### Common libraries

| Name | Description |
|------|-------------|
| [bmi160](https://github.com/esp-idf-lib/bmi160) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/bmi160/badge.svg)](https://components.espressif.com/components/esp-idf-lib/bmi160) | A template for esp-idf-lib component ([Documentation](https://esp-idf-lib.github.io/bmi160)) |
| [calibration](https://github.com/esp-idf-lib/calibration) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/calibration/badge.svg)](https://components.espressif.com/components/esp-idf-lib/calibration) | Multi-point calibration library ([Documentation](https://esp-idf-lib.github.io/calibration)) |
| [color](https://github.com/esp-idf-lib/color) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/color/badge.svg)](https://components.espressif.com/components/esp-idf-lib/color) | Common library for RGB and HSV colors ([Documentation](https://esp-idf-lib.github.io/color)) |
| [esp_idf_lib_helpers](https://github.com/esp-idf-lib/esp_idf_lib_helpers) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/esp_idf_lib_helpers/badge.svg)](https://components.espressif.com/components/esp-idf-lib/esp_idf_lib_helpers) | Common support library for esp-idf-lib ([Documentation](https://esp-idf-lib.github.io/esp_idf_lib_helpers)) |
| [framebuffer](https://github.com/esp-idf-lib/framebuffer) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/framebuffer/badge.svg)](https://components.espressif.com/components/esp-idf-lib/framebuffer) | RGB framebuffer component ([Documentation](https://esp-idf-lib.github.io/framebuffer)) |
| [i2cdev](https://github.com/esp-idf-lib/i2cdev) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/i2cdev/badge.svg)](https://components.espressif.com/components/esp-idf-lib/i2cdev) | ESP-IDF I2C master thread-safe utilities ([Documentation](https://esp-idf-lib.github.io/i2cdev)) |
| [lib8tion](https://github.com/esp-idf-lib/lib8tion) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/lib8tion/badge.svg)](https://components.espressif.com/components/esp-idf-lib/lib8tion) | Math functions specifically designed for LED programming ([Documentation](https://esp-idf-lib.github.io/lib8tion)) |
| [noise](https://github.com/esp-idf-lib/noise) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/noise/badge.svg)](https://components.espressif.com/components/esp-idf-lib/noise) | Noise generation functions ([Documentation](https://esp-idf-lib.github.io/noise)) |
| [onewire](https://github.com/esp-idf-lib/onewire) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/onewire/badge.svg)](https://components.espressif.com/components/esp-idf-lib/onewire) | Bit-banging 1-Wire driver ([Documentation](https://esp-idf-lib.github.io/onewire)) |

### Real-time clocks

| Name | Description |
|------|-------------|
| [ds1302](https://github.com/esp-idf-lib/ds1302) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ds1302/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ds1302) | Driver for DS1302 RTC module ([Documentation](https://esp-idf-lib.github.io/ds1302)) |
| [ds1307](https://github.com/esp-idf-lib/ds1307) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ds1307/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ds1307) | Driver for DS1307 RTC module ([Documentation](https://esp-idf-lib.github.io/ds1307)) |
| [ds3231](https://github.com/esp-idf-lib/ds3231) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ds3231/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ds3231) | Driver for DS1337 RTC and DS3231 high precision RTC module ([Documentation](https://esp-idf-lib.github.io/ds3231)) |
| [pcf8563](https://github.com/esp-idf-lib/pcf8563) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/pcf8563/badge.svg)](https://components.espressif.com/components/esp-idf-lib/pcf8563) | Driver for PCF8563 (BM8563) real-time clock/calendar ([Documentation](https://esp-idf-lib.github.io/pcf8563)) |

### Humidity sensors

| Name | Description |
|------|-------------|
| [aht](https://github.com/esp-idf-lib/aht) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/aht/badge.svg)](https://components.espressif.com/components/esp-idf-lib/aht) | Driver for AHT10/AHT15/AHT20 temperature and humidity sensor ([Documentation](https://esp-idf-lib.github.io/aht)) |
| [am2320](https://github.com/esp-idf-lib/am2320) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/am2320/badge.svg)](https://components.espressif.com/components/esp-idf-lib/am2320) | Driver for AM2320 temperature and humidity sensor (I2C) ([Documentation](https://esp-idf-lib.github.io/am2320)) |
| [bme680](https://github.com/esp-idf-lib/bme680) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/bme680/badge.svg)](https://components.espressif.com/components/esp-idf-lib/bme680) | Driver for BME680 digital environmental sensor ([Documentation](https://esp-idf-lib.github.io/bme680)) |
| [dht](https://github.com/esp-idf-lib/dht) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/dht/badge.svg)](https://components.espressif.com/components/esp-idf-lib/dht) | Driver for DHT11, AM2301 (DHT21, DHT22, AM2302, AM2321), Itead Si7021 ([Documentation](https://esp-idf-lib.github.io/dht)) |
| [hdc1000](https://github.com/esp-idf-lib/hdc1000) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/hdc1000/badge.svg)](https://components.espressif.com/components/esp-idf-lib/hdc1000) | Driver for HDC1000 temperature and humidity sensor ([Documentation](https://esp-idf-lib.github.io/hdc1000)) |
| [hts221](https://github.com/esp-idf-lib/hts221) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/hts221/badge.svg)](https://components.espressif.com/components/esp-idf-lib/hts221) | Driver for HTS221 temperature and humidity sensor ([Documentation](https://esp-idf-lib.github.io/hts221)) |
| [sfa3x](https://github.com/esp-idf-lib/sfa3x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/sfa3x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/sfa3x) | Driver for SFA30 formaldehyde detection module (I2C) ([Documentation](https://esp-idf-lib.github.io/sfa3x)) |
| [sht3x](https://github.com/esp-idf-lib/sht3x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/sht3x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/sht3x) | Driver for Sensirion SHT30/SHT31/SHT35 digital temperature and humidity sensor ([Documentation](https://esp-idf-lib.github.io/sht3x)) |
| [sht4x](https://github.com/esp-idf-lib/sht4x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/sht4x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/sht4x) | Driver for Sensirion SHT40/SHT41/SHT45 digital temperature and humidity sensor ([Documentation](https://esp-idf-lib.github.io/sht4x)) |
| [si7021](https://github.com/esp-idf-lib/si7021) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/si7021/badge.svg)](https://components.espressif.com/components/esp-idf-lib/si7021) | Driver for Si7013/Si7020/Si7021/HTU2xD/SHT2x and compatible temperature and humidity sensors ([Documentation](https://esp-idf-lib.github.io/si7021)) |

### Temperature sensors

| Name | Description |
|------|-------------|
| [aht](https://github.com/esp-idf-lib/aht) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/aht/badge.svg)](https://components.espressif.com/components/esp-idf-lib/aht) | Driver for AHT10/AHT15/AHT20 temperature and humidity sensor ([Documentation](https://esp-idf-lib.github.io/aht)) |
| [am2320](https://github.com/esp-idf-lib/am2320) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/am2320/badge.svg)](https://components.espressif.com/components/esp-idf-lib/am2320) | Driver for AM2320 temperature and humidity sensor (I2C) ([Documentation](https://esp-idf-lib.github.io/am2320)) |
| [bh1900nux](https://github.com/esp-idf-lib/bh1900nux) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/bh1900nux/badge.svg)](https://components.espressif.com/components/esp-idf-lib/bh1900nux) | Driver for BH1900NUX temperature sensor ([Documentation](https://esp-idf-lib.github.io/bh1900nux)) |
| [bme680](https://github.com/esp-idf-lib/bme680) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/bme680/badge.svg)](https://components.espressif.com/components/esp-idf-lib/bme680) | Driver for BME680 digital environmental sensor ([Documentation](https://esp-idf-lib.github.io/bme680)) |
| [bmp180](https://github.com/esp-idf-lib/bmp180) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/bmp180/badge.svg)](https://components.espressif.com/components/esp-idf-lib/bmp180) | Driver for BMP180 digital pressure sensor ([Documentation](https://esp-idf-lib.github.io/bmp180)) |
| [bmp280](https://github.com/esp-idf-lib/bmp280) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/bmp280/badge.svg)](https://components.espressif.com/components/esp-idf-lib/bmp280) | Driver for BMP280/BME280 digital pressure sensor ([Documentation](https://esp-idf-lib.github.io/bmp280)) |
| [dht](https://github.com/esp-idf-lib/dht) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/dht/badge.svg)](https://components.espressif.com/components/esp-idf-lib/dht) | Driver for DHT11, AM2301 (DHT21, DHT22, AM2302, AM2321), Itead Si7021 ([Documentation](https://esp-idf-lib.github.io/dht)) |
| [dps310](https://github.com/esp-idf-lib/dps310) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/dps310/badge.svg)](https://components.espressif.com/components/esp-idf-lib/dps310) | Driver for DPS310 barometric pressure sensor ([Documentation](https://esp-idf-lib.github.io/dps310)) |
| [ds18x20](https://github.com/esp-idf-lib/ds18x20) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ds18x20/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ds18x20) | Driver for DS18B20/DS18S20 families of 1-Wire temperature sensor ICs ([Documentation](https://esp-idf-lib.github.io/ds18x20)) |
| [hdc1000](https://github.com/esp-idf-lib/hdc1000) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/hdc1000/badge.svg)](https://components.espressif.com/components/esp-idf-lib/hdc1000) | Driver for HDC1000 temperature and humidity sensor ([Documentation](https://esp-idf-lib.github.io/hdc1000)) |
| [hts221](https://github.com/esp-idf-lib/hts221) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/hts221/badge.svg)](https://components.espressif.com/components/esp-idf-lib/hts221) | Driver for HTS221 temperature and humidity sensor ([Documentation](https://esp-idf-lib.github.io/hts221)) |
| [lm75](https://github.com/esp-idf-lib/lm75) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/lm75/badge.svg)](https://components.espressif.com/components/esp-idf-lib/lm75) | Driver for LM75, a digital temperature sensor and thermal watchdog ([Documentation](https://esp-idf-lib.github.io/lm75)) |
| [max31725](https://github.com/esp-idf-lib/max31725) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/max31725/badge.svg)](https://components.espressif.com/components/esp-idf-lib/max31725) | Driver for MAX31725/MAX31726 temperature sensors ([Documentation](https://esp-idf-lib.github.io/max31725)) |
| [max31855](https://github.com/esp-idf-lib/max31855) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/max31855/badge.svg)](https://components.espressif.com/components/esp-idf-lib/max31855) | Driver for MAX31855 cold-junction compensated thermocouple-to-digital converter ([Documentation](https://esp-idf-lib.github.io/max31855)) |
| [max31865](https://github.com/esp-idf-lib/max31865) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/max31865/badge.svg)](https://components.espressif.com/components/esp-idf-lib/max31865) | Driver for MAX31865 resistance converter for platinum RTDs ([Documentation](https://esp-idf-lib.github.io/max31865)) |
| [mcp960x](https://github.com/esp-idf-lib/mcp960x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/mcp960x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/mcp960x) | Driver for MCP9600/MCP9601, thermocouple EMF to temperature converter ([Documentation](https://esp-idf-lib.github.io/mcp960x)) |
| [mcp9808](https://github.com/esp-idf-lib/mcp9808) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/mcp9808/badge.svg)](https://components.espressif.com/components/esp-idf-lib/mcp9808) | Driver for MCP9808 digital temperature sensor ([Documentation](https://esp-idf-lib.github.io/mcp9808)) |
| [ms5611](https://github.com/esp-idf-lib/ms5611) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ms5611/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ms5611) | Driver for barometic pressure sensor MS5611-01BA03 ([Documentation](https://esp-idf-lib.github.io/ms5611)) |
| [qmp6988](https://github.com/esp-idf-lib/qmp6988) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/qmp6988/badge.svg)](https://components.espressif.com/components/esp-idf-lib/qmp6988) | Driver for QMP6988 digital temperature and pressure sensor ([Documentation](https://esp-idf-lib.github.io/qmp6988)) |
| [sfa3x](https://github.com/esp-idf-lib/sfa3x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/sfa3x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/sfa3x) | Driver for SFA30 formaldehyde detection module (I2C) ([Documentation](https://esp-idf-lib.github.io/sfa3x)) |
| [sht3x](https://github.com/esp-idf-lib/sht3x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/sht3x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/sht3x) | Driver for Sensirion SHT30/SHT31/SHT35 digital temperature and humidity sensor ([Documentation](https://esp-idf-lib.github.io/sht3x)) |
| [sht4x](https://github.com/esp-idf-lib/sht4x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/sht4x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/sht4x) | Driver for Sensirion SHT40/SHT41/SHT45 digital temperature and humidity sensor ([Documentation](https://esp-idf-lib.github.io/sht4x)) |
| [si7021](https://github.com/esp-idf-lib/si7021) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/si7021/badge.svg)](https://components.espressif.com/components/esp-idf-lib/si7021) | Driver for Si7013/Si7020/Si7021/HTU2xD/SHT2x and compatible temperature and humidity sensors ([Documentation](https://esp-idf-lib.github.io/si7021)) |
| [sts21](https://github.com/esp-idf-lib/sts21) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/sts21/badge.svg)](https://components.espressif.com/components/esp-idf-lib/sts21) | Driver for STS21 temperature sensor ([Documentation](https://esp-idf-lib.github.io/sts21)) |
| [sts3x](https://github.com/esp-idf-lib/sts3x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/sts3x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/sts3x) | Driver for Sensirion STS30/STS31/STS35 digital temperature sensor ([Documentation](https://esp-idf-lib.github.io/sts3x)) |
| [tsys01](https://github.com/esp-idf-lib/tsys01) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/tsys01/badge.svg)](https://components.espressif.com/components/esp-idf-lib/tsys01) | Driver for precision digital temperature sensor TSYS01 ([Documentation](https://esp-idf-lib.github.io/tsys01)) |

### Pressure sensors

| Name | Description |
|------|-------------|
| [bme680](https://github.com/esp-idf-lib/bme680) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/bme680/badge.svg)](https://components.espressif.com/components/esp-idf-lib/bme680) | Driver for BME680 digital environmental sensor ([Documentation](https://esp-idf-lib.github.io/bme680)) |
| [bmp180](https://github.com/esp-idf-lib/bmp180) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/bmp180/badge.svg)](https://components.espressif.com/components/esp-idf-lib/bmp180) | Driver for BMP180 digital pressure sensor ([Documentation](https://esp-idf-lib.github.io/bmp180)) |
| [bmp280](https://github.com/esp-idf-lib/bmp280) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/bmp280/badge.svg)](https://components.espressif.com/components/esp-idf-lib/bmp280) | Driver for BMP280/BME280 digital pressure sensor ([Documentation](https://esp-idf-lib.github.io/bmp280)) |
| [dps310](https://github.com/esp-idf-lib/dps310) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/dps310/badge.svg)](https://components.espressif.com/components/esp-idf-lib/dps310) | Driver for DPS310 barometric pressure sensor ([Documentation](https://esp-idf-lib.github.io/dps310)) |
| [ms5611](https://github.com/esp-idf-lib/ms5611) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ms5611/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ms5611) | Driver for barometic pressure sensor MS5611-01BA03 ([Documentation](https://esp-idf-lib.github.io/ms5611)) |
| [qmp6988](https://github.com/esp-idf-lib/qmp6988) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/qmp6988/badge.svg)](https://components.espressif.com/components/esp-idf-lib/qmp6988) | Driver for QMP6988 digital temperature and pressure sensor ([Documentation](https://esp-idf-lib.github.io/qmp6988)) |

### Air quality sensors

| Name | Description |
|------|-------------|
| [ccs811](https://github.com/esp-idf-lib/ccs811) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ccs811/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ccs811) | Driver for AMS CCS811 digital gas sensor ([Documentation](https://esp-idf-lib.github.io/ccs811)) |
| [mhz19b](https://github.com/esp-idf-lib/mhz19b) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/mhz19b/badge.svg)](https://components.espressif.com/components/esp-idf-lib/mhz19b) | Driver for MH-Z19B NDIR CO₂ sensor ([Documentation](https://esp-idf-lib.github.io/mhz19b)) |
| [scd30](https://github.com/esp-idf-lib/scd30) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/scd30/badge.svg)](https://components.espressif.com/components/esp-idf-lib/scd30) | Driver for SCD30 CO₂ sensor ([Documentation](https://esp-idf-lib.github.io/scd30)) |
| [scd4x](https://github.com/esp-idf-lib/scd4x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/scd4x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/scd4x) | Driver for SCD40/SCD41 miniature CO₂ sensor ([Documentation](https://esp-idf-lib.github.io/scd4x)) |
| [sfa3x](https://github.com/esp-idf-lib/sfa3x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/sfa3x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/sfa3x) | Driver for SFA30 formaldehyde detection module (I2C) ([Documentation](https://esp-idf-lib.github.io/sfa3x)) |
| [sgp40](https://github.com/esp-idf-lib/sgp40) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/sgp40/badge.svg)](https://components.espressif.com/components/esp-idf-lib/sgp40) | Driver for SGP40 Indoor Air Quality Sensor for VOC Measurements ([Documentation](https://esp-idf-lib.github.io/sgp40)) |

### Gas sensors

| Name | Description |
|------|-------------|
| [ccs811](https://github.com/esp-idf-lib/ccs811) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ccs811/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ccs811) | Driver for AMS CCS811 digital gas sensor ([Documentation](https://esp-idf-lib.github.io/ccs811)) |
| [mhz19b](https://github.com/esp-idf-lib/mhz19b) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/mhz19b/badge.svg)](https://components.espressif.com/components/esp-idf-lib/mhz19b) | Driver for MH-Z19B NDIR CO₂ sensor ([Documentation](https://esp-idf-lib.github.io/mhz19b)) |
| [scd30](https://github.com/esp-idf-lib/scd30) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/scd30/badge.svg)](https://components.espressif.com/components/esp-idf-lib/scd30) | Driver for SCD30 CO₂ sensor ([Documentation](https://esp-idf-lib.github.io/scd30)) |
| [scd4x](https://github.com/esp-idf-lib/scd4x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/scd4x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/scd4x) | Driver for SCD40/SCD41 miniature CO₂ sensor ([Documentation](https://esp-idf-lib.github.io/scd4x)) |
| [sfa3x](https://github.com/esp-idf-lib/sfa3x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/sfa3x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/sfa3x) | Driver for SFA30 formaldehyde detection module (I2C) ([Documentation](https://esp-idf-lib.github.io/sfa3x)) |

### Current and power sensors

| Name | Description |
|------|-------------|
| [ina219](https://github.com/esp-idf-lib/ina219) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ina219/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ina219) | Driver for INA219/INA220 bidirectional current/power monitor ([Documentation](https://esp-idf-lib.github.io/ina219)) |
| [ina260](https://github.com/esp-idf-lib/ina260) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ina260/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ina260) | Driver for INA260 precision digital current and power monitor ([Documentation](https://esp-idf-lib.github.io/ina260)) |
| [ina3221](https://github.com/esp-idf-lib/ina3221) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ina3221/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ina3221) | Driver for INA3221 shunt and bus voltage monitor ([Documentation](https://esp-idf-lib.github.io/ina3221)) |

### Magnetic sensors

| Name | Description |
|------|-------------|
| [hmc5883l](https://github.com/esp-idf-lib/hmc5883l) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/hmc5883l/badge.svg)](https://components.espressif.com/components/esp-idf-lib/hmc5883l) | Driver for 3-axis digital compass HMC5883L and HMC5983L ([Documentation](https://esp-idf-lib.github.io/hmc5883l)) |
| [lsm303](https://github.com/esp-idf-lib/lsm303) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/lsm303/badge.svg)](https://components.espressif.com/components/esp-idf-lib/lsm303) | Driver for LSM303 3-axis accelerometer and magnetometer sensor ([Documentation](https://esp-idf-lib.github.io/lsm303)) |
| [qmc5883l](https://github.com/esp-idf-lib/qmc5883l) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/qmc5883l/badge.svg)](https://components.espressif.com/components/esp-idf-lib/qmc5883l) | Driver for QMC5883L 3-axis magnetic sensor ([Documentation](https://esp-idf-lib.github.io/qmc5883l)) |
| [qmi8658c](https://github.com/esp-idf-lib/qmi8658c) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/qmi8658c/badge.svg)](https://components.espressif.com/components/esp-idf-lib/qmi8658c) | Driver for QMI8658C 6-axis IMU sensor ([Documentation](https://esp-idf-lib.github.io/qmi8658c)) |

### Light sensors

| Name | Description |
|------|-------------|
| [bh1750](https://github.com/esp-idf-lib/bh1750) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/bh1750/badge.svg)](https://components.espressif.com/components/esp-idf-lib/bh1750) | Driver for BH1750 light sensor ([Documentation](https://esp-idf-lib.github.io/bh1750)) |
| [tsl2561](https://github.com/esp-idf-lib/tsl2561) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/tsl2561/badge.svg)](https://components.espressif.com/components/esp-idf-lib/tsl2561) | Driver for light-to-digital converter TSL2561 ([Documentation](https://esp-idf-lib.github.io/tsl2561)) |
| [tsl2591](https://github.com/esp-idf-lib/tsl2591) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/tsl2591/badge.svg)](https://components.espressif.com/components/esp-idf-lib/tsl2591) | Driver for light-to-digital converter TSL2591 ([Documentation](https://esp-idf-lib.github.io/tsl2591)) |
| [tsl4531](https://github.com/esp-idf-lib/tsl4531) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/tsl4531/badge.svg)](https://components.espressif.com/components/esp-idf-lib/tsl4531) | Driver for digital ambient light sensor TSL4531 ([Documentation](https://esp-idf-lib.github.io/tsl4531)) |
| [veml7700](https://github.com/esp-idf-lib/veml7700) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/veml7700/badge.svg)](https://components.espressif.com/components/esp-idf-lib/veml7700) | Driver for VEML7700 ambient light sensor ([Documentation](https://esp-idf-lib.github.io/veml7700)) |

### GPIO expanders

| Name | Description |
|------|-------------|
| [mcp23008](https://github.com/esp-idf-lib/mcp23008) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/mcp23008/badge.svg)](https://components.espressif.com/components/esp-idf-lib/mcp23008) | Driver for 8-bit I2C GPIO expander MCP23008 ([Documentation](https://esp-idf-lib.github.io/mcp23008)) |
| [mcp23x17](https://github.com/esp-idf-lib/mcp23x17) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/mcp23x17/badge.svg)](https://components.espressif.com/components/esp-idf-lib/mcp23x17) | Driver for I2C/SPI 16 bit GPIO expanders MCP23017/MCP23S17 ([Documentation](https://esp-idf-lib.github.io/mcp23x17)) |
| [pca9557](https://github.com/esp-idf-lib/pca9557) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/pca9557/badge.svg)](https://components.espressif.com/components/esp-idf-lib/pca9557) | Driver for PCA9536/PCA9537/PCA9557/TCA9534 remote 4/8-bit I/O expanders for I2C-bus ([Documentation](https://esp-idf-lib.github.io/pca9557)) |
| [pcf8574](https://github.com/esp-idf-lib/pcf8574) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/pcf8574/badge.svg)](https://components.espressif.com/components/esp-idf-lib/pcf8574) | Driver for PCF8574 remote 8-bit I/O expander for I2C-bus ([Documentation](https://esp-idf-lib.github.io/pcf8574)) |
| [pcf8575](https://github.com/esp-idf-lib/pcf8575) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/pcf8575/badge.svg)](https://components.espressif.com/components/esp-idf-lib/pcf8575) | Driver for PCF8575 remote 16-bit I/O expander for I2C-bus ([Documentation](https://esp-idf-lib.github.io/pcf8575)) |
| [tca6424a](https://github.com/esp-idf-lib/tca6424a) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/tca6424a/badge.svg)](https://components.espressif.com/components/esp-idf-lib/tca6424a) | Driver for TCA6424A low-voltage 24-bit I2C I/O expander ([Documentation](https://esp-idf-lib.github.io/tca6424a)) |
| [tca95x5](https://github.com/esp-idf-lib/tca95x5) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/tca95x5/badge.svg)](https://components.espressif.com/components/esp-idf-lib/tca95x5) | Driver for TCA9535/TCA9555 remote 16-bit I/O expanders for I2C-bus ([Documentation](https://esp-idf-lib.github.io/tca95x5)) |

### LED drivers

| Name | Description |
|------|-------------|
| [ht16k33](https://github.com/esp-idf-lib/ht16k33) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ht16k33/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ht16k33) | HT16K33 LED controller driver ([Documentation](https://esp-idf-lib.github.io/ht16k33)) |
| [led_strip](https://github.com/esp-idf-lib/led_strip) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/led_strip/badge.svg)](https://components.espressif.com/components/esp-idf-lib/led_strip) | RMT-based driver for WS2812B/SK6812/APA106/SM16703 LED strips ([Documentation](https://esp-idf-lib.github.io/led_strip)) |
| [led_strip_spi](https://github.com/esp-idf-lib/led_strip_spi) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/led_strip_spi/badge.svg)](https://components.espressif.com/components/esp-idf-lib/led_strip_spi) | SPI-based driver for SK9822/APA102 LED strips ([Documentation](https://esp-idf-lib.github.io/led_strip_spi)) |
| [max7219](https://github.com/esp-idf-lib/max7219) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/max7219/badge.svg)](https://components.espressif.com/components/esp-idf-lib/max7219) | Driver for 8-Digit LED display drivers, MAX7219/MAX7221 ([Documentation](https://esp-idf-lib.github.io/max7219)) |
| [pca9632](https://github.com/esp-idf-lib/pca9632) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/pca9632/badge.svg)](https://components.espressif.com/components/esp-idf-lib/pca9632) | Driver for PCA9632 4-channel PWM chip ([Documentation](https://esp-idf-lib.github.io/pca9632)) |

### Input device drivers

| Name | Description |
|------|-------------|
| [button](https://github.com/esp-idf-lib/button) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/button/badge.svg)](https://components.espressif.com/components/esp-idf-lib/button) | HW timer-based driver for GPIO buttons ([Documentation](https://esp-idf-lib.github.io/button)) |
| [encoder](https://github.com/esp-idf-lib/encoder) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/encoder/badge.svg)](https://components.espressif.com/components/esp-idf-lib/encoder) | HW timer-based driver for incremental rotary encoders ([Documentation](https://esp-idf-lib.github.io/encoder)) |
| [ls7366r](https://github.com/esp-idf-lib/ls7366r) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ls7366r/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ls7366r) | Driver for LS7366R Quadrature Encoder Counter ([Documentation](https://esp-idf-lib.github.io/ls7366r)) |

### Other misc libraries

| Name | Description |
|------|-------------|
| [ds3502](https://github.com/esp-idf-lib/ds3502) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ds3502/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ds3502) | Driver for nonvolatile digital potentiometer DS3502 ([Documentation](https://esp-idf-lib.github.io/ds3502)) |
| [example](https://github.com/esp-idf-lib/example) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/example/badge.svg)](https://components.espressif.com/components/esp-idf-lib/example) | An example component ([Documentation](https://esp-idf-lib.github.io/example)) |
| [hd44780](https://github.com/esp-idf-lib/hd44780) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/hd44780/badge.svg)](https://components.espressif.com/components/esp-idf-lib/hd44780) | Driver for HD44780 compatible LCD text displays ([Documentation](https://esp-idf-lib.github.io/hd44780)) |
| [impulse_sensor](https://github.com/esp-idf-lib/impulse_sensor) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/impulse_sensor/badge.svg)](https://components.espressif.com/components/esp-idf-lib/impulse_sensor) | Driver for impulse output sensors ([Documentation](https://esp-idf-lib.github.io/impulse_sensor)) |
| [pca9685](https://github.com/esp-idf-lib/pca9685) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/pca9685/badge.svg)](https://components.espressif.com/components/esp-idf-lib/pca9685) | Driver for 16-channel, 12-bit PWM PCA9685 ([Documentation](https://esp-idf-lib.github.io/pca9685)) |
| [rda5807m](https://github.com/esp-idf-lib/rda5807m) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/rda5807m/badge.svg)](https://components.espressif.com/components/esp-idf-lib/rda5807m) | Driver for single-chip broadcast FM radio tuner RDA5807M ([Documentation](https://esp-idf-lib.github.io/rda5807m)) |
| [tca9548](https://github.com/esp-idf-lib/tca9548) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/tca9548/badge.svg)](https://components.espressif.com/components/esp-idf-lib/tca9548) | Driver for TCA9548A/PCA9548A low-voltage 8-channel I2C switch ([Documentation](https://esp-idf-lib.github.io/tca9548)) |
| [tda74xx](https://github.com/esp-idf-lib/tda74xx) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/tda74xx/badge.svg)](https://components.espressif.com/components/esp-idf-lib/tda74xx) | Driver for TDA7439/TDA7439DS/TDA7440D audioprocessors ([Documentation](https://esp-idf-lib.github.io/tda74xx)) |
| [tps63101x](https://github.com/esp-idf-lib/tps63101x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/tps63101x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/tps63101x) | Driver for Texas Instruments TPS631012 and TPS631013 1.6-V to 5.5-V Input Voltage 1.5-A Buck-boost Converter with I2C ([Documentation](https://esp-idf-lib.github.io/tps63101x)) |
| [ultrasonic](https://github.com/esp-idf-lib/ultrasonic) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/ultrasonic/badge.svg)](https://components.espressif.com/components/esp-idf-lib/ultrasonic) | Driver for ultrasonic range meters, e.g. HC-SR04, HY-SRF05 ([Documentation](https://esp-idf-lib.github.io/ultrasonic)) |
| [wiegand](https://github.com/esp-idf-lib/wiegand) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/wiegand/badge.svg)](https://components.espressif.com/components/esp-idf-lib/wiegand) | Wiegand protocol receiver ([Documentation](https://esp-idf-lib.github.io/wiegand)) |

### Inertial measurement units

| Name | Description |
|------|-------------|
| [icm42670](https://github.com/esp-idf-lib/icm42670) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/icm42670/badge.svg)](https://components.espressif.com/components/esp-idf-lib/icm42670) | Driver for TDK ICM-42670-P 6-Axis IMU ([Documentation](https://esp-idf-lib.github.io/icm42670)) |
| [l3gx](https://github.com/esp-idf-lib/l3gx) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/l3gx/badge.svg)](https://components.espressif.com/components/esp-idf-lib/l3gx) | Driver for L3Gx(L3GD20/L3G4200D) 3-axis gyroscope sensors ([Documentation](https://esp-idf-lib.github.io/l3gx)) |
| [lsm303](https://github.com/esp-idf-lib/lsm303) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/lsm303/badge.svg)](https://components.espressif.com/components/esp-idf-lib/lsm303) | Driver for LSM303 3-axis accelerometer and magnetometer sensor ([Documentation](https://esp-idf-lib.github.io/lsm303)) |
| [mpu6050](https://github.com/esp-idf-lib/mpu6050) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/mpu6050/badge.svg)](https://components.espressif.com/components/esp-idf-lib/mpu6050) | Driver for MPU6000/MPU6050 6-axis MotionTracking device ([Documentation](https://esp-idf-lib.github.io/mpu6050)) |

### Battery controllers

| Name | Description |
|------|-------------|
| [lc709203f](https://github.com/esp-idf-lib/lc709203f) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/lc709203f/badge.svg)](https://components.espressif.com/components/esp-idf-lib/lc709203f) | Driver for LC709203F battery fuel gauge ([Documentation](https://esp-idf-lib.github.io/lc709203f)) |
| [max1704x](https://github.com/esp-idf-lib/max1704x) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/max1704x/badge.svg)](https://components.espressif.com/components/esp-idf-lib/max1704x) | Driver for MAX17043/MAX17044/MAX17048/MAX17049 battery fuel gauge ([Documentation](https://esp-idf-lib.github.io/max1704x)) |
| [mp2660](https://github.com/esp-idf-lib/mp2660) <br> [![Component Registry](https://components.espressif.com/components/esp-idf-lib/mp2660/badge.svg)](https://components.espressif.com/components/esp-idf-lib/mp2660) | Driver for MP2660 5V USB, 500mA, I2C-Controlled Linear Charger with Power Path Management for Single-Cell Li-Ion Battery ([Documentation](https://esp-idf-lib.github.io/mp2660)) |


## Contributors

  - [Alex Stewart](https://github.com/astewart-consensus) `ds18x20`
  - [Alexander Bodenseher](https://github.com/saasaa) `hts221`
  - [Andrej Krutak](https://github.com/andree182) `bh1750`
  - Angelo Elias Dalzotto `mpu6050`
  - [BernhardG](https://gitlab.com/mrnice) `ms5611`
  - [BhuvanchandraD](https://github.com/bhuvanchandra) `ds3231`
  - [Brian Schwind](https://github.com/bschwind) `tsl2561` `tsl4531`
  - [Cedric von Gunten](https://github.com/vonguced) `qmp6988`
  - [Christian Skjerning](https://github.com/slimcdk) `sts3x`
  - [David Douard](https://github.com/douardda) `mhz19b`
  - [Erriez](https://github.com/Erriez) `mhz19b`
  - [FastLED project](https://github.com/FastLED) `color` `lib8tion` `noise`
  - Frank Bargstedt `bmp180`
  - Gabriel Boni Vicari `mpu6050`
  - [Grupo de Pesquisa em Cultura Digital](http://gepid.upf.br/) `mpu6050`
  - GrzegorzH `ds18x20`
  - [Gunar Schorcht](https://github.com/gschorcht) `bme680` `ccs811` `sht3x` `sts3x`
  - [Jakub Turek](https://github.com/QB4-dev) `impulse_sensor` `l3gx` `lsm303` `pca9632`
  - [Jan Veeh](https://github.com/janveeh) `icm42670`
  - [Jeff Rowberg](https://www.i2cdevlib.com/) `mpu6050`
  - [Jose Manuel Perez](https://github.com/jmpmscorp) `lc709203f` `sgm58031`
  - [Joshua Butler](https://github.com/shuki25) `max1704x`
  - [Joshua Kallus](https://github.com/Jkallus) `ls7366r`
  - [Julian Doerner](https://github.com/juliandoerner) `tsl2591`
  - [Lucio Tarantino](https://github.com/dianlight) `ads111x`
  - [Manuel Markwort](https://github.com/mmarkwort) `mp2660` `tps63101x`
  - [Marc Luehr](https://github.com/th3link) `veml7700`
  - [Nate Usher](https://github.com/nated0g) `scd30`
  - Pavel Merzlyakov `ds1302`
  - [Raghav Jha](https://github.com/horsemann07) `mpu6050`
  - RichardA `ds3231`
  - [Ruslan V. Uss](https://github.com/UncleRus) `ads111x` `aht` `am2320` `bh1750` `bh1900nux` `bme680` `bmp180` `bmp280` `button` `calibration` `ccs811` `dht` `ds1302` `ds1307` `ds18x20` `ds3231` `ds3502` `encoder` `framebuffer` `hd44780` `hdc1000` `hmc5883l` `hx711` `i2cdev` `ina219` `ina260` `ina3221` `led_strip` `led_strip_spi` `max31725` `max31855` `max31865` `max7219` `mcp23008` `mcp23x17` `mcp342x` `mcp4725` `mcp960x` `mcp9808` `mpu6050` `ms5611` `onewire` `pca9557` `pca9685` `pcf8563` `pcf8574` `pcf8575` `pcf8591` `qmc5883l` `qmp6988` `rda5807m` `scd30` `scd4x` `sfa3x` `sgp40` `sht3x` `sht4x` `si7021` `sts21` `sts3x` `tca6424a` `tca9548` `tca95x5` `tda74xx` `tsl2561` `tsl4531` `tsys01` `ultrasonic` `wiegand`
  - [Sensirion AG](https://github.com/Sensirion) `scd30` `scd4x` `sfa3x`
  - [Thanh Pham](https://github.com/panoti) `pcf8591`
  - [Timofei Korostelev](https://github.com/chudsaviet) `ht16k33`
  - [Tomoyuki Sakurai](https://github.com/trombik) `bmi160` `dps310` `esp_idf_lib_helpers` `example` `led_strip_spi` `lm75`
  - [Weslley Duarte](https://github.com/weslleymfd) `ads130e08`
  - [Zaltora](https://github.com/Zaltora) `ina3221`
  - [jsuiker](https://github.com/jsuiker) `dht`
  - [lukbieli](https://github.com/lukbieli) `bmi160`
  - [quinkq](https://github.com/quinkq) `i2cdev`
  - [sheinz](https://github.com/sheinz) `bmp280`
  - [xyzroe](https://github.com/xyzroe) `qmi8658c`
  - zeroday `onewire`
