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
          ('Linkedin', 'https://www.linkedin.com/in/mathieu-depetris-ab3b3b90/'),
          ('viadeo', 'http://fr.viadeo.com/fr/profile/mathieu.depetris'),
          ('Facebook', 'https://www.facebook.com/MathieuDepetris'))

# Plugins
# PLUGIN_PATHS = ['C:\\ProgramData\\Anaconda3\\pkgs\\python-3.7.3-h8c8aaf0_1\\pelican-addon-clones\\pelican-plugins']
PLUGIN_PATHS = ['plugins']
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
  'mail': 'mdepetris@live.fr',
  # keep it a string if you dont need multiple languages
  'text': '9 avenue Raymond Pitet, 1er étage<br/> 34300 Agde, <br/>France',
  #'link': 'contact.html',
  # the address is also taken for google maps
  'address': '9 avenue Raymond Pitet, 1er étage<br/> 34300 Agde, <br/>France',
  'phone': '+33(0) 6 61 62 72 04'
}

# Background home
HERO = [
  # {
  #   'image': '/images/hero/background-1.jpg',
  #   # for multilanguage support, create a simple dict
  #   'title': {
  #     'en':'Some special content',
  #     'fr': 'Spezieller Inhalt'
  #   },
  #   'text': {
  #     'fr': 'Any special content you want to tease here',
  #     'de': 'Jeglicher spezieller Inhalt den Sie hier bewerben möchten'
  #   },
  #   'links': [
  #     {
  #       'icon': 'icon-code',
  #       'url': 'https://github.com/claudio-walser/pelican-fh5co-marble',
  #       'text': 'Github'
  #     }
  #   ]
  # },
  {
    'image': '/pictures/background/background_1.jpg',
    'title': {
        'fr': 'A le rencontre du grand blanc', 
        'en': 'Meet the big white'
        },
    'text': {
        'fr': '&copy; Pascal Kobeh', 
        'en': '&copy; Pascal Kobeh'
        },
    'links': []
  },
  {
    'image': '/pictures/background/background_2.jpg',
    'title': {
        'fr': '"Interdiction de pêcher !"', 
        'en': '"No fishing !"'
        },
    'text': {
        'fr': '&copy; Jamie MacArthur', 
        'en': '&copy; Jamie MacArthur'
        },
    'links': []
  },
  {
    'image': '/pictures/background/background_3.jpg',
    'title': {
        'fr': 'Orque (<i>Orcinus orca</i>)', 
        'en': 'Orca (<i>Orcinus orca</i>)'
        },
    'text': {
        'fr': '&copy; Agence des aires marines protégées', 
        'en': '&copy; Agence des aires marines protégées'
        },
    'links': []
  },
  {
    'image': '/pictures/background/background_4.jpg',
    'title': {
        'fr': 'Parc national de la Mauricie au Canada', 
        'en': 'Canada La Mauricie National Park'
        },
    'text': {
        'fr': '&copy; Mathieu Depetris', 
        'en': '&copy; Mathieu Depetris'
        },
    'links': []
  },
  {
    'image': '/pictures/background/background_5.jpg',
    'title': {
        'fr': 'Débarquement de thonidés aux Seychelles', 
        'en': 'Landing of tunas in Seychelles'
        },
    'text': {
        'fr': '&copy; Mathieu Depetris', 
        'en': '&copy; Mathieu Depetris'
        },
    'links': []
  },
  {
    'image': '/pictures/background/background_6.jpg',
    'title': {
        'fr': 'Phoque gris (<i>Halichoerus grypus</i>) en mer d\'Iroise', 
        'en': 'Grey seal (<i>Halichoerus grypus</i>) in Iroise sea'
        },
    'text': {
        'fr': '&copy; S. Brégeon / Agence des aires marines protégées', 
        'en': '&copy; S. Brégeon / Agence des aires marines protégées'
        },
    'links': []
  }
]