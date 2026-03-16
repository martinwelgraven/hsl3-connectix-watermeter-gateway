# Auto-generated Python file
# Logic Node: 14648 - Connectix Watermeter Gateway
# Author:
# Description: 
# INFO: JSON Message recieved looks like: {"mac_address":"94_54_C5_75_A3_48","gateway_model":"connectix_watermeter_gateway_v1.0 - A","startup_time":"2026-01-05T06:03:16Z","firmware_running":"2025070301","firmware_available":"2025070301","firmware_update_available":"false","wifi_rssi":"-66","mqtt_configured":"false","watermeter_value":"644798","watermeter_pulse_factor":"1","watermeter_used_last_minute":"0.00","watermeter_pulsecount":"55924","leak_detect":"false"}
# DISCLAIMER: 

from datetime import datetime
import requests

class LogicModule:

    def __init__(self, hsl3):
        self.fw = hsl3
        self.debug = self.fw.create_debug_section()
        self.input_values = {}
        self.stores = []
        self.timers = []

        self.path = "watermeter/api/read"
        
        self.output_values =  {
			'mac_address' : 'OUT01_MAC_ADDRESS',
			'gateway_model' : 'OUT02_MODEL',
			'startup_time' : 'OUT03_STARTUP_TIME',
			'firmware_running' : 'OUT04_FIRMWARE_RUNNING',
			'firmware_available' : 'OUT05_FIRMWARE_AVAILABLE',
            'firmware_update_available' : 'OUT06_FIRMWARE_UPDATE_AVAILABLE',
			'wifi_rssi' : 'OUT07_WIFI_RSSI',
			'mqtt_configured' : 'OUT08_MQTT_CONFIGURED',
			'watermeter_pulse_factor' : 'OUT09_WATERMETER_PULSE_FACTOR',
			'watermeter_value' : 'OUT10_WATERMETER_VALUE',
			'watermeter_used_last_minute' : 'OUT11_WATERMETER_USED_LAST_MINUTE',
			'watermeter_pulsecount' : 'OUT12_WATERMETER_PULSECOUNT',
			'leak_detect' : 'OUT13_LEAK_DETECT'}

    def on_init(self, inputs, store):
        """
        Initialize the module with input connections and store information
        Args:
            inputs: Hsl3Slots object containing input slot definitions
            store: Hsl3Slots object containing the storage object for maintaining state (for this node unused)
        """

        for key in inputs.keys():
            # .keys() returns both indexes and keynames
            if key in ['IN01_HOST', 'IN02_PORT', 'IN03_READ_INTERVAL']:
                self.input_values[key] = inputs.value(key)
            
            if key == 'IN03_READ_INTERVAL':
                self.fw.set_timer("TIME01_READ_GATEWAY", inputs.value('IN03_READ_INTERVAL'))

    def on_calc(self, inputs):
        """
        Calculate called if any new input is received by the logic node.

        Args:
            inputs:  Hsl3Slots object containing input slot definition
        """

        if inputs.changed('IN01_HOST') or inputs.changed('IN02_PORT'):  
            self._get_data(inputs.value('IN01_HOST'), inputs.value('IN02_PORT'))
        
        elif inputs.changed('IN03_READ_INTERVAL'):
            self.fw.set_timer("TIME01_READ_GATEWAY", inputs.value('IN03_READ_INTERVAL'))


    def on_timer(self, timer):
        if timer.changed("TIME01_READ_GATEWAY"):
            self.fw.run_in_context(self._get_data, (self.input_values["IN01_HOST"], self.input_values["IN02_PORT"]))
            self.fw.set_timer("TIME01_READ_GATEWAY", self.input_values["IN03_READ_INTERVAL"])  


    def _get_data(self, host, port):
        """ Helper function to start the client with the given host and port """
        host = self.input_values["IN01_HOST"].decode("ascii")
        port = self.input_values["IN02_PORT"]

        url = f"http://{host}:{port}/{self.path}"
        print(f"Attempting to connect to watermeter gateway at {url}")
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                self.debug.log(f"Successfully connected to watermeter gateway: {response.json()}")
                self._process_data(response.json())
            else:
                self.debug.log(f"Failed to connect, status code: {response.status_code}")
                return {}
        except requests.RequestException as e:
            self.debug.log(f"Error connecting to watermeter gateway: {e}")
            return {}
        
    def _process_data(self, data):
        """ Helper function to process the received data and set output values accordingly """
        if not data:
            self.debug.log("No data to process")
            return
        
        for key, output in self.output_values.items():
            if key in data:
                value = data[key]
                if key in ['mqtt_configured', 'leak_detect', 'firmware_update_available']:
                    value = 1 if data[key].lower() in ['true', '1', 'yes'] else 0
                elif key in ['startup_time', 'firmware_running','firmware_available']:
                    value = self._dateformat(value)
                elif key in ['wifi_rssi', 'watermeter_value', 'watermeter_pulse_factor', 'watermeter_used_last_minute', 'watermeter_pulsecount']:
                    if value.find(".") > -1:
                        value = float(value)
                    else:
                        value = int(value)
                    

                if isinstance(value, str):
                    value = value.encode("ascii")
                
                self.fw.set_output(output, value)
                self.debug.log(f"Set output {output} to {value}")
            else:
                self.debug.log(f"Key {key} not found in data")  

    def _dateformat(self, value) -> str:
        """ Helper function to convert date format if needed (not used in this example) """
        if len(value) == 20:
            # 2026-01-05T06:03:16Z
            value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%m-%Y %H:%M:%S")
        elif len(value) == 10:
            version = datetime.strptime(value[:8], "%Y%m%d").strftime("%d-%m-%Y")
            version = f"{version} v{int(value[8:])}" 
            value = version

        return value
    
    