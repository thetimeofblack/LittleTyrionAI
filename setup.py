import os
import setuptools

setuptools.setup(
    name='LittleBoyAI',
    version='0.1',
    packages=setuptools.find_packages(),
    description='New response robotics for NLP',
    long_description=open(os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'README.md')).read(),
    license=' ',
    url=' ',
    install_requires=['numpy',
                      'Theano',],
    dependency_links=['  ',],
    classifiers=['  ',
                 '   ',
                 '   ',
                 '   ',
                 '  '],
)