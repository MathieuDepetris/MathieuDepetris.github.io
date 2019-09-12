#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mathieu Depetris'
#SITEURL = 'https://mathieudepetris.github.io/'
#SITEURL = 'http://localhost:8000/'
#SITENAME = 'Mathieu Depetris\'s website'
SITETITLE = 'MathieuDepetris'
#SITESUBTITLE = 'Web Developer'
#SITE_DESCRIPTION = ('')
TIMEZONE = 'Europe/Paris'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
DEFAULT_LANG = 'fr'
OG_LOCALE  = 'fr_FR'
LOCALE = 'fr_FR'
DEFAULT_PAGINATION = 10

# Paths
STATIC_PATHS = ['pictures', 'documents', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
  'extra/favicon.ico': {'path': 'favicon.ico'}
}
PATH = ['content']
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
SOCIAL = (
  ('github', 'https://github.com/MathieuDepetris'),
  ('linkedin', 'https://www.linkedin.com/in/mathieu-depetris-ab3b3b90/'),
  #('viadeo', 'http://fr.viadeo.com/fr/profile/mathieu.depetris'),
  ('skype', "https://join.skype.com/invite/dwotPkVYUPLD"),
  ('mail', 'mailto:mdepetris@live.fr')
)

# Plugins
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
#I18N_GETTEXT_LOCALEDIR = 'pelican-fh5co-marble/locale/'
#I18N_GETTEXT_DOMAIN = 'messages'
#I18N_GETTEXT_NEWSTYLE = True
I18N_TEMPLATES_LANG = 'fr'

#AUTHORS_BIO = {
#    "timothycrosley": {
#        "name": "Timothy Crosley",
#        "cover": "images/spring/trees.jpg",
#        "image": "https://avatars1.githubusercontent.com/u/2090154?s=400&u=4f46538354444ce0a0d4d89cd676f769d7d846d3&v=4",
#        "location": "Licton Springs, Seattle, WA",
#        "bio": "During the day, I work at DomainTools, where I’m helping to develop predictive security solutions on top of truly large data sets. I can’t resist a good craft beer, a new board game, an arcade, or any food that contains peanut butter."
#    },
#    "amandacrosley": {
#        "name": "Amanda Crosley",
#        "cover": "images/spring/bird.jpg",
#        "image": "images/amandacrosley.jpg",
#        "location": "Licton Springs, Seattle, WA",
#        "bio": "When I'm not mentoring the next generation of STEM leaders, urban hiking through Seattle or playing arcade/board games, you can find me @ Microsoft driving analytics for Bing Ads search advertising."
#    },
#    "janicelichtenwaldt": {
#        "name": "Janice Lichtenwaldt",
#        "cover": "images/spring/bird.jpg",
#        "image": "images/JaniceLichtenwaldt.jpg",
#        "location": "Licton Springs, Seattle, WA",
#        "bio": "During the day, I am the CEO of I Am Virago where we coach folks to become more engaged and effective leaders. I’m a sucker for anything related to arts & crafts and women’s empowerment. I love music, sci-fi, my husband, and my dog…not necessarily in that order."
#    }
#}

# Theme and theme localization
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
    'text': {},
    'links': []
  },
  {
    'image': '/pictures/background/background_4.jpg',
    'title': {
        'fr': '"Une étincelle dans la nuit"', 
        'en': '"A spark in the night"'
        },
    'text': {
        'fr': '&copy; Claudiu D.', 
        'en': '&copy; Claudiu D.'
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
        'fr': 'Baleine à bosse (<i>Megaptera novaeangliae</i>) au large de La Réunion', 
        'en': 'Humpback whale (<i>Megaptera novaeangliae</i>) in large of Reunion island'
        },
    'text': {
        'fr': '&copy; Mathieu Depetris', 
        'en': '&copy; Mathieu Depetris'
        },
    'links': []
  }
]