AUTHOR = 'Carla, Jonay'
SITENAME = 'NekoSoft'
SITEURL = "localhost:8000"

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

RELATIVE_URLS = True


ARTICLE_PATHS = []
PAGE_PATHS = ['.']
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = False



THEME = 'attila-2.0'

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'Pelican-DSW/static/custom.css'},
    'extra/favicon.ico': {'path': 'Pelican-DSW/favicon.ico'},
}
CUSTOM_CSS = 'Pelican-DSW/static/custom.css'




PLUGINS = []
