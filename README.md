# Django Projeto AV2 CRUD - Eduardo Ribeiro Leal - 28034702

Este projeto consiste em um CRUD simples de produtos feito em Django, com controle de login e permissões.

## Funcionalidades

- **CRUD de Produtos**:  
  - Listar produtos  
  - Detalhar um produto específico  
  - Criar novo produto  
  - Editar produto existente  
  - Deletar produto

- **Autenticação**:  
  - Página de login padrão na rota `/`  
  - Apenas usuários superusuários podem acessar as telas de produtos  
  - Caso o usuário não esteja logado ou não seja superusuário, será redirecionado para a página de login

- **Redirecionamentos**:  
  - Ao efetuar login com sucesso, o usuário é direcionado automaticamente para a página `/produtos/`  
  - Caso o usuário tente acessar qualquer página de produto sem permissão, é redirecionado para a tela de login

## Detalhes do Usuário Criado

- **Superusuário**:  
  - **Nome**: Eduardo Ribeiro Leal  
  - **E-mail**: eduardoleal.contact@gmail.com  
  - **Username**: eduardo  
  - **Senha**: 12345

Esse superusuário pode ser utilizado para fazer login no sistema e testar todas as funcionalidades do CRUD.
