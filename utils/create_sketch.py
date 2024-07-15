import os
from datetime import datetime

def create_sketch_file():
    dateToday = datetime.today().strftime('%Y_%m_%d')
    nameFile = f"./scripts/sketch_{dateToday}"
    os.makedirs(nameFile, exist_ok=True)
    return nameFile

def create_sketch_folder():
    dateToday = datetime.today().strftime('%Y_%m_%d')
    nameFile = f"./scripts/sketch_{dateToday}"
    nameFolder = f"sketch_{dateToday}.py"
    folderPath = os.path.join(nameFile, nameFolder)
    with open(folderPath, 'w') as folder:
        pass

if __name__ == "__main__":
    create_sketch_file()
    create_sketch_folder()

# poetry run python utils\create_sketch.py