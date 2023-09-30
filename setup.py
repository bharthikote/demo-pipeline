from setuptools import setup, find_packages

setup(name = "census-income",
      version= "0.0.1",
      author = "bharath",
      author_email = "bharathharthikote@gmail.com",
      pacages = find_packages(),
      install_requires = ["pandas", "numpy", "flask"]
      )