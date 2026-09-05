from django.db import models



class Category(models.Model):
    '''
    Representa uma categoria de produto do sistema.

    Armazena nome, descrição, data de criação e a data de atualização do registro.
    '''
    name = models.CharField(max_length= 500)
    description = models.TextField(null= True, blank= True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)


    class Meta:
        '''
        Ordena pelo nome.
        '''
        ordering = ["name"]


    def __str__(self):
        return self.name