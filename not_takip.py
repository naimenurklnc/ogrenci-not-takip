
import json
import os
if os.path.exists("ogrenciler.json"):
    with open("ogrenciler.json", "r", encoding="utf-8") as dosya:
        ogrenciler = json.load(dosya)
else:
    ogrenciler = []
def kaydet(veri):
    with open("ogrenciler.json", "w", encoding="utf-8") as dosya:
        json.dump(veri, dosya, ensure_ascii=False, indent=4)

def menu():
    print("\n--- Öğrenci Not Takip Sistemi ---")
    print("1- Öğrenci ekle")
    print("2- Not gir")
    print("3- Listele")
    print("4- Öğrenci sil")
    print("5- Çıkış")

def ogrenci_ekle():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")

    ogrenci = {
        "ad": ad,
        "soyad": soyad,
        "vize": None,
        "final": None
    }

    ogrenciler.append(ogrenci)
    kaydet(ogrenciler)
    print("Öğrenci eklendi ✅")

def not_gir():
    if not ogrenciler:
        print("Önce öğrenci eklemelisin.")
        return

    print("\n--- Not Gir (Vize / Final) ---")
    for i, ogrenci in enumerate(ogrenciler, start=1):
        def yazi(n):
            if n is None:
                return "Yok"
            if n == -2:
                return "Girmedi"
            return str(n)

        print(f"{i}. {ogrenci['ad']} {ogrenci['soyad']} "
              f"(Vize: {yazi(ogrenci['vize'])}, Final: {yazi(ogrenci['final'])})")

    secim = input("Not gireceğin öğrencinin numarası: ").strip()
    if not secim.isdigit():
        print("Numara girmelisin!")
        return

    idx = int(secim) - 1
    if idx < 0 or idx >= len(ogrenciler):
        print("Geçersiz öğrenci numarası!")
        return

    def not_al(etiket):
        s = input(f"{etiket} notu (0-100, -2 = girmedi): ").strip()
        try:
            n = int(s)
        except ValueError:
            print("Not sayı olmalı!")
            return None, False

        if not (0 <= n <= 100 or n == -2):
            print("Not 0-100 arasında ya da -2 olmalı!")
            return None, False

        return n, True

    vize, ok = not_al("Vize")
    if not ok:
        return

    final, ok = not_al("Final")
    if not ok:
        return

    ogrenciler[idx]["vize"] = vize
    ogrenciler[idx]["final"] = final

    kaydet(ogrenciler)
    print("Vize / Final kaydedildi ✅")

def ogrenci_sil():
    if not ogrenciler:
        print("Silinecek öğrenci yok.")
        return

    print("\n--- Öğrenci Sil ---")
    for i, ogrenci in enumerate(ogrenciler, start=1):
        print(f"{i}. {ogrenci['ad']} {ogrenci['soyad']}")

    secim = input("Silmek istediğin öğrencinin numarası: ").strip()
    if not secim.isdigit():
        print("Numara girmelisin!")
        return

    idx = int(secim) - 1
    if idx < 0 or idx >= len(ogrenciler):
        print("Geçersiz numara!")
        return

    silinen = ogrenciler.pop(idx)
    kaydet(ogrenciler)
    print(f"Silindi ✅: {silinen['ad']} {silinen['soyad']}")
def ortalama_hesapla(vize, final):
    # Henüz not girilmediyse
    if vize is None or final is None:
        return None

    # Sınava girmediyse
    if vize == -2 or final == -2:
        return -2

    return round(vize * 0.4 + final * 0.6, 2)

def ogrencileri_listele():
    if not ogrenciler:
        print("Henüz öğrenci yok.")
        return

    def yazi(n):
        if n is None:
            return "Yok"
        if n == -2:
            return "Girmedi"
        return str(n)

    print("\n--- Öğrenci Listesi ---")
    for i, ogrenci in enumerate(ogrenciler, start=1):
        vize = ogrenci.get("vize")   # yoksa None döner
        final = ogrenci.get("final")

        ort = ortalama_hesapla(vize, final)

        if ort is None:
            ort_yazi = "Yok"
        elif ort == -2:
            ort_yazi = "Girmedi"
        else:
            ort_yazi = str(ort)

        print(
            f"{i}. {ogrenci.get('ad', '')} {ogrenci.get('soyad', '')} | "
            f"Vize: {yazi(vize)} | Final: {yazi(final)} | Ortalama: {ort_yazi}"
        )




while True:
    menu()
    secim = input("Seçimin: ")

    if secim == "1":
        ogrenci_ekle()

    elif secim == "2":
        not_gir()

    elif secim == "3":
        ogrencileri_listele()

    elif secim == "4":
        ogrenci_sil()
        
    elif secim == "5": 
        print("Çıkılıyor...")

        break
    else:
        print("Geçersiz seçim!")
