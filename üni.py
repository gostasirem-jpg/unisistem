import sys
YESIL="\033[32m"
KIRMIZI="\033[31m"
MAVI="\033[34m"
SIYAH_BEYAZ="\033[30;47m"
RESET="\033[0m"
dersler = ["Türkçe","Tarih","Matematik","Veri Bilimi","Toplam Kalite Yönetimi","Veri Gizliliği ve Güvenliği","Yapay Zeka","Programlama","İngilizce"]

print(f"{SIYAH_BEYAZ} TÜRK HAVA KURUMU ÜNİVERSİYESİ{RESET}")
print(f"{SIYAH_BEYAZ}   *NOT HESAPLAMA SİSTEMİ*    {RESET}")
print("."*30)

for ders in dersler:
    print(f"\n{MAVI}>>> {ders} Dersi İçin Notları Gir:{RESET}")
    
    if vize<0:
        print(f"{KIRMIZI}Eksi not girildi. Sistemden çıkılıyor...{RESET}")
        break

    final=int(input("Final notu: "))
    if final<0:
        print(f"{KIRMIZI}Eksi not girildi. Sistemden çıkılıyor...{RESET}")
        break

    ortalama=(vize * 0.4)+(final * 0.6)
    
    if ortalama>=90:
        harf_notu="AA"

    elif ortalama>=85:
        harf_notu="BA"

    elif ortalama>=80:
        harf_notu="BB"

    elif ortalama>=75:
        harf_notu="CB"

    elif ortalama>=70:
         harf_notu="CC"

    elif ortalama>=65:
        harf_notu="DC"

    elif ortalama>=60:
        harf_notu="DD"

    elif ortalama>=50:
        harf_notu="FD"

    else:
        harf_notu="FF"
        
    if ortalama>=45:
        print(f"{YESIL}Ortalama: {ortalama:.2f} - GEÇTİN{RESET}")
    else:
        print(f"{KIRMIZI}Ortalama: {ortalama:.2f} - KALDIN{RESET}")

    print(f"Harf Notunuz: {harf_notu}")

print(f"\n{SIYAH_BEYAZ} İşlem Tamamlandı. {RESET}")

