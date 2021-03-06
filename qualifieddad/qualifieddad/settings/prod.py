from qualifieddad.settings.base import *

# Override base.py settings here
DEBUG = False

ALLOWED_HOSTS =  ['kingcommerce.herokuapp.com', 'https://git.heroku.com/kingcommerce.git']


CORS_REPLACE_HTTPS_REFERER      = True
HOST_SCHEME                     = "https://"
SECURE_PROXY_SSL_HEADER         = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT             = True
SESSION_COOKIE_SECURE           = True
CSRF_COOKIE_SECURE              = True
SECURE_HSTS_INCLUDE_SUBDOMAINS  = True
SECURE_HSTS_SECONDS             = 1000000
SECURE_FRAME_DENY               = True

try:
    from keycontrol.settings.local import *
except:
    pass
