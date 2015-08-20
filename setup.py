from distutils.core import setup
import sys

requirements = ["Jinja2(>=2.6)"]

if "win" in sys.platform:
    requirements.append("PySide(>=1.2.2)")

setup(
    name='htmlPy',
    version='2.0.0',
    author='Amol Mandhane',
    author_email='amol.mandhane@gmail.com',
    packages=['htmlPy'],
    scripts=[],
    url='http://pypi.python.org/pypi/htmlPy/',
    license='LICENSE.txt',
    description="A wrapper around PySide's QtWebKit library which helps " +
    "developer create beautiful UI with HTML5, CSS and Javascript for " +
    "standalone applications.",
    long_description=open('README.md').read(),
    requires=requirements,
)
