import sublime, sublime_plugin
import sys
import os
sys.path.append("/home/kahlil/.config/sublime-text-3/Packages/User/lib/python3.4/site-packages")
from git import Repo
import git



class ExampleCommand(sublime_plugin.WindowCommand):
	def run(self, edit):
		repo = git.Repo('/home/kahlil/test')
		sublime.message_dialog(str(repo.git.status())
		








# repo = git.Repo("/home/kahlil/test")
		# tree = repo.tree()
		# for obj in tree:
		# 	self.view.insert(edit, 0, str(obj), obj.path, repo.iter_commits(paths=obj.path, max_count=1).next())
#Repo.init("/home/kahlil/gitpython.git")


# # checkout and track a remote branch
# print repo.git.checkout( 'origin/somebranch', b='somebranch' )
# # add a file
# print repo.git.add( 'somefile' )
# # commit
# print repo.git.commit( m='my commit message' )
# # now we are one commit ahead
# print repo.git.status()

# class myOpener(sublime_plugin.EventListener):		
# 		def on_post_save(self,view):
# 			sublime.message_dialog("You have saved the file")
			
		

# 		#git commit code here
#  		# if (counter%5 == 0):
# 			# hello=0#git push code here