# telephones = [380673406767, 2380673406767, 380673406767, 380673406767, 380675156060,380675156262]
numbers = ['380673406767', '2380673406767', '380673406767', '380673406767', '380675156060', '380675156262', '380675156262', '380675156262', '380675156262', '380675156262', '380675156262', '380675156262', '380675156262', '380675156262']

def check_telephones(start_with):
    result_out = []
    counter = 0
    for number in numbers:
        if number.startswith(str(start_with)):
            counter +=1
            result_out.append(int(number))
            if counter >= 10: break
    return result_out


while True:
    try:
        number = int(input("In: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
    else:
        print("Out: ", check_telephones(number))