from setuptools import setup

setup(
    name='wsa-cli',
    version='0.0.1',
    py_modules=['wsa'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        mkwsa=wsa:mkwsa
    ''',
)
