'''
Program który potrafi przekonwertować obraz lub plik wideo w jego odpowiednik w ASCII
'''

import obraz_a, film_a, pobieranie_z_yt, sys

def menu():
    while True:

        wybor = input('Wybierz opcje:\n1 - Generowanie obrazu\n2 - Generowanie filmu lokalnie\n3 - Generowanie filmu z Youtube\n4 - Wyjście\n')

        try:
            wybor = int(wybor)
        except Exception:
            print('Niepoprawna wartość. Proszę wybrać numer opcji\n')
            continue

        if wybor == 1:
            obraz_a.obraz_ascii()
            break
            
        elif wybor == 2:
            try:
                film_a.film_ascii()
            except KeyboardInterrupt:
                print("\nZatrzymano odtwarzanie!")


        elif wybor == 3:
            
            file_path = pobieranie_z_yt.pobieranie_filmu_z_yt()

            try:
                film_a.film_ascii(nazwa=file_path)
            
            except KeyboardInterrupt:
                pobieranie_z_yt.usuwanie_filmu(file_path)
                print("\nZatrzymano odtwarzanie!")
                
        
        elif wybor == 4:
            print("\nDziękuję za skorzystanie z programu!")
            sys.exit(1)
        else:
            print('\nNiepoprawne dane, spróbuj ponownie')
menu()