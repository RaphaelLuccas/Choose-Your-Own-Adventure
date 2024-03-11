name = input("Qual o seu nome?: ")
print(f"Seja bem vindo {name}, a esta aventura!")

answer = input(
    "Voce esta em uma floresta escura e so pode ir para direita ou esquerda: ").lower()

if answer == "esquerda":
    print("Voce morreu!")

elif answer == "direita":
    answer = input(
        "Voce encontrou um castelo, deseja entrar ou olhar os arredores: ").lower()
    
    if answer == "entrar":
        print("Voce encontrou um tesouro e sobreviveu!")
    elif answer == "olhar":
        print("Voce encontrou um Minotauro, e morreu!")
    else:
        print("Comando invalido")

else:
    print("Comando invalido!")