from setuptools import setup, find_packages

setup(
    name='template_injector',
    version='0.1.0',  # The initial release version
    author='Ricardo Semião e Castro',  # Your name or your organization's name
    author_email='ricardo.semiao@outlook.com',  # Your email or your organization's email
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[
        sys,
        os,
        re,
        bs4
    ],
    python_requires='>=3.6',  # Minimum version requirement of the Python interpreter
)
