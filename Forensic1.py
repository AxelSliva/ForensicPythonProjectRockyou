
#! /usr/bin/python3

from tkinter import * 
import re
import os
import string
import matplotlib


#
# Algo des differents
#

#fopen = (line for line in open("/home/nexxis/Documents/Python/rockyou.txt", "r").readlines())
fopen = (line for line in open("/home/nexxis/Documents/Python/toooo.txt", "r").readlines())

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
"""



#
# fonction qui affiche les diferentes statistic
#
def pourcentageDeCarctere():
    # Cette function est utilise pour effectue le pourcentage des resultats d'un calcule
    #return "nombre"
    for letter in alpha_list:
    	#print(letter,":",str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1)), "%")
    	labelBonjour['text']= letter,":",str(round(list_count_letter.count(letter) / count_total_alpha * 100, 1)), "%"
    print("\n")


def one():
    #return "January"
    #labelBonjour['text']= 'Bonjour : January\nBonjour : one'
    #pourcentageDeCaractere()
    #labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_upper : \n\ncount_upper_total : '
    #"--------------------------------------------------"
    #"Passwod Length"
    #labelBonjour['text']= "Pourcentage de lettres majuscules:", str(round(count_upper_total / count_total_characters * 100, 2)), "%"
    labelBonjour['text']= "Smallest word:", min(list_count_char), "character(s)"
 
def two():
    #labelBonjour['text']= 'Bonjour : Febreray'
    #return "February"
    #labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_lower : \n\ncount_lower_total : '
    #labelBonjour['text']= "Pourcentage de lettres minuscules:", str(round(count_lower_total / count_total_characters * 100, 2)), "%"
    labelBonjour['text']= "Longest word:", max(list_count_char), "character(s)"
 
def three():
    #labelBonjour['text']= 'Bonjour : March'
    #return "March"
    #labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_numeric : \n\ncount_numeric_total : '
    #labelBonjour['text']= "Pourcentage de numériques:", str(round(count_numeric_total / count_total_characters * 100, 2)), "%"
    labelBonjour['text']= "Average word length:", round(count_total_char / count_total_lines), "character(s)"
 
def four():
    #labelBonjour['text']= 'Bonjour : April'
    #return "April"
    #labelBonjour['text']= 'Caracteres : \n\nnumber of lines : \n\ncount_symbol : \n\ncount_symbol_total : '
    #labelBonjour['text']= "Pourcentage de symboles:", str(round(count_symbol_total / count_total_characters * 100, 2)), "%"
    labelBonjour['text']= "Uppercase only:", str(round(upper_stat, 2)), "%"
 
def five():
    #labelBonjour['text']= 'Bonjour : Mary'
    #return "May"
    #labelBonjour['text']= 'number of lines : \n\nLongueur Maximale de la ligne trouve dans le fichier : \n\n'
    #labelBonjour['text']= "Nombre max de caractères:", max(List1), "caractères"
    labelBonjour['text']= "Lowercase only:", str(round(lower_stat, 2)), "%"
 
def six():
    #labelBonjour['text']= 'Bonjour : June'
    #return "June"
    #labelBonjour['text']= 'number of lines : \n\nLongueur Minimale de la ligne trouve dans le fichier : \n\n'
    #labelBonjour['text']= "Nombre min de caractères:", min(List1), "caractères"
    labelBonjour['text']= "Numbers only", str(round(num_stat, 2)), "%"

def seven():
    #labelBonjour['text']= 'number of lines : \n\nLongueur Moyenne de la ligne trouve dans le fichier : \n\n'
    #labelBonjour['text']= "Pourcentage de lettres:", str(round(count_alpha_total / count_total_characters * 100, 2)), "%"
    labelBonjour['text']= "Symbols only:", str(round(symb_stat, 2)), "%"

def eight():
    #labelBonjour['text']= 'number of lines : \n\nfrequence des lettres utilise par ligne dans le fichier : \n\n'
    #labelBonjour['text']= "Nombre moyen de caractères:", round(count_total_characters / number_of_lines), "caractères"
    labelBonjour['text']= "Multiple character sets:", str(round(other_stat, 2)), "%"


#
# La fenetre
#
mafenetre = Tk()
mafenetre.title('Project Python')
mafenetre.geometry('1800x720')


#
# Les differents button qui donne des resultats
#
boutonOne = Button(mafenetre,text='Smallest word',activeforeground="red",command=one)
boutonOne.place(x=50,y=650)
boutonTwo = Button(mafenetre,text='Longest word',activeforeground="red",command=two)
boutonTwo.place(x=250,y=650)
boutonThree = Button(mafenetre,text='Average word length',activeforeground="red",command=three)
boutonThree.place(x=450,y=650)
boutonFour = Button(mafenetre,text='Uppercase only',activeforeground="red",command=four)
boutonFour.place(x=650,y=650)
boutonFive = Button(mafenetre,text='Lowercase only',activeforeground="red",command=five)
boutonFive.place(x=850,y=650)
boutonSix = Button(mafenetre,text='Numbers only',activeforeground="red",command=six)
boutonSix.place(x=1050,y=650)
boutonSeven = Button(mafenetre,text='Symbols only',activeforeground="red",command=seven)
boutonSeven.place(x=1250,y=650)
boutonEight = Button(mafenetre,text='Multiple character sets',activeforeground="red",command=eight)
boutonEight.place(x=1450,y=650)
boutonEight = Button(mafenetre,text='list Caracteres',activeforeground="red",command=pourcentageDeCarctere)
boutonEight.place(x=1650,y=650)

labelBonjour = Label(mafenetre,text='Bonjour',bg='white',font=('Arial',12))
labelBonjour.place(x=50,y=50)
mafenetre.mainloop()


