import sublime
import sublime_plugin


class ToggleReadonlyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if (self.view.is_read_only()):
            self.view.set_read_only(False)
            self.view.set_status('toggle_readonly', '')
            sublime.status_message("Buffer " + str(self.view.file_name()) + " is writeable again.")
        else:
            self.view.set_read_only(True)
            self.view.set_status('toggle_readonly', 'Readonly')
            sublime.status_message("Buffer " + str(self.view.file_name()) + " is set readonly.")


class ToggleReadonlyListener(sublime_plugin.EventListener):
    @staticmethod
    def check_readonly(view):
        if view.is_read_only():
            view.set_status('toggle_readonly', 'Readonly')
        else:
            view.set_status('toggle_readonly', '')

    def on_activated(self, view):
        ToggleReadonlyListener.check_readonly(view)