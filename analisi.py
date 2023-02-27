
import pandas as pd

# membaca file Excel
data = pd.read_excel('periksa - Copy.xlsx')

# menampilkan semua kolom dan baris
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# memilih kolom yang diinginkan dan menampilkan semua baris
subset = data[['FACNAME', 'ADDRESS', 'NEW_ADDRESS']]

# menampilkan hasil
print(subset)
