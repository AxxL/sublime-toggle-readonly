import sublime, sublime_plugin, os, stat

class ToggleReadonlyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
      # myFile = self.view.file_name()
      # sublime.status_message("hi")
      if (self.view.is_read_only()):
        self.view.set_read_only(0)
        sublime.status_message("Buffer " + self.view.file_name() + " is writeable again.")
      else :
        self.view.set_read_only(1)
        sublime.status_message("Buffer " + self.view.file_name() + " is set readonly.")
      