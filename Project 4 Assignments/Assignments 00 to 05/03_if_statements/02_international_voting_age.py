Peturksbouipo_age = 16
Stanlau_age = 25
Mayengua_age = 48
def main():
    user_age = int(input("Enter your age: "))
    if user_age >= Peturksbouipo_age:
        print("You can vote in Peturksbouipo.")
    else:
        print("You cannot vote in Peturksbouipo.")
    if user_age >= Stanlau_age:
        print("You can vote in Stanlau.")
    else:
        print("You cannot vote in Stanlau.")
    if user_age >= Mayengua_age:
        print("You can vote in Mayengua.")
    else:
        print("You cannot vote in Mayengua.")
    # The code above checks if the user is old enough to vote in each of the three countries.


if __name__ == '__main__':
    main()