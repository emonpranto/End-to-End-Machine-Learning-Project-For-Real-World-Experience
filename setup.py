from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)->List[str]:
    HYPEN_E_DOT = '-e .'
    '''
    This func will return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='End-to-End-Machine-Learning-Project',
    version='0.0.1',
    author='Tawshok',
    author_email='emon.pranto@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)