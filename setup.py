from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='console_elk_logger_handlers',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,
    author='Efi Butovski',
    description='Simple colored console and ELK logger for Python',
    python_requires='>=3.12',
)
