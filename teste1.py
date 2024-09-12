import random

def adivinhe_o_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("Adivinhe o número entre 1 e 100")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1
        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break

def jogo_da_forca():
    palavras = ["python", "programacao", "desenvolvedor", "inteligencia"]
    palavra = random.choice(palavras)
    palavra_oculta = ["_" for _ in palavra]
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca!")
    print(" ".join(palavra_oculta))

    while tentativas > 0 and "_" in palavra_oculta:
        letra = input("Digite uma letra: ").lower()
        if letra in palavra:
            for i, char in enumerate(palavra):
                if char == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas -= 1
            print(f"Letra incorreta. Você tem {tentativas} tentativas restantes.")

        print(" ".join(palavra_oculta))

    if "_" not in palavra_oculta:
        print("Parabéns, você venceu!")
    else:
        print(f"Você perdeu! A palavra era '{palavra}'.")

def perguntas_e_respostas():
    perguntas = [
        {"pergunta": "Qual é a capital da França?", "respostas": ["Paris", "Londres", "Berlim", "Madri"], "correta": "Paris"},
        {"pergunta": "Qual é o maior planeta do sistema solar?", "respostas": ["Terra", "Marte", "Júpiter", "Saturno"], "correta": "Júpiter"},
        {"pergunta": "Quem escreveu 'Dom Casmurro'?", "respostas": ["Machado de Assis", "José de Alencar", "Graciliano Ramos", "Monteiro Lobato"], "correta": "Machado de Assis"}
    ]

    pontuacao = 0

    print("Perguntas e Respostas")

    for pergunta in perguntas:
        print(pergunta["pergunta"])
        for i, resposta in enumerate(pergunta["respostas"], 1):
            print(f"{i}. {resposta}")
        escolha = int(input("Escolha a resposta correta (1-4): "))
        if pergunta["respostas"][escolha - 1] == pergunta["correta"]:
            pontuacao += 1
            print("Correto!")
        else:
            print(f"Incorreto! A resposta correta era '{pergunta['correta']}'.")

    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")

def main():
    while True:
        print("\nEscolha um jogo:")
        print("1. Adivinhe o número")
        print("2. Jogo da Forca")
        print("3. Perguntas e Respostas")
        print("4. Sair")

        escolha = input("Digite o número do jogo desejado: ")

        if escolha == "1":
            adivinhe_o_numero()
        elif escolha == "2":
            jogo_da_forca()
        elif escolha == "3":
            perguntas_e_respostas()
        elif escolha == "4":
            print("Saindo do programa...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
