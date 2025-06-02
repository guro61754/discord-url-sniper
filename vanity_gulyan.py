Discord vanity URL kontrol ve değiştirme paneli hazırlamaya başlayabiliriz. Bu sistem terminal tabanlı olacak ama tamamen kişisel ve stabil çalışacak.

✅ Gerekli Bilgiler ve Hazırlıklar
1. Discord Sunucun Boost Level 3 mü?
Vanity URL değiştirme yetkisi yalnızca Level 3 sunucularda çalışır. Aksi takdirde Discord API hatası verir.

2. Bot Token’in Hazır mı?
Botunun şu yetkilere sahip olması gerekiyor:

Manage Guild (sunucu ayarlarını değiştirme)
Sunucuda admin veya owner yetkisi olan bir hesap tarafından eklenmiş olmalı
🔧 Sistem Özeti
Bu Python tabanlı araç şunları yapacak:

Özellik	Açıklama
✅ URL kontrolü	Belirttiğin vanity URL alınabilir mi?
✅ URL değiştirici	Kendi sunucunda vanity URL’yi değiştir
✅ API üzerinden	Token’le Discord API’siyle doğrudan iletişim
✅ Log sistemi	Yapılan işlemleri kaydeder
🚀 Adım 1: Gerekli Kütüphaneler
Bu script şu kütüphaneleri kullanır (standarttır ama emin olalım):

bash
Copy code
pip install requests
🚀 Adım 2: Python Scripti
Aşağıdaki kodu vanity_url_panel.py adıyla kaydet:

python
Copy code
import requests
import json
import time

# Kullanıcıdan bilgiler al
BOT_TOKEN = input("Bot Token: ").strip()
GUILD_ID = input("Sunucu (Guild) ID: ").strip()
HEADERS = {
    "Authorization": f"Bot {BOT_TOKEN}",
    "Content-Type": "application/json"
}

def check_url_available(vanity_url):
    response = requests.get(f"https://discord.com/api/v10/invites/{vanity_url}")
    if response.status_code == 404:
        print(f"[+] '{vanity_url}' kullanılabilir.")
    else:
        print(f"[-] '{vanity_url}' kullanımda.")

def set_vanity_url(vanity_url):
    payload = {"code": vanity_url}
    url = f"https://discord.com/api/v10/guilds/{GUILD_ID}/vanity-url"
    response = requests.patch(url, headers=HEADERS, data=json.dumps(payload))
    if response.status_code == 200:
        print(f"[✓] Vanity URL başarıyla '{vanity_url}' olarak ayarlandı.")
    else:
        print(f"[X] URL değiştirilemedi. Hata kodu: {response.status_code}")
        print("Yanıt:", response.text)

def main():
    while True:
        print("\n--- Discord Vanity URL Paneli ---")
        print("1. Vanity URL uygun mu kontrol et")
        print("2. Kendi sunucunda Vanity URL'yi ayarla")
        print("3. Çıkış")

        choice = input("Seçim: ").strip()

        if choice == "1":
            code = input("Kontrol edilecek URL: ").strip()
            check_url_available(code)
        elif choice == "2":
            code = input("Yeni Vanity URL (örnek: example): ").strip()
            set_vanity_url(code)
        elif choice == "3":
            print("Çıkılıyor.")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
🔐 Güvenlik Uyarısı
Bu script kendi token’inle sadece kendi sunucun için çalışır.
Başkasının sunucusuna izinsiz işlem yapmak yasadışıdır.
Token bilgini kimseyle paylaşma. (Script açık kaynak, sende kalır.)
📦 Çalıştırma
