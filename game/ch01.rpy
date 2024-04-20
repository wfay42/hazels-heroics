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
    scene bg cave outside
    "We join our heroines as they work to hunt down a mischievous cave-dwelling slimegirl."

    scene bg cave ground side
    show sg ground
    "The slime girl is diligently creating eggs to convert new slime girls."

    scene bg cave upper
    "But where are our intrepid heroines?"

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
    "Without much effort (or at least enthusiasm), Eriko conjures flames on each of the three slime prisons. After quickly melting away, our heroines begin to drop meet their foe below."

    scene bg cave ceiling
    show e upside falling
    "Of course, they did not think they would need to confront their enemy while still upside down."

    scene bg cave ground
    show e upside egg
    "Unable to right themselves quickly, our three heroines fall directly into the slime eggs waiting for them."

    scene bg cave ground
    show eggsback
    show eggsfront
    "The skin of the eggs seals up almost instantly, completely trapping our heroines inside."

    window hide
    show eggsfront transp
    show e upside egg sit behind eggsfront
    with d2
    pause
    window show
    "The slime is both caustic to their clothing, but soothing to their bodies. Floating in the sac of slime, they are lulled into a dreamless sleep; unable to struggle against their impending transformation."

    window hide
    show e upside egg slime behind eggsfront
    with d2
    pause
    window show
    "In a matter of minutes, the slime transformation is complete. Our heroines sit, resting their beautiful slime bodies as the membrane on their eggs begins to thin."

    scene bg cave floor slimes
    show e upside slimes
    "Eriko, Hazel, and Maika emerge from their eggs with an expression of dull joy. Their bodies are titillated by the dramatic transformation they have just gone through."

    scene bg cave floor slimes 02
    show e upside slimes 02
    "Without hesitation they being to pleasure themselves, enjoying every second of the experience. The slime girl who helped them come to experience this joins her new progeny."

    show e upside slimes 03
    "It only takes a few moments more before they all begin to pair off to find the limits of their new bodies. Of course, they can only have so much fun until the next set of adventurers arrives."

    camera:
        matrixcolor SaturationMatrix(0)
    "Slime Party End"
    camera

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
    "Although it only lasts a few moments, her divine strength should be enough for her to tear the slime girl apart."

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

    camera:
        matrixcolor SaturationMatrix(0)
    "Slime Maika End"
    camera
    jump ch01_start_menu
