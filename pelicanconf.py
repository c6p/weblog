#!/usr/bin/env python

# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Can Altıparmak'
SITENAME = 'Log'
SITEURL = ''
FEED_DOMAIN = ''

TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = 'tr'
DEFAULT_DATE = 'fs'

#LOCALE = ( 'tr_TR', 'en_US' )

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (,)

# Social widget
#SOCIAL = (,)
DIRECT_TEMPLATES = ['index']

#DEFAULT_PAGINATION = 1
DEFAULT_CATEGORY = 'Genel'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "pelican-themes/_can"
#basic,bootstrap,built-texts,cebong,chunk,dev-random2,jesuislibre,martyalchin,mnmlist,monospace,notmyidea-cms,pelican-cait,pujangga,SoMA,svbhack,waterspill-en

# captions      : helderco/markdown-figures
# mkdcomments   : ryneeverett/python-markdown-comments
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'captions']
#'video(youtube_width=768, youtube_height=432)',

STATIC_PATHS = ['static']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math']
