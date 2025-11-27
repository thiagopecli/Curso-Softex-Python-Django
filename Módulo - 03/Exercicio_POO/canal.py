class Notificacao:
    def enviar(self, mensagem):
        raise NotImplementedError

class Email(Notificacao):
    def enviar(self, mensagem):
        print(f"Email enviado: {mensagem}")

class SMS(Notificacao):
    def enviar(self, mensagem):
        print(f"SMS enviado: {mensagem}")