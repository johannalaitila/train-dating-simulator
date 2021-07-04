# The script of the game goes in this file.

# GUI and game properties
define gui.choice_button_text_idle_color = '#000000'
define config.name = "Train Dating Simulator"
define gui.about = _("Pride Game Jam 2021 project by Johanna Laitila, Kaisa Rautiainen & Lukki Virtanen.\nPhoto credit: {a=https://fi.wikipedia.org/wiki/Kouvolan_rautatieasema#/media/Tiedosto:Kouvolan_matkakeskus.JPG}Otto Karikoski{/a}.\nSounds by {a=https://freesound.org/people/alexkandrell/sounds/277755/}alexkandrell{/a}, {a=https://freesound.org/people/SubUnit_FieldRec/sounds/155042/}SubUnit_FieldRec{/a}, {a=https://freesound.org/people/Thomas_Marcum/sounds/447943/}Thomas_Marcum{/a} and {a=https://freesound.org/people/InspectorJ/sounds/332015/}InspectorJ{/a}.")
define gui.text_color = '#000000'
define gui.accent_color = '#000000' #Main menu title etc

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define vr = Character("Blonde Woman", color="#62B92B")
define vrFullName = Character("Valpuri Rautatie", color="#62B92B")
define scotrail = Character("Tréana MacTravel", color="#62B92B")
define cat = Character("Cat", color="#000000")
define player = Character("You")
define anc = Character("Announcement")

define lemmikkivaunu = False
define sinkkuvaunu = False
define talkedToVR = False
define talkedToScotRail = False
define talkedToCat = False
define gaveCucumber = False
define studentCardShown = False
define askedAboutScotland = False

# The game starts here.

label start:

    play music "audio/station_ambience.wav"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg helsinki
    "You are in Helsinki railway station. You have just attended Helsinki Pride and now are returning to your home in Kouvola."
    scene bg traincarriage
    "You can choose whether you want to take a seat in the single’s carriage, the pet carriage or economy class carriage."
    
    "Which carriage will you want to sit in?"
    menu:
        "the single’s carriage.":
            $ sinkkuvaunu = True
            jump singleCar
        "the pet carriage":
            $ lemmikkivaunu = True
            jump petCar
        "the economy class":
            jump economyCar
    
label economyCar:

    scene bg traininside
    play music "audio/basic_ambience.mp3"
    "You step into the train into the economy class."
    "There is no one in the carriage but an old man who is snoring very loudly. You have forgotten your headphones at the Pride event and have to suffer the snoring for hours as a punishment."
    jump arrivalAtStation

label petCar:

    scene bg traininside
    play music "audio/basic_ambience.mp3"
    "You step into the train into the pet carriage."
    show kissa at center with fade:
                    zoom 0.5
    "You see an aristocratic looking cat sitting on their own seat."

    "Do you want to talk to it?"
    menu:
        "yes":
            jump talkCat
        "no":
            "You couldn’t be bothered to talk to the cat."
            hide kissa
            jump arrivalAtStation


label talkCat:

    $ talkedToCat = True
    "You decide to have a conversation with the cat."
    cat "Meow."
    player "M-meow"
    cat "Meow?"
    player "Meow!"
    cat "Meow."
    "You remember you have some leftover snacks from the Pride event in you bag."
    
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
            hide kissa
            jump arrivalAtStation

label cucumberCat:
    $ gaveCucumber = True
    play sound "audio/cucumber.wav"
    cat "*Eats the cucumber and purrs loudly.*"
    "You pet the cat who seems to enjoy your company very much. The cat thinks you’re a purrfect friend"
    hide kissa
    jump arrivalAtStation


label singleCar:

    scene bg traininside
    play music "audio/basic_ambience.mp3"
    "You step into the train into the single's carriage."
    show vr happy with fade:
        xoffset 300
        yoffset -20
    "You see a dashing blonde Finnish woman. She looks friendly, but a bit shy."
    
    "Do you want to sit in front of her?"
    menu:
        "yes":
            jump talkVR
        "no":
            jump noVR

label noVR:
    
    "You decide not to talk to the blonde woman."
    hide vr
    show bg traininside2
    show scot at center with fade:
        zoom 0.9
        yoffset 550
    "In a few seats away, you notice a red-haired, joyful person glowing with untypical, even magical energy rarely. She smiles at you invitingly and moves her bagpipes offering you a seat next to her."

    "Do you want to sit next to her?"
    menu: 
        "yes":
            jump talkSR
        "no":
            hide scot with fade
            "You decide not to talk to the red-haired woman either, preferring to take a seat in the corner of the carriage, spending the journey alone looking out of the window."
            "You forgot your headphones at the Pride event so you cannot even listen to the latest episode of your favourite True Crime podcast."
            jump arrivalAtStation


label talkVR:

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    $ talkedToVR = True

    "You sit in front of her, exchanging an awkward smile. You notice she is still a bit out of breath."
    "As you notice she is also wearing a bracelet given at the Pride event you just attended, you decide to strike a conversation, breaking the Finnish rules of not talking to strangers."
    "She looks a bit surprised as you open your mouth, showing her your own bracelet as well."
    
    player "I see you went to Pride as well. Did you have fun?"
    vr "Oh…  Yes, even though my friends couldn’t make it."
    vr "I was supposed to come here with Onni B. but he forgot he had booked a holiday with his family at Koli this weekend"

    "She notices there’s a student badge of the honoroble KRAO academy on your bag."
    vr "Your badge... Are you a student?"
    # show vr excited
    player "Yes, I am."
    vr "*smirk* Really? Can you prove it? Do you have a student card with you?"

    "Show your student card to the woman?"

    menu:
        "Yes":
            $ studentCardShown = True
            jump vr_yes
        "No":
            jump vr_no

label vr_yes:
    player "Here it is."
    "The woman inspects your student card."
    # show vr with hearts in eyes
    vr "You look cute in the picture."
    vrFullName "Allow me to introduce myself as well. My name is Valpuri Rautatie."
    "You have solved the mystery of the woman’s name."
    hide vr
    jump arrivalAtStation

label vr_no:
    vr "I actually lost mine at Pride…. Sorry about that."
    "She looks disappointed."
    vr "Oh well. I won’t tell you my name then."
    hide vr
    jump arrivalAtStation

label talkSR:

    "You sit next to the magical person."

    scotrail "Hello. My name is Tréana MacTravel."
    player "Hi Tréana. Nice to meet you."
    "She seems very likeable and you want to continue talking to her. What do you want to ask her?"
    menu:
        "Do you like music?":
            jump bagpipes
        "Where are you from?":
            jump scotland

label bagpipes:
    scotrail "Yes. Actually, I'm a musician."
    player "Oh. What instrument do you play then?"
    scotrail "The bagpipes."
    "Tréana begins to play the bagpipes."
    # play audio bagpipes
    "You keep listening Tréana and her bagpipes for the rest of the journey."
    jump arrivalAtStation
label scotland:
    $ askedAboutScotland = True
    scotrail "Aberdeen, Scotland."
    player "That's exciting. Have you ever seen the Loch Ness monster?"
    scotrail "Hahaha... Loch Ness is near Inverness. I have been there but haven't seen the monster."
    player "Hahaha."
    "You have an interesting conversation with her for the rest of the journey."
    jump arrivalAtStation

label arrivalAtStation:
    play music "audio/station_ambience.wav"
    scene bg kouvola
    anc "Seuraavaksi Kouvola. Nästä Kouvola. The next stop, Kouvola. Taajamajuna Joensuuhun lähtee raiteelta kuusi… kuusi… kuusi"
    "You have arrived at your destination. You step out of the train into the station."

    if sinkkuvaunu:
        if talkedToVR:
            show vr happy at center with fade:
                    zoom 0.4
                    yoffset -150
            if studentCardShown:
                # GOOD VR ENDING
                vrFullName "Do you want to grab a cup of coffee?"
                "You went to get a cup of coffee with Valpuri."
                hide vr
            else:
                # BAD VR ENDING
                player "Do you want to grab a cup of coffee?"
                vr "Sorry, maybe not. I still do not know if you are really a student."
                hide vr with fade
                "The woman walked away from you."
        elif askedAboutScotland:
            show scot at center with fade:
                zoom 0.9
                yoffset 550
            scotrail "Hey, I'm a bit hungry. Would you like to come to my place for some deep-fried mars bars?"
            player "I would love to."
            "You went to her place, fell in love and now plan to move to Scotland to travel in the great ScotRail train and to see the Loch Ness monster."
    elif lemmikkivaunu and talkedToCat:
        show kissa at center with fade:
                    zoom 0.5
        if gaveCucumber:
            "The cat you met at the carriage joins you and you walk together to the bus stop."
        else:
            "The cat you met at the carriage walks into their limousine and puts on their top hat and looks at you with a smug face."
