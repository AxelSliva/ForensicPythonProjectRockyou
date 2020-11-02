#! /usr/bin/python3

from tkinter import * 
import re
import os
import matplotlib


#
# Algo des differents
#

#fopen = (line for line in open("/home/nexxis/Documents/Python/rockyou.txt", "r").readlines())
fopen = (line for line in open("/home/nexxis/Documents/Python/toooo.txt", "r").readlines())

number_of_lines, count_characters, count_total_characters, count_alpha_total, count_upper_total, count_lower_total, count_numeric_total, count_symbol_total, count_other_total = 0, 0, 0, 0, 0, 0, 0, 0, 0

List1 = list()
List2 = list()

for line in fopen:
  List1.append(count_characters)
  number_of_lines += 1
  count_characters = len(line)
  count_total_characters += count_characters

  count_alpha, count_upper, count_lower, count_numeric, count_symbol, count_other = 0, 0, 0, 0, 0, 0

  for character in line:
    if(character.isalpha()):
      List2.append(character.lower())
      count_alpha = count_alpha + 1
      count_alpha_total = count_alpha_total + 1

      if(character.isupper()):
        count_upper = count_upper + 1
        count_upper_total = count_upper_total + 1
      else:
        count_lower = count_lower + 1
        count_lower_total = count_lower_total + 1

    elif(character.isnumeric()):
      count_numeric = count_numeric + 1
      count_numeric_total = count_numeric_total + 1
    elif(re.search(r'([:blank:]|[:punct:])', character)):
      count_symbol = count_symbol + 1
      count_symbol_total = count_symbol_total + 1
    else:
      count_symbol = count_symbol + 1
      count_symbol_total = count_symbol_total + 1

#print("\n")
#print("Nombre moyen de caractères:", round(count_total_characters / number_of_lines), "caractères")
#print("Nombre max de caractères:", max(List1), "caractères")
#print("Nombre min de caractères:", min(List1), "caractères")
#print("Pourcentage de lettres:", str(round(count_alpha_total / count_total_characters * 100, 2)), "%")
#print("Pourcentage de lettres majuscules:", str(round(count_upper_total / count_total_characters * 100, 2)), "%")
#print("Pourcentage de lettres minuscules:", str(round(count_lower_total / count_total_characters * 100, 2)), "%")
#print("Pourcentage de numériques:", str(round(count_numeric_total / count_total_characters * 100, 2)), "%")
#print("Pourcentage de symboles:", str(round(count_symbol_total / count_total_characters * 100, 2)), "%")
#print("\n")

print("Pourcentage des lettres utilisées:")
print("a:", str(round(List2.count("a") / count_alpha_total * 100, 2)), "%")
print("b:", str(round(List2.count("b") / count_alpha_total * 100, 2)), "%")
print("c:", str(round(List2.count("c") / count_alpha_total * 100, 2)), "%")
print("d:", str(round(List2.count("d") / count_alpha_total * 100, 2)), "%")
print("e:", str(round(List2.count("e") / count_alpha_total * 100, 2)), "%")
print("\n")

#fopen.next()
fopen.close()
#exit()

#
# fonction qui affiche les diferentes statistic
#
def pourcentageDeCarctere():
    # Cette function est utilise pour effectue le pourcentage des resultats d'un calcule
    return "nombre"


def one():
    #return "January"
    #labelBonjour['text']= 'Bonjour : January\nBonjour : one'
    #pourcentageDeCaractere()
    #labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_upper : \n\ncount_upper_total : '
    labelBonjour['text']= "Pourcentage de lettres majuscules:", str(round(count_upper_total / count_total_characters * 100, 2)), "%"
 
def two():
    #labelBonjour['text']= 'Bonjour : Febreray'
    #return "February"
    #labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_lower : \n\ncount_lower_total : '
    labelBonjour['text']= "Pourcentage de lettres minuscules:", str(round(count_lower_total / count_total_characters * 100, 2)), "%"
 
def three():
    #labelBonjour['text']= 'Bonjour : March'
    #return "March"
    #labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_numeric : \n\ncount_numeric_total : '
    labelBonjour['text']= "Pourcentage de numériques:", str(round(count_numeric_total / count_total_characters * 100, 2)), "%"
 
def four():
    #labelBonjour['text']= 'Bonjour : April'
    #return "April"
    #labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_symbol : \n\ncount_symbol_total : '
    labelBonjour['text']= "Pourcentage de symboles:", str(round(count_symbol_total / count_total_characters * 100, 2)), "%"
 
def five():
    #labelBonjour['text']= 'Bonjour : Mary'
    #return "May"
    #labelBonjour['text']= 'number of lines : \n\nLongueur Maximale de la ligne trouve dans le fichier : \n\n'
    labelBonjour['text']= "Nombre max de caractères:", max(List1), "caractères"
 
def six():
    #labelBonjour['text']= 'Bonjour : June'
    #return "June"
    #labelBonjour['text']= 'number of lines : \n\nLongueur Minimale de la ligne trouve dans le fichier : \n\n'
    labelBonjour['text']= "Nombre min de caractères:", min(List1), "caractères"

def seven():
    #labelBonjour['text']= 'number of lines : \n\nLongueur Moyenne de la ligne trouve dans le fichier : \n\n'
    labelBonjour['text']= "Pourcentage de lettres:", str(round(count_alpha_total / count_total_characters * 100, 2)), "%"

def eight():
    #labelBonjour['text']= 'number of lines : \n\nfrequence des lettres utilise par ligne dans le fichier : \n\n'
    labelBonjour['text']= "Nombre moyen de caractères:", round(count_total_characters / number_of_lines), "caractères"


#
# La fenetre
#
mafenetre = Tk()
mafenetre.title('Project Python')
mafenetre.geometry('1600x720')


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


