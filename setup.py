from setuptools import setup, find_packages

setup(
    name='hello_world',
    version='1.0.0',
    description='A simple Python script that prints "hello world"',
    py_modules=['hello_world'],
    entry_points={
        'console_scripts': [
            'hello_world = hello_world:main',
        ],
    },
)