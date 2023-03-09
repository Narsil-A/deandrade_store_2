from io import BytesIO
from PIL import Image 
from django.core.files import File
from django.db import models


"""
Class for category products where each product has its thumbnail image field, slug address version of the name
"""
class Category(models.Model):

    name = models.CharField(max_length=255) # name of products
    slug = models.SlugField() # address version of the name


    class Meta:
    
        ordering = ('name',) # order the category, ordering create a tuple

    def __str__(self):
        return self.name  # string representation of the object
    
    def get_absolute_url(self):
        return f'/{self.slug}/' # get the url for the object, address version of url for the produc
                                
class Product(models.Model):

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) # Cascade deletes. Django emulates the behavior of the SQL constraint ON DELETE CASCADE and also deletes the object containing the ForeignKey.
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    image = models.ImageField(upload_to='uploads/', blank=True)        
    thumbnail = models.ImageField(upload_to='uploads/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        
        ordering = ('-date_added',) # date create it in descending order

    def __str__(self):

        return self.name   # returns a string representation of any object
    
    def get_absolute_url(self):

        return f'/{self.category.slug}/{self.slug}/' # to get the url of each product
    
    def get_image(self):

        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):

        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        
        else:

            if self.image:

                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            
            else:
                return''

    def make_thumbnail(self, image, size=(300, 200)):
        
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        
        return 

    @property   # property for sales price 
    def sales_price(self):
        return "%.2f" %(float(self.price) * 0.9)
