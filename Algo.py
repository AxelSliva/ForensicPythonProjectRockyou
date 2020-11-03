### Module(s) ###

import os
import re
import string

### Windows Clear ###

os.system('cls')

### Variable(s) ###
filepath = "D:\\Cloud\\OneDrive\\Documents\\Travail\\MyScripts\\Python\\Projets\\School\\toto.txt"

count_total_lines, count_char, count_total_char, count_total_alpha, count_total_upper, count_total_lower, count_total_num, count_total_symb = 0, 0, 0, 0, 0, 0, 0, 0

symb_list = ('[@\[ \]^_!"#$%&\'()*+,-./:;{\}<>=|~?]')
alpha_list = list(string.ascii_lowercase)
list_count_char = list()
list_count_letter = list()

### Main ###
file = open(filepath, "r")

for line in file:
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

file.close()

### Results ###
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

### Windows Exit ###
exit()