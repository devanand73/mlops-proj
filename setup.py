from setuptools import setup, find_packages

HYPEN_E_DOT = '-e .'
def get_requirement():
    
    requirements=[]
    with open('requirements.txt', 'r') as f:
        requirements = f.read().splitlines()
        if HYPEN_E_DOT in requirements:
          requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="mlops-proj",
    version="0.1",
    description="End to end ML-opd Project Deployment to cloud",
    author="devanand73",
    author_email="devanand73@yahoo.c0.uk",
    packages=find_packages(),
    install_requires=get_requirement(),
    entry_points={
        "console_scripts": [
            "your_command_name = your_package_name.module:main",
        ],
    },
)
