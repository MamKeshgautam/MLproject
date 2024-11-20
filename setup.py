from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","") for req in requirements ]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='MLproject',
    author='Mamkesh',
    author_email='keshgautam25@gmail.com',
    version='1.0.0',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)