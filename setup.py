from setuptools import setup

setup(
    name='i3-workspace-switch',
    version='0.2-dev',

    author='Johannes Wienke',
    author_email='languitar@semipol.de',
    url='https://github.com/languitar/i3-workspace-switch',
    license='LPGLv3+',

    install_requires=['i3-py'],

    scripts=['i3-workspace-switch']
)
