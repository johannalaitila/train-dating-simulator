# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define vr = Character("VR-Senpai", color="#62B92B")


# The game starts here.

label start:

    #play music "audio/trainbgmusic.mp3"
    
    # Nää tulee mustalle taustalle jos ei näytä backgroundia
    "You are now on a train"
    "Go talk to people"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # Täs on tekstiä taustakuvan päällä
    "You see a person"
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show vr happy

    # These display lines of dialogue.

    vr "Hello I am a train"

    vr "Do you want to travel with VR?"

    menu:
        "Yes":
            jump vr_yes
        "No":
            jump vr_no

label vr_yes:
    vr "Good choice"
    jump vr_end

label vr_no:
    vr "Bad choice"
    jump vr_end

label vr_end:
    vr "uwu owo"

    # This ends the game.
    return
