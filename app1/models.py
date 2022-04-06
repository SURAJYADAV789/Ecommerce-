from django.db import models

# Create your models here.
class Product(models.Model):
    p_id = models.BigAutoField(primary_key=True)
    p_name = models.CharField(max_length=50)
    p_price = models.FloatField()
    p_desc = models.TextField()
    p_image=models.ImageField(upload_to='product_img/',default='NO_image')