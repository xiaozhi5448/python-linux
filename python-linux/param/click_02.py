#!/usr/bin/env python
import click

@click.command()
@click.option('--host',type=click.Choice(['127.0.0.1']), prompt='please type host:')
def hash(host):
    print host

hash()

