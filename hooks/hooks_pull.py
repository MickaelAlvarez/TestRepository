from hooks_util import *
from hooks_refactor import *



def pull_hook(argv):
	pre_pull()
	
	execute_git_cmd(argv)
	#post_pull 
	post_pull()

	
def pre_pull():
	git_reset_head_hard(1)


def post_pull():
	user_refactor()
	
