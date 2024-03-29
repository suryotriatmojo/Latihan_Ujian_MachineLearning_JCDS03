# Machine Learning Exam

![Lintang_Purwadhika](https://static.wixstatic.com/media/2e6af2_f69a4271c3534ae1869a7ed63e278b2b~mv2.png/v1/fill/w_246,h_39,al_c,usm_0.66_1.00_0.01/2e6af2_f69a4271c3534ae1869a7ed63e278b2b~mv2.png)

#

### **Soal 1 - Jumlah Penduduk Indonesia**

Disediakan __1 buah dataset (file Excel)__ hasil sensus BPS (Badan Pusat Statistik) tentang jumlah penduduk Indonesia berdasarkan provinsi pada tahun 1971, 1980, 1990, 1995, 2000 & 2010. Unduh dataset via BPS: [unduh di sini](https://www.bps.go.id/statictable/2009/02/20/1267/penduduk-indonesia-menurut-provinsi-1971-1980-1990-1995-2000-dan-2010.html). __Dilarang keras untuk menyunting/mengubah konten dataset!__ Kemudian dengan memanfaatkan dataset tersebut, selesaikanlah soal-soal berikut:

1. Buatlah sebuah file python (__*soal1_1.py*__) yang dapat menampilkan grafik: *(1)* jumlah penduduk __Indonesia__, *(2)* jumlah penduduk dari provinsi yang memiliki __*penduduk terbanyak di tahun 2010*__, dan *(3)* jumlah penduduk dari provinsi yang memiliki __*penduduk paling sedikit di tahun 1971*__! 

    Provinsi dengan jumlah penduduk terbanyak di tahun 2010 adalah __Jawa Barat__, dan provinsi dengan jumlah penduduk paling sedikit di tahun 1971 adalah __Bengkulu__. Namun Anda __dilarang__ untuk menuliskan kata _"Jawa Barat"_, _"Bengkulu"_ dan _"Indonesia"_ di dalam script python Anda. Hasil yang diharapkan kurang lebih ditunjukkan oleh grafik berikut:

    ![grafik_1](images/1_maxminindo.png)

2. Buatlah sebuah file python (__*soal1_2.py*__) yang dapat melakukan __regresi linear__ terhadap hasil di soal sebelumnya, untuk memprediksi jumlah penduduk di masa mendatang. _(1)_ Gambarkan _best fit line_ (garis terbaik) hasil regresi pada grafik, dan _(2)_ prediksikan berapa jumlah penduduk Indonesia, Jawa Barat & Bengkulu pada tahun 2050! 

    Anda __dilarang__ untuk menuliskan kata _"Jawa Barat"_, _"Bengkulu"_ dan _"Indonesia"_ di dalam script python Anda. Hasil yang diharapkan kurang lebih ditunjukkan oleh gambar berikut:

    ![2050](images/2_linregresi.png)

    Dan di terminal akan muncul hasil prediksi: 

    ```bash
    Prediksi jumlah penduduk Jawa Barat di tahun 2050: 65443585
    Prediksi jumlah penduduk Bengkulu di tahun 2050: 3139135
    Prediksi jumlah penduduk INDONESIA di tahun 2050: 359273669
    ```

_**Catatan:**_ _Commit & push source code jawaban soal ini (beserta screenshot grafik) ke __Github__ Anda, buatlah repo dengan nama __Ujian_Penduduk_Indonesia__. Kemudian lampirkan __url link repo Github__ Anda via email ke lintang@purwadhika.com!_

#

### **Soal 2 - Pemain Bola Muda Berbakat**

Anda adalah seorang manager klub sepakbola ternama, yang ingin merekrut pemain sepakbola muda berbakat. Pemain yang anda targetkan memiliki kriteria sebagai berikut: 

- usia (__Age__) __<= 25__ tahun, 
- skill umum (__Overall__) __>= 80__ point, dan
- potensi (__Potential__) __>= 80__. 

Tersedia __1 buah dataset (file csv)__ yang memuat daftar lengkap pemain sepakbola profesional kelas dunia. Unduh dataset via kaggle: [unduh di sini](https://www.kaggle.com/karangadiya/fifa19). __Dilarang keras untuk menyunting/mengubah konten dataset!__ Kemudian dengan memanfaatkan dataset tersebut, selesaikanlah soal-soal berikut:

1. Buatlah sebuah file python (__*soal2_1.py*__) yang dapat menampilkan 2 buah grafik dalam 1 figure: *(1)* grafik kaitan antara usia (__Age__) vs skill umum (__Overall__) dan *(2)* grafik kaitan antara usia (__Age__) vs potensi (__Potential__). Hasil yang diharapkan kurang lebih ditunjukkan oleh gambar di bawah. Titik hijau adalah daftar pemain target yang ingin Anda rekrut.

    ![grafik_1](images/3_fifa.png)

2. Buatlah sebuah file python (__*soal2_2.py*__) yang berisi algoritma machine learning yang dapat melakukan pengelompokkan pemain: target & non-target. Gunakan minimal __3 algoritma__, lalu bandingkan dengan metode __k-fold cross validation__ & tentukan mana algoritma yang memiliki akurasi terbaik.

3. Buatlah sebuah file python (__*soal2_3.py*__) yang menggunakan algoritma terbaik di soal sebelumnya, untuk memprediksi/mengelompokkan data pemain berikut apakah tergolong pemain target yang ingin kita rekrut atau tidak:

    Name | Age | Overall | Potential
    -|-|-|-
    Andik Vermansyah | 27 | 87 | 90
    Awan Setho Raharjo | 22 | 75 | 83
    Bambang Pamungkas | 38 | 85 | 75
    Cristian Gonzales | 43 | 90 | 85
    Egy Maulana Vikri | 18 | 88 | 90
    Evan Dimas | 24 | 85 | 87
    Febri Hariyadi | 23 | 77 | 80
    Hansamu Yama Pranata | 24 | 82 | 85
    Septian David Maulana | 22 | 83 | 80
    Stefano Lilipaly | 29 | 88 | 86

_**Catatan:**_ _Commit & push source code jawaban soal ini (beserta screenshot grafik) ke __Github__ Anda, buatlah repo dengan nama __Ujian_Pemain_Muda_Berbakat__. Kemudian lampirkan __url link repo Github__ Anda via email ke lintang@purwadhika.com!_

#

### *__#HappyCoding__* :relaxed:

#### Lintang Wisesa :love_letter: _lintangwisesa@ymail.com_

[Facebook](https://www.facebook.com/lintangbagus) | 
[Twitter](https://twitter.com/Lintang_Wisesa) |
[Google+](https://plus.google.com/u/0/+LintangWisesa1) |
[Youtube](https://www.youtube.com/user/lintangbagus) | 
:octocat: [GitHub](https://github.com/LintangWisesa) |
[Hackster](https://www.hackster.io/lintangwisesa)
