from hsl3.hsl3_generator.configs.dcls_module import ConfigModule

class PythonfileParser:
    """ Class for handling the generation of Python code for a logic module. """
    
    def write_first_python(self, python_file: str, config: ConfigModule):

        python_content = f'# Auto-generated Python file\r\n'
        python_content += f'# Logic Node: {config.title}\r\n'
        python_content += f'# Author:\r\n'  
        python_content += f'# Description: \r\n'
        python_content += f'# INFO: \r\n'
        python_content += f'# DISCLAIMER: \r\n\r\n'
        
        nl = '\n'
        nt = '\t\t\t'
        python_content += f"""
    class LogicModule:

        def __init__(self, hsl3):
            self.fw = hsl3
            self.debug = self.fw.create_debug_section()
            self.input_values = []
            self.stores = []
            self.timers = []

            self.output_values =  {{{ nl + nt + (',' + nl + nt).join([f"{output.index } : '{output.identifier}'" for output in config.outputs]) }}}

        def on_init(self, inputs, store):
            \"\"\"
            Initialize the module with input connections and store information
            Args:
                inputs: Hsl3Slots object containing input slot definitions
                store: Hsl3Slots object containing the storage object for maintaining state (for this node unused)
            \"\"\"

            for key in inputs.keys():
                # .keys() returns both indexes and keynames
                if key in [{', '.join([f"'{input.identifier}'" for input in config.inputs])}]:
                    pass

        def on_calc(self, inputs):
            \"\"\"
            Calculate called if any new input is received by the logic node.

            Args:
                inputs:  Hsl3Slots object containing input slot definition
            \"\"\"

            if inputs.changed('IN01'):  
                pass

        def on_timer(self, timer):
            \"\"\" Timers \"\"\"
            pass

        def get_input_value(self, input_index):
            \"\"\" Actively retrieve an input value \"\"\"
            pass
        """

        with open(python_file, 'w', encoding='utf-8') as f:
            f.write(python_content)
