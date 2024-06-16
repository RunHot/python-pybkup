def backup_folder(source_folder, backup_folder):
 try:
 # Check if source folder exists
 if not os.path.exists(source_folder):
 print(f"Source folder {source_folder} does not exist.")
 return

 # Check if backup folder exists, create if not
 if not os.path.exists(backup_folder):
 os.makedirs(backup_folder)

 # Get list of all files in source folder
 files = os.listdir(source_folder)

 # Loop through each file
 for file in files:
 # Construct full file path
 file_path = os.path.join(source_folder, file)

 # Backup file to backup folder
 shutil.copy2(file_path, backup_folder)

 print(f"Backed up {file_path} to {backup_folder}")
 except Exception as e:
 print(f"An error occurred: {e}")
