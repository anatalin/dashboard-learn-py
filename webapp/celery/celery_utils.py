from celery import current_app


def make_celery(app):
    celery = current_app
    celery.config_from_object(app.config, namespace="CELERY")

    return celery
