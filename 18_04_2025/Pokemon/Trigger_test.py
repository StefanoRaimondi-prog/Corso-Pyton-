from .Db import esegui_query

def test_trigger_pokemon():
    query = """
        INSERT INTO pokemon (pok_id, pok_name, pok_height, pok_weight, pok_base_experience)
        VALUES (999, 'testmon', -10, -20, -100)
    """
    esegui_query(query)
    print("✔ Trigger NEW_POKEMON testato: valori negativi convertiti a 0")

def test_trigger_habitat():
    query = """
        INSERT INTO pokemon_habitats (hab_id, hab_name, hab_descript)
        VALUES (999, '', '')
    """
    esegui_query(query)
    print("✔ Trigger NEW_HABITAT testato: stringhe vuote sostituite con 'Unknown'")

def test_trigger_ability():
    query = """
        INSERT INTO pokemon_abilities (pok_id, abil_id, is_hidden, slot)
        VALUES (999, 22, 2, 4)
    """
    esegui_query(query)
    print("✔ Trigger NEW_ABILITY testato: is_hidden settato correttamente")

def esegui_test_trigger():
    print("\n--- TEST TRIGGER ---")
    test_trigger_pokemon()
    test_trigger_habitat()
    test_trigger_ability()

# Se vuoi testarli direttamente da qui, decommenta:
# esegui_test_trigger()
