# 14648 Connectix Watermeter Gateway

A logic node for the GIRA HomeServer that connects to the REST API of the Connectix Watermeter Gateway. The node polls the gateway at a configurable interval, retrieves the data and exposes it as HSL3 outputs. In this repository is an independently developed framework for building HSL3 (HomeServer Logic 3) modules for Gira HomeServer / Facility Server included. This is developed via [GiraHS HSL3 Development Framework](https://github.com/martinwelgraven/girahs-hsl3)

> **EARLY STAGES OF DEVELOPMENT**<br/>
> This software is in the early stages of development. Please use accordingly and provide feedback if you experience issues.

> **Independent Development & Non-Affiliation Disclaimer**<br/>
> This software is an independently developed integration. It is not affiliated with, endorsed by, or supported by Gira Giersiepen GmbH & Co. KG or Connectix or any of their affiliated companies. All referenced product and company names are trademarks of their respective owners and are used for identification purposes only.

## Features

- **REST API Integration**: Polls the Connectix Watermeter Gateway REST API at a configurable interval
- **Watermeter Data**: Exposes watermeter value, pulse count, pulse factor, and water used last minute
- **Leak Detection**: Exposes the gateway's leak detection status as an HSL3 output
- **Device Info**: Exposes gateway model, MAC address, startup time, firmware version, WiFi RSSI, and MQTT status
- **Automatic Data Conversion**: Booleans are converted to 0/1 numbers; timestamps and firmware versions are formatted for readability

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Protocol](#protocol)
- [Testing](#testing)
- [License](#license)
- [Contributing](#contributing)
- [Additional Resources](#additional-resources)
- [Support](#support)

## Installation

### Requirements

- Python 3.9.x (as installed on the HomeServer/FacilityServer itself)
- Package `requests`: `pip install requests`

### Setup

1. Clone the repository:
```bash
git clone https://github.com/martinwelgraven/hsl3-connectix-watermeter-gateway.git
cd hsl3-connectix-watermeter-gateway
```

2. Install the required package:
```bash
pip install requests
```

## Quick Start

### Basic Example

```python
from hsl3.hsl3 import Hsl3Framework
from hsl3.hsl3_wrapper import Hsl3WrapperModule
from src.hsl3_14648_connectix_watermeter_gateway import LogicModule

# Create HSL3 instance
hsl3fw = Hsl3Framework("14648_connectix_watermeter_gateway")
logic_module = LogicModule(hsl3fw)

# Create wrapper with configuration
wrapper_node = Hsl3WrapperModule("src/config_connectix-watermeter-gateway.json", logic_module)

# Set input values
wrapper_node.set_input_value("IN01_HOST", "connectix_watermeter.local")
wrapper_node.set_input_value("IN02_PORT", 82)
wrapper_node.set_input_value("IN03_READ_INTERVAL", 60)
```

### Running the Example

```bash
python tests/test_14648_connectix_watermeter_gateway.py
```

This connects to the gateway using the default host `connectix_watermeter.local` on port `82` and retrieves watermeter data.

## Project Structure

```
hsl3/                                          # Core HSL3 framework
src/                                           # Logic node files
├── config_connectix-watermeter-gateway.json   # Module configuration
├── hsl3_14648_connectix_watermeter_gateway.py # Generated logic module
├── 14648_connectix_watermeter_gateway.hsl     # HSL3 source file
└── log14648.html                              # HTML information file
tests/                                         # Test suite
└── test_14648_connectix_watermeter_gateway.py # Test and demo
README.md
LICENSE
```

## Configuration

The module is configured through `src/config_connectix-watermeter-gateway.json`.

### Inputs

| Identifier | Type | Default | Description |
|------------|------|---------|-------------|
| `IN01_HOST` | string | `connectix_watermeter.local` | Gateway host address |
| `IN02_PORT` | number | `82` | Gateway port |
| `IN03_READ_INTERVAL` | number | `60` | Poll interval in seconds |

### Outputs

| Identifier | Type | Description |
|------------|------|-------------|
| `OUT01_MAC_ADDRESS` | string | MAC address of the gateway |
| `OUT02_MODEL` | string | Gateway model name |
| `OUT03_STARTUP_TIME` | string | Timestamp of last gateway startup |
| `OUT04_FIRMWARE_RUNNING` | string | Currently running firmware version |
| `OUT05_FIRMWARE_AVAILABLE` | string | Latest available firmware version |
| `OUT06_FIRMWARE_UPDATE_AVAILABLE` | number | Firmware update available (0 = No, 1 = Yes) |
| `OUT07_WIFI_RSSI` | number | WiFi signal strength (RSSI) |
| `OUT08_MQTT_CONFIGURED` | number | MQTT configured (0 = No, 1 = Yes) |
| `OUT09_WATERMETER_PULSE_FACTOR` | number | Pulse factor |
| `OUT10_WATERMETER_VALUE` | number | Current watermeter value |
| `OUT11_WATERMETER_USED_LAST_MINUTE` | number | Water used in the last minute |
| `OUT12_WATERMETER_PULSECOUNT` | number | Total pulse count |
| `OUT13_LEAK_DETECT` | number | Leak detected (0 = No, 1 = Yes) |

## Protocol

The gateway exposes a REST API. The logic node performs a `GET` request to:

```
GET http://{host}:{port}/watermeter/api/read
```

An example JSON response is shown below:

```json
{
    "mac_address": "A4_B5_C5_D6_E7_F8",
    "gateway_model": "connectix_watermeter_gateway_v1.0 - A",
    "startup_time": "2026-01-05T06:03:16Z",
    "firmware_running": "2025070301",
    "firmware_available": "2025070301",
    "firmware_update_available": "false",
    "wifi_rssi": "-68",
    "mqtt_configured": "false",
    "watermeter_value": "645223",
    "watermeter_pulse_factor": "1",
    "watermeter_used_last_minute": "0.00",
    "watermeter_pulsecount": "56349",
    "leak_detect": "false"
}
```

## Testing

### Running Tests

```bash
python tests/test_14648_connectix_watermeter_gateway.py
```

### Test Configuration

Inside the test file, update the input values to match your gateway's network address:

```python
wrapper_node.set_input_value("IN01_HOST", "connectix_watermeter.local")
wrapper_node.set_input_value("IN02_PORT", 82)
wrapper_node.set_input_value("IN03_READ_INTERVAL", 60)
```

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0). See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please ensure:

- Code follows the existing structure and naming conventions
- JSON configurations are properly formatted and validated
- Tests pass before submitting pull requests
- New features include corresponding documentation

## Additional Resources

- [Gira HomeServer Documentation](https://www.gira.de/) (official Gira resources)
- [GiraHS HSL3 Development Framework](https://github.com/martinwelgraven/girahs-hsl3)

## Support

For issues or questions:

1. Check existing issues on the repository
2. Review configuration examples in `src/`
3. Run tests to isolate problems
4. Enable debug output using HSL3 debug sections