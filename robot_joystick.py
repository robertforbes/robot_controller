import pygame
    
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
                button_state = [js. get_button(x) for x in range(buttons)]
                print button_state
                
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button up.")
        """
        if axes >= 2:
            axis_0 = js.get_axis(0)
            axis_1 = js.get_axis(1)
            print axis_0, axis_1       
        """
        # Limit the frame rate to 50Hz.
        clock.tick(20)
else:
    print "No joysticks found."

# Quit on exit.    
pygame.quit ()
