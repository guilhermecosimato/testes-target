def contar_letra_a(s):
    # Converte a string para minúsculas para facilitar a contagem
    s_minuscula = s.lower()
    
    # Conta a ocorrência da letra 'a'
    contagem = s_minuscula.count('a')
    
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vez(es) na string.")
    else:
        print("A letra 'a' não está presente na string.")

# Solicita uma string ao usuário
entrada = input("Informe uma string: ")
contar_letra_a(entrada)
