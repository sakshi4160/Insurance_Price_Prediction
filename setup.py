from setuptools import find_packages, setup
from typing import List


requirement_file_name = "requirements.txt"

HYPHEN_E_DOT = "-e ."


def get_requirements() -> List[str]:
    with open(requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.strip() for requirement_name in requirement_list]

 
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        
        return requirement_list



setup(name='Insurance Price Prediction',
      version='0.0.1',
      description= """The goal of this project is to provide individuals with an estimate of 
                    how much coverage they need based on their individual health situation. 
                    Subsequently, customers can engage with any health insurance carrier and 
                    explore its plans and perks while keeping the projected cost from our study in mind. 
                    This can assist individuals in focusing on the health aspects of an insurance policy 
                    rather than the less effective parts.""",
      author='Sakshi Choube',
      author_email='sakshichoube423@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements()
     )