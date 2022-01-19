import pandas as pd
import numpy as np
import os
from upload_data import *
import plotly.express as px

os.system('cls')

#quantos pokemons lendarios por tipo? e quais são eles?

list_legendary = pokemon_df[pokemon_df['is_legendary'] == True]
print('----- Lista de Pokémon lendário por geração -----')
print(list_legendary[['gen','english_name','primary_type']])
print('----------------------------------------')
print(f'Total de Pokémon Lendário: {list_legendary.shape[0]}')
print('----------------------------------------')

fig = px.bar(pokemon_df, 
            x='primary_type',
            y='is_legendary',
            color = 'primary_type',
            title='Pokémon Lendário x Tipo')

fig.show()


