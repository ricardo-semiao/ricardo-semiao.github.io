from setuptools import setup, find_packages

setup(
    name='template_injector',
    version='0.1.0',
    author='Ricardo Semião e Castro',
    author_email='ricardo.semiao@outlook.com',
    packages=find_packages(),
    install_requires=[
        'beautifulsoup4>=4.9.0'
    ],
    python_requires='>=3.6',
)
