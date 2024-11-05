

def lets_see(number):
    # see if x is in a range i make up
    # make a range
    # check if x is in a range

    if 50 <= number <=60:
        print(f"The number {number} is in the range 50-60.")
        return True
    else:
        print(f"The number {number} is not in the range 50-60.")
        return False


print("I am in resources function")


def main():
    print("This is only runs when I run the file directly.")


print("I will always get printed.")

if __name__== "__main__":
    main()