chest = {
	'42': 'It is the Answer to Life the universe and everthing.',
	'666': 'If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things.',
	'8':'It is wrong always, everywhere and for everyone, to believe anything upon insufficient evidence. ',
	'13':'the truth is in the heart.',
	'0': 'freedom is secured not by the fullfilling of ones desires, but by the removal of desire.',
	'9': 'The unexpected life is not worth living.',
	'76': 'Life is series of natural and spontaneous changes.',
	'70': 'God is dead! He reamins dead! And we have killed him.'
}

# Q.1 sorting the dictionary using keys in traditional way
def dict_sort(key):
  for i in range(1,len(key)):
    for j in range(len(key)-i):
      if key[j] > key[j+1]:                #comparing each key
        key[j],key[j+1] = key[j+1],key[j]
  return key

keys = [ int(key) for key in chest.keys()]  #typecast string keys to integers
sorted_keys = dict_sort(keys)    #sorting keys of the dictionary
print("sorted keys",sorted_keys)

sorted_dict = {}
for key in sorted_keys:
    sorted_dict[str(key)] = chest[str(key)]

print(sorted_dict)



# Q.2
dict_values = list(sorted_dict.values())
first_val = dict_values[0]    #First value of the sorted dictionary
print(first_val)
second_val = dict_values[1]    #Second value of the sorted dictionary
print(second_val)

last_val = dict_values[-1]     #Last value of the sorted dictionary
print(last_val)
second_last_val = dict_values[-2]    #Second Last value of the sorted dictionary
print(second_last_val)

#Q.3  Concatenating obtained values from question 2
conc_str = first_val +" " + second_val +" " +last_val +" " +second_last_val
print("concatenated string is, ",conc_str)

# Q.4
str_split = conc_str.split()  #splitted concatednated string to get list of string 

fst_lst_str =''
for i in range(len(str_split)):
	fst_lst_str += str_split[i][0] + str_split[i][-1]  #Adding first and last chaarcters of each elements of the list
print("first and last characters are",fst_lst_str)

# Q.5 Finding number of occurences of each string literals
occurences = {}
  
for i in fst_lst_str:
    if i in occurences:
        occurences[i] += 1
    else:
        occurences[i] = 1
# print("Number of occurences of each letter of the string is", occurences)

desc_letters= sorted(occurences, key=occurences.get, reverse=True)[:5]  #sorting keys in descending order to get top 5 letters
print("top 5 letters",desc_letters)

top_letters = {}
for key in desc_letters:
    top_letters[key] = occurences[key]  #sorted top 5 dictionary values

print("top five occuring characters are",top_letters)
top_vals = list(top_letters.values()) # Number of occurences of each letters
print("NO of occurences",top_vals)

# Q.6
key_list = [52,51,61,71,58]

#Q.7
sum_list = [a+b for a, b in zip(key_list, top_vals)]
print("sum of two list is", sum_list)

# Q.8
ascii_values = []
for elements in sum_list:
	ascii_values.extend(ord(character) for character in str(elements)) #ord method to get AScii values of each characters of the list

print("ASCII values of the characters of the list is",ascii_values)

