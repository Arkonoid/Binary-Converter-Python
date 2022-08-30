endProgram = False

while not endProgram:
    numberToConvert = input("\n\nEnter a number between 0 and 255 (inclusive) to convert to binary: ")
    number_test_failed = False

    for i in range(0, len(numberToConvert), 1):
        temp = numberToConvert[i]
        x = temp.isalpha()
        if x:
            number_test_failed = True

    if number_test_failed:
        print("You need to enter a number. Please try again...")
    else:
        numberToConvert = float(numberToConvert)

        if numberToConvert > 255:
            print("Number is too high. Please try again...\n\n")
        elif numberToConvert < 0:
            print("Number cannot be negative. Please try again...\n\n")
        elif numberToConvert % 1 != 0:
            print("Number cannot be a decimal. Please try again...\n\n")
        else:
            place128 = '0'
            place64 = '0'
            place32 = '0'
            place16 = '0'
            place8 = '0'
            place4 = '0'
            place2 = '0'
            place1 = '0'

            binary_divider = 128
            placeholder = 0

            for i in range(0, 8, 1):
                if numberToConvert - binary_divider >= 1 or numberToConvert == binary_divider:
                    numberToConvert -= binary_divider

                    match binary_divider:
                        case 128:
                            place128 = '1'
                        case 64:
                            place64 = '1'
                        case 32:
                            place32 = '1'
                        case 16:
                            place16 = '1'
                        case 8:
                            place8 = '1'
                        case 4:
                            place4 = '1'
                        case 2:
                            place2 = '1'
                        case 1:
                            place1 = '1'

                binary_divider /= 2

            print(
                "The number in binary is: {0}{1}{2}{3}{4}{5}{6}{7}".format(place128, place64, place32, place16, place8,
                                                                           place4, place2, place1))
            exit_option = input("Enter 'x' to close the program. Enter anything else to run again: ")

            if exit == 'x':
                endProgram = True
