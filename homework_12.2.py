
if __name__ == '__main__':

    my_dict = {"0": "zero", "1":["O", "unu"], "2":["doua", "doi"], "3": "trei", "4": "patru", "5": "cinci",
           "6": "sase", "7": "sapte", "9": "noua" , "10": "zece", "111": "unsprezece" ,
           "12": "doisprezece", "100": "O suta"}
    with open ("text.txt", "r") as f:
        numbers = f.read().split()

    print(numbers)
    for number in numbers:
        if number in my_dict:
            print(f"Numarul {number} se traduce in -> {my_dict[number]}")
            continue
        if len(number) % 2 == 0:
            if number[0] == "2":
                first_number = my_dict[number[0]][0]
            else:
                first_number = my_dict[number[0]]
            if number[1] == "2" or number[1] == "1":
                second_number = my_dict[number[1]][1]
            else:
                second_number = my_dict[number[1]]

            print(f"Number {number} se traduce in ->{first_number}zeci si {second_number} ")

        else:
            if number[0] == "2" or number[0] == "1":
                first_number = my_dict[number[0]][0]
            else:
                first_number = my_dict[number[0]]
            if number[1] == "2" or number[1] == "1":
                second_number = my_dict[number[1]][0]
            else:
                second_number = my_dict[number[1]]

            if number[2] == "2" or number[2] == "1":
                third_number = my_dict[number[2]][1]
            else:
                third_number = my_dict[number[1]]

            print(f"Number {number} se traduce in ->{first_number}sute {second_number}zeci "
                f"si {third_number} ")


