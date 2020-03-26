"""Script that installs 'extractor' package.

To install one should run 'python3 setup.py install' 
command. Afterwards, you will be able to run the package
using 'extractor' command.
"""

from setuptools import setup, find_packages

setup(
    name='extractor',
    version='1.0',
    packages=find_packages(),
    install_requires=('Scrapy>=2.0.0',),
    entry_points={
        'console_scripts': (
            'extractor=extractor.main:run',
        )
    }
)
