import htmlPy
import os

app = htmlPy.AppGUI(title=u"htmlPy Quickstart", maximized=True)

app.template_path = os.path.abspath(".")
app.static_path = os.path.abspath(".")

app.template = ("index.html", {"username": "htmlPy_user"})

app.start()
