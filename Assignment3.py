import pandas as pd
import matplotlib.pyplot as plt

# Steg 1: Läs in data från CSV-filen
file_path = "openDamagesinTrains.csv" 
df = pd.read_csv(file_path)

# Steg 2: Konvertera datumkolumner till datetime-format
df['Damage reporting date'] = pd.to_datetime(df['Damage reporting date'], errors='coerce', dayfirst=False)
df['Damage closing date'] = pd.to_datetime(df['Damage closing date'], errors='coerce', dayfirst=False)

# Steg 3: Beräkna MTTF (Mean Time to Failure)
df = df.sort_values(by=['Vehicle', 'Damage reporting date'])  # Sortera per fordon och datum

df['TTF'] = df.groupby('Vehicle')['Damage reporting date'].diff().dt.days  # Beräkna skillnad i dagar

# Steg 4: Beräkna MTTR (Mean Time to Repair)
df['TTR'] = (df['Damage closing date'] - df['Damage reporting date']).dt.days

# Steg 5: Rita histogram för MTTF
plt.figure(figsize=(10, 5))
plt.hist(df['TTF'].dropna(), bins=20, edgecolor='black', alpha=0.7)
plt.xlabel('Time to Failure (Days)')
plt.ylabel('Frequency')
plt.title('Histogram över MTTF')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Steg 6: Rita histogram för MTTR
plt.figure(figsize=(10, 5))
plt.hist(df['TTR'].dropna(), bins=20, edgecolor='black', alpha=0.7, color='orange')
plt.xlabel('Time to Repair (Days)')
plt.ylabel('Frequency')
plt.title('Histogram över MTTR')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Steg 7: Beräkna och skriva ut medelvärde och varians för MTTF och MTTR
mttf_mean = df['TTF'].mean()
mttf_var = df['TTF'].var()
mttr_mean = df['TTR'].mean()
mttr_var = df['TTR'].var()

print(f"Medelvärde MTTF: {mttf_mean:.2f} dagar")
print(f"Varians MTTF: {mttf_var:.2f}")
print(f"Medelvärde MTTR: {mttr_mean:.2f} dagar")
print(f"Varians MTTR: {mttr_var:.2f}")#
#pusha