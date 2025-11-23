import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Impor data
df = pd.read_csv('DataTest3.csv')

# 2. Tambahkan kolom 'overweight'
# BMI = Berat (kg) / (Tinggi (m) ^ 2)
# Tinggi di data dalam cm, jadi harus dibagi 100
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

# 3. Normalisasi data
# 0: Baik, 1: Buruk
# Jika 1 -> 0, Jika >1 -> 1
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


# 4. Gambar Plot Kategorial
def draw_cat_plot():
    # 5. Buat DataFrame untuk plot kucing menggunakan pd.melt
    # Kita hanya mengambil kolom-kolom tertentu sesuai instruksi
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Kelompokkan dan format ulang data
    # Kita menghitung jumlah kemunculan setiap fitur berdasarkan kategori cardio
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Buat bagan menggunakan sns.catplot()
    # kind='bar' digunakan karena kita sudah menghitung jumlahnya (total) secara manual di langkah sebelumnya
    chart = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    )

    # 8. Simpan figure ke variabel fig
    fig = chart.fig

    # 9. Jangan memodifikasi dua baris berikutnya
    fig.savefig('catplot.png')
    return fig


# 10. Gambar Peta Panas
def draw_heat_map():
    # 11. Bersihkan data
    # Filter data yang tidak logis (tekanan darah salah, tinggi/berat ekstrem)
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Hitung matriks korelasi
    corr = df_heat.corr()

    # 13. Hasilkan masker untuk segitiga atas
    # Ini agar grafik tidak menampilkan data ganda (cerminan)
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Siapkan matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Plot matriks korelasi menggunakan sns.heatmap()
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,       # Menampilkan angka di dalam kotak
        fmt='.1f',        # Format angka 1 desimal
        center=0,         # Titik tengah warna
        vmin=-0.1,        # Batas minimal skala warna
        vmax=0.25,        # Batas maksimal skala warna
        square=True,      # Kotak berbentuk persegi
        linewidths=.5,    # Garis pemisah antar kotak
        cbar_kws={'shrink': .5} # Ukuran color bar
    )

    # 16. Jangan memodifikasi dua baris berikutnya
    fig.savefig('heatmap.png')
    return fig