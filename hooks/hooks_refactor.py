from hooks_util import *
from hooks_files import *
from hooks_declare import *

hooks_folder = "hooks/"
server_profile_path = "profiles/server/profile.xml"
client_profile_path = "profiles/client/profile.xml"
refactor_jar = "refactor.jar"

def srv_refactor(commit_msg=None):
	refractor = get_root_directory() + hooks_folder + refactor_jar
	srv_profile = get_root_directory() + hooks_folder + server_profile_path
	folder = get_root_directory()

	os.system("java -jar " + refractor + " " + srv_profile + " " + folder)
	
	#the rebased commit (if we have to)
	if commit_msg :
		git_add_all()
		git_simple_commit(commit_msg)
	
	
def user_refactor():
	refractor = get_root_directory() + hooks_folder + refactor_jar
	client_profile = get_root_directory() + hooks_folder + client_profile_path
	folder = get_root_directory()

	os.system("java -jar " + refractor + " " + client_profile + " " + folder)
	
	
	#adding all refactored files
	git_add_all()
	
	#then we commit it with our default message
	git_simple_commit(user_refact_msg)