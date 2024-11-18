import turtle as trtl
import random as rand

# ----- Setup -----
apple_image = "pear.gif"  # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)  # Make the screen aware of the new file

drawer = trtl.Turtle()
drawer.hideturtle()  # Hide the drawer turtle

# List of all available letters
all_letters = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
letters = rand.sample(all_letters, 5)  # Randomly choose 5 letters from the list
used_letters = []  # To track which letters have been used
current = None
apples = []
apple_positions = [(0, 150), (-100, 150), (100, 150), (-200, 150), (200, 150)]  # Positions for apples

# ----- Functions -----
# Given a turtle, set that turtle to be shaped by the image file
def draw_letter(letter, x, y):
    drawer.penup()
    drawer.goto(x, y)
    drawer.color("white")
    drawer.write(letter, font=("Arial", 18, "bold"))

# Create apples at the top of the screen
def create_apples():
    global apples
    for i in range(len(letters)):
        apple_instance = trtl.Turtle()
        apple_instance.shape(apple_image)
        apple_instance.penup()
        apple_instance.goto(apple_positions[i])
        apple_instance.letter = letters[i]  # Assign the corresponding letter to the apple
        apples.append(apple_instance)
        draw_letter(letters[i], apple_positions[i][0], apple_positions[i][1] + 20)  # Draw the letter above each apple

# Move the apple corresponding to the key pressed
def apple_fall(selected_apple):
    selected_apple.goto(selected_apple.xcor(), -150)
    selected_apple.goto(selected_apple.xcor(), 80)

# Handle key presses and manage falling apples
def key_press(key):
    global apples, used_letters
    # Check if the letter has already been used
    if key not in used_letters:
        used_letters.append(key)
        # Find the apple with the matching letter
        for apple_instance in apples:
            if apple_instance.letter == key:
                apple_fall(apple_instance)
                apples.remove(apple_instance)  # Remove the apple from the list after it falls
                break

    # If all letters have been used, stop the game and display a message
    if len(used_letters) == len(letters):
        drawer.clear()
        drawer.penup()
        drawer.goto(0, 0)
        drawer.color("white")
        drawer.write("Game Over! All letters have been used.", align="center", font=("Arial", 24, "bold"))

# ----- Function Calls -----
create_apples()  # Create the apples and display letters at the top
wn.listen()

# Map the key press events to the corresponding letter
for key in letters:
    wn.onkeypress(lambda key=key: key_press(key), key)

wn.bgpic("background.gif")  # Background image
wn.mainloop()
