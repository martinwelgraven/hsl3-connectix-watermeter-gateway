import os
import re
from dataclasses import dataclass, field
from typing import Optional

from hsl3.hsl3_generator.configs.dcls_module import ConfigModule


@dataclass
class ConfigProject:

    root: str
    state: str = 'new'
    
    id: str = ''
    name: str = ''
    title: str = ''
    category: str = ''
    context: str = ''

    has_timers: bool = False
    has_stores: bool = False
    has_translations: bool = False
    
    source_path: str = ''
    json_file: str = ''
    html_file: str = ''
    python_file: str = ''
    node_file: str = ''


    def __post_init__(self):
        if self.root is None:
           print('Root directory could not be retrieved. Process exits with error code 1.')
           exit(1)

        paths = self.root.split(os.sep)
        if( not re.match(r'[0-9]{5}-[A-Za-z0-9_]+(?:-[A-Za-z0-9_]+)*$', paths[-1]) ):
            print(f'Root directory {self.root} has an incorrect valid format. Please use the format "12345-project-name". Process exits with error code 1.')
            exit(1)
        else:
            self.id = paths[-1].split('-')[0]
            self.name = '-'.join(paths[-1].split('-')[1:])
            
        if not os.path.exists(self.root):
            print(f"Root directory '{self.root}' could not be validated. Process exits with error code 1.")
            exit(1)
        else:
            self.source_path = os.path.join(self.root, 'src')
            self.json_file = f"config_{self.name.lower()}.json"
            
            self.html_file = f"log{str(self.id)}.html"
            self.python_file = f"hsl3_{self.id}_{self.name.replace('-','_').lower()}.py"
            self.node_file = f"{self.id}_{self.name.replace('-','_').lower()}.hsl"
            
            if not os.path.exists(self.source_path):
                os.mkdir(self.source_path)
                self.state = 'initialized'
            elif not os.path.exists(os.path.join(self.source_path, self.json_file)):
                self.state = 'initialized'
            else:
                self.state = 'load'
        
        