from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''this function will return the list of requirements'''
    requirement=[]
    with open(file_path) as file_obj:
        requirement= file_obj.readlines()
        requirement= [req.replace("\n","") for req in requirement]

        if HYPHEN_E_DOT in requirement:
            requirement.remove(HYPHEN_E_DOT)

    return requirement

setup(
name= 'mlprojects',
version= "0.0.1",
author= "Aditya",
author_email= "arrowav36@gmail.com",
packages= find_packages(),
install_requires= get_requirements('requirements.txt')  #this function is used as it is very hectic to write multiple libraries, hence this function will fetch it from requirements.txt
)