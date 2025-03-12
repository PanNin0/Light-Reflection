# Config

class config:

    # -----------------------------

    # Important settings for the logic of the program
    
    # -----------------------------

    # This determines how frequently the program will update, this shouldn't effect how fast the simulation moves unless
    # the fps is exceeding too high of numbers.
    fps = 60 # Default is 60.
    
    # How fast the rays will move, slow this down if you want to better observe the movement of the rays
    velocity = 100 # Default is 100

    # The radius of the circle in the center of the screen, the larger this number is the more precise the reflections
    # of the rays will be due to weird math stuff.
    radius = 50 # Default is 50

    # How large of an arc the rays can spawn at. This should be changed if you only want the rays to come from certain
    # directions. This variable will not do anything different once it exceeds 360.
    spawningArc = 360 # Default is 360
    
    # Rotates the spawning location by x amount, this is seperate to spawningArc and will add a constant number to the
    # spawning angle.
    spawnRotation = 0 # Default is 0

    # How many rays the program will spawn before ending.
    rays = 5 # Default is 5.

    # How frequently the program will spawn a new ray.
    spawnSpeed = 20 # Default is 20

    # -----------------------------

    # Visual settings (these are not important)

    # -----------------------------

    # How thick the lines drawn by the program will be, this effects the circle and rays.
    lineThickness = 1 # Default is 1

    # The color of the lines drawn by the program, this effects the circle and the rays.
    lineColor = 'black' # Default is 'black'