from setuptools import setup, find_packages

setup(
    name='console_elk_logger_handlers',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'elastic-transport==9.2.1',
        'elasticsearch==9.3.0',
        'python-dateutil==2.9.0.post0',
        'requests==2.33.1',
        'termcolor==3.3.0',
    ],
    author='Efi Butovski',
    description='Simple colored console and ELK logger for Python',
    python_requires='>=3.12',
)
