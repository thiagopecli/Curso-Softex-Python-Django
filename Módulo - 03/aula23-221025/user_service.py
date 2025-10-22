# user_service.py
from user_model import UserModel
from hasher import hash_senha, verificar_senha


class UserService:

    def __init__(self):
        """
        Cria um atributo que receberá a UserModel como composição.
        """
        self.user_model = UserModel()  # Instancia o UserModel

    def _safe_user_data(self, user) -> dict | None:
        """
        Este é um método privado que recebe um usuário do banco.
        Verifica se o usuário existe e então retorna ele sem a sua senha.
        Caso ele não exista retorna None.
        """
        if user:
            safe_data = user.copy()  # Cria uma cópia para não modificar o original
            # Remove a senha (ajuste a chave 'senha' se o nome for diferente no seu UserModel)
            if 'senha_hash' in safe_data:
                del safe_data['senha_hash']
            return safe_data
        return None

    def _is_authorized(
        self,
        current_user_id: int | None,
        current_user_profile: str,
        target_user_id: int | None,  # Permite None para verificações gerais
        action: str,
    ) -> bool:
        """
        Método que verifica o perfil do usuário, se for Diretoria retorne true.
        Se não tiver target_user_id (para ações que o exigem implicitamente, como editar outro), retorne false (exceto Diretoria).
        Se action == "edit_self" retorne current_user_id == target_user_id.
        No geral retorne false.
        """
        if current_user_profile == "Diretoria":
            return True
        
        # Se a ação exige um alvo, mas ele não foi fornecido (e não é Diretoria)
        if target_user_id is None and action != "general_check":  # Adicionado "general_check" como exemplo
             return False

        if action == "edit_self":
            # Verifica se o usuário atual está tentando editar a si mesmo
            return current_user_id == target_user_id

        # Para outras ações, apenas Diretoria tem permissão por padrão (já tratado acima)
        return False

    def register_user(
        self,
        senha: str,
        email: str,
        nome_completo: str,
        perfil: str = "Afiliado",  # Valor padrão para perfil
    ) -> tuple[bool, str]:
        """
        Método para criar um usuário.
        Validações de senha, email e nome.
        Faz o hash da senha e salva usando o método create_user da User Model.
        """
        # Validação da senha
        if len(senha) < 8:
            return False, "Erro: A senha deve ter no mínimo 8 caracteres."

        # Validação do email
        if len(email) < 10 or '@' not in email or not email.endswith('.com'):
            return False, "Erro: Formato de email inválido (mínimo 10 caracteres, conter '@' e terminar com '.com')."

        # Validação do nome
        nome_sem_espacos = nome_completo.replace(' ', '')  # Remove espaços para checar só letras
        if not nome_completo.strip():  # Verifica se está vazio ou só com espaços
             return False, "Erro: O nome completo não pode estar vazio."
        if not nome_sem_espacos.isalpha():
            return False, "Erro: O nome completo deve conter apenas letras e espaços."

        # Se todas as validações passaram
        try:
            senha_hashed = hash_senha(senha)
            # Assume que create_user retorna o usuário criado ou None em caso de erro (ex: email duplicado)
            # Ajuste os parâmetros conforme a sua classe UserModel
            success, message = self.user_model.create_user(
                senha_hash=senha_hashed,
                email=email,
                nome_completo=nome_completo,
                perfil_acesso=perfil
            )
            if success:
                 return True, "Usuário registrado com sucesso!"
            else:
                 # Pode ser um erro interno do model ou email duplicado
                 return False, message
        except Exception as e:
            # Captura erros inesperados durante o hash ou criação
            return False, f"Erro inesperado no registro: {e}"


    def login_user(self, email: str, senha: str) -> tuple[dict | None, str]:
        """
        Este método é o login do usuário, deve receber um email e senha não vazios.
        Usa o método find_user_by_email para buscar o usuário.
        Compara a senha passada com a senha hash do DB usando verificar_senha.
        Retorna os dados seguros do usuário e mensagem de sucesso, ou None e mensagem de erro.
        """
        if not email or not senha:
            return None, "Email e senha são obrigatórios."

        user_db = self.user_model.find_user_by_email(email)

        if user_db:
            # Converte Row para dict e assume que a senha no banco está na chave 'senha_hash'
            user_dict = dict(user_db)
            senha_hash_db = user_dict.get('senha_hash')
            if senha_hash_db and verificar_senha(senha, senha_hash_db):
                safe_data = self._safe_user_data(user_dict)
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
        """
        Método para atualizar usuários.
        Verifica autorização, valida os dados a serem atualizados e chama o método da UserModel.
        """
        # Define a ação para a verificação de autorização
        action = "edit_self" if current_user_id == target_user_id else "edit_other"

        if not self._is_authorized(current_user_id, current_user_profile, target_user_id, action):
            return False, "Acesso negado."

        # Verifica se há dados válidos para atualizar
        allowed_keys = {'senha', 'nome_completo', 'email'}
        data_to_update = {key: value for key, value in new_data.items() if key in allowed_keys and value}  # Filtra chaves permitidas e não vazias

        if not data_to_update:
            return False, "Nenhum dado válido para atualização fornecido."

        # Validações adicionais (exemplo para senha)
        if 'senha' in data_to_update:
            nova_senha = data_to_update['senha']
            if len(nova_senha) < 8:
                return False, "Erro: A nova senha deve ter no mínimo 8 caracteres."
            # Faz o hash da nova senha antes de atualizar
            data_to_update['senha_hash'] = hash_senha(nova_senha)
            del data_to_update['senha']
            
        # Adicione aqui validações para 'nome_completo' e 'email' se desejar, similar ao register_user

        # Chama o método de atualização do UserModel
        success, message = self.user_model.update_user_by_id(target_user_id, data_to_update)

        if success:
            return True, "Usuário atualizado com sucesso!"
        else:
            return False, message

    def delete_user(
        self,
        current_user_profile: str,
        user_id: int,
    ) -> tuple[bool, str]:
        """
        Método para deletar usuários.
        Só é permitido se o perfil for Diretoria.
        """
        if current_user_profile != "Diretoria":
            return False, "Acesso negado. Apenas Diretoria pode deletar usuários."

        success, message = self.user_model.delete_user_by_id(user_id)

        if success:
            return True, "Usuário deletado com sucesso!"
        else:
            return False, message

    def get_user_by_id(self, user_id: int) -> dict | None:
        """
        Método para pegar um usuário pelo id.
        Retorna os dados seguros do usuário.
        """
        user_db = self.user_model.find_user_by_id(user_id)
        if user_db:
            return self._safe_user_data(dict(user_db))
        return None

    def get_all_users(self) -> list[dict | None]:
        """
        Método para retornar todos os usuários.
        Retorna uma lista com os dados seguros de todos os usuários.
        """
        all_users_db = self.user_model.get_all_users()
        # Usa List Comprehension para aplicar _safe_user_data a cada usuário
        return [self._safe_user_data(dict(user)) for user in all_users_db]
