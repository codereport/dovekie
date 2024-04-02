from setuptools import setup, find_packages

setup(
    name="dovekie",
    version="0.2.0",
    packages=find_packages(),
    description="A library that defines common SKI combinators from Combinatory Logic.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Conor Hoekstra",
    author_email="codereport@outlook.com",
    license="MIT",
    install_requires=[],
    python_requires='>=3.6',
)
