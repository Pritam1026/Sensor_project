from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(filepath:str='requirements.txt')->List[str]:
    requirements=[]
    # reading the files
    with open(filepath,'r') as file_obj:
        lines=file_obj.readlines()

        #Replacing '\n' with ''
        for line in lines:
            requirements.append(line.replace('\n',''))

    #Removing '-e .' from requirements list
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements



#Setup file
setup(
    name='Sensor',
    version='0.0.1',
    author='Pritam',
    author_email='singhpritam983@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)