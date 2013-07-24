import sublime, sublime_plugin, os, stat

class ToggleReadonlyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if (self.view.is_read_only()):
			if (int(sublime.version()) > 3000):
				self.view.set_read_only(False)
			else:
				self.view.set_read_only(0)
			sublime.status_message("Buffer " + str(self.view.file_name()) + " is writeable again.")
		else:
			if (int(sublime.version()) > 3000):
				self.view.set_read_only(True)
			else:
				self.view.set_read_only(1)
			sublime.status_message("Buffer " + str(self.view.file_name()) + " is set readonly.")