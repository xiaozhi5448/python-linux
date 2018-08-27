#!/usr/bin/env python
import click


@click.command()
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
def getpass(password):
    print 'you password:',password

getpass()
