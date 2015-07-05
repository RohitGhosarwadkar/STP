import sublime, sublime_plugin
import subprocess

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		counter =0
		self.view.on_load(view)
		#initialize git repository here
		self.view.on_post_save(view)
		#git commit code here
		counter += 1
		if (counter%5 == 0):
			hello=0#git push code here