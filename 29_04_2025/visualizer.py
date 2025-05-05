# visualizer.py

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from data_cleaning import load_data, clean_data
from feature_engineering import add_features


def show_head(df: pd.DataFrame, n: int = 5):
    """
    Stampa le prime n righe del DataFrame.
    """
    print(df.head(n))


def show_description(df: pd.DataFrame):
    """
    Stampa le statistiche descrittive del DataFrame.
    """
    print(df.describe(include='all'))


def show_price_mean(df: pd.DataFrame):
    """
    Stampa la media e la mediana del prezzo.
    """
    mean_price = df['price'].mean()
    median_price = df['price'].median()
    print(f"Prezzo medio: {mean_price:.2f}")
    print(f"Prezzo mediano: {median_price:.2f}")


def plot_price_distribution(df: pd.DataFrame):
    """
    Mostra l'istogramma della distribuzione dei prezzi.
    """
    plt.figure()
    plt.hist(df['price'], bins=50)
    plt.title('Distribuzione dei prezzi')
    plt.xlabel('Prezzo')
    plt.ylabel('Frequenza')
    plt.show()


def plot_scatter_sqft_price(df: pd.DataFrame):
    """
    Mostra uno scatter plot di prezzo vs superficie interna.
    """
    plt.figure()
    plt.scatter(df['sqft_living'], df['price'], alpha=0.5)
    plt.title('Prezzo vs Metri quadri interni')
    plt.xlabel('sqft_living')
    plt.ylabel('price')
    plt.show()


def plot_correlation_heatmap(df: pd.DataFrame):
    """
    Mostra la matrice di correlazione come heatmap.
    """
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    plt.imshow(corr, cmap='coolwarm', interpolation='none')
    plt.colorbar()
    plt.xticks(range(len(corr)), corr.columns, rotation=90)
    plt.yticks(range(len(corr)), corr.columns)
    plt.title('Matrice di correlazione')
    plt.tight_layout()
    plt.show()


def run_menu(filepath: str = 'kc_house_data.csv'):
    """
    Esegue un menu interattivo per visualizzare dati e grafici.
    """
    df = load_data(filepath)
    df = clean_data(df)
    df = add_features(df)

    options = {
        '1': ('Mostra prime righe del dataset', show_head),
        '2': ('Descrizione statistica del dataset', show_description),
        '3': ('Prezzo medio e mediano', show_price_mean),
        '4': ('Istogramma dei prezzi', plot_price_distribution),
        '5': ('Scatter plot: prezzo vs dimensione', plot_scatter_sqft_price),
        '6': ('Mappa di correlazione', plot_correlation_heatmap),
        '0': ('Esci', None)
    }

    while True:
        print('\nMenu Visualizzazione Dati:')
        for key, (desc, _) in options.items():
            print(f" {key}. {desc}")
        choice = input('Seleziona un\'opzione: ').strip()

        if choice == '0':
            print('Uscita...')
            break

        action = options.get(choice)
        if action:
            desc, func = action
            if choice == '1':
                n = input('Quante righe mostrare? [5]: ').strip() or 5
                show_head(df, int(n))
            else:
                func(df)
        else:
            print('Opzione non valida, riprova.')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Menu per visualizzazione dati e grafici'
    )
    parser.add_argument(
        '--input', '-i',
        type=str,
        default='kc_house_data.csv',
        help='Percorso al CSV di input'
    )
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = args.input
    if not os.path.isfile(input_path):
        input_path = os.path.join(script_dir, args.input)

    run_menu(input_path)
