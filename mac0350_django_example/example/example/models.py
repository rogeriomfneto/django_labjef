# # from django.db import models

# # class Perfil(models.Model):
# #     codigo = models.CharField(max_length=255)
# #     tipo = models.CharField(max_length=255)

# #     def __str__(self):
# #         return self.codigo +','+ self.tipo
    
# # class Usuario(models.Model):
# #     cpf = models.CharField(max_length=11)
# #     nome = models.CharField(max_length=255)
# #     area_de_pesquisa = models.CharField(max_length=255, blank=True, null=True)
# #     instituicao = models.CharField(max_length=255, blank=True, null=True)
# #     data_de_nascimento = models.DateField('data de nascimento')
# #     login = models.CharField(max_length=255)
# #     senha = models.CharField(max_length=255)
# #     cpf_tutor = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
# #     # Esse campo não aparece nas tabelas do bd. Utilizado somente para compatibilidade com a criacao
# #     #de objetos
# #     perfis = models.ManyToManyField(Perfil, through='Usuario_Possui_Perfil')
    
# #     class Meta:
# #         constraints = [
# #                 models.UniqueConstraint(fields=['login'], name='unique_login')
# #                 ]

# #     def __str__(self):
# #         return self.nome

# # #relacionamento Possui
# # class Usuario_Possui_Perfil(models.Model):
# #     usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
# #     perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    
# #     class Meta:
# #         constraints = [
# #                 models.UniqueConstraint(fields=['usuario', 'perfil'], name='unique_usuario_perfil')
# #                 ]

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Exame(models.Model):
    id_exame = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=255)
    virus = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'exame'
        unique_together = (('tipo', 'virus'),)

class Gerencia(models.Model):
    id_servico = models.ForeignKey('Servico', models.DO_NOTHING, db_column='id_servico')
    id_exame = models.ForeignKey(Exame, models.DO_NOTHING, db_column='id_exame')

    class Meta:
        managed = False
        db_table = 'gerencia'
        unique_together = (('id_servico', 'id_exame'),)

class Perfil(models.Model):
    id_perfil = models.IntegerField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=255)
    tipo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil'

class Pertence(models.Model):
    id_servico = models.ForeignKey('Servico', models.DO_NOTHING, db_column='id_servico')
    id_perfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='id_perfil')

    class Meta:
        managed = False
        db_table = 'pertence'
        unique_together = (('id_servico', 'id_perfil'),)


class Pessoa(models.Model):
    id_pessoa = models.IntegerField(primary_key=True, verbose_name='Id usuário:')
    cpf = models.CharField(unique=True, max_length=11)
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    nascimento = models.DateField()

    class Meta:
        managed = False
        db_table = 'pessoa'
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Possui(models.Model):
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_perfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='id_perfil')

    class Meta:
        managed = False
        db_table = 'possui'
        unique_together = (('id_usuario', 'id_perfil'),)

class Servico(models.Model):
    id_servico = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    classe = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'servico'
        unique_together = (('nome', 'classe'),)

class Usuario(Pessoa):
    id_usuario = models.OneToOneField(Pessoa, models.DO_NOTHING, db_column='id_usuario', primary_key=True, parent_link=True)
    # da uma comittada :)
    area_de_pesquisa = models.CharField(max_length=255, blank=True, null=True)
    instituicao = models.CharField(max_length=255, blank=True, null=True)
    login = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    #id_tutor = models.ForeignKey('self', models.DO_NOTHING, db_column='id_tutor', blank=True, null=True)

    # perfis = models.ManyToManyField(Perfil, through='Possui')
    class Meta:
        managed = False
        db_table = 'usuario'
