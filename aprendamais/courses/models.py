from django.db import models

class Course(models.Model):

    name = models.CharField(
        'Nome',
        max_length=100
    )

    slug = models.SlugField(
        'Atalho'
    )

    about = models.TextField(
        'Sobre o curso',
        blank= True
    )

    description = models.TextField(
        'Descrição do curso',
        blank=True
    )

    start_date = models.DateField(
        'Data de Início',
        null=True,
        blank=True
    )

    image = models.FileField(
        upload_to='courses/images',
        verbose_name = 'Imagem',
        null = True,
        blank=True
    )

    created_at = models.DateTimeField(
        'Criado em', 
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        'Atualizado em', 
        auto_now=True
    )

    def __str__(self):
        return self.name

class Meta:
    verbose_name = 'Curso'
    verbose_name_plural = 'Cursos'
    ordering = ['name']