import os, sys

##########################################################################################

#############################################################
# CONFIGURATION - Change this to better suit you
#############################################################

# Name of the folder you want to create to auto-organize files
dop_folder_name = "Auto-Organized Files"

# Your desktop path goes here
desktop_path = "C:/Users/Edmilson/Desktop"

# A dictionary with the file extension and its subfolder name e.g "png": "Images/Static"
extensions_to_catch = {"gif": "Images/Animated","jpg": "Images/Static","txt":
"Texts","mobi": "Books","epub": "Books","png": "Images/Static","mp3": "Audios", "pdf": 
"Documents", "unitypackage": "Unity/Packages", "zip": "Zipped Files", "rar": "Zipped Files",
"7z": "Zipped Files"}

##########################################################################################

#############################################################
# LOGIC - Do not change below unless you know what you're doing
#############################################################

def move_file_to_folder(file, folder_name):
	final_path_name = desktop_path + "/" + dop_folder_name + "/" + folder_name

	if not os.path.exists(final_path_name):
		os.makedirs(final_path_name)

	os.rename(desktop_path + "/" + file, final_path_name + "/" + file)


def organize_desktop():
    
	files_to_move = []

	if not os.path.exists(desktop_path + "/" + dop_folder_name):
		print("Didn't find folder {0}, creating one now.".format(dop_folder_name))
		os.makedirs(desktop_path + "/" + dop_folder_name)

	for file in os.listdir(desktop_path):
		for extension_key in extensions_to_catch:
			if file.endswith(extension_key):
				files_to_move.append(file)
				break

	for file in files_to_move:
		moved_folder = ""
		for key, value in extensions_to_catch.items():
			if file.endswith(key):				
				moved_folder = value
				break

		print("Moving file: {0}... to\t\t\t\t\t{1}".format(file[:10], moved_folder))
		move_file_to_folder(file, moved_folder)

	print("Successfully moved {0} files. Yay, cleaner desktop!".format(len(files_to_move)))


def main(argv):
	organize_desktop()

if __name__ == "__main__":
	main(sys.argv)