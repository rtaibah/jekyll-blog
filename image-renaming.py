import os
import glob
import re

directory = '/home/rami/projects/jekyll-blog/assets/images/content/lifestream/'
picfiles = glob.glob(r'/home/rami/projects/jekyll-blog/assets/images/content/zeitgeist/*/*/*/*.png')

# clean up the folder namings with these replacements

#[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace(' ', '-').lower()) for f in os.listdir(directory)]
#[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace('.', '')) for f in os.listdir(directory)]
#[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace(',', '')) for f in os.listdir(directory)]
#[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace(':', '')) for f in os.listdir(directory)]
#[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace('!', '')) for f in os.listdir(directory)]
#[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace('[PIC]', '')) for f in os.listdir(directory)]


# Use below to rename all images, add numbers to the end of the file and move them to the root of the folder

# file_list = []
# 
# for f in picfiles:
#     file_list.append(f)
# 
# counter = 1
# current_filename_path = ''
# 
# for file in file_list:
#     new_filename = re.search('(?<=zeitgeist\/).+?(?=\/)',file).group(0)+'-'+str(counter)+'.png'
#     new_filename_path = directory + new_filename
# 
#     working_filename_path = re.search('.+(?<=image)',file ).group(0)
# 
#     if current_filename_path == working_filename_path:
#         os.rename(file, new_filename_path)
#         counter =counter + 1
#     else:
#         counter = 1
#         current_filename_path = re.search('.+(?<=image)',file ).group(0)
#         os.rename(file, new_filename_path)

# After manually removing duplicate images, you can remove the appended numbers to the file
[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace('-1', '')) for f in os.listdir(directory)]
