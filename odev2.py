import json

class Film:
    def __init__(self, filmadi, filmyili, yonetmen, tur):
        self.filmadi = filmadi
        self.filmyili = filmyili
        self.yonetmen = yonetmen
        self.tur = tur

def film_olustur():
    filmadi = input("Filminizin adı :: ")
    filmyili = input("Filminizin yılı :: ")
    yonetmen = input("Filminizin yönetmeni :: ")
    tur = input("Filminizin türü :: ")

    film = Film(filmadi, filmyili, yonetmen, tur)
    film_ekle(film)

def film_ekle(film):
    with open("filmler.json", "r") as file:
        filmler = json.load(file)

    filmler.append(vars(film))

    with open("filmler.json", "w") as file:
        json.dump(filmler, file)

def film_sil(filmadi):
    with open("filmler.json", "r") as file:
        filmler = json.load(file)

    yeni_filmler = [film for film in filmler if film['filmadi'] != filmadi]

    with open("filmler.json", "w") as file:
        json.dump(yeni_filmler, file)

def film_ara(filmadi):
    with open("filmler.json", "r") as file:
        filmler = json.load(file)

    bulunan_filmler = [film for film in filmler if film['filmadi'] == filmadi]

    if len(bulunan_filmler) > 0:
        print("Bulunan filmler ::")
        for film in bulunan_filmler:
            print(film['filmadi'], film['filmyili'], film['yonetmen'], film['tur'])
    else:
        print("Film bulunamadı !!")

def filmleri_goster():
    with open("filmler.json", "r") as file:
        filmler = json.load(file)

    for film in filmler:
        print(film['filmadi'], film['filmyili'], film['yonetmen'], film['tur'])

def menu_goster():
    print("\nFilm App")
    print(":: 1. Filmleri göster ::")
    print(":: 2. Film ekle ::")
    print(":: 3. Film sil ::")
    print(":: 4. Film ara ::")
    print(":: 5. Çıkış ::")

while True:
    menu_goster()
    secim = input("\n:: Bir işlem seçin (1-5) :: ")

    if secim == "1":
        print("\nFilmler ::")
        filmleri_goster()
    elif secim == "2":
        print("\nFilm ekle ::")
        film_olustur()
    elif secim == "3":
        print("\nFilm sil")
        filmAdi = input("Silmek istediğiniz film adı :: ")
        film_sil(filmAdi)
    elif secim == "4":
        print("\nFilm ara")
        filmAdi = input("Bulmak istediğiniz film adı ::")
        film_ara(filmAdi)
    elif secim == "5":
        print("\nÇıkılıyor.")
        break
    else:
        print("\nBaşarısız. Tekrar deneyin.")