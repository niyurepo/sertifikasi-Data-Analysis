import numpy as np

def calculate(list):
    # 1. Validasi Input
    # Jika panjang list bukan 9, bangkitkan ValueError dengan pesan spesifik
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # 2. Transformasi Data
    # Mengubah list menjadi Numpy Array dan membentuk matriks 3x3
    matrix = np.array(list).reshape(3, 3)

    # 3. Kalkulasi Statistik
    # Kita menggunakan metode bawaan Numpy: mean, var, std, max, min, sum.
    # Kita menghitung untuk axis 0 (kolom), axis 1 (baris), dan flattened (semua).'''
    # .tolist() digunakan untuk mengubah array Numpy menjadi list Python biasa agar sesuai format.
    
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), 
            matrix.mean(axis=1).tolist(), 
            matrix.mean().tolist()
        ],
        'variance': [
            matrix.var(axis=0).tolist(), 
            matrix.var(axis=1).tolist(), 
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(), 
            matrix.std(axis=1).tolist(), 
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(), 
            matrix.max(axis=1).tolist(), 
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(), 
            matrix.min(axis=1).tolist(), 
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(), 
            matrix.sum(axis=1).tolist(), 
            matrix.sum().tolist()
        ]
    }

    return calculations