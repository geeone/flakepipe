import os

from setuptools import setup, find_packages


path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(path, "requirements.txt")) as f:
    requirements = f.read().splitlines()

with open(os.path.join(path, "README.md"), "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='flakepipe',
    version='0.1.2',
    author='Sergei Denisenko',
    author_email='sergei.denisenko@ieee.org',
    description='Reusable module for uploading datasets to Snowflake via stage',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/geeone/flakepipe',
    project_urls={
        'Documentation': 'https://github.com/geeone/flakepipe',
        'Source': 'https://github.com/geeone/flakepipe',
        'Bug Tracker': 'https://github.com/geeone/flakepipe/issues',
    },
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    license='MIT',
    python_requires='>=3.8,<3.12',
    install_requires=requirements,
    keywords='snowflake upload ETL csv stage data',
)
