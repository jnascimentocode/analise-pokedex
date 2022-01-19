from encodings import utf_8
import pandas as pd

pokemon_df = pd.read_csv('data/pokemon.csv',  sep=';', encoding = 'utf8')
