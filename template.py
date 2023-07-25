import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "text_summarizer_CI_CD"

list_of_file = [
    ".githubworkflow/.gitkeep", # for the deployment CI/CD
    f"scr/{project_name}/__init__.py", # __init__.py constructor file
    f"scr/{project_name}/component/__init__.py",
    f"scr/{project_name}/utils/__init__.py",
    f"scr/{project_name}/utils/common.py",
    f"scr/{project_name}/logging/__init__.py",
    f"scr/{project_name}/config/__init__.py",
    f"scr/{project_name}/config/configuration.py",
    f"scr/{project_name}/pipeline/__init__.py",
    f"scr/{project_name}/entity/__init__.py",
    f"scr/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "notebooks/test.ipynb"
]

for file_n_path in list_of_file:

    file_n_path = Path(file_n_path)  # it will automatically detach the operating system path
    filedir, filename = os.path.split(file_n_path)

    # create the folder
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory:{filedir} for the {filename}")
    
    #create the file

    if (not os.path.exists(file_n_path)) or (os.path.getsize(file_n_path)== 0):

        with open(file_n_path, 'w') as f:
            pass
        logging.info(f"Creaating empty file: {filename}")
    
    else:
        logging.info(f"{filename} already exists")




