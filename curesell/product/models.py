from django.db import models
from user.models import UserInfo

# Create your models here.
class ProdInfoManager(models.Manager):
    def create_prod(self, title, description, picture, price, seller):
        prod = self.create(title=title, description=description, picture=picture, price=price, isSold=False, seller=seller)
        return prod
    
    # get the corrosponding product with the given title
    def get_title(self, title):
        return super(ProdInfoManager, self).get_queryset().filter(title=title)
    
    # get all unsold products
    def get_unsold(self):
        return super(ProdInfoManager, self).get_queryset().filter(isSold=False)
    
    # get all products in the database
    def get_all(self):
        return super(ProdInfoManager, self).get_queryset()
    
class ProductInfo(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=2000)
    picture = models.ImageField(upload_to='product')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    posted_at = models.DateTimeField((u"Conversation Time"),  auto_now_add=True)
    isSold = models.BooleanField(default=False)
    seller = models.ForeignKey(UserInfo, on_delete=models.CASCADE, default='')
    product = ProdInfoManager()
    # buyer = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    def __str__(self):
        return self.title