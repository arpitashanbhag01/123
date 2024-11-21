import turtle as trtl
import random as rand


apple_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)

drawer = trtl.Turtle()
drawer.hideturtle()

all_letters = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
letters = rand.sample(all_letters, 5) 
used_letters = [] 
current = None
apples = []
apple_positions = [(0, 150), (-100, 150), (100, 150), (-200, 150), (200, 150)]

def draw_letter(letter, x, y):
    drawer.penup()
    drawer.goto(x, y)
    drawer.color("white")
    drawer.write(letter, font=("Arial", 18, "bold"))

def create_apples():
    global apples
    for i in range(len(letters)):
        apple_instance = trtl.Turtle()
        apple_instance.shape(apple_image)
        apple_instance.penup()
        apple_instance.goto(apple_positions[i])
        apple_instance.letter = letters[i]
        apples.append(apple_instance)
        draw_letter(letters[i], apple_positions[i][0], apple_positions[i][1] + 20)

def apple_fall(selected_apple):
    selected_apple.goto(selected_apple.xcor(), -150)
    selected_apple.goto(selected_apple.xcor(), 80)

def key_press(key):
    global apples, used_letters
    if key not in used_letters:
        used_letters.append(key)
        for apple_instance in apples:
            if apple_instance.letter == key:
                apple_fall(apple_instance)
                apples.remove(apple_instance)
                break

    if len(used_letters) == len(letters):
        drawer.clear()

create_apples()
wn.listen()
for key in letters:
    wn.onkeypress(lambda key=key: key_press(key), key)

wn.bgpic("background.gif")  
wn.mainloop()
