import pandas as pd
import numpy as np
import os
from upload_data import *
import plotly.express as px

os.system('cls')
pokemon_df.info()
print(pokemon_df)

#quais os tipos de pokemons tem os melhores status?

pokemon_status = pokemon_df[['english_name','primary_type','hp','attack','defense','sp_attack','sp_defense','speed','is_legendary','is_mythical']]

print('-----Os 10 melhores com status de HP --------')
print(pokemon_status.sort_values(by='hp', ascending=False).head(10))
print('-----------------------------------')

print('-----Os 10 melhores com status de ataque --------')
print(pokemon_status.sort_values(by='attack', ascending=False).head(10))
print('-----------------------------------')

print('-----Os 10 melhores com status de defesa --------')
print(pokemon_status.sort_values(by='defense', ascending=False).head(10))
print('-----------------------------------')

print('-----Os 10 melhores com status de ataque especial --------')
print(pokemon_status.sort_values(by='sp_attack', ascending=False).head(10))
print('-----------------------------------')

print('-----Os 10 melhores com status de defesa especial --------')
print(pokemon_status.sort_values(by='sp_defense', ascending=False).head(10))
print('-----------------------------------')

print('-----Os 10 melhores com status de velocidade --------')
print(pokemon_status.sort_values(by='speed', ascending=False).head(10))
print('-----------------------------------')