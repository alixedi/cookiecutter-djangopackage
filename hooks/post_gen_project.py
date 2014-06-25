#! /usr/bin/python
import os
from subprocess import check_call

repo_name = os.environ['repo_name']
app_name = os.environ['app_name']

os.chdir('../%s/%s/testproject' % (repo_name, app_name))
check_call(['ln', '-s', '../../%s' % app_name, './'])
