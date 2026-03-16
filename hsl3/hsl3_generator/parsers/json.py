import os
import json
from datetime import datetime

from hsl3.hsl3_generator.configs.dcls_module import ConfigModule
from hsl3.hsl3_generator.configs.dcls_output import ConfigOutput
from hsl3.hsl3_generator.configs.dcls_input import ConfigInput
from hsl3.hsl3_generator.configs.dcls_project import ConfigProject
from hsl3.hsl3_generator.configs.dcls_store import ConfigStore
from hsl3.hsl3_generator.configs.dcls_timer import ConfigTimer
from hsl3.hsl3_generator.configs.dcls_script import ConfigScript
from hsl3.hsl3_generator.configs.dcls_translation import ConfigTranslation

class JSONfileParser:
    """ Class for parsing the JSON configuration file for a logic module. """

    def parse_json(self, file_content):
        root = json.loads(file_content)
        inputs = []
        outputs = []
        stores = []
        timers = []
        scripts = []
        
        translations = []
        
        for elem in root['module']['inputs']:
            list_item = ConfigInput(**elem)
            inputs.append(list_item)
        
        for elem in root['module']['outputs']:
            list_item = ConfigOutput(**elem)
            outputs.append(list_item)
        
        if 'stores' in root['module']:
            for elem in root['module']['stores']:
                list_item = ConfigStore(**elem)
                stores.append(list_item)
        
        if 'timers' in root['module']:
            for elem in root['module']['timers']:
                list_item = ConfigTimer(**elem)
                timers.append(list_item)
        
        for elem in root['module']['scripts']:
            list_item = ConfigScript(**elem)
            scripts.append(list_item)
        
        if 'translations' in root['module']:
            for elem in root['module']['translations']:
                translation_inputs = []
                
                for ti in elem['translation_inputs']:
                    translation_inputs.append(ti['label'])
                translation_outputs = []
                
                for to in elem['translation_outputs']:
                    translation_outputs.append(to['label'])
                
                elem_dict = dict(elem)
                elem_dict['translation_inputs'] = translation_inputs
                elem_dict['translation_outputs'] = translation_outputs
                
                list_item = ConfigTranslation(**elem_dict)
                translations.append(list_item)
        
        root['module']['inputs'] = inputs
        root['module']['outputs'] = outputs
        root['module']['stores'] = stores
        root['module']['timers'] = timers
        root['module']['scripts'] = scripts
        root['module']['translations'] = translations

        return ConfigModule(**root['module'])

    def write_first_json(self, config: ConfigProject):

        config_dict = {
            "module": {
                "id": config.id,
                "name": config.title,
                "version": "0.1.0",
                "version_date": datetime.now().strftime('%Y-%m-%d'),
                "description": "This is a description for the module.",
                "warning": "",
                "note": "",
                "category": config.category,
                "context": config.context,
                "hsl_filename": config.node_file,
                "inputs": [
                    {
                        "type": "string", 
                        "identifier": "IN01", 
                        "init_value": "", 
                        "label": "Input 01",
                        "description": "This is a description for Input 01"
                    }
                ],
                "outputs": [
                    {
                        "type": "string", 
                        "identifier": "OUT01", 
                        "init_value": "", 
                        "sbc": "s",
                        "label": "Output 01",
                        "description": "This is a description for Output 01"
                    }
                ],
                "stores": [
                    {
                        "identifier": "STORE01",
                        "type": "string",
                        "init_value": "",
                        "label": "Store 01",
                        "description": "This is a description for Store 01"
                    }
                ] if config.has_stores == True else [],
                "timers": [
                    {
                        "identifier": "TIMER01",
                        "description": "This is a description for Timer 01"
                    }
                ] if config.has_timers == True else [],
                "scripts": [
                    {
                        "filename": config.python_file
                    }
                ],
                "translations": [
                    {
                        "language": "en",
                        "category": "",
                        "name": "English",
                        "translation_inputs": ["Input 01"],
                        "translation_outputs": ["Output 01"]
                    }
                ] if config.has_translations == True else []
            }
        }

        json_content = json.dumps(config_dict, indent=4, ensure_ascii=True)

        with open(os.path.join(config.source_path, config.json_file), 'w', encoding='utf-8') as f:
            f.write(json_content)