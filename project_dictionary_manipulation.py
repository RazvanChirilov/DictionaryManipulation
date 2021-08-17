"""this function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return
 the sum of the values of the dictionary"""


def sum_values(my_dictionary):
    our_values_sum = 0
    for values in my_dictionary.values():
        our_values_sum += values
    return our_values_sum


test = sum_values({"a": 1, "b": 2, "c": 3})
print(test)

"""this function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values,
 as a parameter. This function should return the sum of the values of all even keys."""


def even_key(my_dictionary):
    our_sum_of_keys = 0
    for key in range(len(my_dictionary.keys())):
        if key % 2 == 0:
            our_sum_of_keys += 1
    return our_sum_of_keys


test = even_key({"a": 1, "b": 2, "c": 3})
print(test)

"""Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter.
 The function should add 10 to every value in my_dictionary and return my_dictionary"""


def add_ten(my_dictionary):
    modified_dictionary = {}
    for key, value in my_dictionary.items():
        my_dictionary[key] = 10
        modified_dictionary.update(my_dictionary)
    return modified_dictionary


test = add_ten({"a": 1, "b": 2, "c": 3})
print(test)

"""this function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
This function should return a list of all values in the dictionary that are also keys."""


def values_that_are_keys(my_dictionary):
    hold_the_values = []
    for key, value in my_dictionary.items():
        if value in my_dictionary.keys():
            hold_the_values.append(value)
    return hold_the_values


test = values_that_are_keys({"a": "a", "b": 2, "c": "c"})
print(test)

"""Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should
 return the key associated with the largest value in the dictionary."""


def largest_value(my_dictionary):
    minimum_value = float("-inf")
    largest_value = float("+inf")
    for value in my_dictionary.values():
        if str(value) > str(minimum_value):
            largest_value = value
    return largest_value


test = largest_value({"a": "a", "b": 2, "c": 10})
print(test)


"""this function named word_length_dictionary that takes a list of strings named words as a parameter. The function
 should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that
  word."""


def word_length_dictionary(words):
    new_dict = {}
    for word in words:
        new_dict[word] = len(word)
    return new_dict


test = word_length_dictionary(["maia", "mamaia", "grepfruit", "apa", "piersici", "caise", "pomi"])
print(test)


"""this function named frequency_dictionary that takes a list of elements named words as a parameter.
 The function should return a dictionary containing the frequency of each element in words."""


def frecvency_count(words):
    new_dict = {}
    for word in words:
        if word not in new_dict:
            new_dict[word] = 0
            new_dict[word] += 1
    return new_dict


test = frecvency_count(["maia", "mamaia", "grepfruit", "apa", "piersici", "caise", "pomi"])
print(test)


"""this function named unique_values that takes a dictionary named my_dictionary as a parameter.
 The function should return the number of unique values in the dictionary."""


def unique_values(my_dictionary):
    values = []
    for value in my_dictionary.values():
        if value not in values:
            values.append(value)
    return len(values)


test = unique_values({"a": 10, "b": 2, "c": 10})
print(test)


"""Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be
 a dictionary where the key is a last name and the value is a list of first names. """


def count_first_letter(names):
    letters = {}
    for key in names.keys():
        first_letter = key[0]
        if key[0] not in letters:
            letters[first_letter] = 0
            letters[first_letter] += len(names[key])
    return letters


print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))