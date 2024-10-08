def check_a(string):
    count = string.lower().count('a')
    if count > 0:
        print(f"A letra 'a' aparece {count} vezes na palavra {string}.")
    else:
        print(f"A letra 'a' não aparece na palavra {string}.")

check_a("Anticonstitucionalissimamente")
check_a("Python")
