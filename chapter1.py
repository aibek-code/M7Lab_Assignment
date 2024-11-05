import random

import resources

def say_my_name(string):

    my_list = [0,1]
    choice = random.choice(my_list)
    if choice == 0:
        print(f"Hey! Hope you're having a great day! {string}")

    elif choice == 1:
        print(f"Have a bad day? {string}")

    else:
        print("You chose the wrong number. Choose 0 or 1!!!")

say_my_name("Aibek")


#check to make sure you can use the function 

resources.lets_see(40)

# make a random number between 0 and 1
# evaluating wheather the number is less than 0.5

# make a choice list, that has only 0 or 1 in it
# use random choice to pick one value and ...

def multiply_if():

    my_list = [random.randint(1,100) for _ in range(10)]
    results = []
    #make list of random number 
    for x in my_list:
        if resources.lets_see(x):
            results.append(x*5)
        else:
            results.append(x)
        print(results)
    return results

multiply_if()


def unique_elements(input_list):
    unique_set = set(input_list)
    sorted_unique = sorted(unique_set)
    result = []
    for element in sorted_unique:
        result.append(element)
        return result

input_list = [1,3,3,3,6,2,3,5]
print(unique_elements(input_list))
