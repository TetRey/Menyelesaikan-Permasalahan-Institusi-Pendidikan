# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Saat ini institusi tersebut telah mencetak ribuan lulusan dengan reputasi yang sangat baik. Meskipun telah menjadi institusi ternama, institusi tersebut masih banyak mahasiswa yang tidak menyelesaikan pendidikannya alias dropout. Hal tersebut menyebabkan tingginya _dropout rate_ hingga lebih dari 32%. Jumlah dropout yang tinggi tersebut tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

- **_Dropout Rate_ yang tinggi:** Intitusi mengalami ketidakstabilan kondisi mahasiswa yang menyebabkan tingkat _dropout rate_ yang tinggi
- **Kesulitan dalam perancangan:** Tentunya efek samping dari tingginya _dropout_ menyebabkan institusi kesulitan dalam melakukan perancangan. Seperti estimasi anggaran, persiapan ruang kelas, tenaga didik dan sebagainya
- **Reputasi Perusahaan:** Tingkat _dropout_ yang tinggi dapat mempengaruhi akreditasi kampus. Lembaga akreditasi sering mempertimbangkan tingkat kelulusan dan dropout sebagai salah satu indikator kinerja institusi.

### Cakupan Proyek

- Business Understanding
- Data Understanding
- Data Preprocessing
- Exploratory Data Analysis
- Dashboard Visualization
- Modeling
- Evaluation
- Deployment

### Persiapan

Sumber data:

```
https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv
```

Setup environment:

```
mkdir Kemahasiswaan_Jaya_Maju
cd Kemahasiswaan_Jaya_Maju
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Business Dashboard & Setup Dropout Prediction

Business Dashboard dibuat untuk memberikan _insight_ kepada institusi mengenai data mahasiswa. Terdapat KPI yang memberikan informasi secara langsung kepada _stakeholder_. Selain itu, terdapat beberapa chart yang menunjukan korelasi antara data yang ada dengan _dropout_. Dashboard tersebut dapat dikunjungi pada tautan berikut:

```
https://public.tableau.com/views/DashboardKemahasiswaanJaya/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
```

Untuk _dropout prediction_ dapat dijalankan secara local maupun online. Tulis code dibawah ini pada terminal folder Kemahiswaan_Jaya_Maju untuk menjalankan secara local

```
streamli run prediction.py
```

Kunjungi link di bawah ini untuk mengakses _dropout prediction_ secara online

```
https://jaya-dropout-prediction.streamlit.app/
```

## Conclusion

- Hal yang perlu diperhatikan adalah tingkat finasial mahasiswa, bisa kita lihat bahwa mahasiswa yang memiliki hutang untuk mengikuti kegiatan kuliah sangat cenderung memiliki tingkat dropout yang sangat tinggi, hal tersebut berbanding terbalik dengan mahasiswa yang menjadi penerima beasiswa.
- Rata-rata mahasiswa yang mengambil kelas malam sering mengalami dropout, hal ini mungkin dikarenakan mahasiswa yang mengikuti kelas malam kemungkinan juga pada siang hari sedang bekerja. Oleh karena itu, fokus mereka terpecah.
- Mata kuliah seperti manajemen perlu adanya perhatian lebih lanjut.

### Rekomendasi Action Items

Terdapat beberapa langkah yang dapat menurunkan tingkat _Dropout rate_, berikut merupakan rekomnedasi yang dapat diberikan.

- Meningkatkan kouta beasiswa kepada para mahasiswa
- Meningkatkan tingkat ketetatan penerima mahasiswa dalam bidang finansial, seminimal mungkin tidak menggunakan hutang untuk mengikuti perkuliahan
- Melakukan peninjauan ulang terhadap mata kuliah yang memiliki tingkat dropout cukup tinggi seperti mata kuliah manajemen
- Memberikan pengawasan lebih lanjut kepada mahasiswa yang mengikuti kelas malam
