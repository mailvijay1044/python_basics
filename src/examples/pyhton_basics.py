

from collections import Counter


def dict_functions():
    dict = {"3": "fif", "ghg":"ghhg"}


    # 1 for finding a key in dict
    for i in dict:
        print(i)


def check_string_sort(str):
    #str = 'vijay'
    from collections import Counter
    print(Counter(str))

    print(sorted(str))

def removeChars(a, b):
    # make dictionaries from both strings
    c1 = Counter(a)
    c2 = Counter(b)

    # finding the common elements from both dictonary
    common = c1 & c2
    print(common)
    value = 0

    # adding up the key from common dictionary in order
    # to get the total number of common elements
    for key in common:
        value = value + common[key]

        # returning the number of elements to be
    # removed to form an anagram
    return (len(a) - 2 * value + len(b))


# Driver program
if __name__ == "__main__":
    str1 = 'Night'
    str2 = 'Tighn'
    print(removeChars(str1, str2))
    print(check_string_sort("vijay"))
    dict_functions()

