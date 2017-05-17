#Hisham Galib
#ComputerProgrammingCSA
#Idontevenknowwhatthedatewas

#Don't try to rush this game please.
import random
import time

class Innocent:
   def __init__(self):
       self.civilians=x
       
       
class Suspect:
   def __init__(self):
       self.suspect=m


class Killer:
   def __init__(self):
       self.killer=z 

d1 =['Kristle','Ariana','Huey','Mose','Ciara','Sherryl','Francina','Jeri','Armanda','Azzie','Luana','Natalia','Dyan','Charlette','Kendra','Antony','Sirena','Stacy','Williemae','Loyd','Lora','Adrianna','Florence','Amira','Marquetta','Marybeth','Marielle','Jaclyn','Crista','Alexa','Chaya','Carri','Burma','Gwenda','Charissa' ,'Sharda','Oda','Janina','Dawn','Kimberli','Foxtrot','Juliet','Romeo','Totti','Kenny','Lee','Luke','Johnny','Clint','June']
z = random.choice(d1)
d1.remove(z)
z=(z.lower())

def menu():
   try:
      gamestart = float(input(''' ENTER 1 to Start game
 ENTER 2 to quit
 ENTER 3 for credits '''))
      if gamestart == 1:
         input(''' Welcome to Murder Mystery;
 in this game you are the sheriff
 (press ENTER to continue) ''')
      elif gamestart == 2:
         quit()
      elif gamestart == 3:
         input('''Game created and programmed by Hisham Galib.
            Programmed using Python 3.
            used IDLE Python to make program
            Murder game similar to Mafia concept
            (PRESS ENTER TO CONTINUE)
            ''')
         menu()
      else:
         input("Please enter a valid number that corresponds with the choices.")
         menu()
   except:
      input("Invalid input, please enter a number that corresponds with the menu choices (Press ENTER to continue).")
      menu()
menu()

s=input("What is your name (Please enter a legitimate name for a sheriff)?")
h=input("In this game, you will be known as Sheriff " + s + ".")
e = ("Sheriff " + s)



#LOOPHIGH

profile=['has a criminal record','has custody of multiple weapons','has a bad personality and attitude(fights w/neighbours&family)','was near the area during the time of the murders']
ev=open('evid.txt','r')
cc=ev.read()

def dead():
   global e
   print("During the night the killer finished off everyone...")
   time.sleep(5)
   print("..........")
   time.sleep(2)
   print("...and killed you " + e + ".")
   time.sleep(2)
   print("GAME OVER")
   time.sleep(3)
   quit()
   
def cgi():
   global d1
   global e
   c=len(d1)
   c=(str(c))
   print("There are " + c + " that survived.")
   print("Here are the people that survived:")
   time.sleep(3)
   print(d1)
   input("Well done! " + e + ", you saved your town.")
   quit()

def arsenal():
   global d1
   print("Your Suspects are",i1,i5,i6,z,i2,i3,i4,i7)
   y=input("who do you choose to shoot?")
   if y == i1:
      print("You shot " + i1 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      dead()
   elif y == i2:
      print("You shot " + i2 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      dead()
   elif y == i3:
      print("You shot " + i3 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      dead()
   elif y == i4:
      print("You shot " + i4 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      dead()
   elif y == i5:
      print("You shot " + i5 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      dead()
   elif y == i6:
      print("You shot " + i6 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      dead()
   elif y == i7:
      print("You shot " + i7 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      dead()
   elif y == z:
      d1.append(i1)
      d1.append(i2)
      d1.append(i3)
      d1.append(i4)
      d1.append(i5)
      d1.append(i6)
      d1.append(i7)
      print("The killer was " + z + "! You shot him!")
      time.sleep(2)
      cgi()
   else:
      input("Make sure you type in one of the names of the suspects.")
      arsenal()

def hamroll():
   global profile
   print("Your Suspects are",i6,i1,i5,i2,z,i3,i4)
   time.sleep(.5)
   input("They were brought in only for risen suspicion by the rest of the witnesses.")
   print("You are forced to shoot one of the suspects, " + e + ".")

   time.sleep(2)
   arsenal()

def yolo():
    global nesta
    print("Remember, your witnesses are",ww1,ww2,ww3,ww4,ww5,ww6)
    j=random.choice(nesta)
    u=str(input("[YOU ONLY GET TO CHOOSE ONCE] CHOOSE one of the witnesses for their clues [make sure it is lowercase]"))
    if u == j:
        input("You found an important clue")
        print(z,cc)
        time.sleep(2)
        input("Now we go to the trial with the suspects....")
        hamroll()
    else:
        print("No problem here(you didn't find a significant clue).")
        time.sleep(1)
        hamroll()

def milan():
    try:
        y=float(input("Would you like to talk to more witnesses?[Enter 1] or would you like to search one of their witnessed clues?[Enter 2]?"))
        if y == 1:
            horse()
        elif y == 2:
            yolo()
        else:
            input("Make sure you type in the correct number for this question.")
            milan()
    except ValueError:
        input("Make sure you type in a number that matches the choices/n")
        milan()
      
def horse():
   global d1
   j=random.choice(suspect)
   print("Your witnesses are" ,i1,i2,i3,i4,i5,i6,i7)
   x=input("Type in a name of any of the witnesses that you want to talk to")
   if x == i1:
      print(e +", I think it was "+ j +"!")
      time.sleep(1)
      milan()
   elif x == i2:
      print(e +", I think it was "+ j +"!")
      time.sleep(1)
      milan()
   elif x == i3:
      print(e +", I think it was "+ j +"!")
      time.sleep(1)
      milan()
   elif x == i4:
      print(e +", I think it was "+ j +"!")
      time.sleep(1)
      milan()
   elif x == i5:
      print(e +", I think it was "+ j +"!")
      time.sleep(1)
      milan()
   elif x == i6:
      print(e +", I think it was "+ j +"!")
      time.sleep(1)
      milan()
   else:
      print("Make sure you type in the correct name(in lowercase)")
      horse()

c1=random.choice(d1)
d1.remove(c1)
c2=random.choice(d1)
d1.remove(c2)
c3=random.choice(d1)
d1.remove(c3)
c4=random.choice(d1)
d1.remove(c4)
c5=random.choice(d1)
d1.remove(c5)
c6=random.choice(d1)
d1.remove(c6)
c6=(c6.lower())
c1=(c1.lower())
c2=(c2.lower())
c3=(c3.lower())
c4=(c4.lower())
c5=(c5.lower())
suspect = [c1,c2,c3,c4,z,c5,c6]
i1=random.choice(d1)
d1.remove(i1)
i2=random.choice(d1)
d1.remove(i2)
i3=random.choice(d1)
d1.remove(i3)
i4=random.choice(d1)
d1.remove(i4)
i5=random.choice(d1)
d1.remove(i5)
i6=random.choice(d1)
d1.remove(i6)
i7=random.choice(d1)
d1.remove(i7)
d1.append(i1)
d1.append(i2)
d1.append(i3)
d1.append(i4)
d1.append(i6)
d1.append(i5)
i1=(i1.lower())
i2=(i2.lower())
i3=(i3.lower())
i4=(i4.lower())
i5=(i5.lower())
i6=(i6.lower())
i7=(i7.lower())
nesta=[i1,i2,i3,i4,i5,i6,i7]

def day3():
   global o
   global d1
   input("During the night, a tuesday massacre takes place....")
   time.sleep(.5)
   for x in d1[o]:
      x=random.choice(d1)
      d1.remove(x)
      input(x + " was murdered.")
   time.sleep(.5)
   input("DAY 3")
   time.sleep(.5)
   c=len(d1)
   c=(str(c))
   print("There are " + c + " people left.")
   horse()

def cg():
   global d1
   global e
   c=len(d1)
   c=(str(c))
   print("There are " + c + " that survived.")
   print("Here are the people that survived:")
   time.sleep(1)
   print(d1)
   input("Well done! " + e + ", you saved your town.")
   quit()

def blud():
   global d1
   print("Your Suspects are",ss1,ss5,ss6,z,ss2,ss3,ss4)
   time.sleep(1)
   y=input("who do you choose to shoot?")
   if y == ss1:
      d1.append(ss2)
      d1.append(ss3)
      d1.append(ss4)
      d1.append(ss5)
      d1.append(ss6)
      print("You shot " + ss1 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      day3()
   elif y == ss2:
      d1.append(ss1)
      d1.append(ss3)
      d1.append(ss4)
      d1.append(ss5)
      d1.append(ss6)
      print("You shot " + ss2 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      day3()
   elif y == ss3:
      d1.append(ss1)
      d1.append(ss2)
      d1.append(ss5)
      d1.append(ss4)
      d1.append(ss6)
      print("You shot " + ss3 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      day3()
   elif y == ss4:
      d1.append(ss1)
      d1.append(ss3)
      d1.append(ss2)
      d1.append(ss5)
      d1.append(ss6)
      print("You shot " + ss4 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      day3()
   elif y == ss5:
      d1.append(ss1)
      d1.append(ss3)
      d1.append(ss4)
      d1.append(ss2)
      d1.append(ss6)
      print("You shot " + ss5 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      day3()
   elif y == ss6:
      d1.append(ss1)
      d1.append(ss3)
      d1.append(ss4)
      d1.append(ss5)
      d1.append(ss2)
      print("You shot " + ss6 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      day3()
   elif y == z:
      d1.append(ss1)
      d1.append(ss2)
      d1.append(ss3)
      d1.append(ss4)
      d1.append(ss5)
      d1.append(ss6)
      print("The killer was " + z + "! You shot him!")
      time.sleep(2)
      cg()
   else:
      input("Make sure you type in one of the names of the suspects.")
      blud()

def fam():
   global profile
   print("Your Suspects are",ss6,ss1,ss5,ss2,z,ss3,ss4)
   time.sleep(.5)
   input("Here is the evidence brought in for the suspects who are at this trial for the murders.")
   print(ss1,random.choice(profile))
   time.sleep(1)
   print(ss2,random.choice(profile))
   time.sleep(1)
   print(z,random.choice(profile))
   time.sleep(1)
   print(ss3,random.choice(profile))
   time.sleep(1)
   print(ss4,random.choice(profile))
   time.sleep(1)
   print(ss1,random.choice(profile))
   time.sleep(1)
   print(ss5,random.choice(profile))
   time.sleep(1)
   print(ss6,random.choice(profile))
   time.sleep(1)
   print("You are forced to shoot one of the suspects, " + e + ".")
   time.sleep(2)
   blud()

def yo():
    global ness
    print("Remember, your witnesses are",ww1,ww2,ww3,ww4,ww5,ww6)
    j=random.choice(ness)
    u=str(input("[YOU ONLY GET TO CHOOSE ONCE] CHOOSE one of the witnesses for their clues [make sure it is lowercase]"))
    if u == j:
        input("You found an important clue")
        print(z,cc)
        time.sleep(2)
        input("Now we go to the trial with the suspects....")
        fam()
    else:
        print("No problem here(you didn't find a significant clue).")
        time.sleep(1)
        fam()
        
def sup3():
    try:
        y=float(input("Would you like to talk to more witnesses?[Enter 1] or would you like to search one of their witnessed clues?[Enter 2]?"))
        if y == 1:
            trial2()
        elif y == 2:
            yo()
        else:
            input("Make sure you type in the correct number for this question.")
            sup3()
    except ValueError:
        input("Make sure you type in a number that matches the choices/n")
        sup3()

def trial2():
   global d1
   j=random.choice(suspect)
   print("Your witnesses are" ,ww1,ww2,ww3,ww4,ww5,ww6)
   x=input("Type in a name of any of the witnesses that you want to talk to")
   if x == ww1:
      print(e +", I think it was "+ j +"!")
      time.sleep(1)
      sup3()
   elif x == ww2:
      print(e +", I think it was "+ j +"!")
      time.sleep(1)
      sup3()
   elif x == ww3:
      print(e +", I think it was "+ j +"!")
      time.sleep(1)
      sup3()
   elif x == ww4:
      print(e +", I think it was "+ j +"!")
      time.sleep(1)
      sup3()
   elif x == ww5:
      print(e +", I think it was "+ j +"!")
      time.sleep(1)
      sup3()
   elif x == ww6:
      print(e +", I think it was "+ j +"!")
      time.sleep(1)
      sup3()
   else:
      print("Make sure you type in the correct name(in lowercase)")
      trial2()
   
ss1=random.choice(d1)
d1.remove(ss1)
ss2=random.choice(d1)
d1.remove(ss2)
ss3=random.choice(d1)
d1.remove(ss3)
ss4=random.choice(d1)
d1.remove(ss4)
ss5=random.choice(d1)
d1.remove(ss5)
ss6=random.choice(d1)
d1.remove(ss6)
ss6=(ss1.lower())
ss1=(ss1.lower())
ss2=(ss2.lower())
ss3=(ss3.lower())
ss4=(ss4.lower())
ss5=(ss5.lower())
suspect = [ss1,ss2,ss3,ss4,z,ss5,ss6]
ww1=random.choice(d1)
d1.remove(ww1)
ww2=random.choice(d1)
d1.remove(ww2)
ww3=random.choice(d1)
d1.remove(ww3)
ww4=random.choice(d1)
d1.remove(ww4)
ww5=random.choice(d1)
d1.remove(ww5)
ww6=random.choice(d1)
d1.remove(ww6)
d1.append(ww1)
d1.append(ww5)
d1.append(ww2)
d1.append(ww3)
d1.append(ww4)
ww1=(ww1.lower())
ww2=(ww2.lower())
ww3=(ww3.lower())
ww4=(ww4.lower())
ww5=(ww5.lower())
ww6=(ww6.lower())
ness=[ww1,ww2,ww3,ww4,ww5,ww6]
   
def day2():
   global d1
   global o
   input("During the night, a monday massacre takes place....")
   time.sleep(.5)
   for x in d1[o]:
      x=random.choice(d1)
      d1.remove(x)
      input(x + " was murdered.")
   time.sleep(.5)
   input("DAY 2")
   time.sleep(.5)
   c=len(d1)
   c=(str(c))
   print("There are " + c + " people left.")
   input(d1)
   trial2()
   

def ck():
   global d1
   global e
   c=len(d1)
   c=(str(c))
   print("There are " + c + " that survived.")
   print("Here are the people that survived:")
   time.sleep(1)
   print(d1)
   input("Well done! " + e + ", you saved your town.")
   quit()

def shoot():
   global d1
   print("Your Suspects are",s1,z,s2,s3,s4)
   time.sleep(1)
   y=input("who do you choose to shoot?")
   if y == s1:
      d1.append(s2)
      d1.append(s3)
      d1.append(s4)
      print("You shot " + s1 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      day2()
   elif y == s2:
      d1.append(s1)
      d1.append(s3)
      d1.append(s4)
      print("You shot " + s2 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      day2()
   elif y == s3:
      d1.append(s1)
      d1.append(s2)
      d1.append(s4)
      print("You shot " + s3 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      day2()
   elif y == s4:
      d1.append(s1)
      d1.append(s2)
      d1.append(s3)
      print("You shot " + s4 + ".....")
      time.sleep(2)
      input("....but the killer is still alive.")
      day2()
   elif y == z:
      d1.append(s1)
      d1.append(s2)
      d1.append(s3)
      d1.append(s4)
      print("The killer was " + z + "! You shot him!")
      time.sleep(2)
      ck()
   else:
      input("Make sure you type in one of the names of the suspects.")
      shoot()

def trial():
   global profile
   print("Your Suspects are",s1,s2,s3,z,s4)
   time.sleep(3)
   input("Here is the evidence brought in for the suspects who are at this trial for the murders.")
   print(s1,random.choice(profile))
   time.sleep(3)
   print(s2,random.choice(profile))
   time.sleep(3)
   print(z,random.choice(profile))
   time.sleep(3)
   print(s3,random.choice(profile))
   time.sleep(3)
   print(s4,random.choice(profile))
   time.sleep(3)
   print("You are forced to shoot one of the suspects, " + e + ".")
   time.sleep(3)
   shoot()
   
def mc():
   global witness
   print("Remember, your witnesses are",w1,w2,w3,w4)
   j=random.choice(witness)
   u=str(input("[YOU ONLY GET TO CHOOSE ONCE] CHOOSE one of the witnesses for their clues [make sure it is lowercase]"))
   if u == j:
      input("You found an important clue")
      print(z,cc)
      time.sleep(3)
      input("Now we go to the trial with the suspects....")
      trial()
   else:
      print("No problem here(you didn't find a significant clue).")
      time.sleep(2)
      trial()
   
def inter():
    try:
        y=float(input("Would you like to talk to more witnesses?[Enter 1] or would you like to search one of their witnessed clues?[Enter 2]?"))
        if y == 1:
            wit()
        elif y == 2:
            mc()
        else:
            input("Make sure you type in the correct number for this question.")
            inter()
    except ValueError:
        input("Make sure you type in a number that matches the choices/n")
        inter()

def wit():
   global suspects
   global w1
   global w2
   global w3
   global w4
   w1=(w1.lower())
   w2=(w2.lower())
   w3=(w3.lower())
   w4=(w4.lower())
   j=random.choice(suspects)
   print("Your witnesses are" ,w1,w2,w3,w4)
   x=input("Type in a name of any of the witnesses that you want to talk to")
   try:
      if x == w1:
         print(e +", I think it was "+ j +"!")
         time.sleep(2)
      elif x == w2:
         print(e +", I think it was "+ j +"!")
         time.sleep(2)
      elif x == w3:
         print(e +", I think it was "+ j +"!")
         time.sleep(2)
      elif x == w4:
         print(e +", I think it was "+ j +"!")
         time.sleep(2)
      else:
         print("Make sure you type in the correct name(in lowercase)")
         time.sleep(1)
         wit()
   except ValueError:
      print("Please enter a correct name.")
      inter()
   inter()
 
s1=random.choice(d1)
d1.remove(s1)
s2=random.choice(d1)
d1.remove(s2)
s3=random.choice(d1)
d1.remove(s3)
s4=random.choice(d1)
d1.remove(s4)
s1=(s1.lower())
s2=(s2.lower())
s3=(s3.lower())
s4=(s4.lower())
suspects = [s1,s2,s3,s4,z]
w1=random.choice(d1)
d1.remove(w1)
w2=random.choice(d1)
d1.remove(w2)
w3=random.choice(d1)
d1.remove(w3)
w4=random.choice(d1)
d1.remove(w4)
d1.append(w1)
d1.append(w2)
d1.append(w3)
d1.append(w4)
w1=(w1.lower())
w2=(w2.lower())
w3=(w3.lower())
w4=(w4.lower())
witness=[w1,w2,w3,w4]


def network():
    global d1
    global w1
    global w2
    global w3
    global w4
    input("[GAME INSTRUCTIONS] Before a trial is held on who was the alleged killer behind the murders, you go to a few townspeople who tell you who they think is the killer....")
    print("Your witnesses are" ,w1,w2,w3,w4)
    wit()       
          
o=random.randrange(1,5)

def daystart():
    global o
    global d1
    input("On a dark morning, a terrible event unfolds....")
    time.sleep(2)
    for x in d1[o]:
        x=random.choice(d1)
        d1.remove(x)
        input(x + " was murdered.")
    network()
    
def jumpinto():
   input("You wake up in your town, there are 50 civilians that are currently living in your town [press ENTER to continue)")
   input("Your town is endangered by a serial killer (who has wiped out other nearby towns) is looking to wipe out your town [press ENTER to continue).")
   time.sleep(1)
   input("DAY 1")
   time.sleep(2)
   daystart()

def began():
   global e
   welcome=input("Welcome to Murder Mystery, as a town that was once peaceful is now endangered by a serial killer who plans to murder everyone. It is your job to protect and cease the killer's wrongdoings, " + e + ".")
   jumpinto()

began()
