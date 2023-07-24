# Find all the packages automitically for intire ML application
from setuptools import find_packages,setup

__version__ = '0.0.1'
REPO_NAME = 'text_summarizer_CI_CD_HuggingFace'
AUTHOR_USER_NAME = 'TmnGitHub'
SRC_REPO = "textSummarizerCICD"
AUTHOR_EMAIL = 'tamanupadhaya@gmail.com'
DESCRIPTION = 'A small NLP text summarizer application'


with open("README.md", "r", encoding="utf-8") as file_obj:
    long_description = file_obj.read()


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description = DESCRIPTION,
    long_description = long_description,
    long_descritpion_content="text/markdown",
    url= f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_url = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=find_packages(where="src"),
)
