# Option with collections.Counter

# Import the Counter class from the collections module
from collections import Counter

def are_anagrams_counter(str1, str2):

    # Remove spaces and convert to lowercase
    str1_clean = str1.replace(' ','').lower()
    str2_clean = str2.replace(' ','').lower()

    # Compare letter count using Counter
    return Counter(str1_clean) == Counter(str2_clean)


# Option without collections.Counter
def are_anagrams_manual(str1, str2):

    # Remove spaces and convert to lowercase
    str1_clean = str1.replace(' ','').lower()
    str2_clean = str2.replace(' ','').lower()

    # Count letters manually for first string
    str1_dic = {letter: 0 for letter in str1_clean}
    for letter in str1_clean:
        str1_dic[letter] += 1      

    # Count letters manually for second string
    str2_dic = {letter: 0 for letter in str2_clean}
    for letter in str2_clean:
        str2_dic[letter] += 1

    # Return whether dictionaries match
    return str1_dic == str2_dic

str_1_input = input('Enter the first word: ')
str_2_input = input('Enter the second word: ')

print(f'\n[Using Counter]\n{are_anagrams_counter(str_1_input, str_2_input)}')
print(f'\n[Using manual count]\n{are_anagrams_manual(str_1_input,str_2_input)}')