cd ~/ros2_ws/src/sicaklik_izleyici_py
cat << 'EOF' > README.md
# 🌡️ Sıcaklık İzleyici (sicaklik_izleyici_py)

Bu proje, **ROS 2 (Humble)** kullanılarak geliştirilmiş bir sıcaklık izleme sistemidir. Rastgele sıcaklık verisi üreten bir yayıncı (publisher) ve bu veriyi anlık olarak takip eden bir abone (subscriber) düğümünden oluşur.

## ✨ Özellikler
- **Gerçek Zamanlı Veri:** `/sicaklik` konusuna saniyede bir adet 20°C - 40°C arası rastgele `Float32` veri yayınlar.
- **Anlık Takip:** Abone düğümü gelen veriyi konsola yazdırır.
- **Akıllı Uyarı Sistemi:** Sıcaklık 30°C'yi aştığında `WARN` seviyesinde uyarı verir.
- **Parametrik Kontrol (Bonus):** Uyarı eşik değeri `declare_parameter` ile dinamik hale getirilmiştir.

## 🛠️ Kurulum
Projeyi kendi ROS 2 workspace'inize klonlayın ve derleyin:

```bash
cd ~/ros2_ws/src
git clone https://github.com/furkanortatepe/sicaklik_izleyici_py.git
cd ~/ros2_ws
colcon build --packages-select sicaklik_izleyici_py
source install/setup.bash
