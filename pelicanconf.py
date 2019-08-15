#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mathieu Depetris'
SITENAME = 'MathieuDepetris'
SITEURL = ''
TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
DEFAULT_LANG = 'fr'
LOCALE = 'fr_FR'
STATIC_PATHS = ['pictures', 'documents']
DEFAULT_PAGINATION = 10

# Paths
PATH = 'content'
PAGE_PATHS = ['pages/fr']
ARTICLE_PATHS = ['articles/fr']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/MathieuDepetris'),
          ('Another social link', '#'),)

# Plugins
# PLUGIN_PATHS = ['C:\\ProgramData\\Anaconda3\\pkgs\\python-3.7.3-h8c8aaf0_1\\pelican-addon-clones\\pelican-plugins']
PLUGIN_PATHS = 'plugins'
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n'],}

# i18n
I18N_SUBSITES = {
  'en': {
    'PAGE_PATHS': ['pages/en'],
    'ARTICLE_PATHS': ['articles/en'],
    'LOCALE': 'en_UK'
  }
}
I18N_GETTEXT_LOCALEDIR = 'pelican-fh5co-marble/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
I18N_TEMPLATES_LANG = 'fr_FR'

# theme and theme localization
THEME = 'pelican-fh5co-marble'

# Navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'

# Contact section
ABOUT = {
  'image': '/images/about/objectif.png',
  'mail': 'ob7@ird.fr',
  # keep it a string if you dont need multiple languages
  'text': 'Avenue Jean Monnet,<br/> CS 30171, 34203 Sète cedex, <br/>France',
  #'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'Avenue Jean Monnet,<br/> CS 30171, 34203 Sète cedex, <br/>France ',
  'phone': '+33(0) 4 99 57 32 00'
}