import os
import shutil
with open('label.lst', 'r') as f:
        source_dir = "origin"
        for lin in f:
            line = lin.strip()
            # Split the line into words
            words = line.split(sep=" ")

            # The first word is the image name, the last word is the folder name
            image_name, folder_name = words[0], words[-1]

            # Full path to the image file
            source_path = os.path.join(source_dir, image_name)

            # Check if the image file exists
            if os.path.isfile(source_path):
                # Create the folder if it doesn't exist
                os.makedirs(folder_name, exist_ok=True)

                # Full path to the destination
                dest_path = os.path.join(folder_name, image_name)
                print(f"{image_name} , Done")
                # Move the image file to the folder
                shutil.move(source_path, dest_path)

