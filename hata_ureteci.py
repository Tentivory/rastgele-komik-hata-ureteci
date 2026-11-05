#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Abartılı Komik Hata Mesajı Üreteci
Çalışır mı? Evet. Mantıklı mı? Hayır. Gerekli mi? Asla.
"""

import random
import time

hatalar = [
    "Hata 404: Bu hata mesajı kendisini kaybetti.",
    "Kritik Hata: Program çok düşündü ve bayıldı.",
    "Uyarı: Değişkenleriniz duygusal kriz geçiriyor.",
    "Hata 500: Sunucu çay molasına çıktı, geri dönmeyecek.",
    "SyntaxError: Kodunuz Türkçe konuşmaya çalıştı, başarısız oldu.",
    "IndexError: Liste, varolışsal sorgulama yaptı ve kayboldu.",
    "TypeError: Bu veri tipi 'hayatım' tipi değil, 'kaos' tipi.",
    "Hata: Sonsuz döngü, ama bu sefer bilinçli olarak.",
    "MemoryError: RAM'iniz anılarınızla doldu, yer kalmadı.",
    "Hata 42: Hayatın anlamı bulundu, ama bu programda değil.",
    "PermissionDenied: Bu hataya erişim izniniz yok, çünkü hata da istemiyor.",
    "Hata: Kodunuz o kadar kötü ki, Python bile utanıyor."
]

def hata_uret(adet=5):
    print("=== KOMİK HATA ÜRETİCİSİ ÇALIŞIYOR ===")
    print("(Gerçekten çalışıyor, inanamıyorsanız çalıştırın)\n")
    
    for i in range(adet):
        hata = random.choice(hatalar)
        print(f"[{i+1}] {hata}")
        time.sleep(0.5)  # Dramatik etki için
    
    print("\n=== ÜRETİM TAMAMLANDI ===")
    print("Bu hataları ciddiye almayın. Alırsanız sizin sorununuz.")

if __name__ == "__main__":
    try:
        adet = int(input("Kaç tane komik hata istiyorsunuz? (varsayılan 5): ") or 5)
        hata_uret(adet)
    except:
        print("Hata: Girdiğiniz sayı bile hatalı. Varsayılan kullanılıyor.")
        hata_uret()
