# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define vr = Character("VR-Senpai", color="#62B92B")
define cat = Character("the cat", color="#000000")
define player = Character("you")
define anc = Character("an announcement")


# The game starts here.

label start:

    #play music "audio/trainbgmusic.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg railwaystation
    "You are in Helsinki railway station. You have just attended Helsinki Pride and now are returning to your home in Kouvola."
    "You can choose whether you want to take a seat in the single’s carriage, the pet carriage or economy class carriage."
    
    "Which carriage will you want to sit in?"
    menu:
        "the single’s carriage.":
            jump singleCar
        "the pet carriage":
            jump petCar
        "the economy class":
            jump economyCar
    
label economyCar:

    #scene bg train
    "You step into the economy class."
    "There is no one in the carriage but an old man who is snoring very loudly. You have forgotten your headphones at the Pride event and have to suffer the snoring for hours as a punishment."
    jump arrivalAtStation

label petCar:

    #scene bg train
    "You step into the pet carriage."
    #show cat 
    "You see an aristocratic looking cat sitting on their own seat."

    "Do you want to talk to it?"
    menu:
        "yes":
            jump talkCat
        "no":
            "You couldn’t be bothered to talk to the cat."
            jump arrivalAtStation


label talkCat:

    "You decide to have a conversation with the cat."
    cat "Meow."
    player "M-meow"
    cat "Meow?"
    player "Meow!"
    cat "Meow."
    "You remember you have some leftover snacs from the Pride event in you bag."
    
    "Offer a piece of your delicious Finnish home-grown cucumber to the cat?"
    menu:
        "yes":
            jump cucumberCat
        "no":
            jump staringCat

label staringCat:

    cat "*Stares at you*"

    "The cat looks at your cucumber with hungry eyes. Do you want to offer a piece to it?"
    menu:
        "offer the cucumber":
            jump cucumberCat
        "eat it yourself":
            cat "*Hisses at you*"
            jump arrivalAtStation

label cucumberCat:

    cat "*Eats the cucumber and purrs loudly.*"
    "You pet the cat who seems to enjoy your company very much. The cat thinks you’re a purrfect friend"
    jump arrivalAtStation


label singleCar:

    #scene bg train
    "You see a dashing blonde Finnish woman. She looks friendly, but a bit shy."
    
    "Do you want to sit in front of her?"
    menu:
        "yes":
            jump talkVR
        "no":
            jump noVR

label noVR:
    
    "You decide not to talk to the blonde woman."
    "In a few seats away, you notice a red-haired, joyful person glowing with untypical, even magical energy rarely. She smiles at you invitingly and moves her bagpipes offering you a seat next to her."

    "Do you want to sit next to her?"
    menu: 
        "yes":
            jump talkSR
        "no":
            "You take a seat in the corner of the carriage, spending the journey alone looking out of the window."
            "You forgot your headphones at the Pride event so you cannot even listen to the latest episode of your favourite True Crime podcast."
            jump arrivalAtStation


label talkVR:

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
    hide vr
    jump vr_end

label vr_end:
    vr "uwu owo"

    # This ends the game.
    return

label talkSR:

    "jtn"

label arrivalAtStation:

    anc "Seuraavaksi Kouvola. Nästä Kouvola. The next stop, Kouvola. Taajamajuna Joensuuhun lähtee raiteelta kuusi… kuusi… kuusi"
    "You have arrived at your destination. You step out of the train into the station."
    return

