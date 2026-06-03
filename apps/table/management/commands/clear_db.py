from django.core.management.base import BaseCommand
from apps.table.models import TD_TypeData, DYT_DynamicTable

class Command(BaseCommand):
    help = 'Clear database '

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS(f'Suppression des données'))
            TD_TypeData.objects.all().delete()
            DYT_DynamicTable.objects.all().delete()

            self.stdout.write(self.style.SUCCESS(f'Données supprimées'))


        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erreur lors de la suppression des données : {e}'))