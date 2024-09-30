'''
    Practice Questions: String Manipulation
    Author: Johnny Zhao
    Date Created: Sept 30, 2024
    Date Last Modified: Sept 30, 2024
'''

def q1(): 
  print('"Hello World"') #printing "Hello World" with the quotations using single and double quotations

def q2(): 
  wordQ2 = input("Input a word: ") #asking the user to input a word
  print(wordQ2.lower()) #outputting the result in all lowercase letters
  print(wordQ2.upper()) #outputting the result in all uppercase letters

def q3(): 
  wordQ3 = input("Input a word that is at least 5 letters long: ") #asking the user to input a word that is at least 5 letters long
  print(wordQ3[1:4]) #outputting the 2nd to 4th letter of the result

def q4(): 
  wordQ4 = input("Input a word: ") #asking the user to input a word
  print(wordQ4.index("o")) #outputting the index where the first "o" is in the result

def q5(): 
  wordQ5 = input("Input a word: ") #asking the user to input a word
  print(len(wordQ5)) #outputting the length of the result

#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
q3()
q4()
q5()
'''