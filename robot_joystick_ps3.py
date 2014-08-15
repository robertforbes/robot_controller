import pygame
import robot_udp
    
pygame.init()

# Clock for polling loop
clock = pygame.time.Clock()

# Initialise the joysticks
pygame.joystick.init()

# Find the number of joysticks.
joystick_count = pygame.joystick.get_count()
print "joysticks = ", joystick_count

if joystick_count > 0:
    js = pygame.joystick.Joystick(0)
    js.init()

    axes = js.get_numaxes()
    print "axes = ", axes
    
    buttons = js.get_numbuttons()
    print "buttons = ", buttons
    
    # flag to signal completion
    complete = False

    # Main game loop
    while complete == False:
        
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button down.")
                button_state = [js.get_button(x) for x in range(buttons)]
                print button_state
                
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button up.")
        
        axis_vals = [js.get_axis(x) for x in range(4)]
        # print axis_vals
        # Axis 0 = L/R on left analog control (L = -1.0, R =  1.0)
        # Axis 1 = U/D on left analog control (D =  1.0, U = -1.0)
        # Axis 2 = L/R on right analog control
        # Axis 3 = U/D on right analog control 

        print axis_vals[0], axis_vals[3] 
        left_right = 127 + round(axis_vals[0] * 127)
        speed = 127 + round(-axis_vals[3] * 127)
        print left_right, speed
        robot_udp.udp_test(int(speed), int(left_right))
        """ 
        if axes >= 2:
            axis_0 = js.get_axis(0)
            axis_1 = js.get_axis(1)
            print axis_0, axis_1       
        """
        # Limit the frame rate to 50Hz.
        # clock.tick(20)
else:
    print "No joysticks found."

# Quit on exit.    
pygame.quit ()
