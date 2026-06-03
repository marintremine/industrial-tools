from django.core.management.base import BaseCommand
from apps.table.models import TD_TypeData, DYT_DynamicTable

class Command(BaseCommand):
    help = 'Sample database test'

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.SUCCESS(f'Insertion des données'))
            TD_TypeData.objects.bulk_create([
                TD_TypeData(TD_code="string"),
                TD_TypeData(TD_code="integer"),
                TD_TypeData(TD_code="date"),
                TD_TypeData(TD_code="tag"),
            ])

            table = DYT_DynamicTable.objects.create(
                DYT_name="Personnes",
                DYT_description="Tableau des personnes de la classe"
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erreur lors de l\'insertions des données : {e}'))