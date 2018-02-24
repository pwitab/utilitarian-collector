from setuptools import setup

setup(
    name='utilitarian-collector',
    version='0.0.1',
    description='Server to receive and handle meter data in an extensible way',
    url='https://github.com/pwitab/utilitarian-collector',
    author='Henrik Palmlund Wahlgren, '
           'Palmlund Wahlgren Innovative Technology AB',
    author_email='henrik@pwit.se',
    license='BSD 3-Clause License',
    packages=['utilitarian_collector'],
    install_requires=['dlms_cosem', ]

)
