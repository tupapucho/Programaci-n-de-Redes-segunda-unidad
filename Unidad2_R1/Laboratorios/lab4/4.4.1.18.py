import os

def find(path, target_dir):
    for root, dirs, files in os.walk(path):
        if target_dir in dirs:
            print(os.path.abspath(os.path.join(root, target_dir)))

# Ejemplo de uso
path = "./tree"
target_directory = "python"
find(path, target_directory)
