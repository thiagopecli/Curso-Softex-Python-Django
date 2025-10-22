# test_user_service.py
import pytest
import os
import sys
from user_service import UserService
from database import DatabaseConnection
from hasher import hash_senha


@pytest.fixture(scope="function")
def user_service():
    """Fixture que cria uma instância do UserService com banco de dados de teste."""
    # Usa um banco de dados de teste diferente
    test_db = "test_escola.db"
    
    # Remove o banco de dados de teste se já existir
    if os.path.exists(test_db):
        os.remove(test_db)
    
    # Modifica temporariamente o nome do banco padrão
    original_init = DatabaseConnection.__init__
    
    def custom_init(self, db_name="escola.db"):
        self.db_name = test_db
        self.conn = None
        self.cursor = None
    
    DatabaseConnection.__init__ = custom_init
    
    # Cria o serviço
    service = UserService()
    
    yield service
    
    # Restaura o __init__ original
    DatabaseConnection.__init__ = original_init
    
    # Limpa o banco de dados após os testes
    if os.path.exists(test_db):
        os.remove(test_db)


@pytest.fixture
def user_service_with_users(user_service):
    """Fixture que cria uma instância do UserService com alguns usuários de teste."""
    # Cria usuários de teste
    user_service.register_user(
        senha="senha12345",
        email="teste@example.com",
        nome_completo="João Silva",
        perfil="Afiliado"
    )
    user_service.register_user(
        senha="senha12345",
        email="admin@example.com",
        nome_completo="Admin User",
        perfil="Diretoria"
    )
    user_service.register_user(
        senha="senha12345",
        email="maria@example.com",
        nome_completo="Maria Santos",
        perfil="Associado"
    )
    return user_service


class TestSafeUserData:
    """Testes para o método _safe_user_data"""
    
    def test_safe_user_data_with_valid_user(self, user_service):
        """Testa se o método remove a senha de um usuário válido."""
        user = {
            'id': 1,
            'email': 'teste@example.com',
            'nome_completo': 'João Silva',
            'senha_hash': 'hash_da_senha',
            'perfil_acesso': 'Afiliado'
        }
        
        safe_user = user_service._safe_user_data(user)
        
        assert safe_user is not None
        assert 'senha_hash' not in safe_user
        assert safe_user['id'] == 1
        assert safe_user['email'] == 'teste@example.com'
        assert safe_user['nome_completo'] == 'João Silva'
    
    def test_safe_user_data_with_none(self, user_service):
        """Testa se o método retorna None quando o usuário é None."""
        safe_user = user_service._safe_user_data(None)
        assert safe_user is None
    
    def test_safe_user_data_without_password(self, user_service):
        """Testa se o método funciona quando o usuário não tem senha."""
        user = {
            'id': 1,
            'email': 'teste@example.com',
            'nome_completo': 'João Silva',
            'perfil_acesso': 'Afiliado'
        }
        
        safe_user = user_service._safe_user_data(user)
        
        assert safe_user is not None
        assert safe_user['id'] == 1


class TestIsAuthorized:
    """Testes para o método _is_authorized"""
    
    def test_diretoria_always_authorized(self, user_service):
        """Testa se Diretoria sempre tem autorização."""
        assert user_service._is_authorized(1, "Diretoria", 2, "edit_other") is True
        assert user_service._is_authorized(1, "Diretoria", None, "any_action") is True
    
    def test_edit_self_authorized(self, user_service):
        """Testa se o usuário pode editar a si mesmo."""
        assert user_service._is_authorized(1, "Afiliado", 1, "edit_self") is True
    
    def test_edit_self_not_authorized_different_user(self, user_service):
        """Testa se o usuário não pode editar outro usuário."""
        assert user_service._is_authorized(1, "Afiliado", 2, "edit_self") is False
    
    def test_edit_other_not_authorized(self, user_service):
        """Testa se usuário comum não pode editar outros."""
        assert user_service._is_authorized(1, "Afiliado", 2, "edit_other") is False
    
    def test_no_target_user_id_not_authorized(self, user_service):
        """Testa se não autorizado quando target_user_id é None."""
        assert user_service._is_authorized(1, "Afiliado", None, "edit_other") is False


class TestRegisterUser:
    """Testes para o método register_user"""
    
    def test_register_user_success(self, user_service):
        """Testa o registro bem-sucedido de um usuário."""
        success, message = user_service.register_user(
            senha="senha12345",
            email="novo@example.com",
            nome_completo="Novo Usuario",
            perfil="Afiliado"
        )
        
        assert success is True
        assert message == "Usuário registrado com sucesso!"
    
    def test_register_user_password_too_short(self, user_service):
        """Testa o registro com senha muito curta."""
        success, message = user_service.register_user(
            senha="1234567",
            email="novo@example.com",
            nome_completo="Novo Usuario"
        )
        
        assert success is False
        assert "8 caracteres" in message
    
    def test_register_user_invalid_email_no_at(self, user_service):
        """Testa o registro com email sem @."""
        success, message = user_service.register_user(
            senha="senha12345",
            email="novoexample.com",
            nome_completo="Novo Usuario"
        )
        
        assert success is False
        assert "email inválido" in message
    
    def test_register_user_invalid_email_no_com(self, user_service):
        """Testa o registro com email que não termina com .com."""
        success, message = user_service.register_user(
            senha="senha12345",
            email="novo@example.net",
            nome_completo="Novo Usuario"
        )
        
        assert success is False
        assert "email inválido" in message
    
    def test_register_user_invalid_email_too_short(self, user_service):
        """Testa o registro com email muito curto."""
        success, message = user_service.register_user(
            senha="senha12345",
            email="a@b.com",
            nome_completo="Novo Usuario"
        )
        
        assert success is False
        assert "email inválido" in message
    
    def test_register_user_empty_name(self, user_service):
        """Testa o registro com nome vazio."""
        success, message = user_service.register_user(
            senha="senha12345",
            email="novo@example.com",
            nome_completo=""
        )
        
        assert success is False
        assert "nome completo não pode estar vazio" in message
    
    def test_register_user_name_with_numbers(self, user_service):
        """Testa o registro com nome contendo números."""
        success, message = user_service.register_user(
            senha="senha12345",
            email="novo@example.com",
            nome_completo="João123"
        )
        
        assert success is False
        assert "apenas letras e espaços" in message
    
    def test_register_user_name_with_special_chars(self, user_service):
        """Testa o registro com nome contendo caracteres especiais."""
        success, message = user_service.register_user(
            senha="senha12345",
            email="novo@example.com",
            nome_completo="João@Silva"
        )
        
        assert success is False
        assert "apenas letras e espaços" in message
    
    def test_register_user_duplicate_email(self, user_service_with_users):
        """Testa o registro com email duplicado."""
        success, message = user_service_with_users.register_user(
            senha="senha12345",
            email="teste@example.com",
            nome_completo="Outro Usuario"
        )
        
        assert success is False
        assert "e-mail" in message.lower() or "email" in message.lower()


class TestLoginUser:
    """Testes para o método login_user"""
    
    def test_login_success(self, user_service_with_users):
        """Testa login bem-sucedido."""
        user, message = user_service_with_users.login_user(
            email="teste@example.com",
            senha="senha12345"
        )
        
        assert user is not None
        assert message == "Login bem-sucedido!"
        assert 'senha_hash' not in user
        assert user['email'] == "teste@example.com"
    
    def test_login_empty_email(self, user_service):
        """Testa login com email vazio."""
        user, message = user_service.login_user(
            email="",
            senha="senha12345"
        )
        
        assert user is None
        assert "obrigatórios" in message
    
    def test_login_empty_password(self, user_service):
        """Testa login com senha vazia."""
        user, message = user_service.login_user(
            email="teste@example.com",
            senha=""
        )
        
        assert user is None
        assert "obrigatórios" in message
    
    def test_login_user_not_found(self, user_service_with_users):
        """Testa login com usuário não existente."""
        user, message = user_service_with_users.login_user(
            email="naoexiste@example.com",
            senha="senha12345"
        )
        
        assert user is None
        assert "não encontrado" in message
    
    def test_login_wrong_password(self, user_service_with_users):
        """Testa login com senha incorreta."""
        user, message = user_service_with_users.login_user(
            email="teste@example.com",
            senha="senhaerrada"
        )
        
        assert user is None
        assert "incorreta" in message


class TestUpdateUserProfile:
    """Testes para o método update_user_profile"""
    
    def test_update_own_profile_success(self, user_service_with_users):
        """Testa atualização bem-sucedida do próprio perfil."""
        # Primeiro faz login para obter o ID
        user, _ = user_service_with_users.login_user("teste@example.com", "senha12345")
        user_id = user['id']
        
        success, message = user_service_with_users.update_user_profile(
            current_user_id=user_id,
            current_user_profile="Afiliado",
            target_user_id=user_id,
            new_data={'nome_completo': 'João Silva Santos'}
        )
        
        assert success is True
        assert "atualizado com sucesso" in message
    
    def test_update_other_profile_not_authorized(self, user_service_with_users):
        """Testa que usuário comum não pode atualizar outro perfil."""
        user1, _ = user_service_with_users.login_user("teste@example.com", "senha12345")
        user2, _ = user_service_with_users.login_user("maria@example.com", "senha12345")
        
        success, message = user_service_with_users.update_user_profile(
            current_user_id=user1['id'],
            current_user_profile="Afiliado",
            target_user_id=user2['id'],
            new_data={'nome_completo': 'Maria Silva'}
        )
        
        assert success is False
        assert "Acesso negado" in message
    
    def test_update_diretoria_can_update_others(self, user_service_with_users):
        """Testa que Diretoria pode atualizar outros perfis."""
        admin, _ = user_service_with_users.login_user("admin@example.com", "senha12345")
        user, _ = user_service_with_users.login_user("teste@example.com", "senha12345")
        
        success, message = user_service_with_users.update_user_profile(
            current_user_id=admin['id'],
            current_user_profile="Diretoria",
            target_user_id=user['id'],
            new_data={'nome_completo': 'João Silva Atualizado'}
        )
        
        assert success is True
        assert "atualizado com sucesso" in message
    
    def test_update_no_valid_data(self, user_service_with_users):
        """Testa atualização sem dados válidos."""
        user, _ = user_service_with_users.login_user("teste@example.com", "senha12345")
        
        success, message = user_service_with_users.update_user_profile(
            current_user_id=user['id'],
            current_user_profile="Afiliado",
            target_user_id=user['id'],
            new_data={}
        )
        
        assert success is False
        assert "Nenhum dado válido" in message
    
    def test_update_password_too_short(self, user_service_with_users):
        """Testa atualização com senha muito curta."""
        user, _ = user_service_with_users.login_user("teste@example.com", "senha12345")
        
        success, message = user_service_with_users.update_user_profile(
            current_user_id=user['id'],
            current_user_profile="Afiliado",
            target_user_id=user['id'],
            new_data={'senha': '1234567'}
        )
        
        assert success is False
        assert "8 caracteres" in message
    
    def test_update_password_success(self, user_service_with_users):
        """Testa atualização bem-sucedida de senha."""
        user, _ = user_service_with_users.login_user("teste@example.com", "senha12345")
        
        success, message = user_service_with_users.update_user_profile(
            current_user_id=user['id'],
            current_user_profile="Afiliado",
            target_user_id=user['id'],
            new_data={'senha': 'novasenha123'}
        )
        
        assert success is True
        
        # Verifica se consegue logar com a nova senha
        user_new, msg = user_service_with_users.login_user("teste@example.com", "novasenha123")
        assert user_new is not None


class TestDeleteUser:
    """Testes para o método delete_user"""
    
    def test_delete_user_not_authorized(self, user_service_with_users):
        """Testa que usuário comum não pode deletar."""
        user, _ = user_service_with_users.login_user("teste@example.com", "senha12345")
        
        success, message = user_service_with_users.delete_user(
            current_user_profile="Afiliado",
            user_id=user['id']
        )
        
        assert success is False
        assert "Acesso negado" in message
    
    def test_delete_user_diretoria_success(self, user_service_with_users):
        """Testa que Diretoria pode deletar usuários."""
        user, _ = user_service_with_users.login_user("teste@example.com", "senha12345")
        
        success, message = user_service_with_users.delete_user(
            current_user_profile="Diretoria",
            user_id=user['id']
        )
        
        assert success is True
        assert "deletado com sucesso" in message
    
    def test_delete_nonexistent_user(self, user_service_with_users):
        """Testa deleção de usuário inexistente."""
        success, message = user_service_with_users.delete_user(
            current_user_profile="Diretoria",
            user_id=9999
        )
        
        assert success is False
        assert "não encontrado" in message


class TestGetUserById:
    """Testes para o método get_user_by_id"""
    
    def test_get_user_by_id_success(self, user_service_with_users):
        """Testa buscar usuário por ID com sucesso."""
        user_login, _ = user_service_with_users.login_user("teste@example.com", "senha12345")
        
        user = user_service_with_users.get_user_by_id(user_login['id'])
        
        assert user is not None
        assert user['email'] == "teste@example.com"
        assert 'senha_hash' not in user
    
    def test_get_user_by_id_not_found(self, user_service_with_users):
        """Testa buscar usuário inexistente."""
        user = user_service_with_users.get_user_by_id(9999)
        
        assert user is None


class TestGetAllUsers:
    """Testes para o método get_all_users"""
    
    def test_get_all_users(self, user_service_with_users):
        """Testa listar todos os usuários."""
        users = user_service_with_users.get_all_users()
        
        assert len(users) == 3
        for user in users:
            assert 'senha_hash' not in user
            assert 'email' in user
            assert 'nome_completo' in user
    
    def test_get_all_users_empty(self, user_service):
        """Testa listar usuários quando não há nenhum."""
        users = user_service.get_all_users()
        
        assert len(users) == 0
