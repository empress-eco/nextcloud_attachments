# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in attachments_on_nextcloud/__init__.py
from attachments_on_nextcloud import __version__ as version

setup(
	name='attachments_on_nextcloud',
	version=version,
	description='Grynn App for NextCloud Backup',
	author='Grynn GMBH',
	author_email='deepakpai@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
