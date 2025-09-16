"""14. Gerador de Fibonacci: Crie uma função que receba um número inteiro n e retorne uma 
lista com a sequência de Fibonacci até o n-ésimo termo. A sequência de Fibonacci começa com 0 e 1, e cada termo subsequente é a soma dos dois termos anteriores."""

def gerar_fibonacci(n: int) -> list:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci = [0, 1]
    for i in range(2, n):
        proximo = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(proximo)
    return fibonacci

resultado = gerar_fibonacci(10)
print(f"A sequência de Fibonacci até o 10º termo é: {resultado}")