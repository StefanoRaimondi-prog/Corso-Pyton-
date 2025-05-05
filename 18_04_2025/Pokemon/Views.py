from Db import esegui_query

# Restituisce i Pokémon con statistiche totali (dalla view pokemon_total)
def get_pokemon_total():
    query = "SELECT * FROM pokemon_total ORDER BY total DESC LIMIT 10"
    return esegui_query(query)

# Restituisce Pokémon con attacco, difesa e hp sopra 100 (dalla view att_def_hp)
def get_high_stat_pokemon():
    query = "SELECT * FROM att_def_hp ORDER BY b_atk DESC"
    return esegui_query(query)

# Restituisce i Pokémon di tipo erba (dalla view grass_type_view)
def get_grass_pokemon():
    query = "SELECT * FROM grass_type_view"
    return esegui_query(query)

# Restituisce Pokémon con abilità visibili dalla view pok_abilities
def get_pokemon_abilities():
    query = "SELECT * FROM pok_abilities"
    return esegui_query(query)

# Restituisce info estese sui Pokémon dalla join con species e habitat
def get_species_info():
    query = """
        SELECT pokemon.pok_id, pokemon.pok_name, hab_name , pokemon.pok_height, 
               pokemon.pok_weight, pokemon_species.capture_rate, pokemon_species.base_happiness
        FROM pokemon
        INNER JOIN pokemon_species ON pokemon.species_id = pokemon_species.species_id
        INNER JOIN pokemon_habitats ON pokemon_species.hab_id = pokemon_habitats.hab_id
    """
    return esegui_query(query)
