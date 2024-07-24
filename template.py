import os 
from pathlib import Path
import logging

package_name = "mongodb_connect"

list = [
  ".github/workflows/ci.yaml",
  "src/__init__.py",
  "src/components/__init__.py",
  f"src/{package_name}/__init__.py",
  f"src/{package_name}/mongo_crud.py"
  "tests/__init__.py",
  "tests/unit/__init__.py",
  "tests/unit/test.py",
  "tests/integration/test.py"
  "tests/integration/__init__.py",
  "init_setup.sh",
  "requirements.txt",
  "requirements_dev.txt"
  "setup.py",
  "setup.cfg",
  "pyproject.toml",
  "tox.ini",
  "experiment/trials.ipynb",
  "src/logger/__init__.py",
  "src/exception/__init__.py"
  "src/logger/logging.py",
  "src/exception/exception.py"
]

for filepath in list:
  filepath = Path(filepath)
  filedir,filename = os.path.split(filepath)
  
  if filedir!="":
    os.makedirs(filedir,exist_ok=True)
    
  if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
    with open(filepath,"w") as f:
      pass
  
  