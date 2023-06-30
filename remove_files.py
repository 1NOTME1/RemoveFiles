import os

filename = "pliki_do_usuniecia.txt"

with open(filename, "r") as file:
    for line in file:
        path = line.strip()
        if os.path.isfile(path):
            try:
                os.remove(path)
                print(f"Plik {path} został usunięty.")
            except OSError as e:
                print(f"Nie można usunąć pliku {path}. Błąd: {e}")
        else:
            print(f"Plik {path} nie istnieje.")
