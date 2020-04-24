
import os

def read_and_delete():
	img_files=[]
	path_to_db = os.path.join(os.getcwd(),'static','uploads','img_names.txt')
	with open(path_to_db,'r') as file:
		for line in file:
			img_files.append(line.split('\n')[0])
		#print(img_files)
	for f in img_files:
		if os.path.isfile(f):
			print(f"File :[ {f} ] -> deleted")
			os.remove(os.path.join(os.getcwd(),'static','uploads',f))
	with open(path_to_db,'w') as f:
		print('img_names.txt cleared')
		f.write('')

def write_uploaded(file):
	path_to_db = os.path.join(os.getcwd(),'static','uploads','img_names.txt')
	with open(path_to_db,'a') as f:
		print(f"{file} name updated")
		f.write(file+'\n')