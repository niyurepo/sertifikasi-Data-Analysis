import pandas as pd

def calculate_demographic_data(print_data=True):
    # Baca data dari file
    df = pd.read_csv('datafreecode2.csv')

    # 1. Berapa banyak orang dari setiap ras yang terwakili dalam kumpulan data ini?
    # Menggunakan value_counts() untuk menghitung jumlah setiap kategori unik di kolom 'race'
    race_count = df['race'].value_counts()

    # 2. Berapa usia rata-rata pria?
    # Filter data hanya untuk 'Male', lalu ambil kolom 'age' dan hitung rata-ratanya
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Berapa persentase orang yang memiliki gelar Sarjana (Bachelors)?
    # Hitung jumlah orang dengan pendidikan 'Bachelors', bagi dengan total baris, kali 100
    num_bachelors = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((num_bachelors / len(df)) * 100, 1)

    # 4. Berapa persentase orang dengan pendidikan lanjutan (Bachelors, Masters, atau Doctorate) 
    # yang berpenghasilan lebih dari 50K?
    
    # Kualifikasi pendidikan tinggi
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    # Kualifikasi pendidikan rendah (sisanya)
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Persentase dengan gaji >50K untuk pendidikan tinggi
    non_percentage_higher = len(higher_education[higher_education.salary == ">50K"])
    higher_education_rich = round((non_percentage_higher / len(higher_education)) * 100, 1)

    # 5. Berapa persentase orang tanpa pendidikan lanjutan yang menghasilkan lebih dari 50 ribu?
    non_percentage_lower = len(lower_education[lower_education.salary == ">50K"])
    lower_education_rich = round((non_percentage_lower / len(lower_education)) * 100, 1)

    # 6. Berapa jumlah jam minimum seseorang bekerja per minggu?
    min_work_hours = df['hours-per-week'].min()

    # 7. Berapa persen orang yang bekerja dengan jumlah jam minimum per minggu memiliki gaji lebih dari 50 ribu?
    # Ambil orang-orang yang jam kerjanya sama dengan min_work_hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    # Hitung berapa dari mereka yang gajinya >50K
    rich_min_workers = len(num_min_workers[num_min_workers.salary == ">50K"])
    
    rich_percentage = round((rich_min_workers / len(num_min_workers)) * 100, 1)

    # 8. Negara mana yang memiliki persentase penduduk berpenghasilan >50 ribu tertinggi?
    # Hitung total populasi per negara
    country_count = df['native-country'].value_counts()
    # Hitung populasi kaya per negara
    country_rich_count = df[df['salary'] == '>50K']['native-country'].value_counts()
    
    # Bagi kaya dengan total untuk mendapatkan persentase
    highest_earning_country_stats = (country_rich_count / country_count) * 100
    
    # Ambil nama negara dengan persentase tertinggi
    highest_earning_country = highest_earning_country_stats.idxmax()
    # Ambil nilai persentasenya
    highest_earning_country_percentage = round(highest_earning_country_stats.max(), 1)

    # 9. Identifikasi pekerjaan paling populer bagi mereka yang berpenghasilan >50 ribu di India.
    # Filter: Negara India DAN Gaji >50K
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # --- JANGAN UBAH KODE DI BAWAH INI ---
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }