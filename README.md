<h1>htmlPy</h1>
<h4>HTML5-CSS3-Javascript based GUI library in Python</h4>
<a href="https://travis-ci.org/amol-mandhane/htmlPy" class="badges" target="_blank">
    <img src="https://img.shields.io/travis/amol-mandhane/htmlPy/master.svg">
</a>
<a href="https://pypi.python.org/pypi/htmlPy/" class="badges" target="_blank">
    <img style="max-width:100%;" src="https://img.shields.io/pypi/v/htmlPy.svg">
</a>
<a href="https://pypi.python.org/pypi/htmlPy/" class="badges" target="_blank">
    <img style="max-width:100%;" src="https://img.shields.io/pypi/dm/htmlPy.svg">
</a>
<br><br>

<p>htmlPy is a wrapper around <a href="https://pyside.org/" target="_blank">PySide</a>'s QtWebKit library. It helps with creating beautiful GUIs using <b>HTML5, CSS3 and Javascript</b> for standalone Python applications. It is built on <a href="http://qt.io/" target="_blank">Qt</a> which makes it highly <b>customizable and cross-platform</b>. htmlPy is compatible with both <b>Python2 and Python3</b>. It can be used with any python library or environment like <a href="https://www.djangoproject.com/" target="_blank">django</a>, <a href="http://flask.pocoo.org/" target="_blank">flask</a>, <a href="http://www.scipy.org/" target="_blank">scipy</a>, <a href="http://virtualenv.readthedocs.org/" target="_blank">virtualenv</a> etc. You can use front-end libraries and frameworks like <a href="http://getbootstrap.com/" target="_blank">bootstrap</a>, <a href="http://jquery.com/" target="_blank">jQuery</a>, <a href="http://jqueryui.com/" target="_blank">jQuery UI</a> etc. and create GUIs for your applications in no time.</p>

<h2>Documentation</h2>
<p>The documentation is hosted at <a href="http://htmlpy.readthedocs.org/">http://htmlpy.readthedocs.org/</a>. It contains <b>installation instructions, tutorials, reference guide</b>, compatibility details, and more.</p>

<h2>Example</h2>
<table style="width: 150%; margin-left: -25%;">
    <tr>
        <td>
        <h3>Back-end <br> <small class="typewriter">back_end.py</small></h3>
        <pre>
            <code class="language-python">
import htmlPy


class BackEnd(htmlPy.Object):

    def __init__(self, app):
        super(BackEnd, self).__init__()
        self.app = app

    @htmlPy.Slot()
    def say_hello_world(self):
        self.app.html = u"Hello, world"
                    </code>

                </pre>
        </td>
        <td>
        <h3>GUI <br> <small class="typewriter">main.py</small></h3>
            <pre>
                <code class="language-python">
import htmlPy
from back_end import BackEnd

app = htmlPy.AppGUI(
    title=u"Sample application")
app.maximized = True
app.template_path = "."
app.bind(BackEnd(app))

app.template = ("index.html", {})

if __name__ == "__main__":
app.start()
            </code>
        </pre></td>
        <td>
        <h3>Front-end <br> <small class="typewriter">index.html</small></h3>
        <pre>
            <code class="language-markup highlight">
&lt;html&gt;
  &lt;body&gt;
&lt;a
href="BackEnd.say_hello_world"
data-bind="true"&gt;
  Click to say "Hello, world"
&lt;/a&gt;
  &lt;/body&gt;
&lt;/html&gt;
            </code>
        </pre></td>
    </tr>
</table>

<h2>Code</h2>
<p>htmlPy source code is hosted on <a href="https://github.com/amol-mandhane/htmlPy" target="_blank">GitHub</a>, tested on <a href="https://travis-ci.org/amol-mandhane/htmlPy" target="_blank">Travis CI</a> and released on <a href="https://pypi.python.org/pypi/htmlPy/" target="_blank">PyPI</a>.</p>
</div>
