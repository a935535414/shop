### 石小磊20190424
import xadmin
from shop.models import Category, Product
xadmin.site.register(Category)

class ProductAdmin:
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
xadmin.site.register(Product, ProductAdmin)