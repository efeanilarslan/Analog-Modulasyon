import numpy as np
import matplotlib.pyplot as plt
ogr_no = '233251015'
a = int(ogr_no[4]) #5
b = int(ogr_no[6]) #0
c = int(ogr_no[8]) #5
fm = 10+a
fc = 100 + 5*b
am = 1 + c/10
ac = 5
mu = am/ac
beta = 1 + a/5 #2
kp = 1 + b/5
kf = (beta * fm)/am #frekans duyarlılığı
dalga_suresi  = 1

#Ölçüm yapabilmek için, her girilen sinyale uyacak örnekleme frekansı hazırlama
f_orn = fm*fc*10/3
#bizden istenen 5000 değerini karşılıyor ve olası bir değişiklikte grafiği hala okunabilir yapıyor
ornek_noktalar_arasi_periyot = 1/f_orn
toplam_ornek_noktalar = int(f_orn*dalga_suresi)
noktalar = toplam_ornek_noktalar + 1
t = np.arange(noktalar)*ornek_noktalar_arasi_periyot
#burada t, 0 dan toplam_ornek_noktalar + 1 e giderken(noktalar=5001) aradaki periyot ile çarpılır ve t eksenindeki değerler belirlenmiş olur

s_sin = am*np.sin(2*np.pi*fm*t)
#sinüs dalgası
s_m = s_sin*(4/np.pi)
#sinüs ile elde edilecek olan kare dalganın 1.katı
m_integral = -1 * am * (4 / np.pi) * (1 / (2 * np.pi * fm)) * np.cos(2 * np.pi * fm * t)
#sinyalin 1.katının integrali alınır, ileride tekrar aynı döngüyü açmaktansa tek döngüde halledilir
for i in range(3,9999,2):
    s_m += (am/i)*np.sin(2*np.pi*fm*t*i)*(4/np.pi)
    #görüldüğü gibi 9999 sayısına kadar tek olan harmonik dalgaları ana dalgaya ekleyerek sonucunda kare dalga üretiliyor
    m_integral += -(am / i) * (4 / np.pi) * (1 / (2 * np.pi * i * fm)) * np.cos(2 * np.pi * fm * t * i)
    #1. katın integrali ile tek sayıdaki harmoniklerinin integralleri toplanıp, mesaj sinyalinin integrali bulunur
s_m
#mesaj sinyali
s_c = ac*np.cos(2*np.pi*fc*t)
#taşıyıcı sinyal
s_am = (1 + mu * (s_m / am)) * s_c
#analog modülasyonu
s_fm = ac * np.cos(2 * np.pi * fc * t + 2 * np.pi * kf * m_integral)
#frekans modülasyonu için önce sinyalin integrali bulunur ve genel formül uygulanır
s_pm = ac * np.cos(2 * np.pi * fc * t + kp * s_m)
#faz modülasyonu

#frekans domaini
N = len(t)
f = np.arange(-N/2, N/2) * (f_orn / N)
fft_am = np.fft.fftshift(np.fft.fft(s_am)) / N
fft_fm = np.fft.fftshift(np.fft.fft(s_fm)) / N
fft_pm = np.fft.fftshift(np.fft.fft(s_pm)) / N

#güç , verim ve bant genişliği
p_m  = np.mean(s_m**2)
p_c  = np.mean(s_c**2)
p_am = np.mean(s_am**2)
p_fm = np.mean(s_fm**2)
p_pm = np.mean(s_pm**2)
p_sidebands = p_am - p_c
am_verim = (p_sidebands / p_am) * 100 #genlik modülasyonu verimi
b_am = 2 * fm
b_fm = 2 * fm * (beta + 1) #Carson kuralı
print(f"Modülasyon Verimliliği (AM Verimi): %{am_verim:.2f}")
print(f"AM Bant Genişliği : {b_am} Hz")
print(f"FM Bant Genişliği : {b_fm} Hz")
print(f"Mesaj Sinyali Ortalama Gücü : {p_m:.4f} W")
print(f"Taşıyıcı Sinyali Ortalama Gücü : {p_c:.4f} W")
print(f"AM Sinyali Toplam Gücü : {p_am:.4f} W")
print(f"FM Sinyali Toplam Gücü : {p_fm:.4f} W")
print(f"PM Sinyali Toplam Gücü : {p_pm:.4f} W")
#fm frekans değişimi gözlemi için
t_transition = 1 / (2 * fm)
window = 0.02
idx_fm = np.where((t >= t_transition - window) & (t <= t_transition + window))[0]
#gözlemlenebilmesi için beta değeri değiştirilmiş fm sinyali
beta_vis = beta*4 #beta_vis değeri istenilen 8 değerini karşılıyor
kf_vis = (beta_vis * fm) / am
s_fm_vis = ac * np.cos(2 * np.pi * fc * t + 2 * np.pi * kf_vis * m_integral)
#pm faz sıçraması gözlemi için
idx_pm = np.where((t >= t_transition - window) & (t <= t_transition + window))[0]

#grafik kısmı
fig, axs = plt.subplots(2, 1, figsize=(15,8))
axs[0].plot(t, s_m, linewidth=1.5)
axs[0].set_title("Kare Dalga Mesaj Sinyali - Ogrenci No: " + ogr_no)
axs[0].set_xlabel("Zaman (s)")
axs[0].set_ylabel("Genlik")
axs[0].grid(True)
axs[1].plot(t, s_c, linewidth=1.5)
axs[1].set_title("Tasiyici Sinyal - Ogrenci No: " + ogr_no)
axs[1].set_xlabel("Zaman (s)")
axs[1].set_ylabel("Genlik")
axs[1].grid(True)
#istenen ilk iki grafik

fig1, axs1 = plt.subplots(2, 1, figsize=(15, 8))
axs1[0].plot(t, s_am, linewidth=1.5)
axs1[0].set_title("Genlik Modülasyonu Sinyali - Ogrenci No: " + ogr_no)
axs1[0].set_xlabel("Zaman (s)")
axs1[0].set_ylabel("Genlik")
axs1[0].grid(True)
axs1[1].plot(f, np.abs(fft_am), linewidth=1.5)
axs1[1].set_title("Genlik Modülasyonu Spektrum - Ogrenci No: " + ogr_no)
axs1[1].set_xlabel("Frekans (Hz)")
axs1[1].set_ylabel("Genlik")
axs1[1].grid(True)
axs1[1].set_xlim([-200, 200])
#Genlik modülasyonu kısmı(AM)

fig2, axs2 = plt.subplots(2, 1, figsize=(15, 8))
axs2[0].plot(t, s_fm, linewidth=1.5)
axs2[0].set_title("Frekasn Modülasyonu Sinyali - Ogrenci No: " + ogr_no)
axs2[0].set_xlabel("Zaman (s)")
axs2[0].set_ylabel("Genlik")
axs2[0].grid(True)
axs2[1].plot(f, np.abs(fft_fm), linewidth=1.5)
axs2[1].set_title("Frekans Modülasyonu Spektrum - Ogrenci No: " + ogr_no)
axs2[1].set_xlabel("Frekans (Hz)")
axs2[1].set_ylabel("Genlik")
axs2[1].grid(True)
axs2[1].set_xlim([-200, 200])
#Frekans modülasyonu kısmı(FM)

fig3, axs3 = plt.subplots(2, 1, figsize=(15, 8))
axs3[0].plot(t, s_pm, linewidth=1.5)
axs3[0].set_title("Faz Modülasyonu Sinyali - Ogrenci No: " + ogr_no)
axs3[0].set_xlabel("Zaman (s)")
axs3[0].set_ylabel("Genlik")
axs3[0].grid(True)
axs3[1].plot(f, np.abs(fft_pm), linewidth=1.5)
axs3[1].set_title("Faz Modülasyonu Spektrum - Ogrenci No: " + ogr_no)
axs3[1].set_xlabel("Frekans (Hz)")
axs3[1].set_ylabel("Genlik")
axs3[1].grid(True)
axs3[1].set_xlim([-200, 200])
#Faz modülasyonu kısmı(PM)

fig4, axs4 = plt.subplots(2, 1, figsize=(12, 6))
axs4[0].plot(t[idx_pm], s_m[idx_pm], linewidth=1.5)
axs4[0].set_title("Mesaj Sinyali - Ogrenci No: " + ogr_no)
axs4[0].grid(True)

axs4[1].plot(t[idx_pm], s_c[idx_pm], 'r--', linewidth=1.2, label='Tasiyici')
axs4[1].plot(t[idx_pm], s_pm[idx_pm], 'g', linewidth=1.2, label='PM')
axs4[1].set_title("PM Faz Sicramasi Gözlemi - Ogrenci No: " + ogr_no)
axs4[1].grid(True)
axs4[1].legend()
plt.tight_layout()
#PM faz sıçraması gözlemi (sonradan değiştirildi)

fig5, axs5 = plt.subplots(3, 1, figsize=(12, 8))
axs5[0].plot(t[idx_fm], s_m[idx_fm], linewidth=1.5)
axs5[0].set_title("Mesaj Sinyali - Ogrenci No: " + ogr_no)
axs5[0].grid(True)

axs5[1].plot(t[idx_fm], s_c[idx_fm], 'r', linewidth=1.2)
axs5[1].set_title("Tasiyici Sinyal - Ogrenci No: " + ogr_no)
axs5[1].grid(True)

axs5[2].plot(t[idx_fm], s_fm_vis[idx_fm], 'g', linewidth=1.2)
axs5[2].set_title("FM Frekans Degisimi Gozlemi - Ogrenci No: " + ogr_no)
axs5[2].grid(True)
plt.tight_layout()
# FM Frekans Değişiminin gözlenmesi (sonradan değiştirildi)

fig6, axs6 = plt.subplots(4, 1, figsize=(15, 8))
axs6[0].plot(t, s_m, linewidth=1.5)
axs6[0].set_title("Mesaj Sinyali (Yakınlaştırılmış) - Ogrenci No: " + ogr_no)
axs6[0].set_xlabel("Zaman (s)")
axs6[0].set_ylabel("Genlik")
axs6[0].grid(True)
axs6[0].set_xlim([0.03, 0.13])
axs6[1].plot(t, s_am, linewidth=1.5)
axs6[1].set_title("Genlik Modülasyonu Sinyali (Yakınlaştırılmış) - Ogrenci No: " + ogr_no)
axs6[1].set_xlabel("Zaman (s)")
axs6[1].set_ylabel("Genlik")
axs6[1].grid(True)
axs6[1].set_xlim([0.03, 0.13])
axs6[2].plot(t, s_fm, linewidth=1.5)
axs6[2].set_title("Frekans Modülasyonu Sinyali (Yakınlaştırılmış) - Ogrenci No: " + ogr_no)
axs6[2].set_xlabel("Zaman (s)")
axs6[2].set_ylabel("Genlik")
axs6[2].grid(True)
axs6[2].set_xlim([0.03, 0.13])
axs6[3].plot(t, s_pm, linewidth=1.5)
axs6[3].set_title("Faz Modülasyonu Sinyali (Yakınlaştırılmış) - Ogrenci No: " + ogr_no)
axs6[3].set_xlabel("Zaman (s)")
axs6[3].set_ylabel("Genlik")
axs6[3].grid(True)
axs6[3].set_xlim([0.03, 0.13])
# AM, FM ve PM Sinyallerini Karşılaştırma

plt.tight_layout()
plt.show()