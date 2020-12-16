
#! /usr/bin/python3.8

# Les differentes library utilise
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
# Algo qui effectue des calculent sur le fichier Rockyou.txt et en extrait des statistiques
#

def Algo_Statistique():
    
    # Permet de rendre c'est variable lisible par toutes les fonctions du script
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

    # Demande le chemin du fichier en ligne de commande
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

# La partis affichage des resultat en ligne de commande
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

# Remplace de les resultats deja afficher par des espace pour un soucis de lisibilité
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

# Supprime le titre et la description de l'exercice pour mieux lire les resultats qui sa ficheront apres
def Delete_Text():
    labelBonjour.pack_forget()
    labelDescription.pack_forget()

# De la fonction ci-dessous a la fonctions ten(). Sert l'affichage des differentes statistiques genere avec l'algorithme
def zeroTitre():
    global labelBonjour
    Titre = """Sujet 3 : Analyse statistique d’un fichier"""
    #labelBonjour['text'] = Titre
    labelBonjour = tkinter.Label(mafenetre,text=Titre,font=('Arial',48))
    labelBonjour.pack(ipady=10)

def zeroText():
    global labelDescription
    Text = """
L'objectif de ce programme est d'ouvrir un fichier texte (rockyou.txt) contenant
des mots de passe à raison d’un mot de passe par ligne, et produire des statistiques sur
l’usage des caractères (majuscules, minuscules, numériques, symboles), la longueur
minimale, maximale et moyenne, la fréquence d’usage des lettres dans ce fichier.
    """
    #labelDescription['text'] = Text
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

# Fonctions qui affiche les repetitions de chaque caracteres analyse dans le Rockyou.txt
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

# Fonction qui gere le graph des caracteres
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

# fonction appele pour appeler les fonctions qui affiche les statistiques des mots de Rockyou.txt
def words():
    Delete_Text()
    blankText()
    one()
    two()
    three()
    four()

# fonction appele pour appeler les fonctions qui affiche les statistiques des caracteres de Rockyou.txt
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
# La parti du script qui se lance au demarrage
#
if __name__ == '__main__':
    
    # la fonction qui effectue des statistique sur le fichier text
    Algo_Statistique()
    
    # Attends 2 secondes le entre la fin des calcule et l'affichage des resultats
    time.sleep(2)
    
    mafenetre = tkinter.Tk()                                    # Le nom de la fennetre
    mafenetre.title('Python Project')                           # Le titre de la fenetre
    mafenetre.geometry('1550x650')                              # La taille de la fenetre
    
    # Les diferents label qui contienne un message
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
    # Les differents bouton qui donne des resultats
    #
    
    # Affiche les statistiques sur les mots
    boutonWord = tkinter.Button(mafenetre,text='Words',activeforeground="red",command=words)
    boutonWord.place(relx = 0.15, rely = 0.9, anchor = CENTER)
    
    # Affiche les statistiques sur les caracteres
    boutonCaracters = tkinter.Button(mafenetre,text='characters',activeforeground="red",command=Caracters)
    boutonCaracters.place(relx = 0.30, rely = 0.9, anchor = CENTER)
    
    # Affiche les statistique sur ce qui est ni Majuscule ni Minuscule ni Numerique ni Symbol
    boutonNine = tkinter.Button(mafenetre,text='specific characters',activeforeground="red",command=nine)
    boutonNine.place(relx = 0.50, rely = 0.9, anchor = CENTER)
    
    # Affiche les listes avec chaqu'un son pourcentage repetition de chaque caracteres
    boutonTen = tkinter.Button(mafenetre,text='character frequency',activeforeground="red",command=ten)
    boutonTen.place(relx = 0.70, rely = 0.9, anchor = CENTER)
    
    # Affiche le bouton pour quit les fenetres
    photo = Image.open("icon_poweroff.jpg")
    boutonQuit = tkinter.Button(mafenetre, text="Quit", activebackground="red", command=quit)
    boutonQuit.place(relx = 0.85, rely = 0.9, anchor = CENTER)

    #
    # La fenetre s'affiche avec les resultats
    #
    mafenetre.mainloop()

