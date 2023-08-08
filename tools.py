import os

os.system("pip install pyyaml requests")
import yaml
import requests
import shutil
import argparse
import subprocess

def get_local_version():
    version_path = "config/version.yaml"
    
    if os.path.exists(version_path):
        with open(version_path, "r") as version_file:
            current_version = yaml.safe_load(version_file).get("version", "")
        return current_version
    return ""


def update_local_version(new_version):
    version_path = "config/version.yaml"
    with open(version_path, "w") as version_file:
        yaml.dump({"version": new_version}, version_file)

def execute_commands(commands):
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError:
            print(f"Failed to execute command: {command}")

def install_files():
    download_files = ["main.py", "version.yaml", "config.py"]  # Ajoutez les fichiers à télécharger ici
    
    for file in download_files:
        download_url = f"https://raw.githubusercontent.com/EletrixTimeYT/TimeWeb/main/{file}"
        try:
            response = requests.get(download_url, stream=True)
            response.raise_for_status()
            with open(file, "wb") as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
        except (requests.exceptions.RequestException, IOError):
            print(f"Unable to download {file} from GitHub.")


def check_update(update_libs=False, install=False):
    current_version = get_local_version()

    github_url = "https://raw.githubusercontent.com/EletrixTimeYT/TimeWeb/main/version.yaml"  # Mettez à jour avec votre URL GitHub
    
    response = requests.get(github_url)
    response.raise_for_status()
    data = yaml.safe_load(response.text)  # Chargez les données depuis la réponse YAML

    github_version = data.get("version", "")
    update_files = data.get("update_files", [])
    update_libs_list = data.get("update_libs", [])
    update_commands = data.get("update_commands", [])

    if current_version != github_version:
        print("An update is available.")

        # Supprimer les fichiers qui doivent être mis à jour
        for file in update_files:
            if os.path.exists(file):
                os.remove(file)

        for file in update_files:
            download_url = f"https://raw.githubusercontent.com/EletrixTimeYT/TimeWeb/main/{file}"
            try:
                response = requests.get(download_url, stream=True)
                response.raise_for_status()
                with open(file, "wb") as f:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, f)
            except (requests.exceptions.RequestException, IOError):
                print(f"Unable to download {file} from GitHub.")


        if update_libs:
            print("Updating libraries...")
            for lib in update_libs_list:
                subprocess.run(["pip", "install", "--upgrade", lib])
            print("Libraries update completed.")

        if update_commands:
            print("Executing update commands...")
            execute_commands(update_commands)
            print("Commands execution completed.")

        if install:
            print("Installing files...")
            install_files()
            print("Files installation completed.")

        update_local_version(github_version)  # Mettre à jour la version locale dans le fichier version.yaml
        print("Update completed.")
    else:
        print("No update available.")

def main():
    parser = argparse.ArgumentParser(description="Check for updates and perform upgrades.")
    parser.add_argument("--upgrade", action="store_true", help="Upgrade the application if an update is available.")
    parser.add_argument("--update-libs", action="store_true", help="Update libraries listed in version.yaml.")
    parser.add_argument("--install", action="store_true", help="Install files from GitHub.")
    args = parser.parse_args()

    if args.upgrade:
        check_update(update_libs=args.update_libs, install=args.install)
    elif args.install:
        install_files()
    else:
        print("Please provide the --upgrade or --install flag to perform an upgrade or install.")

if __name__ == "__main__":
    main()
