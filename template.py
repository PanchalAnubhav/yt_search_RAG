import os
from pathlib import Path


project_name = "yt_search_RAG"
list_of_files = [
    f"{project_name}/__init__.py",
   
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/fetch.py",
    f"{project_name}/components/index_searching.py",
    f"{project_name}/components/channel_querry.py",
   
    "app.py",
    "requirements.txt",
    "setup.py",
]


for filepath in list_of_files:

    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)           # to split the path into directory and file name

    if filedir != "":                                    # to check if directory is not empty
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):  # to check if file exists or not
        with open(filepath, "w") as f:
            pass
    else:
        print(f"{filename} already exists")