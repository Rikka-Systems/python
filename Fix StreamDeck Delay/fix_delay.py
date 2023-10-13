import os
import json
from rich.traceback import install

install()


def find_manifests(directory):
    manifests = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file == 'manifest.json':
                manifests.append(os.path.join(root, file))
    return manifests


def replace_values_in_manifests(manifests):
    for manifest in manifests:
        with open(manifest, 'r') as file:
            data = json.load(file)

        # Check if the specific JSON pattern is present in the file
        if data == {"Delay1": 100, "Delay2": 100}:
            data = {"Delay1": 1, "Delay2": 1}

        with open(manifest, 'w') as file:
            json.dump(data, file, indent=4)


if __name__ == "__main__":
    # Replace 'your_directory_path' with the path of the directory you want to search
    directory_path = 'C:\\Users\\Loki\\AppData\\Roaming\\Elgato\\StreamDeck\\ProfilesV2'

    manifests_paths = find_manifests(directory_path)
    replace_values_in_manifests(manifests_paths)
    print("Replacements done successfully.")
