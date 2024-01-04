from django.db import models

class Home(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("I", "Indefindo"),
        ("N", "Nenhuma das opções")
    )

    SERVIDOR_EMAIL_CHOICES = (
        ("G", "gmail.com"),
        ("Y", "yahoo.com"),
        ("H", "hotmail.com"),
        ("N", "Nenhuma das opções")
    )

    nome = models.CharField('Nome', max_length=100, null=False, blank=False)
    email = models.EmailField('E-mail', null=False, blank=False)
    data_nascimento = models.DateField('Data de Nascimento', null=False, blank=False)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES, null=False, blank=False )
    email_servidor = models.CharField('Servidor de E-mail', max_length=1, choices=SERVIDOR_EMAIL_CHOICES, null=False, blank=False)
    foto_usuario = models.ImageField(upload_to='fotos/%Y/%m/%d', blank=True)

    def __str__(self):
        return f'{self.nome}'