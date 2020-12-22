
#! /usr/bin/python3.8

# Les différentes librairies utilisés.
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
# Algo qui effectue des calcules sur le fichier Rockyou.txt et permet d’obtenir des statistiques.  
#

def Algo_Statistique():

    # Permet de rendre les variables lisibles par toutes les fonctions du script.
    global count_total_lines
    global count_char
    global count_total_char
    global count_total_alpha
    global count_total_upper
    global count_total_lower
    global count_total_num
    global count_total_symb
    global symb_list
    global symbols_list
    global digits_list
    global alpha_list
    global list_count_char
    global list_count_letter
    global list_count_digits
    global list_count_symbol
    global count_alpha
    global count_upper
    global count_lower
    global count_numeric
    global count_symbol
    global count_spe
    global upper_stat
    global lower_stat
    global num_stat
    global symb_stat
    global other_stat

    # Emplacement du script sur la machine et demande le chemin du fichier en ligne de commande.
    Path = input("""Rockyou.txt Path :
Example : /home/test/rockyou.txt OR C:\\rockyou.txt
>>> """)

    #fopen = (line for line in open('C:\\rockyou.txt', 'r', encoding='utf-8', errors='replace').readlines())
    fopen = (line for line in open(Path, 'r', encoding='utf-8', errors='replace').readlines())

    count_total_lines, count_char, count_total_char, count_total_alpha, count_total_upper, count_total_lower, count_total_num, count_total_symb = 0, 0, 0, 0, 0, 0, 0, 0

    symb_list = ('[@\[ \]^_!"#$%&\'()*+,-./:;{\}<>=|~?]')
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
                list_count_digits.append(character)
                count_numeric = count_numeric + 1
                count_total_num = count_total_num + 1

            elif(re.search(symb_list,character)):
                list_count_symbol.append(character)
                count_symbol = count_symbol + 1
                count_total_symb = count_total_symb + 1

    upper_stat = count_total_upper / (count_total_char - 1) * 100
    lower_stat = count_total_lower / (count_total_char - 1) * 100
    num_stat = count_total_num / (count_total_char - 1) * 100
    symb_stat = count_total_symb / (count_total_char - 1) * 100
    other_stat = 100 - (upper_stat + lower_stat + num_stat + symb_stat)

    fopen.close()

    print("Analyse Statistique Complete (NO ERROR) ")

#########################################################################################################################################################################

# La partie qui permet d’afficher des résultats en ligne de commande.
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

# Remplace les résultats déjà affichés par des espaces pour une meilleure lisibilité et exploitations des résultats.
def blankText():
    labelMessage['text']=" "
    labelMessage11['text'] = " "
    labelMessage12['text'] = " "
    labelMessage13['text'] = " "
    labelMessage14['text'] = " "
    labelMessage21['text'] = " "
    labelMessage22['text'] = " "
    labelMessage23['text'] = " "
    labelMessage24['text'] = " "

# Supprime la page de garde pour mieux lire les résultats qui seront affichés quand nous allons appuyer sur les boutons.
def Delete_Text():
    labelBonjour.pack_forget()
    labelDescription.pack_forget()

# De la fonction ci-dessous « zeroTitre » a la fonctions ten() un peu plus bas. Cela sert à l'affichage des différentes statistiques généré avec l'algorithme.
def zeroTitre():
    global labelBonjour
    Titre = """Sujet 3 : Analyse statistique d’un fichier"""
    labelBonjour = tkinter.Label(mafenetre,text=Titre,font=('Arial',48))
    labelBonjour.pack(ipady=10)

def zeroText():
    global labelDescription
    Text = """
L’objectif de ce programme est d’analyser un fichier statique (rockyou.txt) contenant
des mots de passe à raison d’un mot de passe par ligne, et produire des statistiques
sur l’usage des caractères (majuscules, minuscules, numériques, symboles),
la longueur minimale, maximale et moyenne, la fréquence d’usage des lettres dans ce fichier.
    """
    labelDescription = tkinter.Label(mafenetre,text=Text,font=('Arial',28))
    labelDescription.pack(ipady=10)

def one():
    i = " Smallest word : ", min(list_count_char), "character(s)"
    labelMessage11['text']= i

def two():
    i = " Longest word : ", max(list_count_char), "character(s)"
    labelMessage12['text']= i

def three():
    i = " Average word length : ", round(count_total_char / count_total_lines), "character(s)"
    labelMessage13['text']= i

def four():
    i = " Number of lines : ", count_total_lines
    labelMessage14['text']= i

def five():
    i = " Uppercase only : ", str(round(upper_stat, 2)), "%"
    labelMessage21['text']= i

def six():
    i = " Lowercase only : ", str(round(lower_stat, 2)), "%"
    labelMessage22['text']= i

def seven():
    i = " Numbers only : ", str(round(num_stat, 2)), "%"
    labelMessage23['text']= i

def eight():
    i = " Symbols only : ", str(round(symb_stat, 2)), "%"
    labelMessage24['text']= i

def nine():
    Delete_Text()
    blankText()
    i = " Multiple character sets : ", str(round(other_stat, 2)), "%"
    labelMessage['text']= i

# Voici les fonctions qui affichent la fréquence de chaque caractère dans le fichier Rockyou.txt.
def ten():
    Delete_Text()
    blankText()
    zeroTitre()
    zeroText()
    global root1
    global root2
    global root3
    root1 = tkinter.Tk()
    root1.geometry('300x800')
    for letter in alpha_list:
        for index,item in enumerate(letter):
            tkinter.Label(root1,text="character : "+letter+" = "+str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1))+" %",font=('Ariel',16)).pack(pady = index+0)

    root1.title('Character table')
    root1.mainloop
    root2 = tkinter.Tk()
    root2.geometry('300x310')
    for chiffre in digits_list:
        for index,item in enumerate(chiffre):
            tkinter.Label(root2,text="character : "+chiffre+" = "+ str(round(list_count_digits.count(chiffre) / count_total_num * 100, 1))+" %",font=('Ariel',16)).pack(pady = index+0)

    root2.title('Table of numeric characters')
    root2.mainloop
    root3 = tkinter.Tk()
    root3.geometry('250x750')
    for symbols in symbols_list:
        for index,item in enumerate(symbols):
            tkinter.Label(root3,text="character : "+symbols+" = "+str(round(list_count_symbol.count(symbols) / count_total_symb * 100, 1))+" %",font=('Ariel',12)).pack(pady = index+0)

    root3.title('Table of symbols')
    root3.mainloop

# Voici la fonction « G1 » qui gère le graphique des caractères.
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
    plt.suptitle('percentage of each type of characters')
    plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')
    plt.show()

# La fonction « words » appelle les autres fonctions pour afficher la longueur max,min et moyenne d’un mot + le nombre de lignes. 
def words():
    Delete_Text()
    blankText()
    one()
    two()
    three()
    four()

# Voici la fonction « Caracters » qui permet d’appeler les fonctions qui affichent les statistiques sur les caractères.
def Caracters():
    Delete_Text()
    blankText()
    five()
    six()
    seven()
    eight()
    G1()

def quit():
    mafenetre.quit()     # stops mainloop
    mafenetre.destroy()  # this is necessary on Windows to prevent
                         # Fatal Python Error: PyEval_RestoreThread: NULL tstate


#
# La partie du script qui se lance au démarrage.
#
if __name__ == '__main__':

    # Voici la fonction « Algo_Statistique » qui permet d’afficher les statistiques. 
    Algo_Statistique()

    time.sleep(2)

    mafenetre = tkinter.Tk()			# Le nom de la fenêtre
    mafenetre.title('Python Project')	# Le titre de la fenêtre
    mafenetre.geometry('1550x650')		# La taille de la fenêtre

    # Les différents label qui contienne un message.
    labelMessage = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage.place(x=100,y=100)
    labelMessage11 = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage11.place(x=100,y=100)
    labelMessage12 = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage12.place(x=100,y=200)
    labelMessage13 = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage13.place(x=100,y=300)
    labelMessage14 = tkinter.Label(mafenetre,font=('Ariel',42))
    labelMessage14.place(x=100,y=400)
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
# Les différents boutons qui permettent d’afficher les résultats.
#
    # Affiche les statistiques sur les mots.
    boutonWord = tkinter.Button(mafenetre,text='Words',activeforeground="red",command=words)
    boutonWord.place(relx = 0.15, rely = 0.9, anchor = CENTER)

    # Affiche les statistiques sur les caractères
    boutonCaracters = tkinter.Button(mafenetre,text='characters',activeforeground="red",command=Caracters)
    boutonCaracters.place(relx = 0.30, rely = 0.9, anchor = CENTER)

    # Affiche les statistiques sur ce qui n’est pas une Majuscule ni Minuscule ni Numérique ni Symbole (caractères spéciaux).
    boutonNine = tkinter.Button(mafenetre,text='specific characters',activeforeground="red",command=nine)
    boutonNine.place(relx = 0.50, rely = 0.9, anchor = CENTER)

    # Affiche la fréquence des caractères. 
    boutonTen = tkinter.Button(mafenetre,text='character frequency',activeforeground="red",command=ten)
    boutonTen.place(relx = 0.70, rely = 0.9, anchor = CENTER)

    # Affiche le bouton pour quitter une fenêtre.
    #photo = Image.open("icon_poweroff.jpg")
    boutonQuit = tkinter.Button(mafenetre, text="Quit", activebackground="red", command=quit)
    boutonQuit.place(relx = 0.85, rely = 0.9, anchor = CENTER)


    # La fenêtre d’accueil.
    mafenetre.mainloop()

# THE END

