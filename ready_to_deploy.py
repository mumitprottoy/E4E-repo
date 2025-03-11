import os


def delete_files_in_folder(folder_path, exclude_files=None):
    exclude_files = exclude_files or []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file not in exclude_files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")


def clean_folders_by_name(root_directory, folder_name, exclude_files=None):
    for root, dirs, _ in os.walk(root_directory):
        if folder_name in dirs:
            folder_path = os.path.join(root, folder_name)
            delete_files_in_folder(folder_path, exclude_files)


if __name__ == "__main__":
    project_root = os.path.abspath(os.path.dirname(__file__))
    exclude_files = ["__init__.py"]
    print("Cleaning files in migrations folders...")
    clean_folders_by_name(project_root, "migrations", exclude_files)
    print("\nCleaning files in __pycache__ folders...")
    clean_folders_by_name(project_root, "__pycache__")
    print("\nCleanup completed!")
