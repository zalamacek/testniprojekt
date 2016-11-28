selected_num = int(raw_input("Vpisite stevilo od 1 do 100."))

for num in range(1, selected_num + 1):
    if (num % 3 == 0) and (num % 5 == 0): print("fizzbuzz")#ce je deljivo s 3, je ostanek 0; and dodaja pogoje
    elif num % 3 == 0: print("fizz")
    elif num % 5 == 0: print("buzz")
    else: print(num)
