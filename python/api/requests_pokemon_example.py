import requests

# Функція для отримання інформації про покемона
def get_pokemon_info(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
    response = requests.get(url)  # Надсилаємо GET запит до API

    if response.status_code == 200:  # Перевіряємо, чи вдалося отримати дані
        pokemon_data = response.json()  # Перетворюємо відповідь в формат JSON
        return pokemon_data  # Повертаємо дані
    else:
        return None  # Якщо запит не вдався, повертаємо None

# Функція для виведення базової інформації про покемона
def display_pokemon_info(pokemon_name):
    pokemon_info = get_pokemon_info(pokemon_name)

    if pokemon_info:
        print(f"Name: {pokemon_info['name'].capitalize()}")
        print(f"Height: {pokemon_info['height']} decimeters")  # Висота покемона в дециметрах
        print(f"Weight: {pokemon_info['weight']} hectograms")  # Вага покемона в гектаграмах
        print("Types:")
        for poke_type in pokemon_info['types']:
            print(f"- {poke_type['type']['name'].capitalize()}")
    else:
        print("Pokémon not found.")

# Головна програма
def main():
    pokemon_name = input("Enter the name of a Pokémon: ")
    display_pokemon_info(pokemon_name)

if __name__ == "__main__":
    main()
