from decimal import Decimal
from django.conf import settings
from .models import Produto

class Carrinho(object):
    
    def __init__(self, request):
        self.session = request.session
        carrinho = self.session.get(settings.CARRINHO_SESSION_ID)
        
        if not carrinho:
            carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}
        
        self.carrinho = carrinho

    def add(self, produto, quantidade=1):
        produto_id = str(produto.id)
        if produto_id not in self.carrinho:
            self.carrinho[produto_id] = {'quantidade': 0, 'preco': str(produto.preco)}
        
        self.carrinho[produto_id]['quantidade'] += quantidade
        self.save()

    def save(self):
        self.session[settings.CARRINHO_SESSION_ID] = self.carrinho
        self.session.modified = True

    def remove(self, produto):
        produto_id = str(produto.id)
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.save()

    def __iter__(self):
        produto_ids = self.carrinho.keys()
        produtos = Produto.objects.filter(id__in=produto_ids)
        
        for produto in produtos:
            self.carrinho[str(produto.id)]['produto'] = produto

        for item in self.carrinho.values():
            item['preco'] = Decimal(item['preco'])
            item['total_preco'] = item['preco'] * item['quantidade']
            yield item

    def get_total_price(self):
        return sum(Decimal(item['preco']) * item['quantidade'] for item in self.carrinho.values())
