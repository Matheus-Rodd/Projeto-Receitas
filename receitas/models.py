from django.db import models

# Create your models here.
class Receita(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    # time_coking = models.IntegerField(help_text="Em minutos")
    image = models.ImageField(upload_to='receitas/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title
    
    class Meta:
        verbose_name = "Receita"
        verbose_name_plural = "Receitas"
        ordering = ['-created_at'] #ordena as receitas da mais nova para a mais antiga