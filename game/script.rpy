# Holy moly, that's a lot of characters.
define k = Character(_("King Ted"), color="#655b00")
define c = Character(_("Minion (Cat)"), color="#4f5869")
define p = Character(_("Minion (Panda)"), color="#4f5869")
define s = Character(_("Minion (Sloth)"), color="#4f5869")
define d = Character(_("Minion (Dinosaur)"), color="#4f5869")
define q = Character(_("Prisoner"), color="#006c07")
define m = Character(_("Masato"), color="#966d1a")
define r = Character(_("Raviolo"), color="#a00")
define e = Character(_("Elf"), color="#9008")
define v = Character(_("Voice"), color="#000b")
define x = Character(_("Stella"), color="#736036")
define y = Character(_("Yukina"), color="#620078")
define t = Character(_("Teacher"), color="#3a3a3ab9")
define a = Character(_("Class"), color="#3a3a3ab9")
define b = Character(_("Student 1"), color="#3a3a3ab9")
define f = Character(_("Student 2"), color="#3a3a3ab9")
define g = Character(_("Student 3"), color="#3a3a3ab9")
define h = Character(_("Student 4"), color="#3a3a3ab9")
define i = Character(_("Student 5"), color="#3a3a3ab9")

default bad_end_location = None
default uluru_wire = None
default sahara_wire = None
default finland_wire = None
default tokyo_wire = None
default brasilia_wire = None
default yuletide_wire = None

transform greyscale:
    matrixcolor SaturationMatrix(0.0)

transform color:
    matrixcolor SaturationMatrix(1.0)

define white_fade = Fade(0.5, 0.0, 0.5, color="#fff")

# This is to pause the title music and not break the game.
label start:
    stop music
    jump chapter_1

label bomb_fail_decider:
    if bad_end_location == "Uluru":
        jump bomb_fail_uluru
    elif bad_end_location == "Sahara":
        jump bomb_fail_sahara
    elif bad_end_location == "Finland":
        jump bomb_fail_finland
    elif bad_end_location == "Tokyo":
        jump bomb_fail_tokyo
    elif bad_end_location == "Brasilia":
        jump bomb_fail_brasilia
    elif bad_end_location == "Canada":
        jump bomb_fail_canada
    elif bad_end_location == "Yuletide":
        jump yuletide_fail

label bomb_fail_final:
    play music "audio/music/17406877-your-own-personal-hell-8685.mp3" loop

    scene earth with fade

    "The camera pulls away from the world."

    "Far above the atmosphere... Earth hangs in silence."

    "Then—"

    play sound "audio/freesound_community-cinematic-rumble-106063.mp3"

    "A pulse."

    "A wave of unnatural cold spreads across the surface."

    scene earth2 with dissolve

    "Clouds crystallise mid-motion."

    "Oceans begin to harden."

    "Cities dim beneath a growing frost."

    "Not an explosion—"

    "An infection."

    "Cold. Absolute. Unstoppable."

    scene 1_3

    "The signal reaches beyond the world."

    "Into something that was never meant to be touched."

    k "...What?"

    "The throne room trembles."

    "The air fractures into shards of frozen light."

    k "No—this wasn't part of the plan—"

    "A spike of energy erupts from nowhere."

    play sound "audio/universfield-blade-piercing-body-352462.mp3"
    voice "audio/kuzu420-dying-guy-288051.mp3"

    scene white

    "It pierces straight through his chest."

    "Not metal."

    "Not matter."

    "Magic."

    k "Ghh—?!"

    "The force lifts him from the throne."

    "Freezes him in place."

    k "This... isn’t... possible..."

    "The cold spreads through him."

    "Up his spine."

    "Across his limbs."

    "Into his voice."

    k "...I..."

    "Silence."

    "The throne room collapses into stillness."

    "Frozen."

    "Abandoned."

    stop music fadeout 3.0
    scene black with fade

    "The signal degrades."

    "Visual feed lost."

    play music "audio/music/freesound_community-infinius-fail-675.mp3" loop

    "Ending: Global Freeze"
    return

label bomb_fail_final_alt:
    scene 1_3
    play music "audio/music/17406877-your-own-personal-hell-8685.mp3" loop

    "The signal reaches beyond the world."

    "Into something that was never meant to be touched."

    k "...What?"

    "The throne room trembles."

    "The air fractures into shards of frozen light."

    k "No—this wasn't part of the plan—"

    "A spike of energy erupts from nowhere."

    play sound "audio/universfield-blade-piercing-body-352462.mp3"
    voice "audio/kuzu420-dying-guy-288051.mp3"

    scene white

    "It pierces straight through his chest."

    "Not metal."

    "Not matter."

    "Magic."

    k "Ghh—?!"

    "The force lifts him from the throne."

    "Freezes him in place."

    k "This... isn’t... possible..."

    "The cold spreads through him."

    "Up his spine."

    "Across his limbs."

    "Into his voice."

    k "...I..."

    "Silence."

    "The throne room collapses into stillness."

    "Frozen."

    "Abandoned."

    stop music

    scene black with fade

    "The signal degrades."

    "Visual feed lost."

    play music "audio/music/freesound_community-infinius-fail-675.mp3" loop

    "Ending: Global Freeze"
    return

label bomb_fail_final_yukina:
    play music "audio/music/17406877-your-own-personal-hell-8685.mp3" loop

    scene earth with fade

    "The camera pulls away from the world."

    "Far above the atmosphere... Earth hangs in silence."

    "Then—"

    play sound "audio/freesound_community-cinematic-rumble-106063.mp3"

    "A pulse."

    "A wave of unnatural cold spreads across the surface."

    scene earth2 with dissolve

    "Clouds crystallise mid-motion."

    "Oceans begin to harden."

    "Cities dim beneath a growing frost."

    "Not an explosion—"

    "An infection."

    "Cold. Absolute. Unstoppable."

    scene 1_3

    "The signal reaches beyond the world."

    "Into something that was never meant to be touched."

    "Yukina, in her disguise, in her throne."

    y "...What?"

    "The throne room trembles."

    "The air fractures into shards of frozen light."

    y "No—this wasn't part of the plan—"

    "A spike of energy erupts from nowhere."

    play sound "audio/universfield-blade-piercing-body-352462.mp3"
    voice "audio/death-scream-female-smartsound-fx-1-00-04.mp3"

    scene white

    "It pierces straight through her chest."

    "Not metal."

    "Not matter."

    "Magic."

    y "Ghh—?!"

    "The force lifts her from the throne."

    "Freezes her in place."

    y "This... isn’t... possible..."

    "The cold spreads through her."

    "Up her spine."

    "Across her limbs."

    "Into her voice."

    y "...I..."

    "Silence."

    "The throne room collapses into stillness."

    "Frozen."

    "Abandoned."

    stop music fadeout 3.0
    scene black with fade

    "The signal degrades."

    "Visual feed lost."

    play music "audio/music/freesound_community-infinius-fail-675.mp3" loop

    "Ending: Global Freeze"
    return

label chapter_1:
    scene 1_1 with fade

    "Chapter 1: Humble Beginnings"

    "The current date is: the four and twentieth day of June, in the thirteenth year of Charles III, a.k.a, 24/4/34"

    scene 1_2
    play music "audio/music/spooky-dark-night.mp3" loop

    "King Ted, ruler of the Land of the Yuletide (The Bad Yuletide), returns from the mountaintop, exhausted and carrying a pile of unmelting snow."

    scene 1_3

    k "Finally... we got the payload."
    
    k "My feet... rub them, all of you."

    scene 1_4

    "The minions kneel, massaging his tired feet. The snow on the floor refuses to melt, shifting as if alive."

    scene 1_5

    p "Your Majesty... we have everything needed to craft the ultimate weapon."

    scene 1_6
    
    p "I have prepared a prototype — Heliohydronate-Argentate, Type Ω-1: C₁₇H₂₆O₁₀He₃Ag⁺. With it, we can freeze an entire room... even with a prisoner inside."

    k "Freeze a room, you say? And... the prisoner?"

    p "We tested it... sire. It will take but a single minute. One minute, and the room will belong to winter alone. The final bombs are still underway, and we will use them to freeze the world, as you commanded."

    scene 1_7

    "A few minutes later... Ted and his minions are getting ready to blast the room with absolute zero."

    k "On my mark, press the button."

    c "O-okay..."

    scene 1_8

    play sound "stomp.mp3"
    k "Ignite!"

    scene 1_9

    play sound "button.mp3"
    "The minion steps forward. At the press of a button, wires ripple across the Core Vessel, acting as electrical circuits."

    scene 1_10

    play sound "ticking.mp3"
    s "Your Majesty... the frost is spreading... even the walls seem to hesitate."

    q "You... monsters... you can't... do this..."

    scene 1_11

    k "Silence. This is the cold truth of my reign. Learn to appreciate it."

    scene 1_12

    c "The air grows heavier... I can almost hear the snow whispering..."

    q "Somebody... help... anyone..."

    k "Enjoy your final solstice. Let it teach you patience... and fear."

    s "Forty seconds have passed... I... I feel the chill crawling up my arms..."

    q "I won't... I won't be forgotten..."

    k "You already are. Now... still yourself."

    scene 1_13

    play sound "ticking.mp3"
    p "Ten seconds... the wires tighten... the light... the light is so bright, sire..."

    "The prisoner pleads for help as Ted appreciates his work from afar."

    stop sound
    play sound "explosion.mp3"
    scene white with dissolve
    scene 1_14 with dissolve
    stop music fadeout 1.0

    "The Core Vessel exhales. The prisoner is no more. King Ted prevents another fatality by ejecting the room into the multiverse."

    k "Perfect. Very good."

    c "It worked, Your Majesty. The room... the prisoner... gone, just as you commanded."

    scene black with fade

    "Chapter 2: The Fox Who Must Act"

    "This chapter is viewed from the eyes of Raviolo."

    "The current date is: June 3, 2032"

    play music "audio/music/yesterday.mp3" loop
    scene 2_1 with fade

    "Masato slowly opens his eyes. Harsh lights shine down; the hum of heaters and the Antarctic wind filter through reinforced steel walls."

    m "...Where... am I...?"

    r "Good, you're awake. I was beginning to worry."

    m "...Again? Why 'again'?"

    r "Long story. Let's focus on the important part: the world is in danger."

    m "...Right. The bombs?"

    scene 2_2

    "Raviolo nods."

    scene 2_3

    r "King Ted planted seven bombs. Six on the surface—one per continent, except Antarctica. The seventh... is in the Earth's inner core."

    m "And the other six? Can't we just—"

    r "Physical devices. Wire cutters, gloves, a steady hand. You? You're only needed for the core bomb."

    m "...Why me?"

    r "I'm required by law to keep info confidential, so I'm afraid I can't tell you right now."

    scene 2_4

    "Masato sighs."

    m "So my destiny... is just the seventh bomb?"

    r "Not really. The others will roam free across continents. Deserts, jungles, mountains... all accessible with proper tools. You have proper tools too."

    scene 2_5

    m "Fine. Show me what I'm dealing with."

    scene 2_6

    "Raviolo projects a holographic map of the world. Some red blips pulse slowly across the continents. One bright blip shines at the Earth's core."

    r "Six surface bombs. Disarm them first to prevent collateral damage. Each one requires care, precision, and courage, but nothing a skilled disarmer can't handle."

    m "And the seventh?"

    r "Encrypted, adaptive, and highly dangerous. That's where your skills come in. One wrong move... global freeze."

    r "You've worked with me once. Do your mission again."

    scene 2_7

    m "Understood. I won't fail."

    r "Good. Start with the first surface bomb. Wire cutters at the ready."

    "Masato feels the weight of responsibility. Each bomb is a ticking reminder of the world depending on him."

    scene 2_8

    m "Let's move. We have work to do."

    scene black with fade
    stop music fadeout 1.0

    play music "audio/music/train-country-blues-rock.mp3" loop
    scene 3_1 with fade
    "Chapter 3: The Road to Uluru"

    scene 3_2
    r "Drink up. Bad Yuletide frostbite is worse than normal frostbite. It insults you."

    r "Now—Australia awaits. The first bomb is hiding behind Uluru."

    scene 3_3
    m "Uluru? THE Uluru?"

    r "Yes. The one tourists take selfies with. Try not to blow it up."

    m "No promises. This is my first bomb."

    scene 3_4
    "Raviolo and Masato go outside to a massive monster truck."

    m "This looks like it was designed during a fever dream."

    r "Correct. Fever of AI°C. Now get in."

    scene 3_5
    r "Just drive straight. Do not turn, do not blink longer than three seconds, and whatever you do, do NOT honk."

    m "What happens if I honk?"
    
    r "The ocean screams back."

    m "...I'm not questioning that."

    scene 3_6
    "Masato slams the accelerator."

    scene 3_7
    play sound "audio/mixkit-cars-starting.mp3"
    m "WHOOAAA—"

    "The truck starts to move. It is on it's way to the famous rock in Australia."

    scene uluru_travel_intermission

    "It travels through hundreds of waves."

    "Here's a fun fact. Uluru used to belong to the Pitjantjatjara people of Pitjantjatjara country."

    "The 4D path threads over invisible roads only the truck can perceive."

    scene 3_8
    stop music
    play music "audio/music/amurich-wail-of-sand.mp3" loop
    "Masato arrives at the outskirts of Uluru."

    r "Testing, 1, 2, 3. Can you hear me? Over."

    m "I read you loud and clear."

    m "Huh... this desert is so red. I've never seen sand this colour before."

    scene 3_9
    r "The bomb is close. It has four wires: red, blue, yellow, and green. They are in the fourth dimension; your engineered eyes can detect them."

    r "Remember: the clue tells you which wire NOT to cut. The rest will defuse it."

    m "So choose anything BUT the wrong choice?"

    r "Yes. Like life."

    m "Miserable, but inspirational..."
    
    scene 3_10
    "Masato approaches the bomb. On it is a word in Pitjantjatjara language: Kutyu"

    m "Hold on, there's a piece of paper written in English and Pitjantjatjara language."

    scene 3_11
    stop music
    play music "audio/music/deadite-ash-vs-evil-dead-song.mp3" loop
    "The category is \"Australia\"."

    r "That's a sign I've not seen. Because we are talking through walkie-talkies."

    m "The clue looks says \"Leave the red deserts of this land alone.\"."
    "Masato thinks. The red deserts of this land..."
    "Which wire should Masato cut?"
    menu:
        "Cut the Red wire":
            $ bad_end_location = "Uluru"
            jump bomb_fail_decider

        "Cut the Blue wire":
            $ uluru_wire = "blue"
            jump bomb_defuse_uluru

        "Cut the Yellow wire":
            $ uluru_wire = "yellow"
            jump bomb_defuse_uluru

        "Cut the Green wire":
            $ uluru_wire = "green"
            jump bomb_defuse_uluru

label bomb_defuse_uluru:
    "Masato cuts the [uluru_wire] wire..."
    play sound "power-down-03.mp3"
    jump chapter_3_continuation

label bomb_fail_uluru:
    "Masato cuts the red wire..."
    "Congratulations! You blew it."
    play sound "explosion.mp3"
    scene 3_fail
    "The bomb explodes in a wave of pure -30°C"
    jump bomb_fail_final

label chapter_3_continuation:
    play music "audio/music/win-and-win.mp3" loop

    scene 3_12 with dissolve

    "The bomb fizzles, then dies. Winter's threat retreats for now."

    m "One down... six to go."
    m "I just hope the next one isn't underwater or something."
    r "Good work, Masato. The first seal is undone."

    scene 3_13 with dissolve
    "The magic truck shimmers, its wheels bending into impossible angles, and the entire structure somehow broken."

    r "Next stop... Africa."
    stop music fadeout 1.0
    stop sound
    play music "audio/music/spooky-dark-night.mp3" loop
    scene 3_after_1 with fade

    "Meanwhile, in a chamber surrounded by maps and war plans, the villains enjoy a perfectly innocent... board game night."

    scene 3_after_2
    play sound "audio/roll.mp3"
    k "Heh... look at that. I rolled a six, and I get to take all the money in the jackpot."
    k "Truly, I am destined to be rich."

    scene 3_after_3
    s "Your Majesty, you already have a vault the size of Uluru!"
    s "Why do you need more money in a board game?"

    scene 3_after_4
    k "Because, victory must be total."
    k "Even in fiction."

    scene 3_after_5
    play sound "audio/roll.mp3"
    pause 0.5
    scene 3_after_6
    pause 0.5
    scene 3_after_7
    play sound "audio/roll.mp3"
    pause 0.5
    scene 3_after_8
    play sound "audio/card-sounds.mp3"
    c "Hey, that card was mine."
    p "Sorry, just thought it was my turn- Oh my god."
    c "Oh! Boss, Panda drew an Event card for me that says I have to pick a player to give $700 to the jackpot... who should give to the jackpot?"

    scene 3_after_9
    k "Is that a question?"
    k "Panda, obviously, since he tried to steal your turn."

    scene 3_after_10
    "The panda slides $700 across the table, crying internally."

    scene 3_after_11
    c "So, Your Majesty, when the solstice arrives, what are you going to do then?"

    scene 3_after_12
    k "First... I will tax happiness."
    k "People should not smile sans royal approval."
    p "Sans? Don't you mean without?"
    k "..."
    "King Ted will remember that."
    s "I'll start drafting a ban on jokes!"
    k "Excellent. Except puns. I like puns."
    k "They are the lowest form of humour, therefore perfect for royalty, and the cold dark nights."

    stop music fadeout 1.0
    scene 4_1 with fade

    "Chapter 4: The Desert Dune"

    "The current date is: June 4, 2032"
    
    play music "audio/music/desert-city.mp3" loop
    "Heat rolls across the desert like a living creature."
    "The dunes shift with every gust of wind, reshaping the horizon faster than Masato can walk."

    scene 4_2
    "Masato wipes the sweat from his forehead."
    "Antarctica feels like a lifetime ago."

    m "Why... did he have to put a bomb... here of all places?"
    m "This place is trying to melt my soul."

    scene 4_3
    play sound "audio/sand-walk.mp3"
    "Each step sinks deep into scorching sand. The ground feels like it might catch fire."
    "Then, he sees it."

    scene 4_4 with dissolve
    play sound "audio/ticking.mp3"

    "A faint ticking repeats under the sand. Masato kneels and sweeps the sand aside with both paws."

    scene 4_5 with dissolve

    "The second bomb."
    "This one is half-buried, like the desert tried to swallow it whole."

    "Four wires emerge from the casing (again, in the fourth dimension): red, blue, yellow, and green."
    "They're so hot from the sun that Masato hesitates before touching them."

    m "Great. Four wires again."
    m "But what's the clue this time...?"

    play sound "audio/042889_sand-on-paper-dragged.mp3"
    "Masato brushes away one last layer of sand."

    scene 4_6
    stop sound
    stop music
    play music "audio/music/deadite-ash-vs-evil-dead-song.mp3" loop

    m "...?"
    m "What is that word supposed to mean here?"

    "He stares at the bomb, confused. No numbers. No diagrams."
    r "Masato, that is the bomb number in Arabic. The people who speak Arabic can read it just fine."

    scene 4_7

    "Masato shields the bomb with his body and thinks."

    scene 4_8
    m "Okay... okay... but then why does the clue I conveniently found tell me \"Cut the second wire in Arabic reading?\""
    m "Arabic is read from right to left..."
    m "So maybe the clue doesn't mean the second wire from the left..."

    "The bomb ticks once, louder than before."

    play sound "audio/ticking.mp3"
    pause 2

    m "Yeah, yeah, okay. Definitely time to decide."

    menu:
        "Cut the Red wire":
            $ bad_end_location = "Sahara"
            $ sahara_wire = "red"
            jump bomb_fail_decider

        "Cut the Blue wire":
            $ bad_end_location = "Sahara"
            $ sahara_wire = "blue"
            jump bomb_fail_decider

        "Cut the Yellow wire":
            $ bad_end_location = "Sahara"
            jump bomb_defuse_sahara

        "Cut the Green wire":
            $ bad_end_location = "Sahara"
            $ sahara_wire = "green"
            jump bomb_fail_decider

label bomb_fail_sahara:
    "Masato cuts the [sahara_wire] wire..."
    "I switched the type of question. Cut the right wire next time."
    play sound "explosion.mp3"
    scene 4_fail
    "The bomb explodes in a wave of pure -30°C"
    jump bomb_fail_final

label bomb_defuse_sahara:
    "Masato cuts the yellow wire."
    play sound "power-down-03.mp3"
    jump chapter_4_continuation

label chapter_4_continuation:
    play music "audio/music/win-and-win.mp3" loop
    scene 4_9
    "A soft hiss escapes the device as its internal energy dissipates harmlessly into the sand."
    "Masato exhales, relief washing over him, but he doesn't relax completely; the next bombs await across the globe, each with its own deadly twist."
    
    "The desert wind carries fine grains of sand into his fur, brushing against his face as he examines the deactivated bomb."
    "Masato notes every detail mentally, knowing the clues here may help him with the bombs yet to come."
    
    "The sun reflects off the dunes in dazzling golden tones, but the beauty is tempered by the shadow of the next threat."
    
    "He stands, brushing sand from his paws, and activates his communication device."
    
    "Raviolo's calm, measured voice fills his earpiece:"
    r "Masato, good work. That bomb is neutralised. But remember, the real challenge is yet ahead — the one hidden in the Earth's core. Prepare yourself. You'll need all your skills and wits to survive that one."
    
    "Masato nods silently, determination hardening in his chest."
    "The Sahara stretches endlessly around him, but for now, a small victory has been claimed."
    "He glances once more at the neutralised device, feeling the weight of responsibility settle on his shoulders."
    
    "With the desert still ringing in his ears and the wind swirling around him, Masato sets off toward the next location, eyes sharp, mind alert, fully aware that the path ahead is as perilous as the blazing sands he leaves behind."

    stop music fadeout 1.0
    scene 5_1 with fade

    "Chapter 5: Christmas in... June?"
        
    play music "audio/music/easy-does-it-jonny-boyle-main-version-02-28-20.mp3" loop
    "The snow outside is melting, the sun refuses to set, and the whole world glows in that strange Finnish midsummer twilight."
    "Yet Masato steps into a cosy cabin... that looks like it froze in time six months ago."

    scene 5_2 with fade

    m "Okay... this cannot be right."
    m "It is June. JUNE. And these people still have their Christmas tree up?"
    m "Either this family really loves Christmas..."
    m "...or something went horribly, horribly wrong."

    "Masato steps forward—when he suddenly hears a muffled noise."

    "???" "Mmmff! H-hey! Down here!"

    m "...What?"

    "Masato crouches and lifts the lower branches of the Christmas tree."

    scene 5_3

    "An elf — a real, pointy-eared, red-hatted Christmas elf — is halfway stuck under the tree.  
    He is trapped partially in the next bomb, and a tiny red restraining wire holds him hostage."

    e "Finally! Someone who isn’t wearing a ski mask! Can you PLEASE get me out of here?!"

    m "You... you're an elf."

    e "Yes! Congratulations! Very observant! Now HELP ME!"

    scene 5_4
    m "Are you... part of the bomb?"

    "The elf tries to move but the collar sparks faintly."

    e "Apparently! I was wrapping presents, next thing I know—BAM! Wires everywhere! Not exactly OSHA compliant!"

    scene 5_5
    "Masato leans closer. On the bomb is the number 3 in Finnish."
    
    "On the side, scribbled on a paper tag in Finnish:"

    stop music
    play music "audio/music/deadite-ash-vs-evil-dead-song.mp3" loop
    scene 5_6
    # Kategoria: Joulu.
    # Vihje: Milloin on lähimpänä Jeesuksen Kristuksen todellista syntymäpäivää?
    "Category: Christmas.\nClue: When is the closest to Jesus Christ's real birthday?"

    m "Right. Another category puzzle."
    m "Uluru was geography. Sahara was numbers."
    m "And now... Christmas history?"

    m "So they want me to think about the actual date Jesus was born."
    m "Not the traditional December 25th... that's the *furthest* from the truth."

    e "HEY! I'm still here! And I would prefer NOT to explode!"
    menu:
        "Cut the Red wire (25 December)":
            $ bad_end_location = "Finland"
            $ finland_wire = "red"
            jump bomb_fail

        "Cut the Blue wire (6 January)":
            $ bad_end_location = "Finland"
            $ finland_wire = "blue"
            jump bomb_fail

        "Cut the Yellow wire (2 February)":
            $ bad_end_location = "Finland"
            $ finland_wire = "yellow"
            jump bomb_fail

        "Cut the Green wire (8 March)":
            jump bomb_defuse_finland

label bomb_fail_finland:
    "Masato cuts the [finland_wire] wire..."
    play sound "audio/explosion.mp3"
    scene 5_fail
    "The bomb detonates, unleashing a wave of freezing -30°C air."
    "The elf's scream echoes as everything fades to white."
    "Now that wasn't very Christmassy, wasn't it?"
    jump bomb_fail_final

label bomb_defuse_finland:
    m "Masato cuts the green wire..."
    play sound "audio/power-down-03.mp3"

    scene 5_7 with dissolve
    play music "audio/music/win-and-win.mp3" loop
    "The bomb's lights fade out completely. The house finally stops humming."
    "Masato takes a slow breath. The smell of cinnamon and pine needles suddenly comes back to life."
    m "It's not even December. Why does it still smell like Christmas?"

    m "Anyway... another bomb down."
    "Masato stands, brushing pine needles from his shoulders. The living room is oddly cosy — warm lighting, knitted socks drying by the heater, a line of tiny Santa figurines on the shelf."

    m "Whoever lives here must *really* love Christmas."
    m "Or... maybe the bomb squad before me never made it out and didn't finish decorating."
    "He turns toward the window. Outside, the sun is bright — impossibly bright. Midsummer Finland. Sun refuses to set."

    m "I should let HQ know the device's neutralised."
    "He reaches for his phone."
    "But before he can press anything — the phone buzzes on its own."

    scene 5_8
    m "...Not again."
    "He answers cautiously."

    v "Very good, Masato. You chose correctly again."

    "Masato freezes."

    m "Who is this?"
    v "Three bombs, three correct cuts. You're predictable... but effective."

    m "You're testing me. All these categories... all these clues..."
    v "Observant. Then listen carefully: you're almost halfway through our game."

    "Masato feels cold despite the summer heat."

    "Static cracks across the line."

    v "Your next bomb is already waiting. East-south-east. Follow the daylight."

    "Click."
    "The caller hangs up."

    m "So I'm only at... number three."
    m "South-east. Daylight. That could mean... Estonia? Latvia? Maybe Lithuania."
    m "Great. More travelling."
    "Just as he starts walking, something glints under the tree:"

    "A piece of folded gold foil."

    "He picks it up. It's a chocolate coin wrapper, but on the inside someone has written, albeit in a language he finally understands: Japanese:"

    scene 5_10
    "CATEGORY: MUSIC\nWho produced the hit song \"Tempestissimo\"?"

    m "...Fantastic."
    m "They're changing the rules again."

    stop music fadeout 1.0
    scene 6_1 with fade

    "Chapter 6: Tokyo Rhythms"

    play music "audio/music/japanese-dark-temple-amp-samurai-yokai.mp3" loop
    "The sun is rising from the rooftops of a quiet Tokyo suburb, casting long shadows across narrow streets."
    "Masato notices that blue bowl-shaped bomb with blinking lights and the Japanese word for \"4\" sitting right next to a low wooden house, its sliding doors slightly ajar."
    
    scene 6_2
    m "Alright... another bomb."
    m "The chocolate coin’s message... let’s see..."
    scene 5_10 at greyscale with white_fade
    m "CATEGORY: MUSIC\nWho produced the hit song 'Tempestissimo'?"

    m "Five wires this time. Red, Blue, Yellow, Green... and Purple."
    m "They’re keeping me on my toes. One wrong cut, and—well, I don’t want to imagine that."

    scene 6_3
    stop music
    play music "audio/music/deadite-ash-vs-evil-dead-song.mp3" loop
    "Masato crouches next to the device, inspecting each wire carefully."
    "Little beads of sweat form on his forehead, despite the mild evening air."

    m "Red... Blue... Yellow... Green... Purple..."
    m "I need to remember the clue from the coin wrapper. The correct producer isn’t obvious."
    m "Time to think strategically."

    menu:
        "Cut the Red wire (REDALiCE)":
            $ bad_end_location = "Tokyo"
            $ tokyo_wire = "red"
            jump bomb_fail_decider

        "Cut the Blue wire (aran)":
            $ bad_end_location = "Tokyo"
            $ tokyo_wire = "blue"
            jump bomb_fail_decider

        "Cut the Yellow wire (P*Light)":
            $ bad_end_location = "Tokyo"
            $ tokyo_wire = "yellow"
            jump bomb_fail_decider

        "Cut the Green wire (t+pazolite)":
            $ tokyo_wire = "green"
            jump bomb_defuse_tokyo

        "Cut the Purple wire (Laur)":
            $ bad_end_location = "Tokyo"
            $ tokyo_wire = "purple"
            jump bomb_fail_decider

label bomb_fail_tokyo:
    "Masato cuts the [tokyo_wire] wire..."
    play sound "audio/explosion.mp3"
    scene 6_fail with white_fade
    "The bomb detonates in a sudden flash of light and sound!"
    "Shards of metal scatter across the wooden floor, the smell of smoke fills the air."
    "Masato barely rolls to the side, coughing as dust and debris settle."
    jump bomb_fail_final

label bomb_defuse_tokyo:
    m "Masato cuts the green wire..."
    play sound "audio/power-down-03.mp3"
    jump chapter_6_continuation

label chapter_6_continuation:
    scene 6_4
    play music "audio/music/win-and-win.mp3" loop
    "The blinking lights stop. The device hums quietly and then goes completely silent."
    "Masato leans back, releasing a long breath he didn’t know he was holding."
    "The tension fades slightly as Masato stands and surveys the small yard outside the traditional house."
    m "One more bomb down. Only two more to go."

    "Masato glances around the quiet street."
    m "Empty houses, soft lantern light, distant cicadas... perfect distraction, if someone wanted it."
    "He picks up the paper, folds it carefully, and tucks it into his pocket."
    
    "Masato takes a cautious step back inside the house, eyes scanning for anything out of place."
    m "Every bomb seems to get more... personal."
    m "This isn’t just a game. Someone knows exactly how to push me to the edge."

    scene 6_3
    "He kneels to inspect the green wire spot again, ensuring there are no hidden triggers."
    "Satisfied, he finally moves towards the door, the cool wooden floor creaking under his steps."
    m "Time to let HQ know the device is neutralized... but something tells me, they’re already watching."

    "Outside, the shadows lengthen. A crow caws in the distance."
    "Masato feels the weight of anticipation. The next bomb... whatever it is... could be even more complicated."

    stop music fadeout 1.0
    scene 7_overhead with fade

    "Chapter 7: The Card of Judgement"

    play music "audio/music/sport-energy.mp3" loop

    "The afternoon sun blazes across Brasília's iconic modernist skyline. Marble curves, sweeping columns, and shadows stretched long across the Praça dos Três Poderes."

    "Masato follows the signal on his tracker until he reaches the grassy edge of a massive football field behind a training centre."

    m "A bomb... on a football pitch."
    m "This is new. Very new."
    
    scene 7_1
    "At midfield, sitting suspiciously upright on the bright green turf, is a compact metal device — blinking lights, humming vents, reading \"5\" in Brazilian Portuguese, and now six wires instead of five."

    m "Six wires... they keep upping the difficulty."
    m "Red, Blue, Yellow, Green, Purple... and now Orange."

    "Beside the bomb, a laminated card flutters in the wind — bright yellow on one side, bright red on the other."

    scene 7_2
    "Masato kneels and flips it over. On the back it reads:"
    scene 7_3
    stop music
    play music "audio/music/deadite-ash-vs-evil-dead-song.mp3" loop
    "Category: Football.\nClue: Which colour card is shown by a referee to signify that a player has been sent off?"

    m "Football... easy. But what is the one that sends a player off?"
    m "So they want me to cut the wire that matches the card that ejects someone from play."

    m "Let’s see the options..."

    menu:
        "Cut the Red wire":
            jump bomb_defuse_brasilia

        "Cut the Blue wire":
            $ bad_end_location = "Brasilia"
            $ brasilia_wire = "blue"
            jump bomb_fail_decider

        "Cut the Yellow wire":
            $ bad_end_location = "Brasilia"
            $ brasilia_wire = "yellow"
            jump bomb_fail_decider

        "Cut the Green wire":
            $ bad_end_location = "Brasilia"
            $ brasilia_wire = "green"
            jump bomb_fail_decider

        "Cut the Purple wire":
            $ bad_end_location = "Brasilia"
            $ brasilia_wire = "purple"
            jump bomb_fail_decider

        "Cut the Orange wire":
            $ bad_end_location = "Brasilia"
            $ brasilia_wire = "orange"
            jump bomb_fail_decider

label bomb_fail_brasilia:
    "Masato cuts the [brasilia_wire] wire..."
    play sound "audio/explosion.mp3"
    scene 7_fail with white_fade
    "A thunderous blast tears across the training field!"
    "The goalposts rattle violently as turf erupts like a green geyser."
    jump bomb_fail_final

label bomb_defuse_brasilia:
    m "Masato cuts the red wire..."
    play sound "audio/power-down-03.mp3"
    jump chapter_7_continuation

label chapter_7_continuation:
    scene 7_4
    play music "audio/music/win-and-win.mp3" loop
    "The device beeps twice, then falls silent."
    "A warm breeze blows across the pitch."

    m "Red card. Right — sends the player off the field."
    m "They really are changing the rules every bomb."

    "Masato stands, brushing grass off his knees. The sun glints off the sleek government buildings in the distance."

    m "Five bombs. Two more to go."
    m "And whoever is behind this knows I’m still in the game."

    "His phone buzzes. Again."

    v "Congratulations, Masato. Brazil suits you."
    m "I'm getting real tired of your phone calls."
    v "Then stop surviving. Problem solved."

    "Click."

    m "...Next location, huh? Bring it on."

    scene 7_after_1 with fade
    play music "audio/music/spooky-dark-night.mp3" loop

    "Somewhere far from Masato’s path..."

    "A narrow hallway stretches through the interior of King Ted’s complex."
    "The air hums softly, charged with unseen energy."

    scene 7_after_2 with dissolve

    "A minion walks briskly down the corridor, checking data on a handheld monitor."

    d "Brazil is clear."
    d "Masato keeps choosing correctly... unfortunately."

    "He steps forward."

    play sound "audio/floraphonic-slime-squish-2-218566.mp3"

    d "—What the—?"

    "He looks down."

    scene 7_after_3 with dissolve

    "His feet are half-submerged in a glossy, semi-transparent slime."
    "It grips instantly, stretching like molten glass."

    d "No no no— what?!"

    "He pulls. The slime tightens."

    scene 7_after_4
    play sound "audio/HB Rubber Stretch SFX.mp3"
    d "Hnnngh!"

    scene 7_after_5
    stop sound
    play sound "audio/floraphonic-slime-squish-2-218566.mp3"
    "It pulls back"

    d "Man, I can't get out!"

    play sound "audio/dragon-studio-epic-dragon-roar-364481.mp3"
    d "TED!!!!!!!"

    "A calm voice answers him."

    scene 7_after_6 with dissolve

    k "Oh, dear."

    "King Ted steps into view, examining the slime with mild irritation."

    k "That trap was designed for Masato."
    k "Not for you."

    d "Y-your Majesty, I swear— the dimensional anchor shifted!"

    k "Which means he avoided it."

    "Ted straightens, eyes narrowing."

    k "Unacceptable."

    "He taps his cane against the floor. The slime stops spreading—but does not release."

    k "Prepare the override."
    k "If Masato will not enter Yuletide willingly..."

    scene 7_after_7 with dissolve

    "Monitors light up. A familiar map appears."

    "One marker flashes over North America."
    "Another pulses faintly... far away."

    k "Then we force a choice."

    "He smiles thinly."

    k "The North American device will arm itself."
    k "But its detonation will remain tethered."

    d "Tethered to...?"

    k "Yuletide."

    "The minion freezes."

    d "You mean— if he disarms the wrong one—"

    k "—they explode."

    "Ted turns away."

    k "Either he saves his world..."
    k "Or he steps into mine."

    scene black with fade
    stop music fadeout 1.0

    "Somewhere, a timer begins to tick."

    scene 8_1 with fade
    play music "audio/music/softsuicide-demeler-118865.mp3" loop

    "Chapter 8: Mikki Pogtan"

    "Meanwhile, the world map flickers violently on Masato’s device."

    "Two signals pulse in opposition."

    "One burns bright over North America."
    "The other... distant, unstable... buried deep within something labelled only as 'YULETIDE'."

    m "Two bombs... but only enough time for one."
    m "That’s what you want, isn’t it...?"

    "The wind around him picks up, unnatural, like the world itself is holding its breath."

    "His communicator suddenly SCREAMS with static."

    play sound "audio/freesound_community-communication-breakdown-28108.mp3"

    m "—What now?!"

    "A second signal forces its way through, overriding everything."

    r "Masato. Do not move."

    stop sound

    m "Raviolo?!"

    "The map stabilises slightly, though the Yuletide signal flickers like a dying star."

    r "Listen carefully. You are being led into a false choice."

    m "False? There are two bombs!"

    r "No."
    r "There is only one that matters."

    "A pause. The North America signal pulses again, louder, more urgent."

    m "Then what is that one?!"

    r "A decoy."

    "Silence."

    m "...You’re joking."

    r "I am not."

    "The screen glitches — schematics briefly flash across the display."

    r "The North American device is incomplete."
    r "Its detonation relies on a central control core."

    m "So if it goes off—?"

    r "It discharges."
    r "A violent release of cold energy. Enough to blanket the area in snow..."
    r "...but not enough to cause total destruction."

    "Masato clenches his fist."

    m "So all this panic... all this pressure..."
    m "It’s just to distract me."

    r "Exactly."

    "A new signal pulses faintly."

    r "That is the core."
    r "The source of every bomb you’ve encountered."

    m "Uluru... Sahara... Finland... Tokyo... Brazil..."

    r "All tethered."
    r "All waiting for a single command."

    "Masato’s voice lowers."

    m "Then why not just go there from the start?"

    r "Because you couldn’t."

    "A beat."

    r "Until now."

    "The device in Masato’s paw begins to glow."

    "Fragments of light — colours he recognises — begin to orbit slowly."

    m "Wait... these are—"

    r "The gemstones."

    "They circle faster."

    r "Every bomb you defused stabilised one fragment."
    r "You weren’t just surviving... you were preparing."

    m "Preparing for what?"

    r "You’ve been carrying them all along."
    r "And now... they’re ready."

    stop sound
    play sound "audio/freesound_community-power-charge-6798.mp3"

    "The air distorts."

    "The ground beneath Masato trembles as heat ripples outward."

    "Flames spark at his fingertips — small at first... then growing."

    m "This power..."

    r "Yuletide is not a place you can simply walk into."
    r "It is a constructed dimension. Cold. Hostile. Controlled."

    "The flames surge up Masato’s arms."

    r "Without protection... you would not survive before reaching the core."

    "Masato steadies his breath."

    m "Let's do it."

    x "*from radio* Oh, come on, not another Sonic transfomation."

    scene 8_2 with white_fade

    "Fire erupts fully around him — controlled, contained, alive."

    "His silhouette sharpens within the blaze."

    m "...Fire Masato."

    "The snow in the distance begins to melt before it even lands."

    "The North America signal suddenly spikes."

    play sound "audio/8footdino_on_scratch-alarm-301729.mp3"

    m "It’s about to go off!"

    r "Let it."

    m "That’s a lot of people!"

    r "Trust me."

    "A long pause."

    "The Yuletide signal flickers... almost disappearing."

    r "If the core completes its cycle, every bomb will reach full power."
    r "Not snow. Not warnings."

    r "Extinction."

    "Masato looks between the two signals."

    "One immediate."
    "One hidden."

    m "Save what I can see..."

    m "...or stop what I can’t."

    "The flames around him pulse in sync with his heartbeat."

    menu:
        "Go to North America and stop the explosion":
            $ chapter_8_choice = "america"
            jump chapter_8_america

        "Go to Yuletide and search for the other bomb":
            $ chapter_8_choice = "yuletide"
            jump chapter_8_yuletide

        "Trust Raviolo and attack the core as Fire Masato":
            $ chapter_8_choice = "core"
            jump chapter_8_core

label chapter_8_america:
    scene 8_sky_burn with white_fade
    play sound "audio/fire_dash.mp3"

    "Masato rockets across the sky, flames trailing behind him like a comet."

    m "No time. I’m not gambling lives on a theory."

    "Clouds tear apart as he descends."

    "A frozen landscape stretches endlessly below."

    "Mountains. Forests. Snowfields."

    "And in the snow"

    scene 8_canada_1 with white_fade

    "A bomb. Larger than the others."

    "Violent. Unstable."

    m "There you are."

    "Masato doesn’t slow down."

    "He drives straight into the device—"

    scene 8_canada_2
    pause 0.5

    "—and slams into it with full force."

    scene 8_canada_3
    pause 0.4
    scene 8_canada_4
    pause 0.4
    scene 8_canada_5
    pause 0.4
    scene 8_canada_6
    pause 0.4
    scene black
    play sound "audio/impact_heavy.mp3"

    "The casing cracks."

    "Wires snap."

    "The device sparks wildly."

    m "..."

    play sound "audio/explosion.mp3"

    "A blinding burst of white consumes everything."

    "...But there is no fire."

    "No shockwave."

    "Only cold."

    "A wave of frost rolls outward."

    "Snow begins to fall."

    "Soft. Silent."

    m "..."

    "The device collapses beneath him."

    "Dead."

    "Empty."

    "Just like Masato."

    "A distant sound answers him."

    "A deep... mechanical pulse."

    "Far below the surface of the Earth—"

    "The core stabilises."

    "The final sequence begins."

    r "Masato..."

    r "You chose the surface."

    "A single signal echoes across the world."

    r "And now... there’s nothing left to stop it."

    scene white with fadein

    $ bad_end_location = "Canada"
    jump bomb_fail_decider

label bomb_fail_canada:
    stop music
    play music "audio/music/freesound_community-infinius-fail-675.mp3" loop

    "Ending: Global Freeze"
    return

label chapter_8_yuletide:
    scene black with fade
    play music "audio/music/floobydust-nuclear-winter-410398.mp3" loop

    "The world fractures."

    "Masato feels the heat around him struggle as reality folds inward."

    "A violent pull drags him forward—"

    scene 8_yuletide_1 with white_fade

    "—and then silence."

    "A vast frozen landscape stretches endlessly in all directions."

    "The sky flickers like a broken screen."

    "Snow falls upward."

    m "...This place."

    m "This isn’t natural."

    r "Yuletide dimension."
    r "Constructed. Controlled."

    "Far in the distance, something pierces the sky."

    "A tower."

    m "That has to be it."

    "Masato steps forward. The ground cracks beneath his heat."

    "With each step, frost retreats... then returns the moment he passes."

    scene 8_yuletide_2 with fade

    "The tower looms overhead — tall, unnatural, humming with energy."

    "At its base..."

    "A tunnel underground..."
    
    scene 8_yuletide_3

    "...leading to a subway..."
    
    scene 8_yuletide_4

    "...upon which, a bomb."

    "But not like the others."

    "It is fused into the structure itself — cables running upward into the tower’s core, and carved into, a 6 in Iñupiaq numerals from Alaska."

    scene 8_yuletide_5

    m "So this is the controller."

    r "A relay node."
    r "Destroy it correctly, and the system collapses."

    r "Destroy it incorrectly..."

    "A pause."

    m "Canada."

    r "Yes."

    "The device lights flicker."

    "Seven wires extend outward:"

    "Red. Blue. Yellow. Green. Purple. Orange... and White."

    "A frozen panel displays a message, glitching between languages:"

    scene 8_yuletide_6
    play music "audio/music/deadite-ash-vs-evil-dead-song.mp3"
    "CATEGORY: ???\n
    CLUE: THE FIRST LIGHT OF CHRISTMAS IS NOT WHITE."

    m "Not white...?"

    m "This doesn't help me at all."

    m "Seven options... and only one chance."

    r "No resets."
    r "No second attempts."

    menu:
        "Cut the Red wire":
            jump yuletide_success

        "Cut the Blue wire":
            $ yuletide_wire = "blue"
            $ bad_end_location = "Yuletide"
            jump bomb_fail_decider

        "Cut the Yellow wire":
            $ yuletide_wire = "yellow"
            $ bad_end_location = "Yuletide"
            jump bomb_fail_decider

        "Cut the Green wire":
            $ yuletide_wire = "green"
            $ bad_end_location = "Yuletide"
            jump bomb_fail_decider

        "Cut the Purple wire":
            $ yuletide_wire = "purple"
            $ bad_end_location = "Yuletide"
            jump bomb_fail_decider

        "Cut the Orange wire":
            $ yuletide_wire = "orange"
            $ bad_end_location = "Yuletide"
            jump bomb_fail_decider

        "Cut the White wire":
            $ yuletide_wire = "white"
            $ bad_end_location = "Yuletide"
            jump bomb_fail_decider

label yuletide_fail:
    scene 8_yuletide_5
    m "Masato cuts the [yuletide_wire] wire..."

    "Nothing happens."

    "A long, horrible silence."

    m "...No explosion?"

    r "Masato."

    "The sky glitches violently."

    scene 8_yuletide_fail with white_fade
    play sound "audio/explosion.mp3"

    "A distant detonation echoes across the void."

    "A projection appears in the sky—"

    "A city in Canada, consumed in a freezing blast."

    m "No..."

    r "You chose wrong."

    "The tower hums louder."

    "Still active."

    jump bomb_fail_final_alt

label yuletide_success:
    m "Masato cuts the green wire..."

    scene 8_yuletide_5
    play sound "audio/power-down-03.mp3"
    play music "audio/music/win-and-win.mp3" loop

    "The entire tower shudders."

    "Light surges upward... then collapses inward."

    "Cracks spread through the frozen sky."

    "The dimension begins to destabilise."

    m "It’s working!"

    r "The relay is down."

    r "Now the core is exposed."

    scene 8_yuletide_portal
    "The ground beneath Masato fractures into light."

    "A deep, distant pulse echoes... from below everything."

    m "That’s the core..."

    r "Yes."

    r "And now... you can reach it."

    m "Then I’m ending this."

    "Masato jumps through the comveniently created portal into the centre of our Earth."

    jump yuletide_core_inner

label chapter_8_core:
    scene 8_sky_burn with white_fade

    "Masato launches forward — flames tearing through the air."

    "The world bends."

    "The map shatters."

    r "Good. Should that distant flash erupt far across the horizon..."

    r "A wave of frost spreads across the land..."

    pause 1.0

    r "...and then settles."

    r "Snow falls gently."

    m "...That’s it?"

    r "Yes."

    r "A quiet breath."

    r "That is the aftermath of your choice."

    m "Then we finish this."

    jump yuletide_core_inner

label yuletide_core_inner:

    scene black with fade
    play music "audio/music/kmacleod-assassin-162042.mp3" loop

    "The world disappears."

    "Light consumes everything."

    "The image cannot hold."

    "The world cannot render this moment."

    "Switching to fallback."

    scene 8_core_1
    "Masato stands at the edge of something that should not exist."

    "A vast hollow space beneath the crust of the Earth — lit by an artificial sun of molten light."

    "Below him: nothing but depth."

    "Above him: collapsing reality."

    m "So this is... the centre."

    r "No."

    r "This is the lock."

    "A massive structure floats in the centre of the chamber."

    "Suspended by unknown forces."

    "At its heart — a bomb."

    "It is unlike the others."

    "No blinking patterns."

    "No simple casing."

    "Just ten wires... each pulsing faintly as if alive."

    m "Ten wires...?"

    r "Red. Blue. Yellow. Green. Purple. Orange. White. Pink. Gold. Platinum."

    "A pause."

    r "You will cut seven."

    r "The remaining three determine the outcome."

    "The bomb hums louder."

    "Reality itself feels unstable here."

    r "Listen carefully."

    r "This is not elimination."

    r "This is selection."

    r "Every wire you remove stabilises the system."

    r "But once the seventh is cut... the system will reach critical equilibrium."

    m "Um, Raviolo? The wires are already cut-"

    "Warning lights explode into existence."

    "The structure begins to fracture."

    r "Leapin' lizards! It must be a trap!"

    r "Leave."

    "An explosion of cold air erupts behind him."

    "A figure steps through the collapsing geometry."

    "Slow. Controlled."

    "Familiar."

    k "You really never learn, do you?"

    m "...Ted?"

    "The figure tilts their head."

    "Then laughs."

    k "Ted was never real."

    k "Not entirely."

    "The voice shifts."

    "Colder."

    "Sharper."

    y "My name is Yukina."

    scene 8_core_2 with dissolve

    "Snow drifts around her like it obeys her breathing."

    "A grey silhouette wrapped in frostlight."

    "Eyes like frozen steel."

    y "Yukina."

    y "Childhood friendly llama."

    y "Worst rival."

    y "And the part of you that always loses."

    m "...That’s impossible."

    y "You brought fire into a place built on ice."

    y "Did you truly think I wouldn’t take heed?"

    r "Masato. You must leave now."

    m "Not without finishing this."

    y "Finishing?"

    y "No."

    y "You are only leted to outlive."

    y "Completion is nas in thy playwork."

    "The core begins collapsing."

    "The final wire pulses in the distance."

    "Waiting."

    m "Then I choose a new role."

    "The flames rise again."

    "Inside the Earth, fire meets ice."

    menu:
        "Run toward the exit rift":
            jump core_escape_route

        "Confront Yukina":
            jump core_confront_yukina

        "Reach for the remaining wire core":
            jump core_wire_choice

label core_escape_route:

    "Masato turns instantly."

    "The core screams behind him."

    "The structure begins collapsing inward — reality folding like burning paper."

    y "You cannot outrun the system."

    m "Watch me."

    "Fire erupts forward."

    "He runs."

    "Straight into the collapsing void."

    jump core_escape_final

label core_confront_yukina:

    m "You’re not stopping this."

    y "I already have."

    "The air freezes mid-motion."

    "Masato’s flames flicker."

    "Not extinguished."

    "Contained."

    y "This is where fire ends."

    jump bomb_fail_final_yukina

label core_wire_choice:

    m "If the system is unstable... then one wire changes everything."

    r "DO NOT—"

    "Too late."

    "Masato reaches out."

    "The final wire pulses."

    stop music
    play sound "audio/8footdino_on_scratch-alarm-301729.mp3"

    "Reality collapses inward."

    y "...Fool."

    scene white_void with white_fade

    "Everything resets."

    jump bomb_fail_final_yukina

label core_escape_final:

    scene 8_core_3 with fade
    play music "audio/music/senormusica81-epic-6-414884.mp3" loop

    "The world fractures around him."

    "Masato bursts forward through a collapsing tunnel of molten rock and shattered geometry."

    "Layers of the Earth peel apart like pages — mantle, stone, magma — all breaking under the strain."

    m "Just a little further—!"

    "Behind him—"

    "A sharp crack."

    "ICE tears through the collapsing tunnel."

    scene 8_core_4 with white_fade

    y "You cannot break out what was layouted to hold you."

    "Yukina glides through the destruction effortlessly, the collapsing world bending around her."

    "Frost spreads faster than the collapse itself."

    m "She’s catching up?!"

    r "Masato, do not slow down!"

    scene 8_core_5 with dissolve

    "He sprints across a crumbling ledge suspended over a sea of magma."

    "Chunks of rock fall away beneath his feet, dissolving into molten light."

    "Heat and cold clash violently — steam explosions rip through the air."

    y "You are running out of space."

    m "Then I’ll make some!"

    "Masato slams his paw forward — a burst of flame propels him across a widening gap."

    scene 8_core_6 with white_fade

    "The ground ahead fractures completely."

    "A dead end."

    "A vertical wall of solid rock."

    "Nowhere left to go."

    m "...No."

    "He turns."

    "Yukina lands silently behind him."

    "Perfect. Unshaken."

    scene 8_core_7 with dissolve

    y "This is the end."

    "The world continues collapsing around them, but this space holds — frozen in her control."

    y "You ran well."

    y "You withseted longer than awatched."

    y "But you were never meant to win."

    m "...You really think that?"

    y "I know it."

    m "Then you don’t get it at all."

    "A pause."

    "Masato steadies himself."

    "The flames around him flicker — weaker than before."

    y "You are exhausted."

    y "Thy fire is dying."

    m "Yeah... maybe."

    "He looks down at his paws."

    "Then clenches them."

    m "But it was never just mine."

    "The gemstones flare."

    "One by one — red, blue, yellow, green, purple, orange—"

    "They ignite around him."

    "Voices echo faintly."

    "Every place. Every trial."

    m "If there’s one..."

    m "There’s everyone."

    "Flames surge violently — no longer just fire, but something brighter."

    y "...Impossible."

    m "Let’s finish this!"

    play sound "audio/freesound_community-power-charge-6798.mp3"

    "The energy condenses into a single point in Masato’s paws."

    "Burning. Unstable. Absolute."

    scene 8_core_8
    m "Molten Destroyer Fire BEAM!!"

    play sound "audio/soundreality-the-end-148843.mp3"

    "A beam of pure destructive fire erupts forward."

    "It tears through the frozen space — shattering Yukina’s control."

    y "—!"

    "The ice fractures."

    "The dimension cracks."

    "Her form destabilises in the blast."

    "The frost collapses."

    "The silence breaks."

    "A deep, final rumble."

    r "Masato..."

    "The core—"

    "It didn’t stop."

    "The bomb begins to collapse inward."

    "Not exploding outward—"

    "But imploding."

    m "Of course it didn’t..."

    m "There’s always one last step."

    "The molten core begins swallowing everything."

    "Reality folds inward toward a single point."

    r "Masato, get out of there NOW!"

    m "If I leave... this doesn’t stop."

    r "You’ve done enough!"

    scene 8_core_9 with dissolve
    m "Not yet."

    "Masato steps forward."

    "Into the collapsing centre."

    "Flames surge around him — pushing back against the implosion."

    "He raises both paws."

    "Trying to hold it together."

    voice "audio/dragon-studio-male-groan-of-pain-357971.mp3"

    m "Ghh—!"

    "The force is overwhelming."

    "His flames begin to flicker."

    r "STOP!"

    r "You will burn out!"

    m "That’s the point!"

    "The fire weakens."

    "Fading."

    "Breaking apart."

    "The gemstones dim."

    "One by one."

    m "Come on...!"

    m "COME ON—!"

    "With everything left—"

    "He forces the flames outward one last time."

    voice "audio/freesound_community-male-voice-screaming-loudly-6147.mp3"

    m "AAAAAAAAAAHHHHHH!!"

    scene 8_core_10 with white_fade

    "The implosion halts."

    "Sealed."

    "Contained."

    "For a moment..."

    "Silence."

    "The flames vanish."

    "The protection is gone."

    "The molten core surges forward."

    r "MASATO—!"

    scene white with white_fade

    "Consumed."

    stop music fadeout 3.0
    stop sound
    stop voice

    "Nothing remains."
    jump epilogue

label epilogue:

    scene epilogue_1 with fade
    play music "audio/music/this should be in a video game.mp3" loop

    "Epilogue"

    "The year is approximately one week later."

    scene epilogue_2
    pause 2
    scene epilogue_3

    "Morning sunlight streams through the windows of a quiet classroom."

    "Children chatter excitedly until their teacher walks to the front."

    scene epilogue_4

    t "Good morning, class. It is I, Invisibility, and I will be your substitute for today."

    t "Today isn't an ordinary history lesson."

    t "Today is Dark Solstice Day."

    "The room grows quiet."

    scene 2_8 at greyscale with dissolve

    "A large photograph appears on the projector."

    "Masato."

    "Smiling."

    "Taken long before the final mission."

    t "Days ago, our world faced a disaster unlike anything recorded in history."

    t "Around the globe, mysterious devices appeared."

    t "Australia."
    t "Africa."
    t "Finland."
    t "Japan."
    t "Brazil."
    t "North America."

    scene epilogue_4 with dissolve

    t "Most people never knew how close the world came to ending."

    scene epilogue_b
    "Several students exchange surprised looks."

    b "Wait..."

    b "That really happened?"

    t "It did."

    t "Governments kept much of it classified for decades."

    t "Only recently were the records released."

    scene uluru_travel_intermission at greyscale with dissolve

    "The projector changes to a map of the world."

    "A path, traced from Antarctica to Uluru."

    t "One creature travelled to every one of these locations."

    t "He solved every puzzle."

    t "He disarmed every device he could."

    scene epilogue_4 with dissolve
    t "And when there was no other choice..."

    "Invisibility pauses."

    t "...he gave his own life."

    "Silence fills the classroom."

    scene epilogue_f
    f "He knew he wouldn't come back?"

    t "Yes."

    scene epilogue_g
    g "Why didn't he run away?"

    t "Because someone had to stay."

    t "Memorials were built by nations that once had little reason to work together."

    t "His sacrifice united them."

    scene epilogue_h
    h "Was he a soldier?"

    t "No."
    
    scene epilogue_4
    t "He was simply someone who refused to give up."

    t "History remembers many powerful people."

    t "But courage..."

    t "...belongs to anyone willing to protect others."

    "The classroom remains silent."

    "One student slowly raises a hand."

    scene epilogue_i
    i "Did they ever catch the people responsible?"

    "Invisibility smiles sadly."

    t "Some mysteries remain unsolved."

    t "But the world they wanted to destroy..."

    t "...is still here."

    scene epilogue_3 with dissolve

    t "Please stand."

    "Every student rises."

    t "For one minute..."

    t "...let us remember Masato."

    stop music fadeout 2.0

    pause 2.0

    "Psst... hey. If you're bored, there's no one stopping you from just skipping the countdown with a press of the Enter key."

    pause 60

    "The silence ends."

    "The students bow their heads."
    
    a "Thank you, Masato."

    scene white with Dissolve(4.5)

    "Far above the clouds..."

    "The sun shines warmly across a peaceful Earth."

    "No alarms."

    "No bombs."

    "Only tomorrow."

    scene black with Dissolve(5)

    "Ending: Rest In Piece"

    $ renpy.quit(relaunch=True)