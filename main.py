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
def wipe_money(color):
    dict["money"][color]["val"] = 0
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
            black = add black
            efficency = add max efficency to color mixes
            export = export the data into an
            exit = exit
            """)
    elif action == "add":
        color = input("What color would you like to add money to? ")
        amount = int(input("What amount would you like to add? "))
        add_money(color, amount)
        print("done!") 
    elif action == "level":
        color = input("What color would you like to add levels to? ")
        amount = input("What amount would you like to add? ")
        add_level(color, amount)
        print("done!") 
    elif action == "wipe":
        wipe_money(input("what color would you like to wipe? "))
    elif action == "spectrum":
        add = int(input("How many spectrums would you like to add? "))
        dict["unlocked"] = True
        dict["specced"] += add
        dict["spectrum"]["val"] = dict["specced"]
        print("done!") 
    elif action == "random":
        for i in range(len(dict["bars"]["red"]["color"])):
            dict["bars"]["red"]["color"][i] = r.randint(0,255)
        for i in range(len(dict["bars"]["green"]["color"])):
            dict["bars"]["green"]["color"][i] = r.randint(0,255)    
        for i in range(len(dict["bars"]["blue"]["color"])):
            dict["bars"]["blue"]["color"][i] = r.randint(0,255)
        if input("Would you like random width as well? (y/n) ") == "y":
            print(dict["bars"]["green"]["width"])
            dict["bars"]["green"]["width"]["val"] = r.randint(10,11)
            dict["bars"]["red"]["width"]["val"] = r.randint(10,11)
            dict["bars"]["blue"]["width"] = r.randint(10,11)
        print("done!")        
    elif action == "black":
        black = int(input("How many black would you like to add? "))
        dict["black"] += black    
    elif action == "efficency":
        dict["potencyEff"]["red"] = 0.002
        dict["potencyEff"]["green"] = 0.002
        dict["potencyEff"]["blue"] = 0.002
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
