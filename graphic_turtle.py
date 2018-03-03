import turtle

def draw_square():

    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.speed(200)
    brad.shape('turtle')
    
    x=0
    while x < 200 :
      i=0 	
      while i < 4:
         brad.forward(100)
         brad.right(90)
         i+=1
      brad.right(20)
      x+=1
    window.exitonclick()
    
draw_square()