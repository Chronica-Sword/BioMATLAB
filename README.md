# BioMATLAB - Biyoinformatik Kodlama Eğitimi

BioMATLAB, biyoloji ve bilgisayar bilimlerinin kesişim noktası olan biyoinformatik alanını MATLAB/Octave programlama dillerini kullanarak öğretmeyi amaçlayan etkileşimli bir web platformudur.

## 🌟 Özellikler
- **Kapsamlı Müfredat**: Başlangıç (20), Orta (20) ve İleri (10) seviyede toplam 50 özel biyoinformatik problemi.
- **İnteraktif Kod Editörü**: MATLAB/Octave uyumlu kod yazma alanı.
- **Detaylı Çözümler ve Anlatım**: Her problemin örnek çözümü, beklenen çıktısı ve derinlemesine konu anlatımı/çözüm yaklaşımı.
- **Modern ve Duyarlı Arayüz**: Cam morfizması (glassmorphism) esintili, karanlık mod odaklı modern tasarım.
- **Veri Üretim Scriptleri**: Problemleri ve verileri dinamik oluşturmak için kullanılan Python scriptleri (`gen_adv_*.py`, `gen_int_*.py`).

## 📂 Dosya Yapısı
- `index.html`: Uygulamanın ana arayüz yapısı.
- `style.css`: Modern karanlık mod stil tanımlamaları.
- `app.js`: Görünümler arası geçişleri ve problem yükleme mantığını yöneten JavaScript dosyası.
- `data.js`: Tüm problemleri, açıklamaları, çözümleri ve beklenen çıktıları içeren veri veri tabanı.
- `generate_data_v*.py`: JavaScript veri dosyasını (`data.js`) otomatik derlemek/üretmek için yazılmış Python kodları.

## 🚀 Nasıl Çalıştırılır?
Uygulama tamamen statik web teknolojileriyle geliştirilmiştir (HTML, CSS, JS). Çalıştırmak için:
1. Projeyi indirin.
2. `index.html` dosyasına çift tıklayarak tarayıcınızda açın. Herhangi bir sunucu kurulumu gerektirmez.
