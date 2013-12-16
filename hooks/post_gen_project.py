#! /usr/bin/python
import os
import json
from subprocess import call
from os.path import abspath, dirname, join

basepath = abspath(dirname(__file__))
path = (os.environ['repo_name'], os.environ['app_name'])
call(['ln', '-s', '../%s/%s' % path, '../%s/demo/%s' % path])
