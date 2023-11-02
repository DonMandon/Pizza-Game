import random


def the_pizza_function():
    pizzas = ['Salami', 'Margherita', 'Diavola', 'Hawaiian', 'Buffalo', 'Pepperoni', 'BBQ', 'Neapolitan', 'Meat']
    toppings = ['salami', 'cheese', 'onions', 'anchovies', 'olives', 'pepperoni', 'BBQ sauce', 'rucola', 'garlic',
                'pineapple', 'meatballs', 'mushrooms']
    pizza_kind = random.choice(pizzas)
    extra_topping = random.choice(toppings)
    return f'a {pizza_kind} pizza with extra {extra_topping}' if random.randint(0, 3) == 3 else f'a {pizza_kind} pizza'


print('''
▄▄▄█████▓ ██░ ██ ▓█████     ██▓███   ██▓▒███████▒▒███████▒ ▄▄▄           ▄████  ▄▄▄       ███▄ ▄███▓▓█████ 
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▓██░  ██▒▓██▒▒ ▒ ▒ ▄▀░▒ ▒ ▒ ▄▀░▒████▄        ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ 
▒ ▓██░ ▒░▒██▀▀██░▒███      ▓██░ ██▓▒▒██▒░ ▒ ▄▀▒░ ░ ▒ ▄▀▒░ ▒██  ▀█▄     ▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██▄█▓▒ ▒░██░  ▄▀▒   ░  ▄▀▒   ░░██▄▄▄▄██    ░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄ 
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██▒ ░  ░░██░▒███████▒▒███████▒ ▓█   ▓██▒   ░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ▒▓▒░ ░  ░░▓  ░▒▒ ▓░▒░▒░▒▒ ▓░▒░▒ ▒▒   ▓▒█░    ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░
    ░     ▒ ░▒░ ░ ░ ░  ░   ░▒ ░      ▒ ░░░▒ ▒ ░ ▒░░▒ ▒ ░ ▒  ▒   ▒▒ ░     ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░
  ░       ░  ░░ ░   ░      ░░        ▒ ░░ ░ ░ ░ ░░ ░ ░ ░ ░  ░   ▒      ░ ░   ░   ░   ▒   ░      ░      ░   
          ░  ░  ░   ░  ░             ░    ░ ░      ░ ░          ░  ░         ░       ░  ░       ░      ░  ░
''')

player_name = input("What's your name? ")
print(f'Hi, {player_name}. In this game, you take orders and tell a delivery guy where to deliver them.')
print('''
|Map of the city of Hyattsville|
 -----1-----2-----3-----4-----
 -                           -
 -                           -
 -                           -
 -                           -
 4    M     N     O     P    4
 -                           -
 -                           -
 -                           -
 -                           -
 3    I     J     K     L    3
 -                           -
 -                           -
 -                           -
 -                           -
 2    E     F     G     H    2
 -                           -
 -                           -
 -                           -
 -                           -
 1    A     B     C     D    1
 -                           -
 -                           -
 -                           -
 -                           -
 ------1-----2-----3-----4----

The above is a map of the homes where you need to send pizzas to.
I recommend you take a picture of it since you'll have to scroll a lot otherwise.
The letters are the first letters of their names.
Your job is to give a truck driver the location (the coordinates) of the home ordering the pizza.''')
introduction_check = input('Do you want an introduction? (recommended for first-time players) ').lower()
if introduction_check == 'yes':
    print(f'''
Somebody will ask for a pizza to be delivered. Then a delivery boy will ask you for the location.
Example: Hello {player_name}'s Pizza. This is Jason. I'd like a pizza.
Driver to {player_name}. where does Jason live? Your answer would be '2,3'
(The first coordinate is horizontal, the second one vertical)
You can quit the game by typing 'quit' when asked about the coordinates.
A bit sad, but I'm sure they'll find someone else to yell the coordinates for you.
    ''')
elif introduction_check == 'no':
    print("You don't need any more explanations!")
else:
    print('Huh?')

print('''
Good luck delivering those pizzas!
''')

caller_coordinates = {
    'Matt': '1,4', 'Nolan': '2,4', 'Oliver': '3,4', 'Paul': '4,4',
    'Isabelle': '1,3', 'Jason': '2,3', 'Kevin': '3,3', 'Lauren': '4,3',
    'Elizabeth': '1,2', 'Felix': '2,2', 'Gregory': '3,2', 'Henry': '4,2',
    'Aaron': '1,1', 'Barbara': '2,1', 'Connor': '3,1', 'David': '4,1'
}

failed_deliveries = 0

while True:
    pizza_got_cold = False
    current_caller = random.choice(list(caller_coordinates.keys()))
    print(f'*ring* *ring* Hello, {player_name}\'s Pizza. This is {current_caller}. I\'d like {the_pizza_function()}.')
    input_coords = input(f'Driver to {player_name}. Where does {current_caller} live? ')
# this version can't handle the player inputting invalid coordinates
    if input_coords.lower() == 'quit':
        break
    elif caller_coordinates.get(current_caller) == input_coords:
        print(f'*ring* *ring* Hello {player_name}, this is {current_caller}. Thanks for the pizza!')
    else:
        pizza_cold_timer = 0
        while True:
            if caller_coordinates.get(current_caller) == input_coords:
                print(f'*ring* *ring* Hello {player_name}, this is {current_caller}. Thanks for the pizza!')
                break
            else:
                print(f'*ring* *ring* Hello {player_name}, this is {list(caller_coordinates.keys())[list(caller_coordinates.values()).index(input_coords)]}. I did not order a pizza. I live at {input_coords}.')
                input_coords = input(f'Driver to {player_name}. Where does {current_caller} live? ')
                pizza_cold_timer += 1
                if pizza_cold_timer == 3:
                    pizza_got_cold = True
                    break

    if pizza_got_cold:
        print(f'Driver to {player_name}. Unfortunately, the pizza got cold. The delivery failed.')
        failed_deliveries += 1
        print(f'Failed deliveries: {failed_deliveries}')
        if failed_deliveries == 3:
            break

if failed_deliveries == 3:
    input('Unfortunately, you failed to deliver too many pizzas. You will be... promoted to customer.')
else:
    input(f'Bye, {player_name}!')
