from fabric.api import *
from fabric.contrib.console import confirm
from fabric.colors import green
from fabric.utils import abort

env.hosts = ['192.168.56.101', '192.168.56.102']
env.user = 'root'
env.password = 'wodemima'
env.port = 22


@task
@runs_once
def local_test():
    local("tar -xf redis-4.0.9.tar.gz")
    with lcd('redis-4.0.9'), settings(warn_only=True):
        result = local("make && make test", capture=True)
        if result.failed and not confirm("Tests failed, continue anyway?"):
            abort("Aborting at user request!")
        else:
            print green("all tests passed without error")


@task
def put_file():
    put('redis-4.0.9.tar.gz', '/tmp/redis-4.0.9.tar.gz')


@task
def install():
    with cd('/tmp'):
        run('tar -xf redis-4.0.9.tar.gz')
        with cd('/tmp/redis-4.0.9'):
            run('make && make install')


@task
def clean_local():
    local("rm -rf redis-4.0.9")


@task
def install_process():
    execute(local_test)
    execute(put_file)
    execute(install)
    execute(clean_local)

