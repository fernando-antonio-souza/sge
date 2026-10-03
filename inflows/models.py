from django.db import models
from products.models import Product
from suppliers.models import Supplier


class Inflow(models.Model):
    """
    Registra a entrada do produto no sistema.

    Cadastra o fornecedor, o produto, a quantidade, descrição, data de criação e data de atualização do registro.
    """

    supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, related_name="inflows"
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="inflows"
    )
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        "Ordena em ordem descendente com base na data de criação"

        ordering = ["-created_at"]

    def __str__(self):
        return str(self.product)
