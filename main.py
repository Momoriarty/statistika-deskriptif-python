import pandas as pd
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt

# 1. PENGORGANISASIAN DATA
print("="*50)
print("PROSES IMPORT DATA")
print("="*50)
# Baca file excel
path = "LatihanExcel_Arifin.xlsx"
dataraw = pd.read_excel(path, header=6)
print("Data Awal (5 baris teratas):")
print(dataraw.head())
print("\n")


# 2. PEMBUATAN TABEL FREKUENSI
print("="*50)
print("TABEL FREKUENSI (Berdasarkan Grade)")
print("="*50)
# Bikin crosstab untuk frekuensi Grade
datafrq = pd.crosstab(index=dataraw["Grade"], columns="Frekuensi")
print(datafrq)
print("\n")


# 3. PENYAJIAN DATA (VISUALISASI)
# Kita bikin 3 grafik (Garis, Batang, dan Pie) dalam satu tampilan figure biar rapi
plt.style.use('seaborn-v0_8-darkgrid') # Kasih style biar lebih estetik (nggak default banget)

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Visualisasi Distribusi Nilai Mahasiswa - Arifin', fontsize=16, fontweight='bold')

# a. Grafik Garis
datafrq.plot(kind='line', ax=axes[0], color='dodgerblue', marker='o', linewidth=2)
axes[0].set_title('Grafik Garis')
axes[0].set_ylabel('Frekuensi')

# b. Grafik Batang
datafrq.plot(kind='bar', ax=axes[1], color='coral', edgecolor='black')
axes[1].set_title('Grafik Batang')
axes[1].set_ylabel('Frekuensi')
axes[1].tick_params(axis='x', rotation=0)

# c. Pie Chart
# Pakai warna custom biar beda dari yang lain
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6']
datafrq.plot(kind='pie', y='Frekuensi', ax=axes[2], autopct='%1.1f%%', legend=False, colors=colors, startangle=90)
axes[2].set_title('Pie Chart')
axes[2].set_ylabel('') # Hilangin label Y biar bersih

plt.tight_layout()
# Simpan gambar biar bisa dilampirin juga kalau butuh
plt.savefig('Visualisasi_Arifin.png', dpi=300)
plt.show()


# 4. STATISTIKA DESKRIPTIF
print("="*50)
print("STATISTIKA DESKRIPTIF (Berdasarkan Final Score)")
print("="*50)
# Pastikan kolom Final Score berupa numerik
# Note: Kalau di Excel kamu namanya 'Nilai', ganti kata 'Final Score' di bawah ini jadi 'Nilai'
dataraw["Final Score"] = pd.to_numeric(dataraw["Final Score"], errors='coerce')
dt = dataraw["Final Score"]

# Ngitung semua statistik yang diminta di modul
stats = dt.describe()
stats['Standard Error'] = dt.sem()
stats['Median'] = dt.median()
# Mode bisa lebih dari satu, kita ambil yang pertama (index 0)
stats['Mode'] = dt.mode().iloc[0] 
stats['variance'] = dt.var()
stats['range'] = dt.max() - dt.min()
stats['skewness'] = dt.skew()
stats['kurtosis'] = dt.kurtosis()

print(stats)
print("="*50)