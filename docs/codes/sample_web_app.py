import htmlPy

web_app = htmlPy.WebAppGUI(title=u"Python Website", maximized=True)
web_app.url = u"http://python.org/"

web_app.start()
