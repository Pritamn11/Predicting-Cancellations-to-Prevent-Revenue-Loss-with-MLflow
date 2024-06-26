from setuptools import setup, find_packages


with open('README.md','r', encoding='utf-8') as f:
    project_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Predicting-Cancellations-to-Prevent-Revenue-Loss-with-MLflow"
AUTHOR_USER_NAME = "Pritamn11"
SRC_REPO = "src"
AUTHOR_EMAIL = "pritamnarwade11@gmail.com"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=project_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages= find_packages(where="src")
)