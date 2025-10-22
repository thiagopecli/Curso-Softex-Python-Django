# Test Suite para UserService

Este diretório contém testes automatizados para a classe `UserService` implementada em `user_service.py`.

## Estrutura dos Testes

O arquivo `test_user_service.py` contém 35 testes organizados nas seguintes classes:

### TestSafeUserData (3 testes)
Testa o método privado `_safe_user_data` que remove informações sensíveis (senhas) dos dados do usuário.

### TestIsAuthorized (5 testes)
Testa o método privado `_is_authorized` que verifica permissões de acesso baseadas no perfil do usuário.

### TestRegisterUser (9 testes)
Testa o registro de novos usuários com validações de:
- Senha (mínimo 8 caracteres)
- Email (formato válido, mínimo 10 caracteres, contém @, termina com .com)
- Nome completo (apenas letras e espaços)
- Emails duplicados

### TestLoginUser (5 testes)
Testa o login de usuários com:
- Credenciais corretas
- Credenciais incorretas
- Campos vazios
- Usuários não existentes

### TestUpdateUserProfile (6 testes)
Testa a atualização de perfis de usuários com:
- Autorização (usuário só pode editar a si mesmo)
- Diretoria pode editar qualquer usuário
- Validação de senha nova
- Validação de dados para atualização

### TestDeleteUser (3 testes)
Testa a exclusão de usuários com:
- Apenas Diretoria pode deletar
- Outros perfis não têm permissão
- Tentativa de deletar usuário inexistente

### TestGetUserById (2 testes)
Testa a busca de usuários por ID.

### TestGetAllUsers (2 testes)
Testa a listagem de todos os usuários.

## Como Executar os Testes

### Pré-requisitos

Instale o pytest:
```bash
pip install pytest
```

### Executar todos os testes

```bash
cd "Módulo - 03/aula23-221025"
python3 -m pytest test_user_service.py -v
```

### Executar testes específicos

Executar uma classe de testes:
```bash
python3 -m pytest test_user_service.py::TestRegisterUser -v
```

Executar um teste específico:
```bash
python3 -m pytest test_user_service.py::TestRegisterUser::test_register_user_success -v
```

### Executar com relatório de cobertura

```bash
pip install pytest-cov
python3 -m pytest test_user_service.py --cov=user_service --cov-report=html
```

## Resultados Esperados

Todos os 35 testes devem passar com sucesso:
- ✓ 35 passed in ~0.2s

## Observações

- Os testes usam um banco de dados temporário (`test_escola.db`) que é criado e removido automaticamente
- Cada teste é independente e não afeta os outros
- Os testes verificam tanto casos de sucesso quanto casos de erro
- As validações incluem edge cases e cenários de segurança

## Cobertura de Código

Os testes cobrem 100% dos métodos públicos e privados da classe `UserService`:
- `__init__`
- `_safe_user_data`
- `_is_authorized`
- `register_user`
- `login_user`
- `update_user_profile`
- `delete_user`
- `get_user_by_id`
- `get_all_users`
