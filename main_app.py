numbers = [380673406767, 2380673406767, 380673406767, 380673406767, 380675156060, 380675156262, 380675156264, 380675156265, 380675156266, 380675156267, 380675156268, 380675156269, 38067515626212, 38067515626213, 38067515626214, 38067515626215, 38067515626217]

def check_telephones(start_with, numbers_list):
    """
        check input value start_with and compares with numbers_list
        if number of numbers_list start with start_with value append this number in result list
        count of result max 10 compares number
        return list
    """
    result_out = []
    if isinstance(numbers_list, (list,)) and isinstance(start_with, (int,)):
        counter = 0
        for number in numbers_list:
            if str(number).startswith(str(start_with)):
                counter +=1
                result_out.append(number)
                if counter >= 10: break
    return result_out

def main():
    while True:
        try:
            number = int(input("In: "))
        except ValueError:
            print("Sorry, only integer value.")
            continue
        else:
            print("Out: ", check_telephones(number, numbers))

if __name__ == '__main__':
    main()