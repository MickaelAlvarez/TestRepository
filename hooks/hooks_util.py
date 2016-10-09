import subprocess
from hooks_declare import *
import hooks_files




# Execute "git diff HEAD~1 HEAD"
def get_diff_between_two_last_commit():
	return execute_git_cmd(["diff", "HEAD~1", "HEAD", "--name-status"], False).strip()

# Execute "git diff --name-status"
def get_diff_name_status() :
	return execute_git_cmd(["diff", "--name-status"], False).strip()

# Execute a command like "git argv..."
def execute_git_cmd(argv, print_it=True):
	full_cmd = argv
	full_cmd.insert(0, git_cmd)
	return execute_cmd(full_cmd, print_it)

"""
will execute the cmd in the system.
the main cmd and each argument have to be in an element of the list
return the value of the command
"""
def execute_cmd(arg_list, print_it=True):
	#create the proc
	proc = subprocess.Popen(arg_list, stdout=subprocess.PIPE)
	#communicate with the proc and get the stdout value
	stdout_value = proc.communicate()[0].decode("utf-8")
	if print_it != False :
		print(stdout_value)
	if proc.returncode != 0 :
		return proc.returncode
	return stdout_value

def get_current_branch_name():
	return execute_git_cmd( [ "rev-parse", "--abbrev-ref", "HEAD"], False ).strip()

def git_simple_commit(message):
	return execute_cmd([git_cmd, "commit", "-m", message ], print_it=False)

def git_reset_head(head):
	execute_cmd( [ git_cmd, "reset",  ("HEAD~" + str(head)) ], print_it=False)

def git_reset_head_hard(head):
	execute_git_cmd( [ "reset", "--hard", ("HEAD~" + str(head)) ], print_it=False)
	
def git_add_all():
	execute_cmd( [ git_cmd, "add", "--all"  ], print_it=False)

def get_the_x_last_commits(x):
	last_commits = execute_git_cmd( [ "log",  "--pretty=format:%h %B",  "-n",  str(x) ], False )
	return last_commits.splitlines()

def change_branch(branch_name):
	execute_git_cmd(["checkout", branch_name], False)

def merge_branch(to_merge):
	return execute_git_cmd(["merge", to_merge], False)

def cherry_pick_commit(sha1):
	return execute_git_cmd([ "cherry-pick", sha1], False)

def get_root_directory():
	return execute_cmd([ git_cmd, "rev-parse" ,"--show-toplevel"], print_it=False).strip() + "/"
