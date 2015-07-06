import sublime, sublime_plugin
import subprocess

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		counter =0
		self.view.on_post_save(view)
		#git commit code here
		counter += 1
		if (counter%5 == 0):
			self.view.insert(edit, 0, str(counter))#git push code here