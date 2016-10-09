from hooks_util import *
from hooks_files import *
from hooks_declare import *
from hooks_commit import *
from hooks_refactor import *


def push_hook(argv):
	
	pre_push()

	res = execute_git_cmd(argv)

	#then post_push operations
	post_push()
	

def pre_push():
	git_reset_head_hard(1)


def post_push():
	#we simply apply the user_refactor process
	user_refactor()
