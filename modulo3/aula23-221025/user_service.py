# user_service.py
from user_model import UserModel
from hasher import hash_senha, verificar_senha


class UserService:
    def __init__(self):
        self.user_model = UserModel()

    def _safe_user_data(self, user) -> dict | None:
        if user is None:
            return None
        user_dict = dict(user)
        user_dict.pop('senha_hast', None)
        return user_dict

    def _is_authorized(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        action: str,
    ) -> bool:
        if current_user_profile == "Diretoria":
            return True
        
        if target_user_id is None and action != "general_check":
            return False
        
        if action == "edit_self":
            return current_user_id == target_user_id
        return False

    def register_user(
        self,
        senha: str,
        email: str,
        nome_completo: str,
        perfil: str = "Afiliado",
    ) -> tuple[bool, str]:
        if len(senha) > 8:
            return False, "Erro: A senha deve ter no minimo 8 caracteres."
        
        if len(email) < 10 or '@' not in email or not email.endswith('.com'):
            return False, "Erro: Formato de email inválido (mínimo 10 caracteres, conter '@' e terminar com '.com')."
        
        nome_sem_espacos = nome_completo.replace(' ', '')
        if not nome_completo.strip():
            return False, "Erro: O nome completo não pode estar vazio."
        if not nome_sem_espacos.isalpha():
            return False, "Erro: O nome completo deve conter apenas letras e espaços."
        try:
            senha_hashed = hash_senha(senha)
            novo_usuario = self.user_model.create_user(
            nome_completo=nome_completo,
            email=email,
            senha=senha_hashed,
            perfil=perfil
            )
            if novo_usuario:
                return True, "Usuário registrado com sucesso!"
            else:
                return False, "Erro ao registrar usuário (verifique se o email já existe)."
        except Exception as e:
            return False, f"Erro inesperado no registro: {e}"

    def login_user(self, email: str, senha: str) -> tuple[dict | None, str]:
        if not email or not senha:
            return None, "Email e senha são obrigatórios."

        user_db = self.user_model.find_user_by_email(email)

        if user_db:
            senha_hash_db = user_db.get('senha')
            if senha_hash_db and verificar_senha(senha, senha_hash_db):
                safe_data = self._safe_user_data(user_db)
                return safe_data, "Login bem-sucedido!"
            else:
                return None, "Senha incorreta."
        else:
            return None, "Usuário não encontrado."

    def update_user_profile(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int,
        new_data: dict,
    ) -> tuple[bool, str]:
        action = "edit_self" if current_user_id == target_user_id else "edit_other"

        if not self._is_authorized(current_user_id, current_user_profile, target_user_id, action):
            return False, "Acesso negado."

        allowed_keys = {'senha', 'nome_completo', 'email'}
        data_to_update = {key: value for key, value in new_data.items() if key in allowed_keys and value} 

        if not data_to_update:
            return False, "Nenhum dado válido para atualização fornecido."

        if 'senha' in data_to_update:
            nova_senha = data_to_update['senha']
            if len(nova_senha) < 8:
                return False, "Erro: A nova senha deve ter no mínimo 8 caracteres."
        
        data_to_update['senha'] = hash_senha(nova_senha)

        success = self.user_model.update_user_by_id(target_user_id, data_to_update)

        if success:
            return True, "Usuário atualizado com sucesso!"
        else:
            return False, "Erro ao atualizar usuário (verifique se o usuário existe)."

    def delete_user(
        self,
        current_user_profile: str,
        user_id: int,
    ) -> tuple[bool, str]:
        if current_user_profile != "Diretoria":
            return False, "Acesso negado. Apenas Diretoria pode deletar usuários."

        success = self.user_model.delete_user_by_id(user_id)

        if success:
            return True, "Usuário deletado com sucesso!"
        else:
            return False, "Erro ao deletar usuário (verifique se o usuário existe)."

    def get_user_by_id(self, user_id: int) -> dict | None:
        user_db = self.user_model.get_user_by_id(user_id)
        return self._safe_user_data(user_db)

    def get_all_users(self) -> list[dict | None]:
        all_users_db = self.user_model.get_all_users()
        return [self._safe_user_data(user) for user in all_users_db]