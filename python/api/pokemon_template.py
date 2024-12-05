import requests
import random


#Here are the first 10 Pokémon names:
#['bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie', 'pikachu']


# Клас Pokemon
class Pokemon:
    def __init__(self, name, hp, attack, defense, speed):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

    # Метод для виведення статистики покемона
    def display_info(self):
        print(f"Name: {self.name.capitalize()}")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Speed: {self.speed}")
        print("")

    # Метод для бою між покемонами
    def battle(self, opponent):
        print(f"\nThe battle begins between {self.name.capitalize()} and {opponent.name.capitalize()}!\n")

        # Виводимо стати обох покемонів
        print(f"Stats for {self.name.capitalize()}:")
        self.display_info()
        print(f"Stats for {opponent.name.capitalize()}:")
        opponent.display_info()


# Функція для отримання даних про покемона з PokeAPI
def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return Pokemon(
            name=pokemon_data['name'],
            hp=pokemon_data['stats'][0]['base_stat'],
            attack=pokemon_data['stats'][1]['base_stat'],
            defense=pokemon_data['stats'][2]['base_stat'],
            speed=pokemon_data['stats'][5]['base_stat']
        )
    else:
        return None


# Головна програма
def main():
    # Отримуємо імена покемонів
    pokemon1_name = input("Enter the name of the first Pokémon: ")
    pokemon2_name = input("Enter the name of the second Pokémon: ")

    # Отримуємо інформацію про покемонів
    pokemon1 = get_pokemon_info(pokemon1_name)
    pokemon2 = get_pokemon_info(pokemon2_name)

    if pokemon1 and pokemon2:
        # Запускаємо бій
        pokemon1.battle(pokemon2)
    else:
        print("One or both Pokémon could not be found. Please check the names.")


# Запускаємо гру
if __name__ == "__main__":
    main()
