AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  
    while user_feedback != AFFIRMATION:   
        print("That was not the affirmation.")

        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")


    print("Now, let's do it again!")
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()
if __name__ == '__main__':
    main()