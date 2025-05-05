# feature_engineering.py

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from typing import Tuple


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggiunge nuove feature utili al dataset:
    - house_age: età della casa in anni
    - years_since_renovated: anni dall'ultimo rinnovo
    - price_log: trasformazione logaritmica di price

    Args:
        df (pd.DataFrame): Dataset pulito.

    Returns:
        pd.DataFrame: Dataset arricchito con nuove feature.
    """
    df = df.copy()

    # Età della casa
    current_year = 2025
    df['house_age'] = current_year - df['yr_built']

    # Anni dall'ultimo rinnovo
    df['years_since_renovated'] = df.apply(
        lambda row: current_year - row['yr_renovated'] if row['yr_renovated'] and row['yr_renovated'] != 0 else 0,
        axis=1
    )

    # Trasformazione logaritmica del prezzo per stabilizzare la varianza
    df['price_log'] = np.log(df['price'] + 1)

    # Rimozione colonne originali non più necessarie
    columns_to_drop = ['date', 'yr_built', 'yr_renovated']
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    return df


def scale_features(df: pd.DataFrame, target_column: str = 'price') -> Tuple[pd.DataFrame, pd.Series]:
    """
    Normalizza le feature numeriche (escluso il target) usando StandardScaler.

    Args:
        df (pd.DataFrame): Dataset con feature.
        target_column (str): Nome della colonna target.

    Returns:
        Tuple[pd.DataFrame, pd.Series]: Feature normalizzate e target originale.
    """
    # Se è presente la colonna price_log, non includerla nelle feature di training
    drop_cols = [target_column]
    if 'price_log' in df.columns:
        drop_cols.append('price_log')

    X = df.drop(columns=drop_cols)
    y = df[target_column]

    scaler = StandardScaler()
    X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    return X_scaled, y
