


def convert_if_needed(temp):
    is_f = input("Is this temp in Fahrenheit")
    if is_f.lower() == 'yes':
        return temp
    #it must be Celcius
    f_temp = temp * 9/5 + 32
    return f_temp


def main():
    temp= float(input("How warm was it today?"))
    f_temp = convert_if_needed(temp)
    print(f"Ok so the temp was {f_temp} fahrenheit")
main()