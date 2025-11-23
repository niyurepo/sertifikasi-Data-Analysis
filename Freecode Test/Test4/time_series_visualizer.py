import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1. Import dan Bersihkan Data
# Parsing tanggal dan set sebagai index
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Bersihkan data: hapus 2.5% teratas dan 2.5% terbawah
df = df[
    (df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # 2. Gambar Line Plot
    # Buat figure dan axes
    fig, ax = plt.subplots(figsize=(16, 6))
    
    # Plot data: Index (Date) vs Value (Page Views)
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    
    # Set Judul dan Label
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Simpan dan kembalikan gambar
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # 3. Siapkan data untuk Bar Plot
    df_bar = df.copy()
    # Ekstrak Tahun dan Bulan
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Kelompokkan berdasarkan tahun dan bulan, lalu hitung rata-rata
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Urutkan kolom bulan agar berurutan (Jan - Dec), bukan alfabetis
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar[months_order]

    # 4. Gambar Bar Plot
    fig = df_bar.plot(kind='bar', figsize=(15, 10), legend=True).figure
    
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=months_order)
    
    # Simpan dan kembalikan gambar
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # 5. Siapkan data untuk Box Plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Urutan bulan (Singkatan 3 huruf) untuk sumbu X
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # 6. Gambar Box Plots (Subplots: 1 Baris, 2 Kolom)
    fig, axes = plt.subplots(1, 2, figsize=(20, 10))
    
    # Plot 1: Year-wise (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Plot 2: Month-wise (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, order=months_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Simpan dan kembalikan gambar
    fig.savefig('box_plot.png')
    return fig