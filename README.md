# 📷 Galeria de Imagens — Django

Sistema web para cadastro e organização de imagens por categorias, com filtro, ordenação e paginação. Projeto da disciplina de Web I (Análise e Desenvolvimento de Sistemas, UNIFIP), feito em dupla.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)

## ✨ Funcionalidades

- CRUD completo de imagens: cadastrar, listar, ver detalhes, editar e excluir
- Organização por **categorias** (cadastradas pelo painel admin do Django)
- **Filtro** por categoria
- **Ordenação** por mais recentes, mais antigas ou título (A-Z)
- **Paginação** com 6 imagens por página, mantendo o filtro e a ordenação ao trocar de página
- Upload de imagens com Pillow

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python 3.13 e Django 6.1 | Back-end e templates |
| PostgreSQL + psycopg2 | Banco de dados |
| Pillow | Upload e validação de imagens |
| python-dotenv | Variáveis de ambiente (`.env`) |
| HTML e CSS | Interface |

## 📁 Estrutura

```
├── manage.py
├── core/                  # configurações do projeto (settings, urls)
└── galeria/               # app principal
    ├── models.py          # Categoria e Imagem
    ├── views.py           # listagem, detalhe, criação, edição e exclusão
    ├── urls.py            # rotas
    ├── templatetags/
    │   └── galeria_extras.py   # tag url_replace (mantém filtro e ordenação)
    └── templates/galeria/ # base, lista, detalhe, formulário, confirmação
```

## 🚀 Como rodar (Windows)

Pré-requisitos: Python 3.13 e PostgreSQL instalados.

```bash
# 1. Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Crie o banco no PostgreSQL (nome padrão: galeria_db)

# 4. Configure o ambiente
copy .env.example .env
# Abra o .env e preencha SECRET_KEY e DB_PASSWORD

# 5. Crie as tabelas e um usuário admin
python manage.py migrate
python manage.py createsuperuser

# 6. Rode o servidor
python manage.py runserver
```

Para gerar uma `SECRET_KEY`:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Acesse `http://127.0.0.1:8000/`. Antes de cadastrar imagens, crie ao menos uma categoria em `http://127.0.0.1:8000/admin/`.

## 🗺️ Rotas

| Rota | Descrição |
|---|---|
| `/` | Lista com filtro, ordenação e paginação |
| `/imagem/<id>/` | Detalhes da imagem |
| `/imagem/novo/` | Cadastro |
| `/imagem/<id>/editar/` | Edição |
| `/imagem/<id>/deletar/` | Confirmação de exclusão |
| `/admin/` | Painel administrativo |

## ⚠️ Limitações conhecidas

- Não há login: qualquer visitante pode cadastrar, editar e excluir imagens (só o painel admin exige autenticação).
- Os testes automatizados ainda não foram escritos.
- Ao excluir uma imagem, o arquivo físico na pasta `media/` não é removido.

## 👥 Equipe

Projeto desenvolvido em dupla:

- **Wesley Pereira Queiroga** — [@wesley-absolut](https://github.com/wesley-absolut)
- **Anderzoumm** — [@Anderzoumm](https://github.com/Anderzoumm) · repositório original: [Anderzoumm/Galeria-de-Fotos](https://github.com/Anderzoumm/Galeria-de-Fotos)

### Minha contribuição

Fiz a parte de back-end:

- Models `Categoria` e `Imagem` (relação `ForeignKey` e upload com `ImageField`) e as migrações.
- CRUD de imagens com class-based views (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`) e as rotas em `urls.py`.
- Filtro por categoria via parâmetro GET e paginação de 6 imagens por página.
- Ordenação (mais recentes, mais antigas, título A-Z) usando um dicionário de campos permitidos.
- Template tag `url_replace`, que mantém filtro e ordenação ao trocar de página.
- Configuração do PostgreSQL com variáveis de ambiente (`python-dotenv`).

A interface (CSS e layout dos templates) vem do repositório original da dupla.
