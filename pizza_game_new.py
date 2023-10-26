import random


def main():
    player_name = input('What is your first name? ')
    print(f'Hi, {player_name}. In this game, you take orders, and then tell a delivery guy where to deliver them.')
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
Your job is to give a truck driver the location (the coordinates) of the home ordering the pizza.
       ''')
    introduction_check = input('Do you need an introduction? (recommended for a first-time player) ').lower()
    if introduction_check == 'yes':
        print('''
Somebody will ask for a pizza to be delivered. Then a delivery boy will ask you for the location.

Example: Hello {player_name}'s Pizza. This is Jason. I'd like a pizza.
Driver to {player_name}. where does Jason live? Your answer would be '2,3'
(The first coordinate is horizontal, the second one vertical)

You can quit the game by typing 'quit' when asked about the coordinates.
A bit sad, but I'm sure they'll find someone else to yell the coordinates for you.
''')
    elif introduction_check == 'no':
        print("Let's get started then.")
    else:
        print('huh?')
    print('''Good luck delivering those pizzas!
''')
    deliver_pizza(player_name)


def deliver_pizza(player_name):
    global game_over
    global pizza_got_cold
    global caller_coordinates
    caller_names = ('Matt', 'Nolan', 'Oliver', 'Paul', 'Isabelle', 'Jason', 'Kevin', 'Lauren', 'Elizabeth', 'Felix',
                    'Gregory', 'Henry', 'Aaron', 'Barbara', 'Connor', 'David')
    failed_deliveries = 0
    consecutive_deliveries = 0
    while True:
        current_caller = random.choice(caller_names)
        print(f"*ring* *ring* Hello, {player_name}'s Pizza. This is {current_caller}. I'd like {the_pizza_function()}.")
        input_coords = get_delivery_coordinates(player_name, current_caller)
        if input_coords.lower() == 'quit':
            break
        if caller_coordinates.get(current_caller) == input_coords:
            input(f'''*ring* *ring* Hello {player_name}, this is {current_caller}. Thanks for the pizza!
''')
            consecutive_deliveries += 1
        if pizza_got_cold:
            failed_deliveries += 1
            consecutive_deliveries = 0
            print(f"Driver to {player_name}. Unfortunately the pizza got cold. I'll have to tell the customer the delivery failed.")
            input(f'Failed deliveries: {failed_deliveries}')
            if failed_deliveries >= 3:
                game_over = True
                break
    end_game(player_name, consecutive_deliveries)


def the_pizza_function():
    pizzas = ['Salami', 'Margherita', 'Diavola', 'Hawaiian', 'Buffalo', 'Pepperoni', 'BBQ', 'Neapolitan', 'Meat']
    toppings = ['salami', 'cheese', 'onions', 'anchovies', 'olives', 'pepperoni', 'BBQ sauce', 'rucola', 'garlic',
                'pineapple', 'meatballs', 'mushrooms']
    pizza_kind = random.choice(pizzas)
    extra_topping = random.choice(toppings)
    if random.randint(0, 3) == 3:
        return f'a {pizza_kind} pizza with extra {extra_topping}'
    else:
        return f'a {pizza_kind} pizza'


def get_delivery_coordinates(player_name, current_caller):
    global pizza_got_cold
    global caller_coordinates
    failed_deliveries= 0
    while True:
        input_coords = input(f'Driver to {player_name}. Where does {current_caller} live? ')
        if input_coords.lower() == 'quit':
            break
        elif caller_coordinates.get(current_caller) == input_coords:
            break
        else:
            if get_caller_by_coordinates(caller_coordinates, input_coords) is None:
                # add easter egg here
                print('coordinates not valid')
            else:
                print(f"*ring* *ring* Hello {player_name}, this is {get_caller_by_coordinates(caller_coordinates, input_coords)}. I did not order a pizza. I live at {input_coords}.")
            failed_deliveries += 1
            if failed_deliveries >= 3:
                pizza_got_cold = True
                break
    return input_coords


# this function was written by ChatGPT
def get_caller_by_coordinates(caller_coordinates_for_function, input_coords):
    return next((name for name, coords in caller_coordinates_for_function.items() if coords == input_coords), None)


def end_game(player_name, consecutive_deliveries):
    global game_over
    with open('High_Score.txt') as f:
        try:
            high_score = int(f.read())
        except ValueError:
            high_score = 0
    if consecutive_deliveries > high_score:
        with open('High_Score.txt', 'w') as f:
            f.write(str(consecutive_deliveries))
        print(f'New High Score!: {consecutive_deliveries}')
    if game_over:
        input('Unfortunately you failed to deliver too many pizzas. You will be... promoted to a customer. ')
    input(f'Bye, {player_name}!')


caller_coordinates = {
    'Matt': '1,4',
    'Nolan': '2,4',
    'Oliver': '3,4',
    'Paul': '4,4',
    'Isabelle': '1,3',
    'Jason': '2,3',
    'Kevin': '3,3',
    'Lauren': '4,3',
    'Elizabeth': '1,2',
    'Felix': '2,2',
    'Gregory': '3,2',
    'Henry': '4,2',
    'Aaron': '1,1',
    'Barbara': '2,1',
    'Connor': '3,1',
    'David': '4,1'
}
failed_deliveries = 0
pizza_got_cold = False
game_over = False
if __name__ == "__main__":
    main()
