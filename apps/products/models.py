from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
# Create your models here.

class Collection(BaseModel):
    
    name = models.CharField("Nombre coleccion", max_length=50,blank=True,null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        verbose_name = "Collection"
        verbose_name_plural = "Colecciones"

    def __str__(self) -> str:
        return self.name
  

class Category(BaseModel):
    
    name = models.CharField("Nombre categoria", max_length=50,blank=True,null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        verbose_name = "Category"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.name

class Indicator(BaseModel):

    discount = models.PositiveSmallIntegerField(default=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="Indicador de oferta")
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        verbose_name = "Indicator"
        verbose_name_plural = "Indicadores"

    def __str__(self) -> str:
        return self.discount

class Country(BaseModel):

    name = models.CharField("Nombre del pais", max_length=50,blank=True,null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        verbose_name = "Country"
        verbose_name_plural = "Paises"

    def __str__(self) -> str:
        return self.name

class Color(BaseModel):

    name = models.CharField("Nombre del color", max_length=50,blank=True,null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        verbose_name = "Color"
        verbose_name_plural = "Colores"

    def __str__(self) -> str:
        return self.name

class Business(BaseModel):

    name = models.TextField("Nombre de la empresa",blank=True,null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        verbose_name = "Business"
        verbose_name_plural = "Empresas"

    def __str__(self) -> str:
        return self.name


class Size(BaseModel):

    description = models.CharField("Descripcion de medida o talla",max_length=50,blank = False,null = False,unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        verbose_name = "Size"
        verbose_name_plural = "Sizes"

    def __str__(self) -> str:
        return self.description

class Sex(BaseModel):

    name = models.TextField("Genero",blank = False,null = False,unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        verbose_name = "Sex"
        verbose_name_plural = "Sexs"
    
    def __str__(self) -> str:
        return self.name

class Reference(BaseModel):

    name = models.TextField("Referencia/modelo",blank = False,null = False,unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        verbose_name = "Reference"
        verbose_name_plural = "Referencias"
    
    def __str__(self) -> str:
        return self.name

class Product(BaseModel):

    # Products variables 
    name = models.CharField("Nombre de producto",max_length=150,unique=True,blank= False ,null=False)
    description = models.TextField("Descripcion del producto",blank = False,null = False)
    material =  models.CharField('Nombre del material de producto', max_length=100)
    

    # Foreing keys
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name="Categoria del producto")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE,verbose_name="Coleccion del producto")
    business = models.ForeignKey(Business, on_delete=models.CASCADE,verbose_name="Empresa del producto")
    reference = models.ForeignKey(Reference, on_delete=models.CASCADE,verbose_name="Referencia del producto")
    image = models.ImageField('Imagen del Producto', upload_to='products/', blank=True, null=True)


    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        unique_together = ("reference",)
        verbose_name = "Product"
        verbose_name_plural = "Productos"
    
    

class Size_Product(BaseModel):

    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="Productos")
    size = models.ForeignKey(Size, on_delete=models.CASCADE,verbose_name="Talla")
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        unique_together = ("product","size")
        verbose_name = "Size_Product"
        verbose_name_plural = "Size_Products"

class Color_Product(BaseModel):

    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="Productos")
    color = models.ForeignKey(Color, on_delete=models.CASCADE,verbose_name="Color")
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        unique_together = ("product","color")
        verbose_name = "Color_Product"
        verbose_name_plural = "Color_Products"

class Business_Product(BaseModel):

    # Products variables 
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2, default=0)
    discount = models.PositiveSmallIntegerField(default=0)
    date =  models.DateTimeField(auto_now_add=True)
    qualification = models.PositiveSmallIntegerField(default=0)
    count_qualification = models.PositiveSmallIntegerField(default=0)
    

    # Foreing keys
    product = models.ForeignKey(Product, on_delete=models.CASCADE,verbose_name="Producto")
    business = models.ForeignKey(Business, on_delete=models.CASCADE,verbose_name="Empresa que vende el producto")
    country = models.ForeignKey(Country, on_delete=models.CASCADE,verbose_name="Pais")


    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        verbose_name = "Business_Product"
        verbose_name_plural = "Business_Products"
    
  


class Sex_Business(BaseModel):
 
    # Foreing keys
    businnes_producto = models.ForeignKey(Business_Product, on_delete=models.CASCADE,verbose_name="Empresa venta del producto")
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE,verbose_name="Sexo como se vende el producto")
    

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        unique_together = ("businnes_producto","sex")
        verbose_name = "Sex_Busines"
        verbose_name_plural = "Sex_Business"



