cd ~/ros2_ws/src/sicaklik_izleyici_py
cat << 'EOF' > README.md
# 🌡️ Sıcaklık İzleyici (sicaklik_izleyici_py)

<p align="center">
  <img src="https://img.shields.io/badge/ROS2-Humble-blue?style=for-the-badge&logo=ros" alt="ROS2 Humble"/>
  <img src="https://img.shields.io/badge/Python-3.10-yellow?style=for-the-badge&logo=python" alt="Python 3.10"/>
  <img src="https://img.shields.io/badge/Lisans-Apache--2.0-green?style=for-the-badge" alt="Apache 2.0"/>
  <img src="https://img.shields.io/badge/Durum-Tamamlandı-brightgreen?style=for-the-badge" alt="Durum"/>
</p>

Bu proje, **ROS 2 (Humble)** kullanılarak geliştirilmiş bir sıcaklık izleme sistemidir. Sistem, iki temel ROS 2 düğümünden (node) oluşur:

1. **Yayıncı (Publisher) — `sensor.py`:** Saniyede bir adet 20°C ile 40°C arasında rastgele sıcaklık verisi üretir ve `/sicaklik` konusuna (`Float32` mesaj tipiyle) yayınlar.
2. **Abone (Subscriber) — `izleyici.py`:** `/sicaklik` konusunu dinler, gelen değeri konsola yazdırır ve değer belirlenen eşik değerinin (varsayılan 30°C) üzerine çıktığında `get_logger().warn()` ile uyarı verir.

Bu proje, ROS 2'de **paket oluşturma**, **düğüm yazma**, **konu (topic) üzerinden haberleşme**, **logger kullanımı** ve **parametre (parameter) tanımlama** gibi temel kavramları uygulamalı olarak göstermektedir.

---

## 📸 1. Sistem Mimarisi ve Donanım Temsili

> **Not:** Bu projede sıcaklık verisi yazılımsal olarak simüle edilmektedir. Aşağıdaki görsel, sistemin gerçek donanım (Arduino + LM35/DHT11 sıcaklık sensörü) ile nasıl entegre edilebileceğini **temsili olarak** göstermektedir.

<p align="center">
  <img src = "https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3e/16x2_LCD_Arduino_LM35_temperature_sensor.svg/960px-16x2_LCD_Arduino_LM35_temperature_sensor.svg.png?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail">
</p>
---

GEREKEN ÇALIŞTIRMA KODLARINI SİZ VERDİNİZ HOCAM ZATEN. 

## Çalıştırma

```bash
source ~/ros2_ws/install/setup.bash
ros2 run sicaklik_izleyici_py sensor
source ~/ros2_ws/install/setup.bash
ros2 run sicaklik_izleyici_py izleyici
source ~/ros2_ws/install/setup.bash
rqt_graph
## 🧩 2. Veri Akış Diyagramı

Aşağıdaki diyagram, sistemin uçtan uca veri akışını göstermektedir. Sensörden okunan verinin ROS 2 düğümleri arasında nasıl hareket ettiğini adım adım görebilirsiniz:

```mermaid
graph LR
    A[🌡️ Sensör / Arduino<br/>Sıcaklık Okuma] -->|1. Veri| B[📤 sensor.py<br/>ROS 2 Yayıncı]
    B -->|2. /sicaklik Konusu<br/>Float32 Mesaj| C[📥 izleyici.py<br/>ROS 2 Abone]
    C -->|3. Ekran / Uyarı| D[💻 Terminal Çıktısı]
    
