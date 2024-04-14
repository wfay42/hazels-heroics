# Characters and other variables are defined in script.rpy

define sg = Character("Slime Girl")

"""
Chapter 1
Introduce Hazel, Maika, and Eriko.
Start stuck to ceiling of slime girl's lair.
Option 1: Use Eriko's ice magic to freeze the slime
  This lets them break free and defeat the slime monster.
Option 2: Use Eriko's fire magic to melt the slime (doesn't work)
  This melts the slime and they fall
Option 3: Maika uses her strength to break free
  Breaks free, falls into slime pit, TFs, then TFs others.
"""
label chapter01_start:
    scene bg cave ground side
    show sg ground
    "We join our heroines as they work to hunt down a mischievous cave-dwelling slimegirl."

    scene bg cave upper
    "However, they seem to be a bit over their heads."

    show h upside normal
    h "Time to analyze the situation!"
    
    show e upside normal at tl
    e "Do we really need to do tha..."
    h "One: We are upside down. Two: We are suspended above the slime girl. Three: She is building slime eggs to turn us into slime girls."

    show m upside normal at tr
    m "Less analyzing, more busting out of here! Hazel, what's your big plan?"
    jump ch01_start_menu

label ch01_start_menu:
    scene bg cave upper
    show h upside normal
    show e upside normal at tl
    show m upside normal at tr

    menu:
        "Eriko's fire magic":
            jump ch01_fire

        "Eriko's ice magic":
            jump ch01_ice
        
        "Maika's holy strength":
            jump ch01_strength

label ch01_fire:
    h "Eriko, use your fire magic to melt the slime!"
    e "Alright, but don't blame me if your eyebrows get singed."

    "Without much effort, or at least enthusiasm, Eriko conjures flames on each of the three slime prisons. After quickly melting away, our heroines begin to drop to the nest below."

    jump ch01_start_menu

label ch01_ice:
    ""
    jump ch01_start_menu

label ch01_strength:
    h "Maika! Use your holy strength and break out!"
    m "Darn, I was hoping to save that for something more interesting. Oh well."
    
    scene bg cave upper
    show m upside divine

    m "Divine guardian, give me strength!"

    scene bg cave ceiling
    show m upside falling
    "Maika breaks free from her slime imprisonment, falling to the slime nest below to confront the slime girl."

    scene bg cave ground
    show m upside egg
    "At least that's what would have happened if she hadn't fallen right into the slime egg prepared for her."
    h "Maika!"
    
    scene bg cave ground side
    show m upside egg side
    "With the short burst of her holy strength already vanished, Maika struggles to escape from the egg."
    "She can feel it seeping into her pores, changing her."
    
    show m upside egg burst with d2
    "Before long, she emerges. Another slime girl, ready to assimilate. Maika's heart has crystalized and is now worn on her chest. The weak point for any slime girl."

    scene bg cave upper
    show m upside end 01
    "She and her new sister don't hesitate to grab Eriko and Hazel and show them the way."

    "Slime Maika End"
    jump ch01_start_menu
