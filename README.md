# Projeto E-commerce 
Um projeto extremamente simples de e-commerce (ainda incompleto) feito com 
Django 2.2.4 e Python 3.7.3.

### Conteúdo educacional
Criado para aula de Tópicos avançados em sistemas de informação. Turma 2024 do Curso de ADS Cruzeiro Do Sul na Vila Leopoldina.

Isso não impede que você baixe, altere, use e/ou distribua o seu conteúdo conforme preferir.

### Este projeto NÃO inclui
Abaixo uma lista de recursos que não adicionei ainda e que você pode me ajudar a adicionar.

- Combinações de variações de produto (tem apenas uma variação)
- Cupons de desconto no carrinho de compras
- Cálculo de frete
- Métodos de pagamento (MercadoPago, PayPal, PagSeguro, enfim...)

### TODOs
Abaixo uma lista do que adicionei ou ainda pretendo adicionar.

- [x] Model produtos
- [x] Model variações
- [x] Listagem e detalhes de produtos e variações
- [x] Carrinho de compras baseado em session
- [x] Remover produtos do carrinho
- [x] Model perfil (criar e atualizar)
- [x] Login e Logout do cliente
- [x] Registrar pedido do cliente
- [x] Página de pagamento

### Tutorial para iniciantes
Abaixo uma lista de comandos para clonar e configurar este projeto na sua 
máquina local:

- Instalar git (Windows) e depois:

```
git clone https://github.com/raulpastrello/roccy_platas.git
```

- Para **Windows**:

```
cd roccy_platas
python3 -m venv django_env
source django_env/Scripts/activate
python3 -m pip install --upgrade pip setuptools wheel --user
python3 -m pip install django django-debug-toolbar django-crispy-forms pillow
python manage.py migrate
python manage.py runserver

```

Pronto!

