# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DRAGEN'
copyright = '2025, siddharth'
author = 'siddharth'
release = 'v1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'pydata_sphinx_theme'
html_theme = 'furo'
html_static_path = ['_static']
html_theme_options = {
    "logo": {
        "text": "DRAGEN Docs",
    },
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
}
html_css_files = [
    "custom.css",
]

