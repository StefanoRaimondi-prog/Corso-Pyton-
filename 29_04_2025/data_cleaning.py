# data_cleaning.py

import os
import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """
    Carica il dataset da un file CSV.

    Args:
        filepath (str): Percorso al file CSV.

    Returns:
        pd.DataFrame: Dataset caricato.

    Raises:
        FileNotFoundError: se il file non esiste.
        ValueError: se il file è vuoto o non è un CSV valido.
    """
    # Verifica esistenza del file
    if not os.path.isfile(filepath):
        raise FileNotFoundError(
            f"File non trovato: '{filepath}'. Assicurati che il percorso sia corretto e che il file esista."
        )

    try:
        df = pd.read_csv(filepath)
    except pd.errors.EmptyDataError:
        raise ValueError(
            f"Il file '{filepath}' è vuoto o non contiene dati CSV validi."
        )
    except pd.errors.ParserError as e:
        raise ValueError(
            f"Errore nel parsing del file '{filepath}': {e}"
        )

    # Controllo che ci siano colonne
    if df.empty:
        raise ValueError(
            f"Il file '{filepath}' è stato caricato ma il DataFrame è vuoto."
        )

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pulisce il dataset:
    - Converte la colonna 'date' in formato datetime.
    - Rimuove duplicati.
    - Rimuove colonne inutili (es. 'id').

    Args:
        df (pd.DataFrame): Dataset originale.

    Returns:
        pd.DataFrame: Dataset pulito.
    """
    df = df.copy()

    # Conversione della colonna 'date' in datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(
            df['date'], format='%Y%m%dT000000', errors='coerce'
        )

    # Rimozione duplicati
    df = df.drop_duplicates()

    # Rimozione colonna 'id' se presente
    if 'id' in df.columns:
        df = df.drop(columns=['id'])

    return df
