from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.safestring import mark_safe


class Category(MPTTModel):
    STATUS_CHOICES = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, 
        null=True, blank=True, related_name='children'
    )
    image = models.ImageField(upload_to="category/", blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default=True, max_length=10)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "категория"
    
    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])
    
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})

    class MPTTMeta:
        order_insertion_by = ['title']


class Product(models.Model):
    STATUS_CHOICES = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product/")
    status = models.CharField(choices=STATUS_CHOICES, default=True, max_length=10)
    slug = models.SlugField(unique=True)
    description = RichTextUploadingField(verbose_name="описание")
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50px">'.format(self.image.url))
        else:
            return ""
    
    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_image/')

    def __str__(self):
        return f"{self.id}"
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50px">'.format(self.image.url))
        else:
            return ""


class Review(models.Model):
    RATING_CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    name = models.CharField(
        max_length=255
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )
    text = models.TextField()
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='review_product',
    )
    rating = models.CharField(
        max_length=5,
        choices=RATING_CHOICE,
    )

    def __str__(self):
        return f'{self.name}: {self.rating}'
