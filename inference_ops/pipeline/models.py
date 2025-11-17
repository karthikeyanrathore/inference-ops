from django.db import models

# Create your models here.
class Tasks(models.Model):
    class Meta:
        db_table="tasks"
    # https://platform.openai.com/docs/api-reference/responses/object
    id = models.AutoField(primary_key=True)
  
