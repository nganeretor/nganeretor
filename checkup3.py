import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Traffic Light Simulation")
screen.bgcolor("white")
screen.setup(width=200, height=400)

# Create the red light
red_light = turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0, 100)

# Create the yellow light
yellow_light = turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0, 0)

# Create the green light
green_light = turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0, -100)

# Define the states and transitions
states = ['Red', 'Red-Yellow', 'Green', 'Yellow']
transitions = [
    {'trigger': 'change', 'source': 'Red', 'dest': 'Red-Yellow', 'duration': 0},
    {'trigger': 'change', 'source': 'Red-Yellow', 'dest': 'Green', 'duration': 30},
    {'trigger': 'change', 'source': 'Green', 'dest': 'Yellow', 'duration': 10},
    {'trigger': 'change', 'source': 'Yellow', 'dest': 'Red', 'duration': 30}
]
state = 'Red'

# Define the function for transitioning between states
def change_state():
    global state
    for transition in transitions:
        if transition['source'] == state:
            state = transition['dest']
            if state == 'Red':
                red_light.color("red")
                yellow_light.color("grey")
                green_light.color("grey")
            elif state == 'Red-Yellow':
                red_light.color("red")
                yellow_light.color("yellow")
                green_light.color("grey")
            elif state == 'Green':
                red_light.color("grey")
                yellow_light.color("grey")
                green_light.color("green")
            elif state == 'Yellow':
                red_light.color("grey")
                yellow_light.color("yellow")
                green_light.color("grey")
            screen.update()
            time.sleep(transition['duration'])

# Simulate the traffic light changes based on the FSM
while True:
    change_state()