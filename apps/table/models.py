from django.db import models

# Create your models here.
# Create your models here.

class DYT_DynamicTable(models.Model):
    DYT_id = models.AutoField(primary_key=True)
    DYT_name = models.CharField(max_length=30)
    DYT_description = models.CharField(max_length=30)

    pass

class COL_Column(models.Model):
    COL_id = models.AutoField(primary_key=True)
    DYT_id = models.ForeignKey(DYT_DynamicTable, on_delete=models.CASCADE)
    COL_order = models.IntegerField()

class TD_TypeData(models.Model):
    TD_id = models.AutoField(primary_key=True)
    TD_code = models.CharField(max_length=30)

class TAG_TagOption(models.Model):
    TAG_id = models.AutoField(primary_key=True)
    TAG_value = models.CharField(max_length=30)
    TAG_color = models.CharField(max_length=8) # chaine caractere en hexa
    COL_id =  models.ForeignKey(COL_Column, on_delete=models.CASCADE)

class CEL_Cell(models.Model):
    CEL_id = models.AutoField(primary_key=True)
    CEL_value = models.CharField(max_length=30)
    COL_id = models.ForeignKey(COL_Column, on_delete=models.CASCADE)
