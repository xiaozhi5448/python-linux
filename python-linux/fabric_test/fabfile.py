from fabric.api import run, sudo
from fabric.api import env, cd, local
from fabric.api import task
from fabric.api import roles
from fabric.api import hosts
from fabric.api import runs_once
from fabric.utils import abort, warn, puts
from fabric.colors import *

env.hosts=['192.168.56.101', '192.168.56.102']
env.port=22
env.user='root'
env.password='wodemima'
env.roledefs={
        'test1':['192.168.56.101'],
        'test2':['192.168.56.102']
        }
@hosts('192.168.56.102')
@task
def hostname():
    warn('test warn message')
    puts(green('green message'))
    puts(red('red message'))
    run('hostname')


@roles('test1')
@task
def ls(path='./'):
    run('ls {}'.format(path))

@roles('test2')
@task
def tail(path='/etc/passwd', line=10):
    sudo('tail -n {0} {1}'.format(line, path))


@roles('test1')
@roles('test2')
@task
def lswww():
    with cd('/var/www'):
        run('ls -l')

@runs_once
@task
def localls():
    local('ls -l')
