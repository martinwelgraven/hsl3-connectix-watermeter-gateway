global debug_mode

__version__ = '0.1.0'
__author__ = 'Martin Welgraven'

import os
import sys

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import argparse
from hsl3.hsl3_generator.parsers.project import ProjectParser
from hsl3.hsl3_generator.configs.dcls_project import ConfigProject

def debug(msg):
    if debug_mode:
        print(msg)

def setup():
    parser = argparse.ArgumentParser(description=f'Generator (v{__version__}) for the generation of HSL3 logic blocks.')
    
    parser.add_argument('-n', '--new', action='store_true', help='Triggers a series of questions to create a new project')
    parser.add_argument('-b', '--build', action='store_true', help='Triggers a series of questions to build the project to a HSL file and generate the documentation')
    parser.add_argument('-d', '--debug', action='store_true', help='Enables debug output')
    
    args = parser.parse_args()

    if args.new == True:
        return 'new'
    elif args.build == True:
        return 'build'
    else:
        print("No valid action provided. Please use '-n/--new' to create a new project or '-b/--build' to build the project.")
        exit(1)

def main():
    global debug_mode
    debug_mode = True

    debug('Debug mode is enabled.')
    debug(f'Version: {__version__}')

    project_config = ConfigProject(root=ROOT_DIR)
    project = ProjectParser(project_config, setup())
   


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n')
    print(f'Creating HSL3 Logic Block')
    print(f'=========================')
    main()
    print(f'=========================')
    print('\n')