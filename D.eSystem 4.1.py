#calculator
import random
from datetime import datetime
import time

class Calculator:
    def setup(self):
        while True:
            time.sleep(1)
            print("""
---------------------------------------
|                                     |
|     Give me your first number!!     |
|type -143.123456789 to close this app|
|                                     |
---------------------------------------
                  """)
            back = float(input("Give me your first number!!\n Type -143.123456789 to close this app!!"))
            if back == -143.123456789:
                break#
            else:
                print("""
---------------------------------------
|                                     |
|    Give me your second number!!!    |
|type -143.123456789 to close this app|
|                                     |
---------------------------------------
                  """) 
                number = float(input("Give me your seccond number!!\n Type -143.123456789 to close this app!!"))

            if number == -143.123456789:
                print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                break
            else:
                print("""
---------------------------------------
|                                     |
| 1: +                                |
| 2: -                                |
| 3: *                                |
| 4: /                                |
| 5: home                             |
|                                     |
---------------------------------------
                  """)
                operator = int(input("Give me an operator (1, 2, 3, 4)\n Type 5 to close this app!!"))
                
                if operator == 1:
                    sum = back + number
                    print(f"""
---------------------------------------
| sum:                                |
|{sum}                                |     
---------------------------------------
                  """)
                    input("Press enter to continue")
                    
                elif operator == 2:
                    sum = back - number
                    print(f"""
---------------------------------------
| sum:                                |
|{sum}                                |     
---------------------------------------
                  """)
                    input("Press enter to continue")
                    
                elif operator == 3:
                    sum = back * number
                    print(f"""
---------------------------------------
| sum:                                |
|{sum}                                |     
---------------------------------------
                  """)
                    input("Press enter to continue")    
                elif operator == 4:
                    sum = back / number
                    print(f"""
---------------------------------------
| sum:                                |
|{sum}                                |     
---------------------------------------
                  """)
                    input("Press enter to continue")
                elif operator == 5:
                    print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                    break
                else:
                    print("""
--------------------------------------
|                                    |
|         Unknown operator!!         |
|                                    |
--------------------------------------
                  """)
                    input("Press enter to continue")
                #calculator

class news:
    def setup(self):
        while True:
            print("""
--------------------------------------
|               D.News               |
|                                    |
| 1: news                            |
| 2: home                            |
|                                    |                                    |
--------------------------------------
                  """)
            newscommand = int(input("Type here!!"))
            if newscommand == 2:
                print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                break
            elif newscommand == 1:
                print("""
--------------------------------------
|               D.News               |
| D.eSystem 4 came out and it is     |
| a big upgrade compared to          |
| D.eSystem 3.                       |
|                                    |
| A new month started.               |
|                                    |
|                                    |
|                                    |
--------------------------------------
                  """)
                input("Press enter to continue")
            else:
                print("""
-------------------------------------
|                                   |
|         Unknown command!!         |
|                                   |
-------------------------------------
                  """)
                #news
            
            
            
class Max:
    def setup(self):
        while True:
            print("""
-------------------------------------
|                Max                |
|       What can I do for you       |
|                                   |
|                                   |
|  Type help to show all commands!  |
|   Type home to close this app!!   |
-------------------------------------
                  """)
            
            commandmax = input("Do everything for me!!(Type home to close max, type help to see all max commands)")
            if commandmax == "hello":
                answers = [
                    "hello",
                    "Hi,I am Max",
                    "Welcome",
                    "Hello friend",
                    "Hi,you are cool"
                ]
                print(f"""
--------------------------------------------
| Answer:                                  
| {random.choice(answers):<42}            
|                                          
--------------------------------------------
                  """)
                input("Press enter to continue!!")
            elif commandmax == "why are you here":
                answers = [
                    "Because I can",
                    "Why not",
                    "Because I want to help you",
                    "Becaus I want to be your friend",
                    "Because I am cool"
                ]
                print(f"""
--------------------------------------------
| Answer:                                  
| {random.choice(answers):<42}            
|                                          
--------------------------------------------
                  """)
            elif commandmax == "what is the biggest planet in the solarsystem ":
                answers = [
                    "Jupiter",
                    "Its jupiter.",
                    "The bigest planet is jupiter.",
                    "It is jupiter."
                    
                ]
                print(f"""
--------------------------------------------
| Answer:                                  
| {random.choice(answers):<42}            
|                                          
--------------------------------------------
                  """)
                input("Press enter to continue!!")
            elif commandmax == "how old are you":
                answers = [
                 "I was introduced with D.OS 8th gen (scratch) on 26 december 2024",
                 "I was introduced on 26 december 2024",
                 "We dont talk about age"
                ]
                print(f"""
--------------------------------------------
| Answer:                                  
| {random.choice(answers):<42}            
|                                          
--------------------------------------------
                  """)
                input("Press enter to continue!!")
            elif commandmax == "what is that":
                answers = [
                    "This is the all new D.eSystem 4.",
                    "It is D.eSystem",
                    "It is the new D.eSystem"
                ]
                print(f"""
--------------------------------------------
| Answer:                                  
| {random.choice(answers):<42}            
|                                          
--------------------------------------------
                  """)
                input("Press enter to continue!!")
                
            elif commandmax == "what do you like":
                answers = [
                 "I like D.electronics,D.OS,D.System,D.eSystem.",
                 "I like you!!",
                 "I like the world"   
                ]
                print(f"""
--------------------------------------------
| Answer:                                  
| {random.choice(answers):<42}            
|                                          
--------------------------------------------
                  """)
                input("Press enter to continue!!")
                
            elif commandmax == "hi":
                answers = [
                    "hi",
                    "hi friend",
                    "welcome"
                ]
                print(f"""
--------------------------------------------
| Answer:                                  
| {random.choice(answers):<42}            
|                                          
--------------------------------------------
                  """)
                input("Press enter to continue!!")
                
            elif commandmax == "home":
                print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                break
            elif commandmax == "help":
                print("You can type: what do you like, what is that, how old are you, what is the bigest planet in the solarsystem, why are you here, hello")
                print(f"""
------------------------------------------------
| You can type:                                |     
| what do you like, what is that, hello,       |
| what is the bigest planet in the solarsystem,|
| how old are you, why are you here, hi        |
------------------------------------------------
                              """)
                input("Press enter to continue")
                
            elif commandmax == "random number":
                small = float(input("Smallest number?\nType 0.0 to close Max!!"))
                if small == 0.0:
                    print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                    break
                else:
                    high = float(input("What is the highest number?\nType 0.0 to close Max!!"))
                    if high == 0.0:
                        print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                        break
                    else:
                        num = random.uniform(small, high)
                        print(f"""
--------------------------------------------
| Answer:                                  
| {num}            
|                                          
--------------------------------------------
                              """)
            elif commandmax == "Whats up":
                answers =["Hi",
                          "Whats up",
                          "Hey",
                          "hello"]
                print(f"""
--------------------------------------------
| Answer:                                  
| {random.choice(answers):<42}            
|                                          
--------------------------------------------
                  """)
                input("Press enter to continue!!")
                
            elif commandmax == "dumb":
                answers = [
                    "why",
                    ":(",
                    "whats wrong",
                    "I am not dumb"
                ]
                print(f"""
--------------------------------------------
| Answer:                                  
| {random.choice(answers):<42}            
|                                          
--------------------------------------------
                  """)
                input("Press enter to continue!!")
                
            elif commandmax == "bad":
                answers = [
                    "why",
                    ":(",
                    "whats wrong",
                    "I am not bad"
                ]
                print(f"""
--------------------------------------------
| Answer:                                  
| {random.choice(answers):<42}            
|                                          
--------------------------------------------
                  """)               
                input("Press enter to continue!!")    
                
                
            else:
                print("""
--------------------------------------------
|                                          |
|             Unknown command!             |
|                                          |
--------------------------------------------
                  """)
                input("Press enter to continue!!")
                #Max chatbot
                
            
                
class clock:
    def setup(self):
        while True:
            import time
            print("""
--------------------------------------------
|                  Clock                   |
|                                          |
| 1: time                                  |
| 2: timer                                 |
| 3: home                                  |
--------------------------------------------
                  """)
            commandclock = int(input("Type here"))
            if commandclock == 1:
                now = datetime.now()
                time = now.strftime("%H:%M:%S")
                print(f"""
--------------------------------------------
|                  Clock                   |
|                                          |
|                 {time}                   |
|                                          |
--------------------------------------------
                  """)
                input("Type anything to continue!!")
            elif commandclock == 2:
                print("""
--------------------------------------------
|                  Clock                   |
|                                          |
|           How many seconds?!?            |
|                                          |
--------------------------------------------
                      """)
                timertime = float(input("Type here!!"))
                print("""
--------------------------------------------
|                  Clock                   |
|                                          |
| If you close the app,the timer will stop.|
|                                          |
--------------------------------------------
                      """)
                
                time.sleep(timertime)
            elif commandclock == 3:
                print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                break
            #elif commandclock == "help":
                #print("You can type: time, timer, home")
            else:
                print("unknown command!!")
            #clock
        
class calendar:
    def setup(self):
        while True:
            print("""
--------------------------------------------
|                 Calendar                 |
|                                          |
| 1: date                                  |
| 2: reminder                              |
| 3: home                                  |
--------------------------------------------
                  """)
            commandcalendar = int(input("Type here!!"))
            if commandcalendar == 1:
                now = datetime.now()
                now2 = (now.strftime("%d.%m.%Y"))
                print(f"""
--------------------------------------------
|                Date today                
|                                          
| {now2}                                
--------------------------------------------
                  """)
                input("Type anything to continue")
            elif commandcalendar == 2:
                print("""
--------------------------------------------
|                 Calendar                 |
|                                          |
|                                          |
|How do you want to call your remind?      |
|                                          |
|Type home to close this window!!          |
--------------------------------------------
                  """)
                remidname = input("Type here!!")
                if remidname =="home":
                    print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                    break
                else:
                    wait1 = float(input("How many days?(Type 999.9 to close this app, if you close the app the reminder will stop)"))
                    if wait1 == 999.9:
                        break
                    else:
                        wait2 = wait1 * 86400
                        time.sleep(wait2)
                        print(remidname)
                    #calendar
                    
            elif commandcalendar == 3:
                print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                break
            
            elif commandcalendar == "help":
                print("You can type: help, reminder, date, home")
                    
                    
class desysversion:
    def setup(self):
        while True:
            print("""
-------------------------------------------
|             About D.eSystem             |
|                                         |
| 1: OS                                   |
| 2: UI                                   |
| 3: UX                                   |
| 4: brand                                |
| 5: kernel version                       |
| 6: codename                             |
| 7: home                                 |
-------------------------------------------
                  """)
            commandversion = int(input("Type here!!"))
            if commandversion == 7:
                print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                break
            elif commandversion == 1:
                print("""
------------------------------------------
|               OS version               |
|                                        |
| OS: D.eSystem 4                        |
|                                        |
------------------------------------------
                  """)
                input("Press enter to continue!!")
                
            elif commandversion == 2:
                print("""
------------------------------------------
|               UI version               |
|                                        |
| UI: D.Touch UI (ASCII edition)         |
|                                        |
------------------------------------------
                  """)
                input("Press enter to continue!!")
            elif commandversion == 3:
                print("""
------------------------------------------
|               UX version               |
|                                        |
| UX: String UX 2                        |
|                                        |
------------------------------------------
                  """)
                input("Press enter to continue!!")
            elif commandversion == 4:
                print("""
-------------------------------------------
|                  brand                  |
|                                         |
| brand: D.electronics                    |
|                                         |
-------------------------------------------
                  """)
                input("Press enter to continue!!")
            #elif commandversion == "help":
                #print("You can type: ui, ux, brand, os, help, kernel ")
            elif commandversion == 5:
                print("""
------------------------------------------
|             kernel version             |
|                                        |
| kernel: D.eCore 3.0                    |
|                                        |
------------------------------------------
                  """)
                input("Press enter to continue!!")
                
            elif commandversion == 6:
                print("""
------------------------------------------
|                Codename                |
|                                        |
| codename:Snakemount                    |
|                                        |
------------------------------------------
                  """)
                input("Press enter to continue!!")
                
            else:
                print("""
-------------------------------------------
|                 error!!                 |
-------------------------------------------
                  """)
                input("Press enter to continue!!")
                #D.eSystem version
                    
                    
                    
class notes:
    def setup(self):
        note = ""
        while True:
            print("""
--------------------------------------------
|                  Notes                   |
|                                          |
| 1: create note                           |
| 2: show notes                            |
| 3: home                                  |
--------------------------------------------
                  """)
            action = int(input("Type create to create a new note!!\nType show to show your note!!\nType home to close this app!!\nYou have to create a note befor you can show your note!!"))
            if action == 1:
                print("""
--------------------------------------------
|                  Notes                   |
|                                          |
| Create a note!!                           |
--------------------------------------------
                  """)
                note = input("Type here!!")
            elif action == 2:
                if note == "":
                    print("""
--------------------------------------------
|                  Notes                   |
|                                          |
| Error,you have no notes!!                |
|                                          |
--------------------------------------------
                  """)
                    input("Press enter to continue!!")
                else:
                    print(note)
                    print(f"""
--------------------------------------------
|                  Notes                   
|                                         
| {note}                
|                                          
--------------------------------------------
                  """)
                    input("Press enter to continue")
            elif action == 3:
                print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                break
            else:
                print("""
--------------------------------------------
|            Unknown command!!             |
--------------------------------------------
                  """)
                input("Press enter to continue!!")
                #notes
                
                
class lockscreen:
    def setup(self):
        while True:
            wall10 = "hi"
            wall9 = "hi"
            wall8 = "hi"
            wall7 = "hi"
            wall6 = "hi"
            wall5 = "hi"
            wall4 = "hi"
            wall3 ="hi"
            wall2 = "hi"
            wall = "hi"
            wall11 = "hi"
            print("""
--------------------------------------------
|                Lockscreen                |
|                                          |
| Type your code!!                         |
|                                          |
| Type home to close this window.          |
--------------------------------------------
                  """)
            code = input("Choose a code!!\nType home to go back to home")
            if code == "home":
                print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                break
            else:
                wall = code
                wall2 = code
                wall3 = code
                wall4 = code
                wall5 = code
                wall6 = code
                wall7 = code
                wall8 = code
                wall9 = code
                wall10 = code
                wall11 = code
                #print
                while True:
                    print("""
--------------------------------------------
|                Lockscreen                |
|                                          |
| Type your code to unlock                 |  
|                                          |
|                                          |
--------------------------------------------
                  """)
                    unlock = input("Type your code!!")
                    if unlock == code:
                        
                
                        if unlock == wall:
                            if unlock == wall2:
                                if code == wall3:
                                    if unlock == wall4:
                                        if unlock == wall5:
                                            if unlock == wall6:
                                                if unlock == wall7:
                                                    if unlock == wall8:
                                                        if unlock == wall9:
                                                            if unlock == wall10:
                                                                if unlock == wall11:
                                                                    print("Unlocked")
                                                                    print("""
--------------------------------------------
|                 Unlocked                 |
--------------------------------------------
                  """)
                                                                    input("Press enter to continue!!")
                                                                    print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                                                                    break
                                                                
                                                                else:
                                                                    print("Hack detected, code reseted!!")
                                                                    print("""
-----------------------------------------------------
|A hack was detected,the lockscreen code was reseted|
-----------------------------------------------------
                  """)
                                                                    input("Press enter to continue!!")
                                                                    code = wall10
                                                                
                                                            else:
                                                                print("""
-----------------------------------------------------
|A hack was detected,the lockscreen code was reseted|
-----------------------------------------------------
                  """)
                                                                input("Press enter to continue!!")
                                                                code = wall11
                                                            
                                                        else:
                                                            print("""
-----------------------------------------------------
|A hack was detected,the lockscreen code was reseted|
-----------------------------------------------------
                  """)
                                                            input("Press enter to continue!!")
                                                            code = wall11
                                                        
                                                    else:
                                                        print("""
-----------------------------------------------------
|A hack was detected,the lockscreen code was reseted|
-----------------------------------------------------
                  """)
                                                        input("Press enter to continue!!")
                                                        code = wall11
                                                    
                                                else:
                                                    print("""
-----------------------------------------------------
|A hack was detected,the lockscreen code was reseted|
-----------------------------------------------------
                  """)
                                                    input("Press enter to continue!!")
                                                    code = wall11
                                                
                                            else:
                                                print("""
-----------------------------------------------------
|A hack was detected,the lockscreen code was reseted|
-----------------------------------------------------
                  """)
                                                input("Press enter to continue!!")
                                                
                                            
                                        else:
                                            print("""
-----------------------------------------------------
|A hack was detected,the lockscreen code was reseted|
-----------------------------------------------------
                  """)
                                            input("Press enter to continue!!")
                                            code = wall11
                                    
                                else:
                                    print("""
-----------------------------------------------------
|A hack was detected,the lockscreen code was reseted|
-----------------------------------------------------
                  """)
                                    input("Press enter to continue!!")
                                    code = wall11
                                
                            else:
                                print("""
-----------------------------------------------------
|A hack was detected,the lockscreen code was reseted|
-----------------------------------------------------
                  """)
                                input("Press enter to continue!!")
                                code = wall11
                                
                            
                        else:
                            print("""
-----------------------------------------------------
|A hack was detected,the lockscreen code was reseted|
-----------------------------------------------------
                  """)
                            input("Press enter to continue!!")
                            code = wall11
                        
                        
                    else:
                        print("""
--------------------------------------------
|               Wrong code!!               |
--------------------------------------------
                  """)
                        input("Press enter to continue!!")
                        
                        #lockscreen
                        
                        
                        
class sports:
    def setup(self):
        while True:
            print("""
--------------------------------------------
|                  Sports                  |
|                                          |
| 1: hiking                                |
| 2: cycling                               |
| 3: walking                               |
| 4: soccer                                |
| 5: home                                  |
|                                          |     
--------------------------------------------
                  """)
            sportscmd = int(input("Type here!!"))
            if sportscmd ==-546775547574745:
                print("You can type: hiking, cycling, walking, soccer, help, home")
            elif sportscmd == 1:

                print("""
------------------------------------------------------
|                  Sports                            |
|                                                    |
| Walk a long time and enjoy the nature and have fun.|
|                                                    |    
------------------------------------------------------
                  """)
                input("Press enter to continue!!")
                
            elif sportscmd == 2:
                
                print("""
------------------------------------------------
|                  Sports                      |
|                                              |
| Go to your bikecycle and go out and ride it. |
|                                              |    
------------------------------------------------
                  """)
                input("Press enter to continue")
                
            elif sportscmd == 3:
                
                print("""
----------------------------------------------------------
|                  Sports                                |
|                                                        |
| Go out and walk fast for 10-15 min to make good sport. |
|                                                        |    
----------------------------------------------------------
                  """)
                input("Press enter to continue!!")
                
            elif sportscmd == 4:
                
                print("""
-------------------------------------------------
|                  Sports                       |
|                                               |
| Go to an soccer place and train and have fun. |
|                                               |    
-------------------------------------------------
                  """)
                input("Press enter to continue!!")
                
                
            elif sportscmd == 5:
                print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                break
            
            else:
                print("""
--------------------------------------------
|            Unknown command!!             |
--------------------------------------------
                  """)
                input("Press enter to continue!!")
            #sports
            
                            
                            
class game:
    def setup(self):
        import random
        while True:
            number2 = random.randint(1, 10)
            print("""
---------------------------------------------------
|                    Game                         |
|                                                 |
| About which number between 1 and 10 im thinking?|
|                                                 |
| Type 11 to close this app!!                     |    
---------------------------------------------------
                  """)
            
            number = int(input("Type here!!)"))
            
            if number == 11:
                print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                break
            else:
                if number == number2:
                    answers= ["Nice",
                              "Right",
                              "You are right:)"]
                    print("Right :)")
                    print(f"""
--------------------------------------------
| Answer:                                  
| {random.choice(answers):<42}            
|                                          
--------------------------------------------
                  """)
                    input("Type anything to continue!!")
                    
                else:
                    print("""
--------------------------------------------
| Answer:                                  
| Wrong:()            
|                                          
--------------------------------------------
                  """)
                    input("Type anything to continue!!")
                    #game
                    
                    
                    
class stresstest:
    def setup(self):
        import time
        import math
        while True:
            print("""
-------------------------------------------------------
|                Singlecore-stresstest                |
|                                                     |
| How many seconds do you want to run the stresstest!?|
|                                                     |
| Type 0 to close this app!!                          |    
-------------------------------------------------------
                  """)
            timestress = int(input("Type here!!)"))
            if timestress == 0:
                print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                break                
            
            else:
                
                try:
                    t = float(timestress)
                    
                except ValueError:
                    print("""
-------------------------------------------------------
|                Singlecore-stresstest                |
|                                                     |
| Type a number                                       |
|                                                     |    
-------------------------------------------------------
                  """)
                    continue
                
                print("Stresstest is running...")
                
                
                start =time.time()
                while time.time() - start < t:
                    math.sqrt(987654321)
                    #stresstest
                    
                    
                    
class thundercalculator:
    def setup(self):
        while True:
            print("""
----------------------------------------------------------
|                   Thundercalculator                    |
|                                                        |
| How many seconds are between the flash and the thunder?|
|                                                        |
| Type 999 to close this app!!                           |    
----------------------------------------------------------
                  """)
            second = float(input("Type here!!"))

            if second == 999:
                print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                break

            calculation = second / 3

            if calculation < 1:
                
                print("""
------------------------------------------------------------
|                   Thundercalculator                      |
|                                                          |
| Go fast to a safe place, the thunderstorm is super near!!|
|                                                          |
| Type 999 to close this app!!                             |    
------------------------------------------------------------
                  """)
                input("Type anything to continue!!")
            elif calculation <= 3:
               # print("Thunderstorm is nearly, stay inside a building!!")
               
                print("""
------------------------------------------------------------
|                   Thundercalculator                      |
|                                                          |
| Thunderstorm is nearly, stay inside a building!!         |
|                                                          |
| Type 999 to close this app!!                             |    
------------------------------------------------------------
                  """)
                input("Type anything to continue!!")
            else:
                #print("The thunderstorm isn't near.")
                
                print("""
------------------------------------------------------------
|                   Thundercalculator                      |
|                                                          |
| The thunderstorm isn't near.                             |
|                                                          |
| Type 999 to close this app!!                             |    
------------------------------------------------------------
                  """)
                input("Type anything to continue!!")
                
                
                #thundercalculator
      
                                   
                
                    
            
                
            


#OS

class DeSyseng:
    def __init__(self, name, complete, mode):
        self.name = name
        self.complete = complete
        self.mode = mode

    def setup(self):
        print("""
 -----------------------------------------
 |                                       |
 |                                       |
 |       Welcome in D.eSystem 4          |
 |     type anything to continue!!       |
 |                                       |
 |                                       |
 -----------------------------------------
 """)             

        if self.complete == 1:
            while True:

                
                # base mode 
                if self.mode == 1:
                    cmd = input("Type here!!: ")
                    if isinstance(cmd, int):
                        command = int(cmd)
                        
                    else:
                        command = -1
                
                    print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: game                             |
| 12: stresstest                       |
| 13:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")

                    if command == 0:
                        print("Commands: help, calculator, shutdown, news, max, clock, d.esys version\ncalendar, notes, lockscreen,sports, game, thunder, stresstest")

                    elif command == 1:
                        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|            Shutting down...           | 
|                                       |
|                                       |
|                                       |                                      
|                                       |
-----------------------------------------
""")
                        time.sleep(3)
                        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|                                       | 
|                                       |
|                                       |
|                                       |                                      
|                                       |
-----------------------------------------
""")
                        break

                    elif command == 2:
                        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|              Calculator               | 
|                                       |
|                                       |
|                                       |                                      
|                                       |
-----------------------------------------
""")
                        self.mode = 2
                    elif command == 3:
                        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|                D.News                 | 
|                                       |
|                                       |
|                                       |                                      
|                                       |
-----------------------------------------
""")
                        self.mode = 3
                    elif command == 4:
                        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|                 Max                   | 
|                                       |
|                                       |
|                                       |                                      
|                                       |
-----------------------------------------
""")
                        self.mode = 4
                    elif command == 5:
                        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|               Clock                   | 
|                                       |
|                                       |
|                                       |                                      
|                                       |
-----------------------------------------
""")
                        self.mode = 5
                    elif command == 6:
                        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|               calendar                | 
|                                       |
|                                       |
|                                       |                                      
|                                       |
-----------------------------------------
""")
                        self.mode = 6
                    elif command == 7:
                        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|             D.eSystem                 | 
|              version                  |
|                                       |
|                                       |                                      
|                                       |
|                                       |   
-----------------------------------------
""")
                        self.mode = 7
                    elif command == 8:
                        print("""
----------------------------------------
|                                      |
|                                      |
|                                      |
|                                      |
|                D.Note                | 
|                                      |
|                                      |
|                                      |                                      
|                                      |
----------------------------------------
""")
                        self.mode = 8
                    elif command == 9:
                        print("""
----------------------------------------
|                                      |
|                                      |
|                                      |
|                                      |
|              lockscreen              | 
|                                      |
|                                      |
|                                      |                                      
|                                      |
----------------------------------------
""")
                        self.mode = 9
                    elif command == 10:
                        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|              sports                   | 
|                                       |
|                                       |
|                                       |                                      
|                                       |
-----------------------------------------
""")
                        self.mode = 10
                    elif command == 11:
                        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|                 game                  | 
|                                       |
|                                       |
|                                       |                                      
|                                       |
-----------------------------------------
""")
                        self.mode = 11
                    elif command == 12:
                        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|         singlecore stresstest         | 
|                                       |
|                                       |
|                                       |                                      
|                                       |
-----------------------------------------
""")
                        self.mode = 12
                    elif command == 13:
                        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|           thundercalculator           | 
|                                       |
|                                       |
|                                       |                                      
|                                       |
-----------------------------------------
""")
                        self.mode = 13
                        
                        
                    else:
                        print("""
----------------------------------------
| 1: shutdown                          |
| 2: calculator                        |
| 3: news                              |
| 4: max                               |
| 5: clock                             |
| 6: calendar                          |
| 7: D.eSystem version                 |
| 8: D.Note                            |
| 9: lockscreen                        |
| 10: sports                           |
| 11: stresstest                       |
| 12:thundercalculator                 |
|                                      |
|                                      |
----------------------------------------
""")
                        #D.eCore 3.0
                        

                # open calculator

                elif self.mode == 2:
                    Calculator().setup()
                    self.mode = 1   # home
                    
                elif self.mode == 3:
                    news().setup()
                    self.mode = 1 #home
                    
                elif self.mode == 4:
                    Max().setup()
                    self.mode = 1 #home
                    
                elif self.mode == 5:
                    clock().setup()
                    self.mode = 1 # home
                    
                elif self.mode == 6:
                    calendar().setup()
                    self.mode = 1 # home
                    
                elif self.mode == 7:
                    desysversion().setup()
                    self.mode = 1 #home
                    
                elif self.mode == 8:
                    notes().setup()
                    self.mode = 1 #home
                elif self.mode == 9:
                    lockscreen().setup()
                    self.mode = 1 #home
                elif self.mode == 10:
                    sports().setup()
                    self.mode = 1 #home
                elif self.mode == 11:
                    game().setup()
                    self.mode = 1 #home
                elif self.mode == 12:
                    stresstest().setup()
                    self.mode = 1 #home
                elif self.mode == 13:
                    thundercalculator().setup()
                    self.mode = 1 #home
                    
                    
                    
            


#D.eSys setup

class Person:
    import random
    def __init__(self, name):
        self.name = name

    def setup(self):
        import time
        import random
        self.mode = 0
        self.complete = 0

        time.sleep(1)
        print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|                                       |
|              Welcome                  |
|                in                     |
|            D.eSystem 4                |
|                                       |                                      
|                                       |
-----------------------------------------
""")

        language = input("Welcome in D.eSystem!!\nYou can type later commands in the shell to use D.eSystem!!\npress enter to continue!!: ")

        if language == "english":
            print("""
-----------------------------------------
|                                       |
|                                       |
|                                       |
|    Welcome in D.eSystem setup!!       |
|                                       |
|                                       |                                      
|                                       |
-----------------------------------------
""")
        elif language == "german":
            print("Sie haben Deutsch ausgewählt.")
        else:
            print("Welcome in D.eSystem setup")
            language = "english"

        input("Press Enter to continue setup...")

        self.mode = 1
        self.complete = 1
        self.language = language


#boot

p = Person("D.eSystem setup")
p.setup()

os = DeSyseng("D.eSystem", p.complete, p.mode)
os.setup()