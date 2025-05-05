from Db import chiama_procedura
# Richiama la procedura per ottenere le statistiche base di un Pokémon
def get_base_stats(pokemon_name):
    return chiama_procedura('output_pokemon_base_stats', [pokemon_name])

# Restituisce le mosse che un Pokémon può imparare
def get_moves_by_pokemon(pokemon_name):
    return chiama_procedura('output_pokemon_moves', [pokemon_name])

# Restituisce le abilità di un Pokémon
def get_abilities_by_pokemon(pokemon_name):
    return chiama_procedura('output_pokemon_abilities', [pokemon_name])

# Restituisce tipo e danno effettivo di una mossa
def get_move_type(move_name):
    return chiama_procedura('output_pokemon_moves_types', [move_name])

# Restituisce efficacia dei tipi
def get_type_efficacy(type_name):
    return chiama_procedura('output_pokemon_type_efficacy', [type_name])

# Restituisce tutte le versioni in cui una mossa è disponibile
def get_move_versions(move_name):
    return chiama_procedura('output_pokemon_moves_version', [move_name])

# Restituisce il metodo con cui una mossa può essere appresa
def get_move_method(move_name):
    return chiama_procedura('output_pokemon_moves_method', [move_name])

# Restituisce le abilità nascoste di un Pokémon
def get_hidden_ability(pokemon_name):
    return chiama_procedura('output_pokemon_hidden_abil', [pokemon_name])

# Restituisce l'habitat di un Pokémon
def get_pokemon_habitat(habitat_name):
    return chiama_procedura('output_pokemon_habitat', [habitat_name])

# Restituisce i tipi di un Pokémon
def get_pokemon_types(pokemon_name):
    return chiama_procedura('output_pokemon_types', [pokemon_name])

# Restituisce se una mossa può mettere KO un Pokémon specifico
def get_pokemon_fainted(move_name, pokemon_name):
    return chiama_procedura('output_pokemon_fainted', [move_name, pokemon_name])

# Restituisce l'evoluzione di un Pokémon a partire dal suo ID
def get_pokemon_evolution(pokemon_id):
    return chiama_procedura('output_pokemon_evol', [pokemon_id])
