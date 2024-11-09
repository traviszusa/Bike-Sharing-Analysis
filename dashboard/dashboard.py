import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

day_df = pd.read_csv("./dashboard/cleaned_day.csv")

st.title("Analisis Penyewaan Sepeda")
st.markdown("---")

# Rata-rata penyewaan sepeda berdasarkan cuaca
rata_rata_weather = day_df.groupby('weather')['total_rental'].mean().sort_values(ascending=False).reset_index()
rata_rata_weather.rename(columns={'total_rental': 'avg_rental'}, inplace=True)
rata_rata_weather['avg_rental'] = rata_rata_weather['avg_rental'].round(2)

st.subheader("Rata-rata Penyewaan Sepeda Berdasar pada Cuaca")

# Plot rata-rata penyewaan sepeda berdasarkan cuaca
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='weather', y='avg_rental', data=rata_rata_weather, hue='weather', palette=['#1F77B4', '#808080', '#808080'], dodge=False, legend=False)
ax.set_xlabel('Cuaca')
ax.set_ylabel('Rata-rata Penyewaan Sepeda')
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Cuaca')
st.pyplot(fig)

# Hasil analisis
st.markdown("Kondisi cuaca dengan rata-rata penyewaan sepeda paling tinggi adalah kondisi `Clear` dengan rata-rata sebesar 4876.79 penyewaan")

st.markdown("---")

# Rata-rata penyewaan sepeda berdasarkan musim
rata_rata_season = day_df.groupby('season')['total_rental'].mean().sort_values(ascending=False).reset_index()
rata_rata_season.rename(columns={'total_rental': 'avg_rental'}, inplace=True)
rata_rata_season['avg_rental'] = rata_rata_season['avg_rental'].round(2)

st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Musim")

# Plot rata-rata penyewaan sepeda berdasarkan musim
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x='season', y='avg_rental', data=rata_rata_season, hue='season', palette=['#1F77B4', '#808080', '#808080', '#808080'], dodge=False, legend=False)
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-rata Penyewaan Sepeda')
ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Musim')
st.pyplot(fig)

st.markdown("Musim dengan rata-rata penyewaan sepeda paling tinggi adalah musim `Fall` atau Gugur dengan rata-rata sebesar 5644.3 penyewaan")

st.markdown("---")

# Agregasi data untuk total penyewaan sepeda per bulan
monthly_trend = day_df.groupby(['year', 'month'])['total_rental'].sum().reset_index()

# Mengurutkan DataFrame berdasarkan bulan
month_order = ["January", "February", "March", "April", "May", "June", 
                "July", "August", "September", "October", "November", "December"]
monthly_trend['month'] = pd.Categorical(monthly_trend['month'], categories=month_order, ordered=True)
monthly_trend = monthly_trend.sort_values(['year', 'month'])

# Membagi data berdasarkan tahun
data_2011 = monthly_trend[monthly_trend['year'] == 2011]
data_2012 = monthly_trend[monthly_trend['year'] == 2012]

st.subheader("Total Penyewaan Sepeda Tahun 2011 dan 2012")

# Membuat subplot untuk dua grafik
fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

# Plot untuk tahun 2011
sns.lineplot(x='month', y='total_rental', data=data_2011, marker='o', ax=axes[0])
axes[0].set_title('Total Penyewaan Sepeda per Bulan Tahun 2011')
axes[0].set_xlabel('Bulan')
axes[0].set_ylabel('Total Penyewaan Sepeda')
axes[0].tick_params(axis='x', rotation=45)
axes[0].grid(True)

# Plot untuk tahun 2012
sns.lineplot(x='month', y='total_rental', data=data_2012, marker='o', ax=axes[1])
axes[1].set_title('Total Penyewaan Sepeda per Bulan Tahun 2012')
axes[1].set_xlabel('Bulan')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(True)

plt.suptitle('Perbandingan Tren Penyewaan Sepeda Tahun 2011 dan 2012')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
st.pyplot(fig)

st.markdown(""" Sehingga didapatkan tren total penyewaan sepeda berubah setiap bulan selama tahun 2011 dan 2012:
1. Pada tahun 2011, terdapat kenaikan signifikan dari bulan `Januari` hingga mencapai titik tertinggi pada bulan `Juni`, yaitu sejumlah 143512 penyewaan pada bulan `Juni`
2. Pada tahun 2012, terdapat kenaikan signifikan dari bulan `Januari` hingga mencapai titik tertinggi pada bulan `September`, yaitu sejumlah 218573 penyewaan pada bulan `September`
""")