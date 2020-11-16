from setuptools import setup, find_packages

setup(
    name='php_parser',
    version='1.0.0',
    url='https://github.com/eljosephavila123/php_parser',
    author='Joseph Danilo Avila Alvarez-Daniel Roberto Sanchez Jarrin-Angel Arturo Jumbo Apolo',
    author_email='josdavil@espol.edu.ec',
    description='php compiler',
    packages=find_packages(),    
    install_requires=['ply >= 3.5']
)