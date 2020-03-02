from setuptools import setup

setup(
    name='extractor',
    version='0.1',
    entry_points={
        'console_scripts': [
            'extractor=app:run'
        ]
    }
)
