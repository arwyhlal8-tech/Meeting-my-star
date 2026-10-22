# Declare characters used by this game.
define f = Character("Ava")
define s = Character("Seller")
define S = Character("Star",color= "#FFEB87")
define R = Character("Security")
define p = Character("[player_name]")

# تمديد الخلفية تلقائياً لتملأ الشاشة بالكامل وتمنع ظهور المربعات الرمادية
image bg kalfiya = im.Scale("kalfiya.png", 1920, 1080)

# تعريف الصور وتكبير حجم شخصية Star لتظهر بشكل ممتاز ومناسب للطاولة
image happy:
    "happy.png"
    zoom 2.5
    yalign 0.85

image normal:
    "normal.png"
    zoom 2.5
    yalign 0.85

image mtwatra:
    "mtwatra.png"
    zoom 2.5
    yalign 0.85


# The game starts here.
label start:

     scene black

label enter_player_name:
      
    $ player_name = renpy.input(
        "What is your name?",
        length=20
    ).strip()

    # التحقق من الاسم الافتراضي
    $ player_name = player_name if player_name else "Emiri"

    # شرط منع اسم Arwa (سواء بحروف كبيرة أو صغيرة)
    if player_name.lower() == "arwa":
        "System" "Sorry, the name 'Arwa' is reserved and cannot be used! Please choose another name."
        jump enter_player_name

    jump win_the_ticket


# ==========================================
# WIN THE TICKET
# black screen + ticket
# ==========================================

label win_the_ticket:

    scene black
    with fade

    show tikit at center
    with dissolve

    # Dialogue lines
    s "Finally, you won!"

    s "This is your lucky day!"
    
    p "Yes, finally I won!"
      
    p "I will meet my star."

    p "Ava, finally I will meet her and I will tell her how much I love her."

    p "I will tell her everything!"
    
    f "Oh my god, I'm so fucking happy for you, [player_name]! You finally won the ticket!"

    jump meet_star


# ==========================================
# MEET THE STAR
# background + star
# ==========================================

label meet_star:

    scene bg kalfiya
    with fade

    # إظهار نجمتك بتعبير سعيد عند اللقاء
    show happy at center
    with dissolve

    # Dialogue lines
    S "Hello, I'm so happy to meet you!"

    S "I heard you are my biggest fan."

    S "So, what is your name?"
    
    p "Oh my god, I can't believe I'm meeting you! Yes yes, I'm a big fan of yours! Oh, my name is [player_name]."
    
    S "Nice to meet you, [player_name]! I love your name."

    S "So, what do you want to do today?"
    
    p "I just want to talk to you, tell you how much I LOVE YOU, and know more about you."
    
    show happy at center
    S "Oh, I loooove talking to my fans! So what do you want to know about me?" 
    
    jump ask_star_questions


# ==========================================
# ASK QUESTIONS & BRANCHES
# background + star
# ==========================================

label ask_star_questions:
      
    scene bg kalfiya
    with fade

    show normal at center
      
    menu:
        "Talk about the first time you met her":
            show happy at center
            p "I-I remember your first concert! I swear it was like the BEST concert I ever watched, you were so pretty, sweetheart!"
            
            show happy at center
            S "Oh, thank you!"
            
            p "You were wearing a short, performance-style dress designed with a fitted, corset-like bodice in pink satin, embellished with shimmering patterns. The bodice featured a prominent bow at the center and delicate, thin straps, while the skirt was short and voluminous, crafted from layers of tulle and accented with two bows on the sides. The look was completed with long, sheer pink tulle gloves, a dainty pearl necklace, and a dual-ponytail hairstyle secured with matching ribbons." 
            
            show mtwatra at center
            S " O-oh .. i thing you are a big fan hh-hh "
            
            menu:
                "Ask what shampoo she uses?":
                    p "What shampoo do you use? Can I use it too, to smell like you?"
                    
                    show mtwatra at center
                    S "Oh, ahhh... it is XXXX."
                    p "No, not the one you did an ad for, but the real one you actually use! I want the real one."
                
                    S "N-no, I really use XXXX!"
                    p "Ahh okay..."
                    
                    R "Time is up!"
                    p "Oh no, that was so fast! Goodbye my sweety, can you sign my bag?"
                    
                    show happy at center
                    S "Of course, baby!"
                    p "Baby..."

                "Give her a gift":
                    p "Oh, I have something for you, do you want to see?"
                    
                    show happy at center
                    S "Oh really! Let me see!"
                    p "These are shoes, and I'm sure they are your size!"
                    
                    show mtwatra at center
                    S "B-but... how did you know my exact size?"
                    p "Oh, it's a long story... hehehe..."
                    
                    show mtwatra at center
                    S "..."
                    
                    R "Time is up."
                    p "Oh, that was fast! Can I take a picture with you?"
                    
                    show mtwatra at center
                    S "Yes, of course..."
                    p "Thank you, bye!"

        "Ask her about how she started": 

            show happy at center
            p "How did your journey start?"
            
            S "Ooh, it's a long story, but I'll make it short!"
            S "I started dancing and singing in middle school. After some auditions, three years later, I became an idol!"
            
            p "Oh wow, that's truly amazing! You worked really hard to get here."
            
            show happy at center
            S "Thank you so much, [player_name]! Your support means the world to me."
            
            p "Can I take a quick picture with you and get an autograph?"
            
            show happy at center
            S "Of course! Let's take a great picture together!"
            
            R "Time is up, thank you!"
            
            p "Thank you so much for this wonderful moment! Keep shining!"
            S "Thank you, [player_name]! Have a wonderful day!"

      
    # This ends the game.
    scene black with fade
    "Thank you for playing Meeting My Star!"
    return