from setuptools import setup
import sys

requirements = ["Jinja2(>=2.6)"]

if "win" in sys.platform:
    requirements.append("PySide(>=1.2.2)")

setup(
    name='htmlPy',
    version='2.0.3',
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
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: User Interfaces'
    ],
)
