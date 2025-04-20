import sys, cv2 as cv, numpy as np

ASCII_CHARS_NORMAL = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."] # 11 stopniowy gradient - najciemniejszy -> najjaśniejszy
ASCII_CHARS_REVERSED = ASCII_CHARS_NORMAL[::-1] 
DEFAULT_WIDTH = 120
ASPECT_RATIO = 0.5

def wpisywanie():
  
  while True:
    try:
      nazwa = input('Wprowadź lokalizację/nazwę obrazu:\n')

      if not nazwa:
        raise Exception('Należy podać lokalizację lub nazwę obrazu\n')
      
    except Exception as e:
      print(e)

    img_path = nazwa

    term_width = DEFAULT_WIDTH

    szerokosc = input('Podaj szerokość obrazu (zostaw puste jeżeli chcesz domyślne)\n')
    
    if szerokosc != '':
        try:
            term_width = int(szerokosc)

        except Exception:
            sys.exit("Szerokość musi być liczbą całkowitą")

    reverse = False
    odwrocone_kolory = input('Czy chcesz odwrócić kolory obrazu? (0 = Nie, 1 = Tak)\n')
    if odwrocone_kolory != '':
        try:
            reverse = bool(int(odwrocone_kolory))

        except Exception:
            sys.exit("Argument odwrócenia kolorów musi być 0 lub 1")

    ascii_chars = ASCII_CHARS_REVERSED if reverse else ASCII_CHARS_NORMAL

    return img_path, term_width, ascii_chars

def wczytanie_obrazu(img_path):
    img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
    if img is None:
        sys.exit(f"Nie można otworzyć pliku {img_path}")
    return img

def wlasciwosci_obrazu(term_width, img, ascii_chars):
    h, w = img.shape
    new_h = int(h * term_width / w * ASPECT_RATIO)
    img = cv.resize(img, (term_width, new_h), interpolation=cv.INTER_AREA)

    chars = np.array(list(ascii_chars))
    n_levels = len(chars)

    indices = (img / 255 * (n_levels - 1)).astype(np.int32)
    return indices, chars

def tworzenie_obrazu(indices, chars):
    for row in indices:
        print("".join(chars[p] for p in row))

def obraz_ascii():
    image_path, width, char_set = wpisywanie()
    image = wczytanie_obrazu(image_path)
    char_indices, ascii_characters = wlasciwosci_obrazu(width, image, char_set)
    tworzenie_obrazu(char_indices, ascii_characters)
