#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

apple = trtl.Turtle()
drawer = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_an_A():
  drawer.hideturtle()
  drawer.penup()
  drawer.goto(18, 40)
  drawer.color("white")
  drawer.write("A", font=("Arial", 55, "bold"))

def draw_apple(active_apple):
  draw_an_A()
  active_apple.shape(apple_image)
  wn.update()

def apple_fall():
  apple.penup()
  apple.goto(apple.xcor(), -150)
  apple.hideturtle()
  drawer.clear()

#-----function calls-----
draw_apple(apple)
wn.bgpic("background.gif")
wn.onkeypress(apple_fall, "a")
wn.listen()
wn.mainloop()
