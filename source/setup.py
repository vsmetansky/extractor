from setuptools import setup

setup(
    name='extractor',
    version='0.1',
    install_requires=(
        'Scrapy>=2.0.0',
    ),
    entry_points={
        'console_scripts': (
            'extractor=app:run',
        )
    }
)
