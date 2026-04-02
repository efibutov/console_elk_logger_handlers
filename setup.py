from setuptools import setup, find_packages

setup(
    name='console-elk-logger-handlers',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'elasticsearch>=7.0.0',
        'termcolor>=1.0.0',
    ],
    author='Efi Butovski',
    description='Simple colored console and ELK logger for Python',
    license='MIT',
    python_requires='>=3.8',
)
