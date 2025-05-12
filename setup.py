from setuptools import setup

setup(
    name='adgctl',
    version='0.1',
    py_modules=['cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''adg
        [console_scripts]
        adgctl=cli:cli
    ''',
)




