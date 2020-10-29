__author__ = "Luca Forzutti"
__email__ = "luca@ahd-creative.com"
__version__ = "1.1.1"

AHPUT_APPS = (
    # Wagtail apps
    "wagtail.core",
    "wagtail.admin",
    "wagtail.documents",
    "wagtail.snippets",
    "wagtail.users",
    "wagtail.images",
    "wagtail.embeds",
    "wagtail.search",
    "wagtail.sites",
    "wagtail.contrib.redirects",
    "wagtail.contrib.forms",
    "wagtail.contrib.sitemaps",
    "wagtail.contrib.routable_page",
    # Third-party apps
    "taggit",
    "modelcluster",
    "django_social_share",
    # AHput apps
    "ahput",
)

default_app_config = "ahput.apps.appconfig"
