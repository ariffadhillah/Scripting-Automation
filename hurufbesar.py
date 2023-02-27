import pandas as pd

# Membaca file Excel
df = pd.read_excel('huruf-besar.xlsx')

# Mengubah semua huruf kecil menjadi huruf besar pada kolom "NEW_ADDRESS"
df['NEW_ADDRESS'] = df['NEW_ADDRESS'].str.upper()

# Menyimpan perubahan pada file Excel
df.to_excel('huruf-besar.xlsx', index=False)
