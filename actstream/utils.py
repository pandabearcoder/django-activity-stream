from django.apps import apps
from django.core.exceptions import ImproperlyConfigured

from actstream.settings import ACTION_MODEL


def get_action_model():
    try:
        return apps.get_model(ACTION_MODEL)
    except ValueError:
        raise ImproperlyConfigured(
            "path must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            "path refers to model '%s' that has not been installed" % ACTION_MODEL
        )
