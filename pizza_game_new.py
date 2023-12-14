#maybe implement system were you need to manage resources (ingedients for pizza, maybe even money)
import random


def intro():
    """introduces the player to game mechanics"""
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
Your job is to give a truck driver the location (the coordinates) of the home ordering the pizza.\n''')
    introduction_check = input('Do you need an introduction? (recommended for a first-time player) ').lower()
    if introduction_check == 'yes':
        print(f'''
Somebody will ask for a pizza to be delivered. Then a delivery guy will ask you for the location.

Example: Hello {player_name}'s Pizza. This is Jason. I'd like a pizza.
Driver to {player_name}. where does Jason live? Your answer would be '2,3'
(The first coordinate is horizontal, the second one vertical)

You can quit the game by typing 'quit' when asked about the coordinates.
A bit sad, but I'm sure they'll find someone else to yell the coordinates for you.\n''')
    elif introduction_check == 'no':
        print("Let's get started then.")
    else:
        print('huh?')
    print("Good luck delivering those pizzas!\n")
    deliver_pizza(player_name)


def deliver_pizza(player_name):
    """main game logic"""
    global game_over
    global pizza_got_cold
    global the_populus
    failed_deliveries = 0
    consecutive_deliveries = 0
    while True:
        current_caller = random.choice(list(the_populus))
        print(f"Customer speaking: Hello, {player_name}'s Pizza. This is {current_caller}. I'd like {the_pizza_function()}.")
        input_coords = handle_input(player_name, current_caller)
        if input_coords.lower() == 'quit':
            break
        if the_populus.get(current_caller) == input_coords:
            input(f"Customer speaking: Hello {player_name}, this is {current_caller}. Thanks for the pizza!\n")
            consecutive_deliveries += 1
        if pizza_got_cold:
            failed_deliveries += 1
            consecutive_deliveries = 0
            print(f"Driver to {player_name}. Unfortunately the pizza got cold. I'll have to tell the customer the delivery failed.\n")
            input(f'Failed deliveries: {failed_deliveries}')
            if failed_deliveries >= 3:
                game_over = True
                break
    end_game(player_name, consecutive_deliveries)


def the_pizza_function():
    """generates a random pizza"""
    pizzas = ['Salami', 'Margherita', 'Diavola', 'Hawaiian', 'Buffalo', 'Pepperoni', 'BBQ', 'Neapolitan', 'Meat',
              'Capricciosa', 'Quatro Formaggi', 'Calzone', 'BBQ Chicken', 'Mexican', 'Greek', ]
    toppings = ['salami', 'mozzarella', 'onions', 'caramelized onions','anchovies', 'olives', 'pepperoni', 'BBQ sauce',
                'arugula', 'garlic', 'pineapple', 'meatballs', 'mushrooms', 'bell peppers', 'artichokes', 'prosciutto',
                'sun-dried tomatoes', 'feta cheese', 'buffalo mozzarella', 'blue cheese', 'jalapenos', 'sausage',
                'bacon', 'corn', 'pine nuts', 'barbecue chicken']
    pizza_kind = random.choice(pizzas)
    extra_topping = random.choice(toppings)
    if random.randint(0, 3) == 3:
        return f'a {pizza_kind} pizza with extra {extra_topping}'
    else:
        return f'a {pizza_kind} pizza'


def handle_input(player_name, current_caller):
    """handles player input and gives 'error messages'"""
    global pizza_got_cold
    global the_populus
    failed_deliveries= 0
    while True:
        input_coords = input(f'Driver to {player_name}. Where does {current_caller} live? ')
        cant_find_statements = [
            f"Driver to {player_name}. Sorry man, I can't find that on the map.",
            f"Driver to {player_name}. Pretty sure that's outside this neighborhood.",
            f"Driver to {player_name}. Sorry I think the connection stuttered, could you repeat that?",
            f"Driver to {player_name}. I think you took a wrong turn. Where does the customer live again?",
            f'''
Driver to {player_name}. Pizza delivery requires precise and accurate coordinates.
What you just said was not that. Could you say that again?''',
            f'''
Driver to {player_name}.

The reason why humanity evolved language, the ability to speak, was, inherently,to be able to communicate information.
By being able to exchange information, humanity could cooperate more efficiently,
like being able to show a good place to collect berries, or warning others of dangerous animals nearby.
Eventually, concrete words and sentences were formed. Going from only being able to describe what was in the here and now,
to forming words for more and more abstract and complicated things.
People philosophised, contemplated life and existence, started to have complicated conversations.
In this sense, language only makes sense, and only really works, because we have agreed upon words that everyone (or at least most)
understand the meaning of. Because we can create very specific sets of sounds, that are immediately recognizable by whoever hears them.

That's why, what you just said violates the laws of language, really, it's and injustice to humanity and its achievements.
You can't just say "{input_coords}" and expect me to know what it means. You can't!
The... sounds you just uttered are utterly and completely meaningless, and when giving instructions to somebody,
one of the fundamental uses of language, it's important that the words you're saying have meaning!

So, I hereby urge you to please, just enter coordinates that i can follow easily, so we can both do our jobs.
'''
            f"Driver to {player_name}. I got lost there for a moment. What are the correct coordinates?",
            f"Driver to {player_name}. It seems we've hit a roadblock. Double-check the coordinates for me.",
            f"Driver to {player_name}. Sorry, what?",
        ]
        if input_coords.lower() == 'quit':
            break
        elif the_populus.get(current_caller) == input_coords:
            break
        else:
            failed_deliveries += 1
            if get_caller_by_coordinates(the_populus, input_coords) is None:
                if '42' in input_coords:
                    input('''
Customer speaking: 42 is the answer to life, the universe, and everything.
But it's not the answer to why there's someone at my door. I didn't order a pizza.\n''')
                elif random.randint(0, 100) == 1:
                    input('''
Customer speaking: You have reached Anton.
I am obliged by contract to put a 4th wall break in any game I make.
Also those coordinates you put in were not on the map. Try again.\n''')
                else:
                    input(random.choice(cant_find_statements))
                if failed_deliveries >= 3:
                    pizza_got_cold = True
                    break
            else:
                print(f"Customer speaking: Hello {player_name}, this is {get_caller_by_coordinates(the_populus, input_coords)}. I did not order a pizza. I live at {input_coords}.\n")
    return input_coords


# this function was written by ChatGPT
def get_caller_by_coordinates(caller_coordinates, input_coords):
    """self-explanatory"""
    try:
        return next((name for name, coords in caller_coordinates.items() if coords == input_coords), None)
    except ValueError:
        return None


def end_game(player_name, consecutive_deliveries):
    """checks for a new high score and ends game"""
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
        input('Unfortunately you failed to deliver too many pizzas. You will be... promoted to customer. ')
    input(f'Bye, {player_name}!')


the_populus = {
    'Aaron': '1,1',
    'Barbara': '2,1',
    'Connor': '3,1',
    'David': '4,1',
    'Emma': '1,2',
    'Felix': '2,2',
    'Gregory': '3,2',
    'Henry': '4,2',
    'Isabelle': '1,3',
    'Jason': '2,3',
    'Kevin': '3,3',
    'Lauren': '4,3',
    'Matt': '1,4',
    'Nolan': '2,4',
    'Oliver': '3,4',
    'Paul': '4,4'
}
failed_deliveries = 0
pizza_got_cold = False
game_over = False
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
player_name = input('What is your first name? ')
if __name__ == "__main__":
    intro()
