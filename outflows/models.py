from django.db import models
from products.models import Product


class Outflow(models.Model):
    '''
    Registra a saída do produto do sistema.

    Armazena o produto, quantidade, descrição, data de criação e data de atualização do registro.
    '''
    product = models.ForeignKey(Product, on_delete= models.PROTECT, related_name= "outflows")
    quantity = models.IntegerField()
    description = models.TextField(null= True, blank= True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)


    class Meta:
        "Ordena em ordem descendente com base na data de criação"
        ordering = ["-created_at"]


    def __str__(self):
        return str(self.product)
