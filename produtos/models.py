from django.db import models
from django.utils.text import slugify
import django.utils.timezone as timezone
from stdimage import StdImageField
from dynamic_filenames import FilePattern
from django.urls import reverse

upload_to_pattern = FilePattern(
    filename_pattern='{model_name:.30}/{uuid:base32}{ext}')

# Modelo para Categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('loja:lista_produtos_por_categoria', args=[srt(self.slug)])

# Modelo para Produto
class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    disponivel = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now=True)
    atualizado = models.DateTimeField(auto_now=True)
    foto_capa = StdImageField('Foto do produto', upload_to=upload_to_pattern, 
    variations={
        'thumb': {'width': 480, 'height': 480, 'crop': True}
        }, delete_orphans=True, max_length=255, default='images/produto_sem_foto.png')
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        
        if self.estoque <= 0:
            self.disponivel = False
        else:
            self.disponivel = True

        super(Produto, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('loja:detalhe_produto', args=[srt(self.slug)])

