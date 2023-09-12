from setuptools import setup ,find_packages


def get_requirements(filepath):
    requirements = []
    with open(filepath, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    return requirements

setup(
    name = "Project Pipe Line",
    version = '0.0.1',
    description= "Implementing Test project for ML Pipe Line",
    author= "SajidMajeed",
    author_email='sajidmajeed.ist@gmail.com',
    packages = find_packages(),
    install_requirements = get_requirements('requirements.txt')
)