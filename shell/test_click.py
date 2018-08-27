import click


@click.command()
@click.option('--host','-H',  default='127.0.0.1', help='host')
@click.option('--port', '-p', prompt='input the port', default=3306, help='port')
def test(port,host):
    click.echo('host:%s,port:%s' % (host,port))


test()
