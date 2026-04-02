from setuptools import setup, find_packages

setup(
    name='console-elk-logger-handlers',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'elasticsearch>=7.0.0',
        'termcolor>=1.0.0',
        'anyio==4.13.0',
        'certifi==2026.2.25',
        'charset-normalizer==3.4.6',
        'coloredlogs==15.0.1',
        'elastic-transport==9.2.1',
        'humanfriendly==10.0',
        'idna==3.11',
        'python-dateutil==2.9.0.post0',
        'requests==2.33.1',
        'six==1.17.0',
        'sniffio==1.3.1',
        'termcolor==3.3.0',
        'typing_extensions==4.15.0',
        'urllib3==2.6.3'
    ],
    author='Efi Butovski',
    description='Simple colored console and ELK logger for Python',
    license='MIT',
    python_requires='>=3.8',
)
