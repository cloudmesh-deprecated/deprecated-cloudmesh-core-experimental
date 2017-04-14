import click

from .boot.main import boot
from .delete.main import delete

import logging
logger = logging.getLogger(__name__)

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS)
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def main(ctx, debug):
    """Some description"""
    logging.basicConfig(level=logging.INFO)


main.add_command(boot)
main.add_command(delete)


if __name__ == '__main__':
    main()
