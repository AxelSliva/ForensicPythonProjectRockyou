#! /usr/bin/python3

from tkinter import * 
import re
import os
import matplotlib

"""
print("Ligne:", number_of_lines,"[A-Z]:", count_upper, "[a-z]:", count_lower, "[0-9]:", count_numeric, "[symbols]:", count_symbol, "")
print("\n")
print("Nombre de lignes:", number_of_lines)
print("Nombre de majuscules total:", count_upper_total)
print("Nombre de minuscules total:", count_lower_total)
print("Nombre de caractères numériques total:", count_numeric_total)
print("Nombre de majuscules total:", count_symbol_total)

"""
"""
# ----
# cherche dans le fichier rockyou.txt
filepath = "rockyou.txt"

number_of_lines, count_characters, count_upper_total, count_lower_total, count_numeric_total, count_symbol_total = 0, 0, 0, 0, 0, 0

fichier = open(filepath, "r")

for line in fichier:
  number_of_lines += 1
  count_characters = len(line)

  count_upper, count_lower, count_numeric, count_symbol = 0, 0, 0, 0

  for character in line:
    if(character.isupper()):
      count_upper = count_upper + 1
      count_upper_total = count_upper_total + 1
    elif(character.islower()):
      count_lower = count_lower + 1
      count_lower_total = count_lower_total + 1
    elif(character.isnumeric()):
      count_numeric = count_numeric + 1
      count_numeric_total = count_numeric_total + 1
    elif(re.search(r'[[:blank:][:punct:]', character)):
      count_symbol = count_symbol + 1
      count_symbol_total = count_symbol_total + 1
    else:
      count_symbol = count_symbol + 1
      count_symbol_total = count_symbol_total + 1

file.close()
exit()
# ----
"""


def one():
    #return "January"
    #labelBonjour['text']= 'Bonjour : January\nBonjour : one'
    labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_upper_total : '
 
def two():
    #labelBonjour['text']= 'Bonjour : Febreray'
    #return "February"
    labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_lower_total : '
 
def three():
    #labelBonjour['text']= 'Bonjour : March'
    #return "March"
    labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_numeric_total : '
 
def four():
    #labelBonjour['text']= 'Bonjour : April'
    #return "April"
    labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_symbol_total : '
 
def five():
    #labelBonjour['text']= 'Bonjour : Mary'
    #return "May"
    labelBonjour['text']= 'number of lines : \n\nLongueur Maximale de la ligne trouve dans le fichier : \n\n'
 
def six():
    #labelBonjour['text']= 'Bonjour : June'
    #return "June"
    labelBonjour['text']= 'number of lines : \n\nLongueur Minimale de la ligne trouve dans le fichier : \n\n'

def seven():
    labelBonjour['text']= 'number of lines : \n\nLongueur Moyenne de la ligne trouve dans le fichier : \n\n'

def eight():
    labelBonjour['text']= 'number of lines : \n\nfrequence des lettres utilise par ligne dans le fichier : \n\n'

#def Clic():

 #   labelBonjour['text']= 'Bonjour : "'+ prenom.get() + ' '  + nom.get() + '"' 

#def Effacer(): 

  #  labelBonjour['text']= 'Bonjour' 

 #   prenom.set('') 

#    nom.set('') 


mafenetre = Tk()
mafenetre.title('Project Python')
mafenetre.geometry('1600x720')
#labelPrenom = Label(mafenetre,text='Prénom :')
#labelPrenom.place(x=50,y=100)
#prenom = StringVar()
#entryPrenom = Entry(mafenetre,textvariable = prenom)
#entryPrenom.place(x=120,y=100)
#labelNom = Label(mafenetre,text=' Nom :')
#labelNom.place(x=50,y=200)
#nom = StringVar()
#entryNom = Entry(mafenetre,textvariable =nom)
#entryNom.place(x=120,y=200)
#boutonGo = Button(mafenetre,text='Go',command=Clic)
#boutonGo.place(x=50,y=150)
#boutonEffacer = Button(mafenetre,text='Effacer',command=Effacer)
#boutonEffacer.place(x=150,y=150)

#
# Les differents button qui donne des resultats
#
boutonOne = Button(mafenetre,text='count_upper',command=one)
boutonOne.place(x=50,y=650)
boutonTwo = Button(mafenetre,text='count_lower',command=two)
boutonTwo.place(x=250,y=650)
boutonThree = Button(mafenetre,text='count_numeric',command=three)
boutonThree.place(x=450,y=650)
boutonFour = Button(mafenetre,text='count_symbol',command=four)
boutonFour.place(x=650,y=650)
boutonFive = Button(mafenetre,text='Longueur Max',command=five)
boutonFive.place(x=850,y=650)
boutonSix = Button(mafenetre,text='Longueur Min',command=six)
boutonSix.place(x=1050,y=650)
boutonSeven = Button(mafenetre,text='Longueur Moy',command=seven)
boutonSeven.place(x=1250,y=650)
boutonEight = Button(mafenetre,text='Frequence',command=eight)
boutonEight.place(x=1450,y=650)

labelBonjour = Label(mafenetre,text='Bonjour',bg='white',font=('Arial',16))
labelBonjour.place(x=50,y=50)
mafenetre.mainloop()


