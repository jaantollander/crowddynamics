#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This file is execfile()d with the current directory set to its
containing dir.

Note that not all possible configuration values are present in this
autogenerated file.

All configuration values have a default; values that are commented out
serve to show the default.
"""

from __future__ import print_function

import os
import sys

import crowddynamics

sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.ifconfig',
    'sphinx.ext.githubpages',
]

extensions += [
    # 'sphinxcontrib.programoutput',
    # 'sphinxcontrib.youtube',
]


templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# General information about the project.
project = 'Crowd Dynamics'
copyright = '2016, Jaan Tollander de Balsch'
author = 'Jaan Tollander de Balsch'

version = '.'.join(crowddynamics.__version__.split('.')[:2])
release = crowddynamics.__version__

language = 'en'
today_fmt = '%Y-%m-%d'
pygments_style = 'sphinx'
todo_include_todos = True

# -- Bokeh -----------------------------------------------------------
# http://bokeh.pydata.org/en/latest/docs/reference/sphinxext.html#bokeh-sphinxext-bokeh-plot

# FIXME
# os.environ.setdefault('BOKEH_DOCS_MISSING_API_KEY_OK', 'yes')
# extensions += [
#     'bokeh.sphinxext.bokeh_plot'
# ]

# -- Napoleon --------------------------------------------------------
# http://www.sphinx-doc.org/en/stable/ext/napoleon.html


# napoleon_google_docstring = True
# napoleon_numpy_docstring = True
# napoleon_include_init_with_doc = False
# napoleon_include_private_with_doc = False
# napoleon_include_special_with_doc = True
# napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_references = False
# napoleon_use_ivar = False
# napoleon_use_param = True
# napoleon_use_rtype = True

# -- Graphviz --------------------------------------------------------

extensions += ['sphinx.ext.graphviz']
graphviz_dot = 'dot'
graphviz_dot_args = []
graphviz_output_format = 'png'  # svg

# -- Options for HTML output ----------------------------------------------

try:
    import sphinx_rtd_theme
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_theme_options = {}
except ImportError() as e:
    html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = ['.']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = project

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = os.path.join('_static', "logo.svg")

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = os.path.join('_static', 'favicon.ico')

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'CrowdDynamicsdoc'

# -- Options for LaTeX output ---------------------------------------------

_latex_preamble = r"""
\usepackage{amsfonts}
\usepackage{parskip}
\usepackage{microtype}
"""

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
    'preamble': _latex_preamble,
    'figure_align': 'htbp',
}

# ('source', 'target', 'title', 'author', 'documentclass')
latex_documents = [
    (master_doc,
     'crowddynamics.tex',
     'Crowd Dynamics',
     author,
     'report'),
]

latex_logo = None


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'crowddynamics', 'Crowd Dynamics Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'CrowdDynamics', 'Crowd Dynamics Documentation',
     author, 'CrowdDynamics', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to _append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False