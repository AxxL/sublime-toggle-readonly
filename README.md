Toggle readonly state of buffer from context menu for Sublime Text 2 and 3 (beta)

## Installation
Install this repository via [Package Control](http://wbond.net/sublime_packages/package_control)
Or put the files into a directory in your {sublime}\Data\Packages\ folder

## Usage
You have a context-menu on:
- the tab
- the open files
- and direct in the edit area.

If you toggle the readonly, the status bar says: "Buffer {buffername} is set readonly." and you cannot make any changes.

If you toggle again the status bar says: "Buffer {buffername} is writeable again." and the file should be editable again.

This tool doesn't change the file properties in the filesystem. It only changes the readonly attribute of the current view.

See: http://www.sublimetext.com/docs/2/api_reference.html#sublime.View

## Update
01.03.2013:
Toggle Read Only as command: https://github.com/AxxL/sublime-toggle-readonly/pull/1
Update for Sublime 3: https://github.com/AxxL/sublime-toggle-readonly/issues/2

Well, it takes some time.... Thanks for your patience. :)

## Link
https://github.com/AxxL/sublime-toggle-readonly