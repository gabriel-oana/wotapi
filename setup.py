import os
from setuptools import setup, find_packages

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))


# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(name='wotapi',
      version='0.4.5',
      description='Extract data from the World of Tanks PC API',
      author='Gabriel Oana',
      author_email='gabriel.oana91@gmail.com',
      license='MIT',
      url='https://gitlab.com/gabriel_oana/worldoftanks',
      zip_safe=False,
      long_description=README,
      long_description_content_type="text/markdown",
      packages=find_packages(),
      install_requires=[
            'requests',
            'sqlalchemy',
      ],
      classifiers=[
            "Development Status :: 4 - Beta",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Typing :: Typed',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
      ]
      )
