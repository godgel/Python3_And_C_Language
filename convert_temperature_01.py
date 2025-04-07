# This Program was made to covert testing from Celsius to Fahrenheit And Vice Versa.

def conver_to_farenheit(celsius_temp):
    int(celsius_temp)
    temp_save_celsius = (celsius_temp*9/5+32)
    int(temp_save_celsius)
    return temp_save_celsius

print( " \n Type Your Celsius Temparature : \n " )

celsius_temp = ''

temp_num = int(input(celsius_temp))

returned_temparature = conver_to_farenheit(temp_num)

print(f" \n You Input {temp_num} Degree. \n \n And Your Fahrenheit is {returned_temparature} \n \n ", temp_num, returned_temparature)







