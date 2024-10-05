import random
from itertools import combinations  # itertools kütüphanesini ekledik

# Oyun başlangıcını gösteren bir değişken tanımlıyoruz (Bu satır bir etkiye sahip değil)
Başlangıç = print()

# Zar atma fonksiyonu
def zar_at():
    return random.randint(1, 6), random.randint(1, 6)

# Kullanıcının kapatmak istediği sayıları kontrol eden fonksiyon
def geçerli_mi(seçimler, yüzler):
    # Seçilen sayıların tahtadaki mevcut sayılar arasında olup olmadığını kontrol eder
    return all(seçim in yüzler for seçim in seçimler)

# Oyun fonksiyonu
def oyunu_oyna():
    yüzler = list(range(1, 10))  # 1'den 9'a kadar olan sayılar

    # Yüzler listesinde sayı olduğu sürece oyunu devam ettir
    while len(yüzler) > 0:
        zar1, zar2 = zar_at()
        toplam = zar1 + zar2
        print(f"Mevcut yüzler: {yüzler}")
        print()
        print(f"Zar sonucu: {zar1} ve {zar2} = {toplam}")
        print()
        
        # Kullanıcıdan hangi sayıları kapatmak istediğini al
        while True:
            try:
                seçim_girdisi = input(f"Toplam {toplam} olacak şekilde hangi sayıları kapatmak istersin? (Örn: 1,2): ")
                seçimler = list(map(int, seçim_girdisi.split(',')))
                
                # Kullanıcı seçimlerinin toplamı zar toplamına eşit mi ve geçerli mi kontrol et
                if sum(seçimler) == toplam and geçerli_mi(seçimler, yüzler):
                    for seçim in seçimler:
                        yüzler.remove(seçim)
                    print()
                    print(f"Kapatılan sayılar: {seçimler}")
                    break
                else:
                    print(f"Lütfen {toplam} olacak geçerli sayılar girin.")
            except ValueError:
                print("Geçerli bir giriş yapmadınız, lütfen tekrar deneyin.")

        # Geçerli hamle var mı kontrol et (çift kombinasyonlar ve tekli seçimler)
        if not any(sum(çift) == toplam for çift in combinations(yüzler, 2)) and toplam not in yüzler:
            print("Oyun bitti! Daha fazla hamle yok.")
            break

    # Oyun bittiğinde tüm sayılar kapatıldı mı kontrol et
    if len(yüzler) == 0:
        print("Tebrikler! Tüm sayıları kapattınız.")
    else:
        print("Kalan sayılar: ", yüzler)

# Oyunu başlat
oyunu_oyna()
