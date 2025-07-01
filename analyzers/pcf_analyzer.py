import os

def find_manifest_and_code(path):
    found_files = []
    for root, _, files in os.walk(path):
        for file in files:
            if file == "manifest.yml" or file.endswith(".java") or file.endswith(".yaml") or file.endswith(".csproj"):
                found_files.append(os.path.join(root, file))
    return found_files
