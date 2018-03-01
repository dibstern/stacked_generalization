from setuptools import setup, find_packages 
from codecs import open  
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='stacked_generalization',
    packages=find_packages(),
    version='0.0.0',
    description='Fork of Python implementation of stacked generalization. Plays nicely with sklearn. Updated for Python 3.',
    long_description=long_description,    
    url='https://github.com/dibstern/stacked_generalization',
    author='David Stern',
    author_email='https://dibstern@gmail.com',
    keywords='machine learning, stacked generalization, ensemble methods, classification algorithms',

    install_requires=['numpy>1.6.1',
                      'scipy',
                      'scikit-learn'
                      ],
)
