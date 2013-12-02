#! /usr/bin/python
import json
from subprocess import call
from os.path import abspath, dirname, join

basepath = abspath(dirname(__file__))
f = open(join(basepath, '../cookiecutter.json'))
conf = json.load(f)
path = (conf['repo_name'], conf['app_name'])
call(['ln', '-s', '../%s/%s' % path, '../%s/demo/%s' % path])