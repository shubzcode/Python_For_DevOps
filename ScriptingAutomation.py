import shutil
import os

def backup_folder(source_folder, backup_folder):
    try:
        if not os.path.exists(source_folder):
            print(f"Error: Source folder '{source_folder}' does not exist.")
            return

        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)

        shutil.copytree(source_folder, os.path.join(backup_folder, os.path.basename(source_folder)))

        print("Backup completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# ✅ Use raw string (r"") or double backslashes (\\) to fix SyntaxWarning
source_folder = r"E:\Code Master 2025\Python Programing\Dev ops py\Python_For_DevOps\source_folder"
backup_folder = r"E:\Code Master 2025\Python Programing\Dev ops py\Python_For_DevOps\backup_folder"
