import click
from yaml import safe_load
import time
from .backend import gnaw_backend_resources


@click.command()
@click.argument('configuration-file')
@click.option('--backend',
              help="Gnaw the cables of a list of backend resources.",
              is_flag=True)
@click.option('--time', default=10,
              help='Maximum period of time between each action.',
              type=int,
              show_default=True)
def main(configuration_file, backend, time):
    config = load_configuration(configuration_file)
    if backend:
        try:
            backend_resources = config["backend"]
        except KeyError:
            print("Missing backend section in configuration file.")
            exit(1)
    start_chaos(time, backend_resources)
    exit(0)


def start_chaos(t, backend_resources):
    while True:
        gnaw_backend_resources(backend_resources)
        time.sleep(sleepTime)


def load_configuration(configuration_file):
    with open(configuration_file, 'r') as stream:
        config = safe_load(stream)
        return config
