from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT ='-e.'
def get_requirements(file_path :str)-> List[str]:
    '''
    This function will return list of requiremnts
    '''
    requirements=[]
    with open(file_path,'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', "") for req in requirements]



        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        
    


setup(
name = "Data Eng",
version = '0.0.1',
author = 'Prajwal',
email = 'ferrari0592@gmail,com',
packages = find_packages(),
install_requires= get_requirements('requirements.txt')  
)