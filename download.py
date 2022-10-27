from os import mkdir
import requests
import zipfile
import os
from os import path
import sys

BASE_DIR = "stack-overflow-developer-survey-2022"
ZIP_FILENAME = "data.zip"

# Create directory if it doesn't exist already
if not path.exists(BASE_DIR):
  os.mkdir(BASE_DIR)
else:
  print(f"Error: Cannot download survey data directory \'{BASE_DIR}\' already exists.", file=sys.stderr)
  exit(1)

# Download zip file
res = requests.get("https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2022.zip")

zip_filepath = path.join(BASE_DIR, ZIP_FILENAME)

open(zip_filepath, "wb").write(res.content)

# Extract zip into folder
with zipfile.ZipFile(zip_filepath) as zip_ref:
  zip_ref.extractall(BASE_DIR)

# Cleanup unneeded files
os.remove(zip_filepath)
os.remove(path.join(BASE_DIR, "README_2022.txt"))
os.remove(path.join(BASE_DIR, "so_survey_2022.pdf"))



