from sample_app import app
# app imported from sample_app file is an instance of htmlPy.AppGUI class.


## Change HTML of the app
app.html = u"<html></html>"

## Change HTML of the app using Jinja2 templates
app.template = ("./index.html", {"template_variable_name": "value"})

## Execute javascript on currently displayed HTML in the app
app.evaluate_javascript("alert('Hello from back-end')")
