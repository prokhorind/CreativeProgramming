import requests
import random


#Here are the first 10 Pokémon names:
#['bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle', 'blastoise', 'caterpie', 'pikachu']

# Функція для отримання даних про покемона
def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return {
            'name': pokemon_data['name'],
            'attack': pokemon_data['stats'][1]['base_stat'],  # Атака
            'defense': pokemon_data['stats'][2]['base_stat'],  # Захист
            'hp': pokemon_data['stats'][0]['base_stat'],  # Здоров'я
            'speed': pokemon_data['stats'][5]['base_stat'],  # Швидкість
        }
    else:
        return None


# Функція для виведення інформації про покемона
def display_pokemon_info(pokemon):
    print(f"Name: {pokemon['name'].capitalize()}")
    print(f"HP: {pokemon['hp']}")
    print(f"Attack: {pokemon['attack']}")
    print(f"Defense: {pokemon['defense']}")
    print(f"Speed: {pokemon['speed']}")
    print("")


# Функція для бою між двома покемонами
def battle(pokemon1, pokemon2):
    print(f"\nThe battle begins between {pokemon1['name'].capitalize()} and {pokemon2['name'].capitalize()}!\n")

    # Виводимо стати обох покемонів
    print(f"Stats for {pokemon1['name'].capitalize()}:")
    display_pokemon_info(pokemon1)
    print(f"Stats for {pokemon2['name'].capitalize()}:")
    display_pokemon_info(pokemon2)



# Головна програма
def main():
    # Отримуємо імена покемонів
    pokemon1_name = input("Enter the name of the first Pokémon: ")
    pokemon2_name = input("Enter the name of the second Pokémon: ")

    # Отримуємо інформацію про покемонів
    pokemon1 = get_pokemon_info(pokemon1_name)
    pokemon2 = get_pokemon_info(pokemon2_name)

    if pokemon1 and pokemon2:
        battle(pokemon1, pokemon2)
    else:
        print("One or both Pokémon could not be found. Please check the names.")


# Запускаємо гру
if __name__ == "__main__":
    main()
