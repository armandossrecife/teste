import random
import time

def play_game():
    print("Bem-vindo ao Jogo de Adivinhação!")
    level = input("Escolha o nível de dificuldade (Fácil, Médio ou Difícil): ").lower()
    if level == "fácil":
        max_guesses = 10
    elif level == "médio":
        max_guesses = 5
    else:
        max_guesses = 3

    secret_number = random.randint(0, 100)
    player_name = input("Qual é o seu nome? ")
    print(f"Olá {player_name}! Estou pensando em um número entre 0 e 100. Tente adivinhar!")

    num_guesses = 0
    start_time = time.time()
    while num_guesses < max_guesses:
        try:
            guess = input("Digite seu palpite: ")
            while not guess.isdigit():
                guess = input("Digite um número inteiro entre 0 e 100: ")
            guess = int(guess)
            if guess < 0 or guess > 100:
                print("Palpite inválido. Tente novamente.")
                continue
        except ValueError:
            print("Palpite inválido. Tente novamente.")
            continue

        num_guesses += 1
        if guess == secret_number:
            end_time = time.time()
            total_time = round(end_time - start_time, 2)
            print(f"Parabéns {player_name}! Você acertou em {num_guesses} jogadas em {total_time} segundos!")
            if num_guesses <= max_guesses:
                print("Você ganhou o jogo!")
            return True
        elif guess < secret_number:
            print("Você errou para baixo... tente um número maior.")
        else:
            print("Você errou para cima... tente um número menor.")

    print("Você excedeu o número máximo de jogadas. O número secreto era:", secret_number)
    return False

while True:
    if not play_game():
        print("Fim de jogo.")
        break
    if input("Deseja jogar novamente? (S/N) ").lower() != "s":
        break
