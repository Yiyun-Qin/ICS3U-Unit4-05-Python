#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in April 2022
# This is the math program, adding numbers input by the user


def main():
    # This function adds numbers from the user

    # input
    add_time_string = input("How many numbers are you going to add: ")

    # process & output
    answer = 0
    print("")
    try:
        add_time_integer = int(add_time_string)
        if add_time_integer <= 0:
            print("Please put in a positive integer.")
        else:
            for counter in range(add_time_integer):
                add_number_string = input("Enter a number to add: ")
                try:
                    add_number_integer = int(add_number_string)
                    if add_number_integer >= 0:
                        answer = answer + add_number_integer
                    else:
                        answer = answer + 0
                    if counter < add_time_integer - 1:
                        continue
                    else:
                        print(
                            "The sum of just the positive numbers is {}.".format(answer)
                        )
                except Exception:
                    print("Invalid number!")
    except Exception:
        print("Invalid number!")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
