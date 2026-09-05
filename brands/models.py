from django.db import models



class Brand(models.Model):
    '''
    Representa uma marca de um equipamento cadastrado no sistema.

    Armazena o nome, a descrição, a data de criação e a data de atualização do registro.
    '''
    
    name = models.CharField(max_length= 500)
    description = models.TextField(null= True, blank= True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)


    class Meta:
        '''
        Ordena pelo nome do produto.
        '''

        ordering = ["name"]


    def __str__(self):
        return self.name
    
