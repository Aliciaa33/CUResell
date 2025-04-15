from django.db import models

# Create your models here.







































































class ProductInfo(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    picture = models.ImageField(upload_to='product')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    posted_at = models.DateTimeField((u"Conversation Time"),  blank=True)
    isSold = models.BooleanField(default=False)
    # seller = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    # buyer = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title