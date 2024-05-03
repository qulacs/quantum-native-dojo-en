# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Quantum Native Dojo'
copyright = '2024, Contributors to Quantum Native Dojo'
author = 'Contributors to Quantum Native Dojo'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_qndojo_theme'
html_theme_path = ['.']
html_theme_options = {
    "theme_display_version": True,
    "current_version": "Qulacs",
    "versions": [
        ("Qulacs", "https://dojo.qulacs.org/en/qulacs_main/"),
        ("QURI-Parts", "https://dojo.qulacs.org/en/qp_main/"),    
    ]
}

html_favicon = None
html_show_sphinx = False

mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-MML-AM_CHTML'
mathjax_config = {
    'CommonHTML': {
        'undefinedFamily': '"Source Serif Pro", "Yakumono", "Noto Serif JP", "Hiragino Mincho ProN", "STIXGeneral", "Arial Unicode MS", serif'
    }
}
