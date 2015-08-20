import htmlPy
import unittest
import os
import random
import string
import json
from nose.plugins.attrib import attr


def random_string():
    return "".join(random.sample(string.ascii_letters, 32))

RANDOM_PARAMS = {
    "LINK_CLICK_STRING": random_string(),
    "LINK_CLICK_ID": random_string(),
    "ARGS_LINK_CLICK_ARGS": random_string(),
    "ARGS_LINK_CLICK_ID": random_string(),
    "DYNAMIC_LINK_ID": random_string(),
    "LINK_404_ID": random_string(),

    "FORM_INPUT_VALUE": random_string(),
    "FORM_ID": random_string(),
    "ARGS_FORM_ID": random_string(),
    "ARGS_FORM_ARGS": random_string(),
    "DYNAMIC_FORM_ID": random_string(),
    "FORM_404_ID": random_string(),
}


class BindingTest(htmlPy.Object):

    def __init__(self, app):
        super(BindingTest, self).__init__()
        self.app = app

    def __set_appname(self, appname):
        context = {"appname": appname}
        context.update(RANDOM_PARAMS)
        self.app.template = ("index.html", context)

    @htmlPy.Slot(str)
    def appname_change(self, appname):
        self.__set_appname(appname)

    @htmlPy.Slot(str, result=str)
    def return_same(self, value):
        return value

    @htmlPy.Slot()
    def appname_link_clicked(self):
        self.__set_appname(RANDOM_PARAMS["LINK_CLICK_STRING"])

    @htmlPy.Slot(str)
    def appname_link_clicked_with_args(self, argstring):
        self.__set_appname(argstring * 2)

    @htmlPy.Slot(str)
    def appname_form_submit(self, form_data):
        jsondata = json.loads(form_data)
        self.__set_appname(jsondata["name"])

    @htmlPy.Slot(str, str)
    def appname_form_submit_with_args(self, form_data, argstring):
        jsondata = json.loads(form_data)
        self.__set_appname(jsondata["name"] + argstring)


class TestAppGUIBinding(unittest.TestCase):

    def setUp(self):
        self.app = htmlPy.AppGUI(allow_overwrite=True)
        self.app.static_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "template_and_static/")
        self.app.template_path = self.app.static_path
        self.frame = self.app.web_app.page().mainFrame()
        self.app.bind(BindingTest(self.app))
        self.app.web_app.loadFinished.connect(self.app.stop)
        self.reloader()

    def reloader(self):
        context = {"appname": "htmlPy Testing"}
        context.update(RANDOM_PARAMS)
        self.app.template = ("index.html", context)

    def refresh_view(self):
        self.app.web_app.loadFinished.connect(self.app.stop)
        self.app.execute()

    def form_submitter(self, form_id):
        self.app.evaluate_javascript(
            "document.getElementById('{}_input').value='{}'".format(
                form_id, RANDOM_PARAMS["FORM_INPUT_VALUE"]))
        self.app.evaluate_javascript(
            "document.getElementById('{}_button').click()".format(form_id))

    # Disabling GUI interaction for travis tests until travis
    @attr("no-coverage")
    def test_binding_activation(self):
        assert self.frame.documentElement().findFirst(
            "body").hasClass("htmlPy-active")

    # Disabling GUI interaction for travis tests until travis
    @attr("no-coverage")
    def test_binding_persistence(self):
        self.test_binding_activation()
        self.html = "<html><head></head><body></body></html>"
        self.test_binding_activation()

    def test_function_call(self):
        rs = random_string()
        assert rs not in self.app.html
        self.app.evaluate_javascript(
            "BindingTest.appname_change('{}')".format(rs))
        assert rs in self.app.html

    def test_function_return(self):
        rs = random_string()
        assert rs not in self.app.html
        self.app.evaluate_javascript(
            "document.write(BindingTest.return_same('{}'))".format(rs))
        assert rs in self.app.html

    def test_non_existent_call(self):
        html = self.app.html
        self.app.evaluate_javascript("BindingTest.non_existent_function()")
        assert self.app.html == html

    # Disabling GUI interaction for travis tests until travis
    @attr("no-coverage")
    def test_link_click(self):
        assert RANDOM_PARAMS["LINK_CLICK_STRING"] not in self.app.html
        self.app.evaluate_javascript(
            "document.getElementById('{}').click()".format(
                RANDOM_PARAMS["LINK_CLICK_ID"]))
        assert RANDOM_PARAMS["LINK_CLICK_STRING"] in self.app.html

    # Disabling GUI interaction for travis tests until travis
    @attr("no-coverage")
    def test_link_click_with_args(self):
        assert RANDOM_PARAMS["ARGS_LINK_CLICK_ARGS"] * 2 not in self.app.html
        self.app.evaluate_javascript(
            "document.getElementById('{}').click()".format(
                RANDOM_PARAMS["ARGS_LINK_CLICK_ID"]))
        assert RANDOM_PARAMS["ARGS_LINK_CLICK_ARGS"] * 2 in self.app.html

    # Disabling GUI interaction for travis tests until travis
    @attr("no-coverage")
    def test_link_click_dynamic(self):
        assert RANDOM_PARAMS["LINK_CLICK_STRING"] not in self.app.html
        self.app.evaluate_javascript("""
        var a = document.createElement("a");
        a.href = "BindingTest.appname_link_clicked";
        a.id = "{}";
        a.innerHTML = "Dynamic link";
        a.setAttribute("data-bind", "true");
        document.body.appendChild(a);""".format(
            RANDOM_PARAMS["DYNAMIC_LINK_ID"]))
        self.app.evaluate_javascript(
            "document.getElementById('{}').click()".format(
                RANDOM_PARAMS["DYNAMIC_LINK_ID"]))
        assert RANDOM_PARAMS["LINK_CLICK_STRING"] in self.app.html

    def test_link_click_404(self):
        html = self.app.html
        self.app.evaluate_javascript(
            "document.getElementById('{}').click()".format(
                RANDOM_PARAMS["LINK_404_ID"]))
        assert self.app.html == html

    # Disabling GUI interaction for travis tests until travis
    @attr("no-coverage")
    def test_form_submit(self):
        assert RANDOM_PARAMS["FORM_INPUT_VALUE"] not in self.app.html
        self.form_submitter(RANDOM_PARAMS["FORM_ID"])
        assert RANDOM_PARAMS["FORM_INPUT_VALUE"] in self.app.html

    # Disabling GUI interaction for travis tests until travis
    @attr("no-coverage")
    def test_form_submit_with_args(self):
        check = RANDOM_PARAMS["FORM_INPUT_VALUE"] + \
            RANDOM_PARAMS["ARGS_FORM_ARGS"]
        assert check not in self.app.html
        self.form_submitter(RANDOM_PARAMS["ARGS_FORM_ID"])
        assert check in self.app.html

    # Disabling GUI interaction for travis tests until travis
    @attr("no-coverage")
    def test_form_submit_dynamic(self):
        assert RANDOM_PARAMS["FORM_INPUT_VALUE"] not in self.app.html
        form_html = """
        <form action="BindingTest.appname_form_submit" id="{}"
        data-bind="true">
            <input type="text" id="{}_input" name="name">
            <br>
            <input type="submit" id="{}_button">
        </form>""".format(*([RANDOM_PARAMS["DYNAMIC_FORM_ID"]]*3))

        self.app.evaluate_javascript(
            "document.body.innerHTML += '{}'".format(
                form_html.replace("\n", ";")))
        self.form_submitter(RANDOM_PARAMS["DYNAMIC_FORM_ID"])
        assert RANDOM_PARAMS["FORM_INPUT_VALUE"] in self.app.html

    def test_form_submit_404(self):
        html = self.app.html
        self.form_submitter(RANDOM_PARAMS["FORM_404_ID"])
        assert self.app.html == html
