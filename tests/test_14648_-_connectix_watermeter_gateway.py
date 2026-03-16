# Auto-generated Python file

import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if ROOT_DIR not in sys.path:
	sys.path.insert(0, ROOT_DIR)
if os.path.join(ROOT_DIR, "src") not in sys.path:
	sys.path.insert(0, os.path.join(ROOT_DIR, "src"))

from hsl3.hsl3 import HSL3
from hsl3.hsl3_wrapper import Hsl3WrapperNode
from hsl3_14648_connectix_watermeter_gateway import LogicModule

json_file = "config_connectix-watermeter-gateway.json"

def main():

	if sys.platform == "win32":
		os.system('cls')
	else:
		os.system('clear')

	print(" === Starting test for 14648 - Connectix Watermeter Gateway === ")
	print("")

	hsl3 = HSL3("14648_connectix_watermeter_gateway")
	logic_module = LogicModule(hsl3)
	wrapper_node = Hsl3WrapperNode(ROOT_DIR, json_file, logic_module)
	if (wrapper_node.module is not None):
		hsl3.config = wrapper_node.module

	wrapper_node.set("IN01_HOST", "connectix_watermeter.local")
	wrapper_node.set("IN02_PORT", 82)
	wrapper_node.set("IN03_READ_INTERVAL", 60)

	print("")

	print(" === DEBUG LOG ===")
	print("")

	logic_module.debug.print_log()


if __name__ == "__main__":
	main()
