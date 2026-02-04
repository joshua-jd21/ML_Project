'''
An “instruction manual” for your project. It tells Python:
This is my project.
This is its name.
This is its version.
These are the libraries it needs.
This is how to install it. 

Without setup.py:
❌ Engineer must:
•Manually copy files
•Install libraries
•Fix errors
•Guess versions
Messy. Slow. Risky.
'''

from setuptools import setup, find_packages

setup(
    name='ML_PROJECT',
    version='0.0.1',
    author='Joshua A David',
    author_email='joshuajdyo@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn']   
)
