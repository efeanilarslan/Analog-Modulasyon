# 📡 Analog Modülasyon Laboratuvarı (AM, FM, PM Simülasyonu & Spektral Analiz)

Bu proje; analog haberleşme sistemlerinin temelini oluşturan **Genlik Modülasyonu (AM)**, **Frekans Modülasyonu (FM)** ve **Faz Modülasyonu (PM)** tekniklerinin Python ortamında matematiksel olarak modellenmesi, zaman ve frekans domenindeki (FFT) davranışlarının simüle edilmesi ve karşılaştırmalı güç/spektrum analizlerinin gerçekleştirilmesi amacıyla geliştirilmiştir.

---

## 🎯 Projenin Amacı ve Öne Çıkan Özellikleri

- **Fourier Serisi ile Mesaj Sinyali Sentezi:** Kare dalga mesaj sinyali doğrudan hazır fonksiyonlar yerine, Fourier serisi açılımı kullanılarak **9999 tekil harmonik** toplanarak matematiksel olarak sıfırdan sentezlenmiştir.
- **Diferansiyel ve İntegral Bazlı Modülasyon:** FM sinyalinin faz açısı için mesaj sinyalinin analitik integrali eş zamanlı hesaplanarak sürekli faz (continuous phase) korunmuş, PM sinyalinde ise doğrudan faz modülasyonu uygulanarak faz sıçramaları incelenmiştir.
- **FFT Spektral Analiz:** Hızlı Fourier Dönüşümü (Fast Fourier Transform - FFT) ile sinyallerin frekans spektrumları ve yan bantları (sidebands) incelenmiştir.
- **Carson Kuralı & Bant Genişliği Doğrulaması:** FM spektrumunda enerjinin yoğunlaştığı sınırlar teorik Carson kuralı hesaplarıyla karşılaştırılmıştır.
- **Sabit Zarf (Constant Envelope) & Güç Analizi:** AM'de yan bantlara güç aktarımı dolayısıyla toplam gücün artışı ile FM/PM'de zarf genliğinin sabit kalması sonucu taşıyıcı gücünün korunması deneysel olarak doğrulanmıştır.

---

## 📐 Matematiksel Modelleme & Teori

### 1. Kare Dalga Mesaj Sinyali (Fourier Yaklaşımı)
Kare dalga mesaj sinyali $s_m(t)$, tekil harmoniklerin süperpozisyonu ile oluşturulmuştur:
$$s_m(t) = \sum_{n=1, 3, 5, \dots}^{9999} \frac{A_m}{n} \sin(2\pi n f_m t) \cdot \frac{4}{\pi}$$

### 2. Genlik Modülasyonu (AM)
$$s_{AM}(t) = \left[1 + \mu \cdot \frac{s_m(t)}{A_m}\right] A_c \cos(2\pi f_c t)$$
- **Modülasyon Verimi:** Yan bantlardaki bilgi taşıyan gücün toplam güce oranı hesaplanır:
$$\eta = \frac{P_{sidebands}}{P_{AM}} \times 100$$

### 3. Frekans Modülasyonu (FM)
FM sinyalinde anlık frekans mesaj sinyali ile orantılı değişir. Faz açısı mesajın integraliyle hesaplanır:
$$s_{FM}(t) = A_c \cos\left(2\pi f_c t + 2\pi k_f \int_0^t s_m(\tau) d\tau\right)$$
- **Carson Kuralı (Bant Genişliği):**
$$B_{FM} \approx 2 f_m (\beta + 1)$$
- Kare dalganın integrali kesintisiz bir üçgen dalga olduğundan, FM faz açısında ani kırılmalar görülmez; anlık frekans mesajın işaretine göre iki seviye ($f_c \pm \Delta f$) arasında geçiş yapar.

### 4. Faz Modülasyonu (PM)
$$s_{PM}(t) = A_c \cos(2\pi f_c t + k_p s_m(t))$$
- Kare dalganın dikey geçiş anlarında ($+A_m \to -A_m$) faz açısı anlık olarak basamak adımı yapar. Bu durum sinyalde belirgin **Faz Sıçraması (Phase Shift)** kırılmalarına yol açar.

---

## 📊 Grafik ve Simülasyon Çıktıları

Kod çalıştırıldığında Matplotlib arayüzü üzerinde aşağıdaki analiz pencereleri oluşturulur:

1. **Mesaj ve Taşıyıcı Sinyali:** 9999 harmonikli kare dalga mesajı ($s_m(t)$) ve yüksek frekanslı taşıyıcı sinüs dalgası ($s_c(t)$).
2. **AM Zaman Domeni & Spektrumu:** Genlik modülasyonu zarfı ve çift taraflı FFT genlik spektrumu.
3. **FM Zaman Domeni & Spektrumu:** Frekans modülasyonlu sinyal ve Carson bant genişliğine oturan yan bant spektrumu.
4. **PM Zaman Domeni & Spektrumu:** Faz modülasyonlu sinyal ve geniş spektral saçılım.
5. **PM Faz Sıçraması Detay İncelemesi (Zoom):** Kare dalganın geçiş kenarlarında oluşan ani faz zıplamalarının büyütülmüş analizi.
6. **FM Frekans Değişimi Detay İncelemesi (Zoom):** Mesajın pozitif ve negatif yarı periyotlarında frekansın sıkışma ($f_c + \Delta f$) ve gevşeme ($f_c - \Delta f$) hareketleri.
7. **Karşılaştırmalı Eşzamanlı Görünüm:** AM, FM ve PM sinyallerinin aynı zaman penceresinde doğrudan karşılaştırılması.

---

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.8 veya üzeri
- `numpy`
- `matplotlib`

### Adımlar

1. Depoyu klonlayın:
```bash
git clone https://github.com/KULLANICI_ADINIZ/analog-modulasyon-lab.git
cd analog-modulasyon-lab
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install numpy matplotlib
```

3. Simülasyonu çalıştırın:
```bash
python lab.py
```

---

## 📁 Proje Dosya Yapısı

```text
├── lab.py              # Fourier serisi, AM/FM/PM modülasyonu ve FFT analiz kodları
├── Rapor.pdf           # Deney sonuçları, grafik yorumları ve teorik soru çözümleri
├── .gitignore          # Git tarafından izlenmeyecek geçici dosya ve sanal ortam tanımları
└── README.md           # Proje belgelendirmesi
```

---

## 👤 Hazırlayan

- **Efe Anıl Arslan**
- Haberleşme Mühendisliği / Analog Haberleşme Laboratuvarı
