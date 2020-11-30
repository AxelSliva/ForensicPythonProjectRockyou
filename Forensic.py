
#! /usr/bin/python3

import re
import os
import string
import matplotlib
from functools import partial

import tkinter
from tkinter import *
from tkinter.ttk import *

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

#from PIL import Image, ImageTk
from PIL import Image

#
# Algo des differents
#

#fopen = (line for line in open('/home/nexxis/Documents/Python/rockyou.txt', 'r', encoding='utf-8', errors='replace').readlines())
fopen = (line for line in open('/home/nexxis/Documents/Python/toooo.txt', 'r', encoding='utf-8', errors='replace').readlines())

count_total_lines, count_char, count_total_char, count_total_alpha, count_total_upper, count_total_lower, count_total_num, count_total_symb = 0, 0, 0, 0, 0, 0, 0, 0

symb_list = ('[@\[ \]^_!"#$%&\'()*+,-./:;{\}<>=|~?]')
alpha_list = list(string.ascii_lowercase)
list_count_char = list()
list_count_letter = list()

### Main ###
for line in fopen:
  count_total_lines += 1
  count_char = len(line)
  list_count_char.append(count_char)
  count_total_char += count_char
  
  count_alpha, count_upper, count_lower, count_numeric, count_symbol, count_spe = 0, 0, 0, 0, 0, 0

  for character in line:
    if(character.isalpha()):
      list_count_letter.append(character.lower()) 
      count_alpha = count_alpha + 1
      count_total_alpha = count_total_alpha + 1

      if(character.isupper()):
        count_upper = count_upper + 1
        count_total_upper = count_total_upper + 1
      else:
        count_lower = count_lower + 1
        count_total_lower = count_total_lower + 1

    elif(character.isnumeric()):
      count_numeric = count_numeric + 1
      count_total_num = count_total_num + 1

    elif(re.search(symb_list,character)):
      count_symbol = count_symbol + 1
      count_total_symb = count_total_symb + 1

upper_stat = count_total_upper / (count_total_char - 1) * 100
lower_stat = count_total_lower / (count_total_char - 1) * 100
num_stat = count_total_num / (count_total_char - 1) * 100
symb_stat = count_total_symb / (count_total_char - 1) * 100
other_stat = 100 - (upper_stat + lower_stat + num_stat + symb_stat)

fopen.close()


"""
print("\n")
print("--------------------------------------------------")
print("Passwod Length")
print("Smallest word:", min(list_count_char), "character(s)")
print("Longest word:", max(list_count_char), "character(s)")
print("Average word length:", round(count_total_char / count_total_lines), "character(s)")
print("\n")
print("Preferences in Choosing Character Sets")
print("Uppercase only:", str(round(upper_stat, 2)), "%")
print("Lowercase only:", str(round(lower_stat, 2)), "%")
print("Numbers only", str(round(num_stat, 2)), "%")
print("Symbols only:", str(round(symb_stat, 2)), "%")
print("Multiple character sets:", str(round(other_stat, 2)), "%")
print("\n")
print("Character Frequency")
for letter in alpha_list:
  print(letter,":",str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1)), "%")
print("\n")

print("--------------------------------------------------")
print("File Properties:")
print("File path:", filepath)
print("Number of lines:", count_total_lines)
print("\n")


"""



#
# fonction qui affiche les diferentes statistic
#
#def pourcentageDeCarctere(label, choices, listbox):
    # Cette function est utilise pour effectue le pourcentage des resultats d'un calcule
    #return "nombre"
    #for letter in alpha_list:
    	#print(letter,":",str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1)), "%")
    	#labelBonjour['text']= letter,":",str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1)), "%"
    #choices = choices.get()
    #text = ""
    #for index in listbox.curselection():
    #    text += choices[index] + " "

    #label.config(text = text)
    #print("\n")

def Delete_Text():
    #print("DELETE DEFAULT")
    #tex.delete('1.0', END)
    #textExample.delete("1.0","end")
    #labelBonjour.delete("1.0","end")
    labelBonjour.pack_forget()
    labelDescription.pack_forget()
    #labelOne.pack_forget()
    #labelTwo.pack_forget()
    #labelThree.pack_forget()
    #labelFour.pack_forget()
    #labelFive.pack_forget()
    #labelSix.pack_forget()
    #labelSeven.pack_forget()
    #labelEight.pack_forget()
    #labelDescription.delete("1.0","end")

def zeroTitre():
    global labelBonjour
    Titre = """Sujet 3 : Analyse statistique d’un fichier"""
    #labelBonjour = tkinter.Label(mafenetre,text='Bonjour',font=('Arial',48))
    labelBonjour = tkinter.Label(mafenetre,text=Titre,font=('Arial',48))
    #labelBonjour.pack(pady=10)
    #labelBonjour.pack(pady=10)
    #labelBonjour.place(x=75,y=75)
    labelBonjour.pack(pady=10)
    #tkinter.delete(labelBonjour)

def zeroText():
    global labelDescription
    Text = """
On souhaite écrire un programme qui va ouvrir un fichier texte (rockyou.txt) contenant
des mots de passe à raison d’un mot de passe par ligne, et produire des statistiques sur
l’usage des caractères (majuscules, minuscules, numériques, symboles), la longueur
minimale, maximale et moyenne, la fréquence d’usage des lettres dans ce fichier.
    """
    #labelDescription = tkinter.Label(mafenetre,text='Bonjour',font=('Arial',18))
    labelDescription = tkinter.Label(mafenetre,text=Text,font=('Arial',28))
    #labelDescription.pack(pady=10)
    #labelDescription.place(x=200,y=200)
    labelDescription.pack(pady=10)


def one():
    Delete_Text()
    #global labelOne
    #return "January"
    #labelBonjour['text']= 'Bonjour : January\nBonjour : one'
    #pourcentageDeCaractere()
    #labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_upper : \n\ncount_upper_total : '
    #"--------------------------------------------------"
    #"Passwod Length"
    #labelBonjour['text']= "Pourcentage de lettres majuscules:", str(round(count_upper_total / count_total_characters * 100, 2)), "%"
    #labelBonjour['text']= "Smallest word:", min(list_count_char), "character(s)"
    #  ---- ECRIRE FUNCTION POUR TOUS EFFACE EN TEXT ----
    #Delete_Text()
    i = "Smallest word:", min(list_count_char), "character(s)"# + e.get
    #labelOne = tkinter.Label(mafenetre,text= i,font=('Arial',18))
    labelMessage['text']= i
    #labelMessage['text']="Smallest word:", min(list_count_char), "character(s)"
    #e.delete(0, 'end')
    #labelOne.place(x=100,y=100)
    #labelOne.pack(pady=10)
 
def two():
    Delete_Text()
    #global labelTwo
    #labelBonjour['text']= 'Bonjour : Febreray'
    #return "February"
    #labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_lower : \n\ncount_lower_total : '
    #labelBonjour['text']= "Pourcentage de lettres minuscules:", str(round(count_lower_total / count_total_characters * 100, 2)), "%"
    #labelBonjour['text']= "Longest word:", max(list_count_char), "character(s)"
    #Delete_Text()
    i = "Longest word:", max(list_count_char), "character(s)"
    #labelTwo = tkinter.Label(mafenetre,text= i,font=('Arial',18))
    #labelTwo.place(x=100,y=100)
    #labelTwo.pack(pady=10)
    labelMessage['text']= i
 
def three():
    Delete_Text()
    #global labelThree
    #labelBonjour['text']= 'Bonjour : March'
    #return "March"
    #labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_numeric : \n\ncount_numeric_total : '
    #labelBonjour['text']= "Pourcentage de numériques:", str(round(count_numeric_total / count_total_characters * 100, 2)), "%"
    #labelBonjour['text']= "Average word length:", round(count_total_char / count_total_lines), "character(s)"
    #Delete_Text()
    i = "Average word length:", round(count_total_char / count_total_lines), "character(s)"
    #labelThree = tkinter.Label(mafenetre,text= i,font=('Arial',18))
    #labelThree.place(x=100,y=100)
    #labelThree.pack(pady=10)
    labelMessage['text']= i

def four():
    Delete_Text()
    #global labelFour
    #labelBonjour['text']= 'Bonjour : April'
    #return "April"
    #labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_symbol : \n\ncount_symbol_total : '
    #labelBonjour['text']= "Pourcentage de symboles:", str(round(count_symbol_total / count_total_characters * 100, 2)), "%"
    #labelBonjour['text']= "Uppercase only:", str(round(upper_stat, 2)), "%"
    #Delete_Text()
    i = "Uppercase only:", str(round(upper_stat, 2)), "%"
    #labelFour = tkinter.Label(mafenetre,text= i,font=('Arial',18))
    #labelFour.place(x=100,y=100)
    #labelFour.pack(pady=10)
    labelMessage['text']= i

def five():
    Delete_Text()
    #global labelFive
    #labelBonjour['text']= 'Bonjour : Mary'
    #return "May"
    #labelBonjour['text']= 'number of lines : \n\nLongueur Maximale de la ligne trouve dans le fichier : \n\n'
    #labelBonjour['text']= "Nombre max de caractères:", max(List1), "caractères"
    #labelBonjour['text']= "Lowercase only:", str(round(lower_stat, 2)), "%"
    #Delete_Text()
    i = "Lowercase only:", str(round(lower_stat, 2)), "%"
    #labelFive = tkinter.Label(mafenetre,text= i,font=('Arial',18))
    #labelFive.place(x=100,y=100)
    #labelFive.pack(pady=10)
    labelMessage['text']= i

def six():
    Delete_Text()
    #global labelSix
    #labelBonjour['text']= 'Bonjour : June'
    #return "June"
    #labelBonjour['text']= 'number of lines : \n\nLongueur Minimale de la ligne trouve dans le fichier : \n\n'
    #labelBonjour['text']= "Nombre min de caractères:", min(List1), "caractères"
    #labelBonjour['text']= "Numbers only", str(round(num_stat, 2)), "%"
    #Delete_Text()
    i = "Numbers only", str(round(num_stat, 2)), "%"
    #labelSix = tkinter.Label(mafenetre,text= i,font=('Arial',18))
    #labelSix.place(x=100,y=100)
    #labelSix.pack(pady=10)
    labelMessage['text']= i

def seven():
    Delete_Text()
    #global labelSeven
    #labelBonjour['text']= 'number of lines : \n\nLongueur Moyenne de la ligne trouve dans le fichier : \n\n'
    #labelBonjour['text']= "Pourcentage de lettres:", str(round(count_alpha_total / count_total_characters * 100, 2)), "%"
    #labelBonjour['text']= "Symbols only:", str(round(symb_stat, 2)), "%"
    #Delete_Text()
    i = "Symbols only:", str(round(symb_stat, 2)), "%"
    #labelSeven = tkinter.Label(mafenetre,text= i,font=('Arial',18))
    #labelSeven.place(x=100,y=100)
    #labelSeven.pack(pady=10)
    labelMessage['text']= i

def eight():
    Delete_Text()
    #global labelEight
    #labelBonjour['text']= 'number of lines : \n\nfrequence des lettres utilise par ligne dans le fichier : \n\n'
    #labelBonjour['text']= "Nombre moyen de caractères:", round(count_total_characters / number_of_lines), "caractères"
    #labelBonjour['text']= "Multiple character sets:", str(round(other_stat, 2)), "%"
    #Delete_Text()
    i = "Multiple character sets:", str(round(other_stat, 2)), "%"
    #labelEight = tkinter.Label(mafenetre,text= i,font=('Arial',18))
    #labelEight.place(x=100,y=100)
    #labelEight.pack(pady=10)
    labelMessage['text']= i

def nine():
    Delete_Text()
    # Cette function est utilise pour effectue le pourcentage des resultats d'un calcule
    #return "nombre"
    root = tkinter.Tk()
    root.geometry('300x800')
 #   scrollbar = Scrollbar(root)
#    scrollbar.pack(side = RIGHT, fill = Y)

 #   myList = Listbox(root, yscrollcommand = scrollbar.set)

    for letter in alpha_list:
    	#print(letter,":",str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1)), "%")
    	#labelBonjour['text']= letter,":",str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1)), "%"
        # Affiche dams le Terminale le pourcentage de chaque caracteres
  #      print(letter,":",str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1)), "%")
        #print(len(letter,":",str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1)), "%"))
        #text = []
   #     i = letter,":",str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1)), "%"
  #      print(i)
#        str1 = ''.join(str(e) for e in i)
 #       print(str1)
        #i = (letter + ":" + str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1)) + "%")
        #i += text

#        myList.insert(END, 'caracteres: ' + i)

        #for i in range(0,26):
        #    labelRoot = Label(root,text=(i),bg='white',font=('Arial',12))

     #for i in range(0,30):
        #    labelRoot = Label(root,text=(i),bg='white',font=('Arial',12))

        #i.replace(" ", "")



        #print(i)


        for index,item in enumerate(letter):
            #i.replace(" ", "_")
            #for index in range(0,26):
            #tkinter.Label(root,text=f'caracteres: {item}').pack(pady = index+0)
            tkinter.Label(root,text="Caractere : "+letter+" = "+str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1))+" %",font=('Ariel',16)).pack(pady = index+0)

        #labelRoot = Label(root,text=(letter,":",str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1)), "%"),bg='white',font=('Arial',12))
        #labelRoot = Label(root,text=("\n"))

    #print("\n")
#    print(text)
   # myList.pack( side = LEFT, fill = BOTH )
  #  scrollbar.config(command = myList.yview)
#    labelRoot = Label(root,text=("\n"),bg='white',font=('Arial',12))
#    labelRoot = Label(root,text=(i),bg='white',font=('Arial',12))
    #labelRoot.place(x=50,y=50)
        # Create while loop
        #listcaractere = 0
        #choices = Variable(root, i.readlines())
        #listbox = Listbox(root, listvariable=choices, selectmode="multiple")
        #label = Label(root, text = '')
        #button = Button(root, text='Ok', command=partial(pourcentageDeCarctere, label, choices,listbox))
    #choices = Variable(root, ('P2r-866', 'PJ2-445', 'P3X-974'))
    #listbox.insert('end', 'P3X-972','P3X-888')
    #button = Button(root, text='Ok', command=partial(pourcentageDeCarctere, label, choices,listbox))
    #listbox.grid(row=0, column=0)
    #button.grid(row=1, column=0)
    #label.grid(row=2, column=0)
    root.title('Tableau de caracteres')
    root.mainloop

def _quit():
    mafenetre.quit()     # stops mainloop
    mafenetre.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


#
# La fenetre
#
if __name__ == '__main__':
    mafenetre = tkinter.Tk()
mafenetre.title('Project Python')
mafenetre.geometry('1800x720')

labelMessage = tkinter.Label(mafenetre,font=('Ariel',48))
labelMessage.place(x=100,y=100)
zeroTitre()
zeroText()

#
# Les differents button qui donne des resultats
#
boutonOne = tkinter.Button(mafenetre,text='Smallest word',activeforeground="red",command=one)
boutonOne.place(x=50,y=650)
boutonTwo = tkinter.Button(mafenetre,text='Longest word',activeforeground="red",command=two)
boutonTwo.place(x=200,y=650)
boutonThree = tkinter.Button(mafenetre,text='Average word length',activeforeground="red",command=three)
boutonThree.place(x=350,y=650)
boutonFour = tkinter.Button(mafenetre,text='Uppercase only',activeforeground="red",command=four)
boutonFour.place(x=500,y=650)
boutonFive = tkinter.Button(mafenetre,text='Lowercase only',activeforeground="red",command=five)
boutonFive.place(x=650,y=650)
boutonSix = tkinter.Button(mafenetre,text='Numbers only',activeforeground="red",command=six)
boutonSix.place(x=800,y=650)
boutonSeven = tkinter.Button(mafenetre,text='Symbols only',activeforeground="red",command=seven)
boutonSeven.place(x=950,y=650)
boutonEight = tkinter.Button(mafenetre,text='Multiple character sets',activeforeground="red",command=eight)
boutonEight.place(x=1100,y=650)
boutonNine = tkinter.Button(mafenetre,text='list Caracteres',activeforeground="red",command=nine)
boutonNine.place(x=1250,y=650)

#load = Image.open("/home/nexxis/Documents/Python/ForensicPythonProjectRockyou/icon_poweroff.jpg")
#photo = ImageTk.PhotoImage(load)
#photo = Tk.PhotoImage(file = r"/home/nexxis/Documents/Python/ForensicPythonProjectRockyou/icon_poweroff.jpg")
#root.iconphoto(False, tk.PhotoImage(file='/path/to/ico/icon.png'))
#mafenetre.iconphoto(False, tkinter.PhotoImage(file='/home/nexxis/Documents/Python/ForensicPythonProjectRockyou/icon_poweroff.jpg'))
#photo = tkinter.PhotoImage(file='/home/nexxis/Documents/Python/ForensicPythonProjectRockyou/icon_poweroff.jpg')
#photo = tkinter.PhotoImage(file='icon_poweroff.jpg')
#photo = ImageTk.PhotoImage(Image.open('icon_poweroff.jpg'))

photo = Image.open("icon_poweroff.jpg")

#boutonTen = tkinter.Button(mafenetre, text="Quit", activebackground="red", command=mafenetre.quit)
#boutonTen.place(x=1400,y=650)

#buttonTen = tkinter.Button(mafenetre, image=photo, text="Quit", command=_quit)
buttonTen = tkinter.Button(mafenetre, text="Quit", activebackground="red", command=_quit)

#buttonTen = tkinter.Button(master=mafenetre, image=photo, text="Quit", command=mafenetre.quit)
#buttonTen = tkinter.Button(master=mafenetre,text="Quit",command=_quit)
#buttonTen.pack(side=tkinter.BOTTOM)
#photo = mafenetre.iconphoto(False, tk.PhotoImage(file='/path/to/ico/icon.png'))
buttonTen.place(x=1740,y=10)

mafenetre.mainloop()

"""
===============
Embedding in Tk
===============

import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.
"""

