

"""Scenario 1: Finding a Number in an Unsorted List

You are given an unsorted list of integers. Write two functions, one for linear search and one for binary search, to find a specific target number in the list. Provide a return value that includes the answer and the number of steps the program took to encounter the answer."""

#You are given an unsorted list of integers
def linear_search(arr, target):
    sorted_arr = sorted(arr)
    steps = 0
    for num in sorted_arr:
        steps += 1
        if num == target:
            return f"STEPS = {steps}, ANSWER = {num}"





def binary_search(arr, target):
    sorted_arr = sorted(arr)
    steps = 0
    left = 0
    right = len(sorted_arr) - 1
    while left <= right:
        steps += 1
        middle = (left + right) // 2
        if sorted_arr[middle] == target:
            return f"STEPS = {steps}, ANSWER = {target}"
        elif sorted_arr[middle] < target:
            left = middle + 1
            break
        else:
            right = middle -1
    return f"STEPS = {steps}, ANSWER = {target}"

# unsorted_list = [42, 15, 7, 30, 22, 10, 18]
# target_1 = 30
# result_linear_search_1 = linear_search(unsorted_list, target_1)
# result_binary_search_1 = binary_search(sorted(unsorted_list), target_1)
# print(result_linear_search_1)

# print(result_binary_search_1)

"""Scenario 2: Finding a Word in a Sorted List

You have a sorted list of words. Write two functions, one for linear search and one for binary search, to find a specific word in the list. Provide a return value that includes the answer and the number of steps the program took to encounter the answer."""


#find a specific word in the list
def linear_search_sorted_words(word_list, target_word):
    steps = 0
    for word in word_list:
        steps += 1
        if word == target_word:
            return f"STEPS = {steps}, ANSWER = {word}"
        
    return f"{target_word} not found"

def binary_search_sorted_words(word_list, target_word):
    steps = 0
    left = 0
    right = len(word_list) -1
    while left < right:
        steps +=1
        middle = (left + right) //2
        if word_list[middle] == target_word:
            return f"STEPS = {steps}, ANSWER = {target_word}"
        elif word_list[middle] < target_word:
            left = middle + 1
        else:
            right = middle - 1
    return f"STEPS = {steps}, ANSWER = {target_word}"


# # Scenario 2 Test
# sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
# target_2 = 'orange'
# result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
# result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)

# print(result_linear_search_2)
# print(result_binary_search_2)

"""Scenario 3: Finding the Last Occurrence in a List

Given a list of integers, write two functions, one for linear search and one for binary search, to find the last occurrence of a specific number in the list. Provide a return value that includes the answer and the number of steps the program took to encounter the answer."""

#find the last occurrence of a specific number in the list.

def linear_search_last_occurence(arr, target):
    steps = 0
    last_index_found = -1
    length = len(arr)
    for i in range(length):
        steps += 1
        if arr[i] == target:
            if i > last_index_found:
                last_index_found = i
    return f"STEPS = {steps}, ANSWER = {target}"



occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurence(occurrence_list, target_3)
print(result_linear_search_3)
# result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)


def binary_search_last_occurence(arr, target):
    pass
