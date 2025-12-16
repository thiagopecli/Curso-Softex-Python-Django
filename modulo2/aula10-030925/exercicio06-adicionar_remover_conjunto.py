"""6.  Adicionar e Remover do Conjunto: 
Crie um conjunto linguas = {'português', 'inglês'}. 
Adicione 'espanhol' e depois remova 'português'. Imprima o conjunto final."""

linguas = {'português', 'inglês'}
print(f"Conjunto inicial: {linguas}")

linguas.add('espanhol')
print(f"Conjunto após adicionar 'espanhol': {linguas}")

linguas.remove('português')
print(f"Conjunto após remover 'português': {linguas}")