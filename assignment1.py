#1. Write a Python program to calculate the length of a string.
var1="this is a string"
print(len(var1))

#2 Write a Python program to count the number of characters (character frequency) in a string.
#Sample
#String : google.com'
#Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
def frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(frequency('google.com'))

#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
#Sample String : 'w3resource'
#Expected Result : 'w3ce'
#Sample String : 'w3'
#Expected Result : 'w3w3'
#Sample String : ' w'
#Expected Result : Empty String
def string_both_ends(str):
  if len(str) < 2:
    return ''
  return str[0:2] + str[-2:]
print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))
a
#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
def change(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]
  return str1
print(change('restart'))

#5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
def charsmixup(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]
  return new_a + ' ' + new_b
print(charsmixup('abc', 'xyz'))

#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
#Sample String : 'abc'
#Expected Result : 'abcing'
#Sample String : 'string'
#Expected Result : 'stringly'
def add_string(str1):
  length = len(str1)
  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'
  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))

#7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
#Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!'
def not_poor(str1):
    snot = str1.find('not')
    spoor = str1.find('poor')
    if spoor > snot and snot > 0 and spoor > 0:
        str1 = str1.replace(str1[snot:(spoor + 4)], 'good')
        return str1
    else:
        return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))


#8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
#Sample Output:
#Longest word: Exercises
#Length of the longest word: 9

def findlongestword(word):
  word_len = []
  for n in word:
    word_len.append((len(n), n))
  word_len.sort()
  return word_len[-1][0], word_len[-1][1]
result = findlongestword(["PHP", "Exercises", "Backend"])
print("\nLongest word: ", result[1])
print("Length of the longest word: ", result[0])

#9. Write a Python program to remove the nth index character from a nonempty string.
def remove_char(str, n):
  first_part = str[:n]
  last_part = str[n + 1:]
  return first_part + last_part
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))

#10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
def change_sring(str1):
  return str1[-1:] + str1[1:-1] + str1[:1]
print(change_sring('abcd'))
print(change_sring('12345'))

#11. Write a Python program to remove the characters which have odd index values of a given string.
def odd_values_string(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
print(odd_values_string('abcdef'))
print(odd_values_string('python'))

#12. Write a Python program to count the occurrences of each word in a given sentence.
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print( word_count('the quick brown fox jumps over the lazy dog.'))

#13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
user_input = input("What's your favourite language? ")
print("My favourite language is ", user_input.upper())
print("My favourite language is ", user_input.lower())

#14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
#Expected Result : black, green, red, white,red

items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

#15. Write a Python function to create the HTML string with tags around the word(s).
#Sample function and result :
#add_tags('i', 'Python') -> '<i>Python</i>'
#add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
[9:15 am, 26/07/2022] Vishakha 😜: #16. Write a Python function to insert a string in the middle of a string.
#Sample function and result :
#insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
#insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]

print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))

#17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
#Sample function and result :
#insert_end('Python') -> onononon
#insert_end('Exercises') -> eseseses
def insert_end(str):
	sub_str = str[-2:]
	return sub_str * 4

print(insert_end('Python'))
print(insert_end('Exercises'))

#18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.
#Sample function and result :
#first_three('ipy') -> ipy
#first_three('python') -> pyt
def first_three(str):
	return str[:3] if len(str) > 3 else str

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))

#19. Write a Python program to get the last part of a string before a specified
#character. 
#https://www.w3resource.com/python-exercises
#https://www.w3resource.com/python
str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/', 1)[0])
print(str1.rsplit('-', 1)[0])

#20. Write a Python function to reverses a string if it's length is a multiple of 4.

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1
print(reverse_string('abcd'))
print(reverse_string('python'))

#21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]:
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1
print(to_uppercase('Python'))
print(to_uppercase('PyThon'))

#22. Write a Python program to remove a newline in Python.
str1='Python Exercises\n'
print(str1)
print(str1.rstrip())

#23. Write a Python program to check whether a string starts with specified characters.
string = "w3resource.com"
print(string.startswith("w3r"))