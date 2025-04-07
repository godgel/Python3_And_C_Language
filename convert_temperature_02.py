# This Program was made to covert testing from Celsius to Fahrenheit And Vice Versa.
def conver_to_farenheit(celsius_temp):
    float(celsius_temp)
    temp_save_celsius = (celsius_temp*9/5+32)
    int(temp_save_celsius)
    return temp_save_celsius
print(" \n ================= From Celsius To Fahrenheit ================== \n ")
print( " \n Type Your Celsius Temparature : \n " )
celsius_temp = ''
temp_num = float(input(celsius_temp))
returned_temparature = conver_to_farenheit(temp_num)
print(f" \n You Input {temp_num} Celsius Degree. \n \n And Your Fahrenheit is {returned_temparature} \n \n ", temp_num, returned_temparature)

print(" \n ========= From Fahrenheit To Celsius ========== \n ")
def conver_to_celsius(fahrenheit_temp):
    float(fahrenheit_temp)
    temp_save_fahrenheit = float(((fahrenheit_temp-32)*5)/9)
    return temp_save_fahrenheit
print( " \n Type Your Fahrenheit Temparature : \n " )
fahrenheit_temp = ''
fahrenheit_temp = float(input(fahrenheit_temp))
returned_celsius_temparature = conver_to_celsius(fahrenheit_temp)
print(f" \n You Input {fahrenheit_temp} Fahrenheit Degree. \n \n And Your Celsius is {returned_celsius_temparature} \n \n ", fahrenheit_temp, returned_celsius_temparature)








