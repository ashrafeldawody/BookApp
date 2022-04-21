from django.db import models
from auther.models import Auther

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="library/static/uploads",blank=True, null=True)
    price = models.DecimalField(decimal_places=2,max_digits=5)
    appropriate = models.CharField(max_length=50, choices=[
        ('under8', 'Under 8'),
        ('8-15', '8-15'),
        ('adults', 'Adults'),
    ], default="under8")
    added_at = models.DateTimeField(auto_now_add=True)
    auther = models.ForeignKey(Auther,null=False, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f"/book/{self.id}/"