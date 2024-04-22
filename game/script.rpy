# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define h = Character("Hazel")
define m = Character("Maika", who_color="#cccc00")
define e = Character("Eriko", who_color="#00aaee")
define sg = Character("Slime Girl", who_color="#cc0000")

# A smooth dissolve over 2 seconds
define d2 = Dissolve(2)

# Custom transformations for positioning
transform tl:
    xpos -0.3
transform tr:
    xpos 0.3

# The game starts here.

label start:

    jump chapter01_start
    # This ends the game.

    return
