
#! /usr/bin/python3

import re
import os
import string
import random
from functools import partial

import time
import timeit
import tqdm

import tkinter
from tkinter import *
from tkinter.ttk import *

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

from PIL import Image

#########################################################################################################################################################################
#
# Algo Statistique
#

Path = input("""Rockyou.txt Path : 
Example : /home/test/rockyou.txt OR C:\\Rockyou.txt
>>> """)

#fopen = (line for line in open('/home/nexxis/Documents/Python/rockyou.txt', 'r', encoding='utf-8', errors='replace').readlines())
#fopen = (line for line in open('/home/nexxis/Documents/Python/toooo.txt', 'r', encoding='utf-8', errors='replace').readlines())
fopen = (line for line in open(Path, 'r', encoding='utf-8', errors='replace').readlines())

count_total_lines, count_char, count_total_char, count_total_alpha, count_total_upper, count_total_lower, count_total_num, count_total_symb = 0, 0, 0, 0, 0, 0, 0, 0

symb_list = ('[@\[ \]^_!"#$%&\'()*+,-./:;{\}<>=|~?]')
#symb_list = ('!"#$%&\'()*+,-./:;<=>?@[ \]^_`{|}~')
symbols_list = list(string.punctuation)
digits_list = list(string.digits)
alpha_list = list(string.ascii_lowercase)
list_count_char = list()
list_count_letter = list()
list_count_digits = list()
list_count_symbol = list()

### Main ###
for line in tqdm.tqdm(fopen):
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
# Modifier la ligne pour pouvoir recuperer les chiffres
      list_count_digits.append(character)
      count_numeric = count_numeric + 1
      count_total_num = count_total_num + 1

    elif(re.search(symb_list,character)):
# Modifier la ligne pour pouvoir recupere les symbols
      list_count_symbol.append(character)
      count_symbol = count_symbol + 1
      count_total_symb = count_total_symb + 1

upper_stat = count_total_upper / (count_total_char - 1) * 100
lower_stat = count_total_lower / (count_total_char - 1) * 100
num_stat = count_total_num / (count_total_char - 1) * 100
symb_stat = count_total_symb / (count_total_char - 1) * 100
other_stat = 100 - (upper_stat + lower_stat + num_stat + symb_stat)

fopen.close()

print(" NO ERROR ")

#########################################################################################################################################################################

"""
# La partis en ligne de commande

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

def blankText():
    labelMessage['text']=" "
    labelMessage11['text'] = " "
    labelMessage12['text'] = " "
    labelMessage13['text'] = " "
    labelMessage21['text'] = " "
    labelMessage22['text'] = " "
    labelMessage23['text'] = " "
    labelMessage24['text'] = " "

def Delete_Text():
    labelBonjour.pack_forget()
    labelDescription.pack_forget()

def zeroTitre():
    global labelBonjour
    Titre = """Sujet 3 : Analyse statistique d’un fichier"""
    labelBonjour = tkinter.Label(mafenetre,text=Titre,font=('Arial',48))
    labelBonjour.pack(pady=10)

def zeroText():
    global labelDescription
    Text = """
On souhaite écrire un programme qui va ouvrir un fichier texte (rockyou.txt) contenant
des mots de passe à raison d’un mot de passe par ligne, et produire des statistiques sur
l’usage des caractères (majuscules, minuscules, numériques, symboles), la longueur
minimale, maximale et moyenne, la fréquence d’usage des lettres dans ce fichier.
    """
    labelDescription = tkinter.Label(mafenetre,text=Text,font=('Arial',28))
    labelDescription.pack(pady=10)

def one():
    i = "Smallest word:", min(list_count_char), "character(s)"
    labelMessage11['text']= i

def two():
    i = "Longest word:", max(list_count_char), "character(s)"
    labelMessage12['text']= i
 
def three():
    i = "Average word length:", round(count_total_char / count_total_lines), "character(s)"
    labelMessage13['text']= i

def four():
    i = "Uppercase only:", str(round(upper_stat, 2)), "%"
    labelMessage21['text']= i

def five():
    i = "Lowercase only:", str(round(lower_stat, 2)), "%"
    labelMessage22['text']= i

def six():
    i = "Numbers only", str(round(num_stat, 2)), "%"
    labelMessage23['text']= i

def seven():
    i = "Symbols only:", str(round(symb_stat, 2)), "%"
    labelMessage24['text']= i

def eight():
    Delete_Text()
    blankText()
    i = "Multiple character sets:", str(round(other_stat, 2)), "%"
    labelMessage['text']= i

def nine():
    Delete_Text()
    blankText()
    i = "Number of lines:", count_total_lines
    labelMessage['text']= i
    global root1
    global root2
    global root3
    root1 = tkinter.Tk()
    root1.geometry('300x800')
    for letter in alpha_list:
        for index,item in enumerate(letter):
            tkinter.Label(root1,text="Caractere : "+letter+" = "+str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1))+" %",font=('Ariel',16)).pack(pady = index+0)

    root1.title('Tableau de Caracteres')
    root1.mainloop
    root2 = tkinter.Tk()
    root2.geometry('300x310')
    for chiffre in digits_list:
        for index,item in enumerate(chiffre):
            tkinter.Label(root2,text="Caractere : "+chiffre+" = "+ str(round(list_count_digits.count(chiffre) / count_total_num * 100, 1))+" %",font=('Ariel',16)).pack(pady = index+0)

    root2.title('Tableau de Chiffres')
    root2.mainloop
    root3 = tkinter.Tk()
    root3.geometry('250x750')
    for symbols in symbols_list:
        for index,item in enumerate(symbols):
            tkinter.Label(root3,text="Caractere : "+symbols+" = "+str(round(list_count_symbol.count(symbols) / count_total_symb * 100, 1))+" %",font=('Ariel',12)).pack(pady = index+0)

    root3.title('Tableau de Symbols')
    root3.mainloop
    x = [random.randint(0,26) for i in range(1000)]
    n, bins, patches = plt.hist(x, 100, facecolor='b', alpha=0.5)
    plt.xlabel('Pourcentage')
    plt.ylabel(u'Alphabet')
    plt.axis([0, 26, 0, 100])
    plt.grid(True)
    plt.show()

def G1():
    #Upper = "Uppercase only:", str(round(upper_stat, 2)), "%"
    #Lower = "Lowercase only:", str(round(lower_stat, 2)), "%"
    #Number = "Numbers only", str(round(num_stat, 2)), "%"
    #Symbol = "Symbols only:", str(round(symb_stat, 2)), "%"
    Upper = str(round(upper_stat, 2))
    Lower = str(round(lower_stat, 2))
    Number = str(round(num_stat, 2))
    Symbol = str(round(symb_stat, 2))
    name = ['Upper', 'Lower', 'Number', 'Symbol']
    data = [Upper, Lower, Number, Symbol]
    explode=(0.05, 0.05, 0.05, 0.05)
    plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')
    plt.show()

def words():
    Delete_Text()
    blankText()
    one()
    two()
    three()

def Caracters():
    Delete_Text()
    blankText()
    four()
    five()
    six()
    seven()
    G1()

def quit():
    mafenetre.quit()     # stops mainloop
    mafenetre.destroy()  # this is necessary on Windows to prevent
                         # Fatal Python Error: PyEval_RestoreThread: NULL tstate


#
# La fenetre
#
if __name__ == '__main__':
    #time.sleep(600)
    time.sleep(10)
    mafenetre = tkinter.Tk()
    mafenetre.title('Project Python')
    mafenetre.geometry('1500x720')
    labelMessage = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage.place(x=100,y=100)
    labelMessage11 = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage11.place(x=100,y=100)
    labelMessage12 = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage12.place(x=100,y=200)
    labelMessage13 = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage13.place(x=100,y=300)
    labelMessage21 = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage21.place(x=100,y=100)
    labelMessage22 = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage22.place(x=100,y=200)
    labelMessage23 = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage23.place(x=100,y=300)
    labelMessage24 = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage24.place(x=100,y=400)
    zeroTitre()
    zeroText()

#
# Les differents button qui donne des resultats
#
boutonWord = tkinter.Button(mafenetre,text='Words',activeforeground="red",command=words)
boutonWord.place(x=200,y=650)
boutonCaracters = tkinter.Button(mafenetre,text='Caracters',activeforeground="red",command=Caracters)
boutonCaracters.place(x=400,y=650)
boutonEight = tkinter.Button(mafenetre,text='Multiple character sets',activeforeground="red",command=eight)
boutonEight.place(x=600,y=650)
boutonNine = tkinter.Button(mafenetre,text='lists',activeforeground="red",command=nine)
boutonNine.place(x=800,y=650)
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
buttonTen = tkinter.Button(mafenetre, text="Quit", activebackground="red", command=quit)

#buttonTen = tkinter.Button(master=mafenetre, image=photo, text="Quit", command=mafenetre.quit)
#buttonTen = tkinter.Button(master=mafenetre,text="Quit",command=_quit)
#buttonTen.pack(side=tkinter.BOTTOM)
#photo = mafenetre.iconphoto(False, tk.PhotoImage(file='/path/to/ico/icon.png'))
buttonTen.place(x=1440, y=10)

mafenetre.mainloop()

