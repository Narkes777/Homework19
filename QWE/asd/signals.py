from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver


@receiver(pre_save)
def pre_save_models(sender, *args, **kwargs):
    print('dwdwadadawdawdadsawdawd')
