from defaults import DefaultConfig
from os import getenv

class ProductionConfig(DefaultConfig):
    DEBUG = (getenv('MOA_DEBUG', 'false') == 'true')
    DEVELOPMENT = (getenv('MOA_DEVELOPMENT', 'false') == 'true')
    TESTING = (getenv('MOA_TESTING', 'false') == 'true')
    CSRF_ENABLED = (getenv('MOA_CSRF_ENABLED', 'true') == 'true')
    # secret key for flask sessions http://flask.pocoo.org/docs/1.0/quickstart/#sessions
    SECRET_KEY = getenv('MOA_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = (getenv('MOA_SQLALCHEMY_TRACK_MODIFICATIONS', 'false') == 'true')
    TWITTER_CONSUMER_KEY = getenv('MOA_TWITTER_CONSUMER_KEY')
    TWITTER_CONSUMER_SECRET = getenv('MOA_TWITTER_CONSUMER_SECRET')
    INSTAGRAM_CLIENT_ID = getenv('MOA_INSTAGRAM_CLIENT_ID')
    INSTAGRAM_SECRET = getenv('MOA_INSTAGRAM_SECRET')
    # define in config.py
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://moa:moa@localhost/moa'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///moa.db'
    SQLALCHEMY_DATABASE_URI = getenv('MOA_SQLALCHEMY_DATABASE_URI')
    SEND = (getenv('MOA_SEND', 'true') == 'true')
    SENTRY_DSN = getenv('MOA_SENTRY_DSN')
    # This option expects a comma delimited list of URLs which Moa will make HTTP GETs to
    HEALTHCHECKS = getenv('MOA_HEALTHCHECKS').split(',') if getenv('MOA_HEALTHCHECKS') != None else []
    MAIL_SERVER = getenv('MOA_MAIL_SERVER')
    MAIL_PORT = int(getenv('MOA_MAIL_PORT', 587))
    MAIL_USE_TLS = (getenv('MOA_MAIL_USE_TLS', 'true') == 'true')
    MAIL_USERNAME = getenv('MOA_MAIL_USERNAME')
    MAIL_PASSWORD = getenv('MOA_MAIL_PASSWORD')
    MAIL_TO = getenv('MOA_MAIL_TO')
    MAIL_DEFAULT_SENDER = getenv('MOA_DEFAULT_SENDER')
    MAX_MESSAGES_PER_RUN = int(getenv('MOA_MAX_MESSAGES_PER_RUN', 5))

    # This option prevents Twitter replies and mentions from occuring when a toot contains @user@twitter.com. This
    # behavior is against Twitter's rules.
    SANITIZE_TWITTER_HANDLES = (getenv('MOA_SANITIZE_TWITTER_HANDLES', 'true') == 'true')

    SEND_DEFERRED_EMAIL = (getenv('MOA_SEND_DEFERRED_EMAIL', 'false') == 'true')
    SEND_DEFER_FAILED_EMAIL = (getenv('MOA_SEND_DEFER_FAILED_EMAIL', 'false') == 'true')
    MAINTENANCE_MODE = (getenv('MOA_MAINTENANCE_MODE', 'false') == 'true')

    STATS_POSTER_BASE_URL = getenv('STATS_POSTER_BASE_URL')
    STATS_POSTER_ACCESS_TOKEN = getenv('STATS_POSTER_ACCESS_TOKEN')

    TRUST_PROXY_HEADERS = (getenv('MOA_TRUST_PROXY_HEADERS', 'false') == 'true')
    WORKER_JOBS = int(getenv('MOA_WORKER_JOBS', 1))
