from Views import *
from Procedures import *
def stampa_risultati(titolo, righe):
    print(f"\n--- {titolo} ---")
    if not righe:
        print("Nessun risultato.")
    for r in righe:
        print(" | ".join(str(x) for x in r))

def avvia_menu():
    while True:
        print("""
1. View Pokémon Top Stats
2. View Pokémon con Atk/Def/HP > 100
3. View Pokémon tipo Erba
4. View Abilità Pokémon
5. View Info Specie + Habitat
6. Procedura: Statistiche Base di un Pokémon
7. Procedura: Mosse apprese da un Pokémon
8. Procedura: Abilità di un Pokémon
9. Procedura: Evoluzione Pokémon (ID)
10. Procedura: Tipo ed efficacia di una mossa
0. Esci
        """)
        scelta = input("Scelta: ")

        if scelta == "1": stampa_risultati("Top 10 Pokémon per Stat Totale", get_pokemon_total())
        elif scelta == "2": stampa_risultati("Pokémon con Atk/Def/HP > 100", get_high_stat_pokemon())
        elif scelta == "3": stampa_risultati("Pokémon tipo Erba", get_grass_pokemon())
        elif scelta == "4": stampa_risultati("Abilità Pokémon", get_pokemon_abilities())
        elif scelta == "5": stampa_risultati("Specie, Habitat e Dati", get_species_info())

        elif scelta == "6":
            nome = input("Nome Pokémon: ")
            stampa_risultati(f"Statistiche Base di {nome}", get_base_stats(nome))

        elif scelta == "7":
            nome = input("Nome Pokémon: ")
            stampa_risultati(f"Mosse di {nome}", get_moves_by_pokemon(nome))

        elif scelta == "8":
            nome = input("Nome Pokémon: ")
            stampa_risultati(f"Abilità di {nome}", get_abilities_by_pokemon(nome))

        elif scelta == "9":
            pok_id = input("ID Pokémon: ")
            stampa_risultati(f"Evoluzioni di Pokémon ID {pok_id}", get_pokemon_evolution(pok_id))

        elif scelta == "10":
            mossa = input("Nome mossa: ")
            stampa_risultati(f"Tipo ed Efficacia di {mossa}", get_move_type(mossa))

        elif scelta == "0":
            print("Uscita...")
            break

        else:
            print("Scelta non valida.")
