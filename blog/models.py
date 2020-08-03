from django.db import models

# Create your models here.
from django.utils import timezone

#Definición del modelo
class Post(models.Model):                           # Define el objeto para el modelo, proveniente de model q es de Django
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):                          # Método para publicar la clase
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title