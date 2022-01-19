import pandas as pd
import numpy as np
from upload_data import *
import plotly.express as px

#quantos pokemons por geração?

print('----- Qtde Pokémon x Geração -----')
gen_df = pokemon_df.groupby('gen').count()
data_gen = gen_df['national_number']
data_gen = pd.DataFrame(data_gen)
print(data_gen)
print('----------------------------------')

print(pokemon_df.shape)

fig = px.bar(data_gen,
            text_auto=True,
            title='Qtde Pokémon x Geração'
            )

fig.show()

#quantos pokemons por tipo primario?

print('----- Qtde Pokémon x Tipo Primário -----')
gen_df = pokemon_df.groupby('primary_type').count()
data_gen = gen_df['national_number']
data_gen = pd.DataFrame(data_gen)
print(data_gen.sort_values(by='national_number', ascending=False))
print('----------------------------------')

fig = px.bar(data_gen,
            text_auto=True,
            title='Qtde Pokémon x Tipo Primário'
            )

fig.show()


