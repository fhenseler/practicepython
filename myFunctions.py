import random
import string

def get_int(message) -> int:
    return int(input(message + "\n>>> "))

def get_str(message) -> str:
    return input(message + "\n>>> ")

def random_number_list(size = None) -> list:
    if size is not None:
        numberList = list(set(random.sample(range(1, 30), size)))
    else:
        numberList = list(set(random.sample(range(1, 30), 10)))
    return numberList

def check_palindrome(str1, str2) -> bool:
    if str1 == str2:
        return True
    else:
        return False

def is_prime(num) -> bool:
        list = [x for x in range(2, num) if num % x == 0]  
        if num > 1:
            if len(list) == 0:
                return True
            else:
                return False
        else:
            return False

def first_and_last(list) -> list:
    return [list[0], list[-1]]

def reverseString(string) -> str:
    splitString = string.split()
    reverse = []
    for word in splitString:
        reverse.insert(0, word)
    return " ".join(reverse)

def pass_generator(size, chars = string.ascii_lowercase + string.ascii_uppercase + string.digits):
    # random.SystemRandom() is cryptographically secure
    return ''.join(random.SystemRandom().choice(chars) for i in range(size)) 