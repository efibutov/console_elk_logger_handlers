from setuptools import setup, find_packages

setup(
    name='console_elk_logger_handlers',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.0',
    ],
    author='Efi Butovski',
    description='Simple colored console and ELK logger for Python',
    python_requires='>=3.12',
)

