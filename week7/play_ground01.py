import pandas as pd
file_url = 'https://docs.google.com/spreadsheets/d/1OGs8KoHGEZDxyFdaxAKmZbeO1BiSWVQ6/export?format=xlsx'

# Header column start from the row 20, using the argument 20 as we shpw in class. Reading the second sheet by using argument sheet 1. 
df = pd.read_excel(file_url, sheet_name=1, header=20)

print(df.head(50))

headers = df.columns.tolist()

print(headers)
print(df['RegName'])
# Droping the columns AREA, REG, DEV, Type, Coverage as we do not seen then in assginment, inplace true to remove permanently
df.drop(columns=['AREA', 'REG', 'DEV', 'Type', 'Coverage'], inplace=True)
print(df.head(20))

# Renaming the columns as shown in the image of assignment. 
df = df.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'})

print(df.head(5))
# Setting up Country as index and making it parmanent
df.set_index('Country', inplace=True)

print(df.head(5))

