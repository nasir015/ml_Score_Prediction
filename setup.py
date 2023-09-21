from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirments(file_path:str)->List[str]:
    '''
    This function will read the requirements.txt file and return a list of requirements
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.strip() for requirement in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = 'ml_project',
    version= '0.0.1',
    author= 'Nasir',
    author_email= 'nasir1515@student.nstu.edu',
    packages= find_packages(),
    install_requires = get_requirments('requirments.txt')
)