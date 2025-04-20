# GrASCII

Jest to prosty skrypt zamieniający plik graficzny bądź wideo w znaki ASCII, który wyświetla się w konsoli. 
Można otworzyć pliki lokalne, bądź po wybraniu opcji filmu z Youtube'a wkleić link który przekonwertuje dany film (musi on być publiczny i nie może być live'm)

Aby skorzystać ze skryptu należy w folderze uruchomić za pomocą pythona plik "GrASCII.py". Otworzy się wtedy menu z którego można wybrać daną opcję lub opuścić program.
Skrypt może zawierać parę bug'ów takich jak brak obsługi niektórych wyjątków w inputach, jednak w następnym patchu to poprawię. 
W celu opuszczenia odtworzonego filmu należy wcisnąć CTRL + C, wtedy się powróci do menu głównego.

Do pobierania filmów z Youtube wykorzystałem bibliotekę yt_dlp. W kodzie też użyte są biblioteki cv2 i numpy.

W planach mam możliwość eksportowanie obrazu do pliku tekstowego, konwertowanie zwykłego tekstu do ascii-art oraz wybór języka (Polski/Angielski)
