n = int(input("vvedite kol_vo chisel: "))

count_zeros = 0

for i in range (n):
    number = int(input(f"Vvedite chislo {i+1}: "))
    if number == 0:
        count_zeros += 1

print("kol_vo null:", count_zeros)