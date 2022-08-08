from setuptools import setup, find_packages
from setuptools.command.install import install
from os import path
import subprocess

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # $ pip install violet
    name='ancestry',
    version='0.0.1',
    description='A tool for ancestry prediction',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ding-lab/ancestry-pipeline',
    author='Erik Storrs',
    author_email='estorrs@wustl.edu',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    keywords='Ancestry bam genomics',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        ],
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'run-ancestry=ancestry.main:main',
        ],
    },
)
