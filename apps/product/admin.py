from django.contrib import admin
from apps.product.models import Category, Product, Images
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','parent', 'slug')
    prepopulated_fields={'slug':['title']}

admin.site.register(Category, CategoryAdmin)

class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'status', 'price', 'image_tag')
    list_filter = ['category']
    prepopulated_fields={'slug':['title']}
    inlines = [ProductImagesInline]
    # readonly_fields = ('image_tag',)

admin.site.register(Product, ProductAdmin)


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id','product', 'image_tag')

admin.site.register(Images, ImagesAdmin)