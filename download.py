from os import mkdir
import requests
import zipfile
import os
from os import path
import sys

MAIN_DIR = "surveys"
ZIP_FILENAME= "data.zip"
dirs = [str(year) for year in range(2011, 2023)]

if not path.exists(MAIN_DIR):
  os.mkdir(MAIN_DIR)
else:
  print(f"Error: Cannot download survey data directory \'{MAIN_DIR}\' already exists.", file=sys.stderr)
  exit(1)

for dirname in dirs:
  os.mkdir(path.join(MAIN_DIR, dirname))
  url = f'https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-{dirname}.zip'
  res = requests.get(url)
  zip_filepath = path.join(MAIN_DIR, dirname, ZIP_FILENAME)
  open(zip_filepath, "wb").write(res.content)
  with zipfile.ZipFile(zip_filepath) as zip_ref:
    zip_ref.extractall(path.join(MAIN_DIR, dirname))
    os.remove(zip_filepath)
