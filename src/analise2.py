import pandas as pd
import numpy as np
from upload_data import *
import plotly.express as px


#Quantos pokemons tem Mega Evolução?

print('----- Mega Evolução X Geração -----')

gen_mega = pokemon_df.groupby('gen')['mega_evolution'].count()
gen_mega = pd.DataFrame(gen_mega)
print(gen_mega)
print('----------------------------------')

fig = px.bar(gen_mega,
            text_auto=True,
            title='Mega Evolução X Geração'
            )

fig.show()

#Quais pokemons tem mega evolução?

mega_df = pokemon_df[pokemon_df['mega_evolution'].notna()]
print('----- Lista de Pokémon Mega Evolução -----')
print(mega_df[['gen','english_name','mega_evolution']])
print('----------------------------------------')
print(f'Total de Pokémon Mega Evolução: {mega_df.shape[0]}')
print('----------------------------------------')









