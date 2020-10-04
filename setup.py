from setuptools import setup

setup(
    name="scf",
    version="0.1.0",
    description=("Python package for working with the Survey of Consumer " +
                 "Finances microdata."),
    url="http://github.com/maxghenis/scf",
    author="Max Ghenis",
    author_email="mghenis@gmail.com",
    license="MIT",
    packages=["scf"],
    install_requires=[
        "numpy",
        "pandas",
        "microdf",
    ],
    zip_safe=False,
)
