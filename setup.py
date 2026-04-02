from setuptools import setup, find_packages

setup(
    name='console_elk_logger_handlers',
    version='0.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    install_requires=[
        'elastic-transport',
        'elasticsearch',
        'python-dateutil',
        'termcolor',
    ],
    author='Efi Butovski',
    author_email='efibutov@gmail.com',
    description='Simple colored console and ELK logger for Python',
    python_requires='>=3.11',
)
