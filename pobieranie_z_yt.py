from yt_dlp import YoutubeDL
import sys, pathlib, shutil, os

def pobieranie_url_od_uzytkownika():
    link_do_filmu = input('Wklej URL filmu Youtube (musi być on publiczny)\n')
    if link_do_filmu != '':
        url = link_do_filmu
    else:
        sys.exit("Należy podać URL filmu!")

    return url

def opcje_pobierania():
    ydl_opcje = {
        "outtmpl": "%(title)s.%(ext)s",
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "progress_hooks": [lambda d: print(f"{d['_percent_str']} {d['status']}")],
    }

    return ydl_opcje

def pobieranie_filmu(url, ydl_opcje):
    with YoutubeDL(ydl_opcje) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    return filename


def pobieranie_filmu_z_yt():
    url = pobieranie_url_od_uzytkownika()
    ydl_opcje = opcje_pobierania()
    file_path = pobieranie_filmu(url, ydl_opcje)
    return file_path

def usuwanie_filmu(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)