# 14648 Connectix Watermeter Gateway

A GIRA HomeServer HSL3 Logic Node for connecting to the REST API of the Connectix Watermeter Gateway. The node creates a connection, retrieves the data and closes the connection. In this repository is an independantly developed framework for building HSL3 (HomeServer Logic 3) modules for Gira HomeServer / Facility Server included. [GiraHS HSL3 Framework](https://github.com/martinwelgraven/girahs-hsl3))

## Features

## Requirements

- Python 3.9.x (as installed on the HomeServer/FacilityServer itself).
- Package requests - $ pip install requests
 
##


## Protocol

No official protocol seems to be used. An example message is shown below.

```json
{
    'mac_address': 'A4_B5_C5_D6_E7_F8', 
    'gateway_model': 'connectix_watermeter_gateway_v1.0 - A', 
    'startup_time': '2026-01-05T06:03:16Z', 
    'firmware_running': '2025070301', 
    'firmware_available': '2025070301', 
    'firmware_update_available': 'false', 
    'wifi_rssi': '-68', 
    'mqtt_configured': 'false', 
    'watermeter_value': '645223', 
    'watermeter_pulse_factor': '1', 
    'watermeter_used_last_minute': '0.00', 
    'watermeter_pulsecount': '56349', 
    'leak_detect': 'false'
}
```