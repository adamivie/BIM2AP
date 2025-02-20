from setuptools import setup, find_packages

setup(
    name='bosch_mode2_automation',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Adam Ivie',
    author_email='adamivie@gmail.com',
    description='A library for interacting with Bosch Intrusion Mode 2 panels',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/adamivie/BIM2AP',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)