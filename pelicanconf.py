#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'toby'
SITENAME = u'Norwich Hackspace'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "themes/monospace"

# pip install pelican-youtube

PLUGINS = [
    #'pelican_youtube'
]

#import 
#STATIC_PATHS = ['images']
MD_EXTENSIONS = [
	'codehilite(css_class=codehilite code)',
#	'youtube'
]

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Home', '/'), ('Blog', '/blog/')]