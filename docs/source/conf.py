# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# standard imports
from datetime import datetime


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))  # the directory of this file
source_dir = os.path.dirname(script_dir)  # the source folder directory
root_dir = os.path.dirname(source_dir)  # the root folder directory

try:
    sys.path.insert(0, root_dir)
    from pyra import definitions  # put this in a try/except to prevent flake8 warning
    from pyra import version
except Exception:
    sys.exit(1)

# -- Project information -----------------------------------------------------
project = definitions.Names().name
copyright = f'{datetime.now ().year}, {project}'
author = 'ReenigneArcher'

# The full version, including alpha/beta/rc tags
version = version.version


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'm2r2',  # enable markdown files
    'numpydoc',  # this automatically loads `sphinx.ext.autosummary` as well
    'sphinx.ext.autodoc',  # autodocument modules
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',  # enable to-do sections
    'sphinx.ext.viewcode'  # add links to view source code
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['toc.rst']

# Extensions to include.
source_suffix = ['.rst', '.md']


# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

html_logo = os.path.join(definitions.Paths().ROOT_DIR, 'web', 'images', 'logo-circle.png')

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    # 'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    # 'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': 'blob',
    # 'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
}

# extension config options
autodoc_preserve_defaults = True  # Do not evaluate default arguments of functions
autosectionlabel_prefix_document = True  # Make sure the target is unique
todo_include_todos = True

# numpydoc config
numpydoc_validation_checks = {'all', 'SA01'}  # Report warnings for all checks *except* for SA01
