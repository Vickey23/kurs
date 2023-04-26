imie = input("Podaj imie: ")
wiek = int(input("Podaj wiek: "))
wiek_p = 32

if wiek < wiek_p:
    print(f"Mów mi Python, mam {wiek_p} lat. Witaj w moim świecie {imie}. Jesteś ode mnie młodszy.")
else:
    print(f"Mów mi Python, mam {wiek_p} lat. Witaj w moim świecie {imie}. Jesteś ode mnie starszy.")
