from django.apps import AppConfig


class RetailNetworkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'retail_network'
    verbose_name = "Розничная сеть"  # переименовали отображение наименования приложения
