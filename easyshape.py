import turtle

#Defining the line function
def line(x1, y1, x2, y2):
    turtle.clear() #Clear the turtle screen
    turtle.penup() # Raise the pen
    turtle.goto(x1, y1) # Move to the starting point
    turtle.pencolor(colour) # Set the pen color
    turtle.pensize(thickness) #Set the pen thickness
    turtle.pendown() # Lower the pen
    turtle.goto(x2, y2) # Draw a line
    #Assigning the values of the current x and y coordinates to the
    #global x and y coordinates
    global current_x,current_y
    current_x=turtle.xcor()
    current_y=turtle.ycor()

#Defining the arc function    
def arc(radius, angle):
    global current_x,current_y
    turtle.clear() #Clear the turtle screen
    turtle.penup() # Raise the pen
    turtle.goto(current_x, current_y - radius) # Position the turtle
    turtle.pencolor(colour) # Set the pen color
    turtle.pensize(thickness) #Set the pen thickness
    turtle.pendown() # Lower the pen
    turtle.circle(radius,angle) # Draw an arc with the given radius and angle
    #Assigning the values of the current turtle x and y coordinates to the
    #global x and y coordinates
    current_x=turtle.xcor()
    current_y=turtle.ycor()

#Defining the text function    
def text(content, size, x3, y3):
    turtle.clear()
    turtle.goto(x3,y3)
    turtle.pencolor(colour) # Set the pen color
    style = ('Courier', size, 'normal')
    turtle.write(content, font=style, align='center')
    #Assigning the values of the current turtle x and y coordinates to the
    #global x and y coordinates
    global current_x,current_y
    current_x=turtle.xcor()
    current_y=turtle.ycor()

#Defining the settings function    
def settings(set_colour, set_thickness):
    #Assigning the values of set_colour and set_thickness
    #(default or inputted by user) to the corresponding global values
    global colour,thickness
    colour=set_colour
    thickness=set_thickness

# Global variable declaration    
global colour, thickness, current_x, current_y
thickness=0.5
colour=str('red')
current_x=float(0)
current_y=float(0)

