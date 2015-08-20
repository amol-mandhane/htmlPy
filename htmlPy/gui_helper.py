import htmlPy
from PySide import QtGui
import json


class GUIHelper(htmlPy.Object):
    """ A class which adds some essential functionalities to GUI javascript.

    An instance of this class is binded to GUI javascript by default. Do not
    use this class manually.

    """

    @htmlPy.Slot(str)
    def log_to_console(self, string):
        """ Prints the string to python console.

        The method is binded to GUI javascript. Thus, the string comes from GUI

        Arguments:
            string (str): The string to be printed.
        """
        print(string)

    @htmlPy.Slot(str, result=str)
    def file_dialog(self, filters="[]"):
        """ Opens a file selection dialog with given extension filter.

        HTML file inputs cannot be directly used with :py:class:`htmlPy.AppGUI`
        . This function, when binded to GUI javascript, gives a method to open
        a file dialog from javascript. With help of ``binder.js``, this task
        is automated with HTML file input.

        Keyword arguments:
            filters (str): A JSON array of javascript objects of type {"title":
                str (Title of the file extension), "extensions": str (space
                separated list of extension wildcards)}. Example ``[{"title":
                "JPEG files", "extensions": "*.jpg *.jpeg"}, {"title":
                "PNG files", "extensions": "*.png"}]``

        """
        extensions = json.loads(filters)
        extensions_filter = ";;".join(map(lambda e: "{} ({})".format(
            e["title"], e["extensions"]), extensions))
        window = QtGui.QMainWindow()
        return QtGui.QFileDialog.getOpenFileName(window, "Select file", ".",
                                                 extensions_filter)[0]
