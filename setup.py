from setuptools import setup

setup(name="MultipleContext",
      version="0.1",
      description="This django package allow to add additionnal context into class-based view",
      author="Anthony Tresontani",
      packages = ['multiplecontexts'],
      install_requires=["Django>=1.3"])