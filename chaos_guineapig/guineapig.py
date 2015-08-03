import click
from yaml import safe_load
from .backend import gnaw_backend_resources


@click.command()
@click.argument('configuration-file')
@click.option('--backend',
              help="Gnaw the cables of a list of backend resources.",
              is_flag=True)
def main(configuration_file, backend):
    config = load_configuration(configuration_file)
    if backend:
        try:
            backend_resources = config["backend"]
            gnaw_backend_resources(backend_resources)
        except KeyError:
            print("Missing backend section in configuration file.")
            exit(1)
    exit(0)


def load_configuration(configuration_file):
    with open(configuration_file, 'r') as stream:
        config = safe_load(stream)
        return config
