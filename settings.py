import os
from decouple import config

ROOT_PATH = os.path.dirname(__file__)

# Django requirements
SECRET_KEY = "xxxxxx BIG secret"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(ROOT_PATH, "templates"),
        ],
        "APP_DIRS": True,
    },
]
INSTALLED_APPS = []

# setting up directory paths
STATIC_DIR = os.path.join(ROOT_PATH, 'static')
BUILD_DIR = os.path.join(ROOT_PATH, 'built')

# setting up some helpful values
STATIC_URL_FORMAT = u"/%s"
STATIC_IMAGE_FORMAT = STATIC_URL_FORMAT % u"img/%s"

# Emails

ANYMAIL = {
    "MAILGUN_API_KEY": config("MAILGUN_API_KEY", default=""),
    "MAILGUN_SENDER_DOMAIN": "mg.englitalia.us",
}
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
RAW_EMAIL = "email@englitalia.us"
SERVER_EMAIL = "englitalia <email@englitalia.us>"
DEFAULT_FROM_EMAIL = "englitalia <email@englitalia.us>"

# creating default rendering context
CONTEXT = {
    "FROM_EMAIL": RAW_EMAIL,
}
