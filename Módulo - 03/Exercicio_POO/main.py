from usuario import Usuario
from canal import Email, SMS
from sistema import SistemaAlerta

if __name__ == "__main__":
    print("*** SISTEMA DE NOTIFICAÇÃO ***")
    
    print("\n--- Verificação de Email ---")
    nome = input("Digite o nome do usuário: ")
    
    while True:
        email_inicial = input("Digite o email: ")
        
        tem_arroba = "@" in email_inicial
        tem_ponto_com = email_inicial.endswith(".com")

        if tem_arroba and tem_ponto_com:
            break
        elif not tem_arroba and not tem_ponto_com:
            print("O email precisa conter '@' e terminar com '.com'.")
        elif not tem_arroba:
            print("O email precisa conter '@'.")
        elif not tem_ponto_com:
            print("O email precisa terminar com '.com'.")
            
    cliente = Usuario(nome, email_inicial)
    
    print(f"\nUsuário criado: {cliente.nome} | Email atual: {cliente.email}")
    
    resposta = input("Deseja alterar o email inicial? (s/n): ")

    if resposta == "s":
        while True:
            novo_email = input("Digite o novo email: ")
            
            tem_arroba = "@" in novo_email
            tem_ponto_com = novo_email.endswith(".com")
            
            if tem_arroba and tem_ponto_com:
                cliente.email = novo_email
                print("Email alterado com sucesso!")
                break
            elif not tem_arroba and not tem_ponto_com:
                print("O novo email precisa conter '@' e terminar com '.com'.")
            elif not tem_arroba:
                print("O novo email precisa conter '@'.")
            elif not tem_ponto_com:
                print("O novo email precisa terminar com '.com'.")

    else:
        print("Mantendo o email cadastrado.")

    print(f"\nEmail do cliente: {cliente.email}")

    print("\n--- Envio de Notificação ---")
    print("Escolha o canal de envio:")
    print("1 - E-mail")
    print("2 - SMS")
    
    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        print("\n--- Enviando Email ---")
        canal = Email()
        sistema = SistemaAlerta(cliente, canal)
        
        msg = input("Digite a mensagem para o E-mail: ")
        sistema.disparar(msg)

    elif opcao == "2":
        print("\n--- Enviando SMS ---")
        canal = SMS()
        sistema = SistemaAlerta(cliente, canal)
        
        msg = input("Digite a mensagem para o SMS: ")
        sistema.disparar(msg)

    else:
        print("\nOpção inválida! Nenhuma mensagem foi enviada.")

    print("\n*** FIM DO SISTEMA ***")