import sys
from hooks_util import *
from hooks_commit import *
from hooks_pull import *
from hooks_push import *


def main(argv):
	if "pull" in argv :
		pull_hook(argv)
	elif "push" in argv :
		push_hook(argv)
	elif "commit" in argv :
		commit_hook(argv)
	else :
		execute_git_cmd(argv, True)

if __name__ == "__main__":
   main(sys.argv[1:])
