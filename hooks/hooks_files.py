import os
from hooks_declare import *
import hooks_util
from distutils.dir_util import copy_tree


# Files

def write_file(path, data, mode="a+"):
	f = open(path, mode)
	if type(data) is list:
		f.write("\n".join(data))
	else:
		f.write(data)
	f.close()


def read_file(path):
	f = open(path, 'r')
	file_str = f.read()
	f.close()
	return file_str

def delete_folder_with_files(path):
	shutil.rmtree(path)

def copy_folder(src, dst):
    # copy subdirectory example
	fromDirectory = src
	toDirectory = dst
	copy_tree(fromDirectory, toDirectory)