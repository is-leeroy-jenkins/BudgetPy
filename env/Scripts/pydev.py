import argparse
import logging
import subprocess
import os
from os import path
from pathlib import Path
import glob
from typing import List
import re
import sys

from pydantic import BaseModel
import colorama


class Plugin(BaseModel):
    path: str
    name: str
    url: str = None
    description: str = None


def docker_works() -> bool:
    logging.debug('running docker --help to make sure docker is installed')
    process = subprocess.run("docker --help",
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    logging.debug(f'docker --help return code: %s', process.returncode)

    return process.returncode == 0


def get_context_info() -> dict:
    return {
        'PYDEV_PROJECT_ROOT': os.getcwd()
    }


def stop_plugin(plugin: Plugin):
    logging.debug(f'Shutting down plugin: {plugin.name}')
    env = {**os.environ.copy(), **get_context_info()}
    process = subprocess.run(f"docker-compose -f {plugin.path} down --remove-orphans",
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             env=env)
    
    logging.debug('shutdown complete with return code: %s', process.returncode)

    if process.returncode != 0:
        logging.debug('stdout: %s', process.stdout)
        logging.error(process.stderr)


def start_plugin(plugin: Plugin):
    logging.debug(f'Starting plugin: {plugin.name}')
    env = {**os.environ.copy(), **get_context_info()}
    process = subprocess.run(f"docker-compose -f {plugin.path} up -d",
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             env=env)
    
    logging.debug('start complete with return code: %s', process.returncode)

    if process.returncode != 0:
        logging.debug('stdout: %s', process.stdout)
        logging.error(process.stderr)


def get_plugins(plugins_dir: str) -> List[Plugin]:
    logging.debug('Searching for plugins in %s', plugins_dir)
    plugin_files = glob.glob(path.join(plugins_dir, '*.yml'))
    plugin_files = plugin_files + glob.glob(path.join(plugins_dir, '*.yaml'))
    plugin_files = list(set(plugin_files))

    logging.debug('Plugin files: %s', plugin_files)

    plugins = []
    for plugin_file in plugin_files:
        name, ext = os.path.splitext(os.path.basename(plugin_file))

        comment_lines = []
        with open(plugin_file) as f:
            for line in f:
                if line.startswith('#'):
                    comment_lines.append(line)
                else:
                    break
        
        url = None
        description = None

        for line in comment_lines:
            matches = re.findall(r'^\s*#\s*url:\s*(.*?)\s*$', line)
            if matches and len(matches) == 1:
                url = matches[0]
            
            matches = re.findall(r'^\s*#\s*description:\s*(.*?)\s*$', line)
            if matches and len(matches) == 1:
                description = matches[0]

        plugins.append(Plugin(
            name=name,
            path=plugin_file,
            url=url,
            description=description
        ))
    
    return plugins
    

def docker_compose_works() -> bool:
    logging.debug('running docker-compose --help to make sure it is installed')
    process = subprocess.run("docker-compose --help",
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
    logging.debug(f'docker-compose --help return code: %s', process.returncode)

    return process.returncode == 0


def main(plugins_dir: str, verify: bool = False, *args, **kwargs):
    if verify:
        if not docker_works():
            logging.error('Docker does not seem to be installed, terminating')
            exit(1)

        if not docker_compose_works():
            logging.error('Docker compose does not seem to be installed, terminating')
            exit(1)
    
    logging.debug('Creating plugins dir at %s', plugins_dir)
    os.makedirs(plugins_dir, exist_ok=True)

    plugins = get_plugins(plugins_dir)
    logging.debug('Found %s plugins', len(plugins))

    colorama.init(autoreset=True)

    for plugin in plugins:
        sys.stdout.write(f'Stopping {plugin.name}...   ')
        stop_plugin(plugin)
        print(colorama.Fore.GREEN + 'Done')
        logging.debug('Plugin %s stopped', plugin.name)
    
    for plugin in plugins:
        sys.stdout.write(f'Starting {plugin.name}...   ')
        start_plugin(plugin)
        print(colorama.Fore.GREEN + 'Done')
    

    print('pydev is up and running!')
    for plugin in plugins:
        if plugin.url:
            print(f'\t{plugin.name} - {plugin.url}')
        else:
            print(f'\t{plugin.name}')
        
        if plugin.description:
            print(f'\t\t{plugin.description}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                            prog='pydev',
                            description='''
A tool for deploying a local containerised python development environment, with a 
full web interface''',
                                     epilog='''
Notes:
  * You need to have docker installed (You can use Docker for windows as well)
  * You need to install docker-compose
                                     '''
                                     )

    parser.add_argument('-p', '--plugins',
                        dest='plugins_dir',
                        type=str,
                        help='The path to the pydev plugins directory, containing docker-compose files',
                        required=False,
                        default=path.join(Path.home(), '.pydev'))
    
    parser.add_argument('--no-verify',
                        action='store_false',
                        dest='verify',
                        default=True,
                        help='If specified the installation of docker & docker-compose will not be verified')

    parser.add_argument('-l', '--log-level',
                        dest='log_level',
                        choices=['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'],
                        default='INFO',
                        help='Sets the log level')

    args = parser.parse_args()

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=getattr(logging, args.log_level))

    logging.debug(f'args: {vars(args)}')

    main(**vars(args))