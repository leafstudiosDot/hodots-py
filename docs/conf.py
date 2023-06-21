import logging
import sys
import os
import re

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('extensions'))

extensions = [
    'builder',
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinxcontrib_trio',
    'details',
    'exception_hierarchy',
    'attributetable',
    'resourcelinks',
    'nitpick_file_ignorer',
    'colour_preview',
]

autodoc_member_order = 'bysource'
autodoc_typehints = 'none'

extlinks = {
    'issue': ('https://github.com/leafstudiosDot/hodots.py/issues/%s', 'GH-%s'),
    'apidocs': ('https://docs.hodots.com/%s', None),
}

intersphinx_mapping = {
  'py': ('https://docs.python.org/3', None),
  'aio': ('https://docs.aiohttp.org/en/stable/', None),
  'req': ('https://requests.readthedocs.io/en/latest/', None)
}

rst_prolog = """
.. |coro| replace:: This function is a |coroutine_link|_.
.. |maybecoro| replace:: This function *could be a* |coroutine_link|_.
.. |coroutine_link| replace:: *coroutine*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = 'hodots.py'
copyright = '2023-present leafstudiosDot'

version = ''
with open('../hodots/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

release = version

branch = 'master' if version.endswith('a') else 'v' + version

language = None

locale_dirs = ['locale/']
gettext_compact = False

exclude_patterns = ['_build']

pygments_style = 'friendly'

nitpick_ignore_files = [
  "migrating_to_async",
  "migrating_to_v1",
  "migrating",
  "whats_new",
]


def _i18n_warning_filter(record: logging.LogRecord) -> bool:
  return not record.msg.startswith(
    (
      'inconsistent references in translated message',
      'inconsistent term references in translated message',
    )
  )


_i18n_logger = logging.getLogger('sphinx')
_i18n_logger.addFilter(_i18n_warning_filter)

html_experimental_html5_writer = True

html_theme = 'basic'

html_context = {
  
}

resource_links = {
  'hodots.': 'https://hodots.com',
  'issues': 'https://github.com/Rapptz/hodots.py/issues',
  'discussions': 'https://github.com/Rapptz/hodots.py/discussions',
}

html_static_path = ['_static']

html_search_scorer = '_static/scorer.js'

html_js_files = [
  'custom.js',
  'settings.js',
  'copy.js',
  'sidebar.js'
]

htmlhelp_basename = 'hodots.pydoc'

latex_elements = {
   
}

latex_documents = [
  ('index', 'hodots.py.tex', 'hodots.py Documentation',
   'leafstudiosDot', 'manual'),
]

man_pages = [
    ('index', 'hodots.py', 'hodots.py Documentation',
     ['leafstudiosDot'], 1)
]

texinfo_documents = [
  ('index', 'hodots.py', 'hodots.py Documentation',
   'leafstudiosDot', 'hodots.py', 'One line description of project.',
   'Miscellaneous'),
]

def setup(app):
   return