import base64
import json
import pyperclip as pc
import random as r
raw = input("Paste yo save string here. Go to rgb idle and click export ")
d = base64.b64decode(raw)
print(str(d))
dict = json.loads(d)
print(dict["money"]["red"])
print(dict["money"]["green"])
print(dict["money"]["blue"])
def add_money(color, amount):
    dict["money"][color]["val"] += int(amount)
def add_level(color, amount):
    if color == "blue":
        dict["unlock"] = True
        for i in range(int(len(dict["level"]["blue"]))):
            dict["level"]["blue"][i] += int(amount)
    else:
        dict["level"][color] += int(amount)    
while True:
    action = input("What action would you like to preform? help for help btw ")
    if action == "help":
        print("""
            help = shows this
            add = add money
            level = add levels
            spectrum = add spectrum
            random = change the bars' colors to random values
            export = export the data into an
            exit = exit
            """)
    elif action == "add":
        color = input("What color would you like to add money to? ")
        amount = input("What amount would you like to add? ")
        add_money(color, amount)
        print("done!") 
    elif action == "level":
        color = input("What color would you like to add levels to? ")
        amount = input("What amount would you like to add? ")
        add_level(color, amount)
        print("done!") 
    elif action == "spectrum":
        add = int(input("How many spectrums would you like to add? "))
        dict["specced"] += add
        print("done!") 
    elif action == "random":
        for i in range(len(dict["bars"]["red"]["color"])):
            dict["bars"]["red"]["color"][i] = r.randint(0,255)
        for i in range(len(dict["bars"]["green"]["color"])):
            dict["bars"]["green"]["color"][i] = r.randint(0,255)    
        for i in range(len(dict["bars"]["blue"]["color"])):
            dict["bars"]["blue"]["color"][i] = r.randint(0,255)
        print("done!")        
    elif action == "exit":
        break
    elif action == "export":
        dict = json.dumps(dict)
        dict_bytes = dict.encode('ascii')
        export = base64.b64encode(dict_bytes)
        export = export.decode("utf-8") 
        try: pc.copy(export)
        except: pass
        print(export)
