import sys, cv2 as cv, numpy as np, time


ASCII_CHARS_NORMAL = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."] # 11 stopniowy gradient - najciemniejszy -> najjaśniejszy
ASCII_CHARS_REVERSED = ASCII_CHARS_NORMAL[::-1] 
DEFAULT_WIDTH = 120
ASPECT_RATIO = 0.5


def wpisywanie(nazwa=None):
  while True:
    try:
      if nazwa is None:
        nazwa = input('Wprowadź lokalizację/nazwę filmu:\n')

      if not nazwa:
        raise Exception('Należy podać lokalizację lub nazwę filmu\n')
        
      
    except Exception as e:
      print(e)

    cap = cv.VideoCapture(nazwa)

    if not cap.isOpened():
        sys.exit("Nie można odtworzyć pliku wideo")

    docelowa_ilosc_fps = input('\nWprowadź docelową ilość klatek na sekundę (zostaw puste jeżeli chcesz domyślną ilość)\n')

    target_fps = float(docelowa_ilosc_fps) if docelowa_ilosc_fps != '' else cap.get(cv.CAP_PROP_FPS) or 24

    frame_time = 1 / target_fps

    odwrocone_kolory = input('Czy chcesz odwrócić kolory? (0 = Nie, 1 = Tak)\n')

    reverse = bool(int(odwrocone_kolory)) if odwrocone_kolory != '' else False

    ascii_chars = ASCII_CHARS_REVERSED if reverse else ASCII_CHARS_NORMAL

    petla = input('Czy chcesz odtworzyć nagranie w pętli? (0 = Nie, 1 = Tak)\n')

    loop = bool(int(petla)) if petla != '' else False



    return target_fps, frame_time, reverse, ascii_chars, cap, loop
  
    


term_clear = "\x1b[H\x1b[J" #łańcuch z dwiema sekwencjami ANSI czyszczące okno terminala i ustawiające kursor w lewym górnym rogu przed narysowaniem klatki

def czytaj_fps(cap):
    while True:
        st = time.time()
        ok, frame = cap.read()
        return st, ok, frame

def generowanie_filmu(frame_time, frame, st, ascii_chars):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    h, w = gray.shape
    new_h = int(h * DEFAULT_WIDTH / w * ASPECT_RATIO)
    gray = cv.resize(gray, (DEFAULT_WIDTH, new_h), interpolation=cv.INTER_AREA)

    idx = (gray / 255 * (len(ascii_chars)-1)).astype(np.uint8)
    ascii_frame = "\n".join("".join(ascii_chars[i] for i in row) for row in idx)

    print(term_clear + ascii_frame, end="", flush=True)

    dt = time.time() - st
    if dt < frame_time:
        time.sleep(frame_time - dt)


def odtworzenie_filmu(cap):
    return cap.release()


def film_ascii_jeden_raz(cap, frame_time, ascii_chars):
        while True:   
            st, ok, frame = czytaj_fps(cap)
            if not ok:
                break
            generowanie_filmu(frame_time, frame, st, ascii_chars)


def film_ascii_loop(cap, frame_time, ascii_chars):

        while True:
            cap.set(cv.CAP_PROP_POS_FRAMES, 0)

            while True:
                   
                st, ok, frame = czytaj_fps(cap)
                if not ok:
                    break
                generowanie_filmu(frame_time, frame, st, ascii_chars)

def film_ascii(nazwa=None):
    target_fps, frame_time, reverse, ascii_chars, cap, loop = wpisywanie(nazwa)

    try:
        if loop == 1:
            film_ascii_loop(cap, frame_time, ascii_chars)
        elif loop == 0:
            film_ascii_jeden_raz(cap, frame_time, ascii_chars)
    finally:
        odtworzenie_filmu(cap)
    

