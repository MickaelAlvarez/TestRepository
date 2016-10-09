from hooks_util import *
from hooks_files import *
from hooks_declare import *
from shutil import copyfile
from shutil import copy2
from hooks_refactor import *


def commit_hook(argv):
	pre_commit()
	res = execute_git_cmd(argv, False)
	post_commit()


def pre_commit():
	git_reset_head(1)
	srv_refactor()
	git_add_all()

def post_commit():
	user_refactor()	