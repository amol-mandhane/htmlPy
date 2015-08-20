import sys
unicode = str if sys.version_info >= (3, 0) else unicode

from PySide.QtCore import QObject as Object
from PySide.QtCore import Slot
from .base_gui import BaseGUI
from .web_app_gui import WebAppGUI
from .app_gui import AppGUI
del app_gui
del base_gui
del descriptors
del gui_helper
del web_app_gui
