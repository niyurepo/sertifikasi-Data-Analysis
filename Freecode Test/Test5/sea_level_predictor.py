import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Impor data dari epa-sea-level.csv
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Buat scatter plot
    # Menggunakan Year sebagai sumbu x dan CSIRO Adjusted Sea Level sebagai sumbu y
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Original Data')

    # 3. Buat garis best fit pertama (Menggunakan semua data)
    # Kita hitung regresi linear dari tahun 1880 s.d. data terakhir
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Buat rentang tahun dari 1880 sampai 2050 (inklusif, jadi range sampai 2051)
    years_extended = pd.Series([i for i in range(1880, 2051)])
    
    # Hitung nilai y (Sea Level) berdasarkan rumus garis lurus: y = mx + c
    # m = slope, c = intercept
    sea_level_pred = res.slope * years_extended + res.intercept
    
    # Plot garis regresi pertama (misal warna merah)
    plt.plot(years_extended, sea_level_pred, 'r', label='Fitted Line 1880-2050')

    # 4. Buat garis best fit kedua (Hanya data sejak tahun 2000)
    # Filter data untuk tahun >= 2000
    df_recent = df[df['Year'] >= 2000]
    
    # Hitung regresi linear baru
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Buat rentang tahun dari 2000 sampai 2050
    years_recent = pd.Series([i for i in range(2000, 2051)])
    
    # Hitung prediksi baru
    sea_level_pred_recent = res_recent.slope * years_recent + res_recent.intercept
    
    # Plot garis regresi kedua (misal warna hijau)
    plt.plot(years_recent, sea_level_pred_recent, 'green', label='Fitted Line 2000-2050')

    # 5. Tambahkan Label dan Judul
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # (Opsional) Tampilkan legenda agar grafik lebih jelas
    ax.legend()

    # Simpan dan kembalikan gambar
    plt.savefig('sea_level_plot.png')
    return plt.gca()