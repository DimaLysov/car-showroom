from django.contrib import admin
from django.apps import apps

app_models = apps.get_app_config('api').get_models()

for model in app_models:
    try:
        admin.site.register(model)  # Регистрируем модель с дефолтными настройками
    except admin.sites.AlreadyRegistered:  # На случай, если модель уже зарегистрирована
        pass
