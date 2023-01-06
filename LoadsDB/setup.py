from setuptools import setup

setup(
    name='LoadsDB',
    version='1.0.0',
    packages=['LoadsDB'],
    include_package_data=True,
    install_requires=[
        'json',
        'sys',
        "os"
    ],
    author='Loads',
    author_email='contact.loadsx@gmail.com',
    description='Working database system for python!',
    keywords='LoadsDB database',
    url='https://github.com/your-username/mypackage',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
