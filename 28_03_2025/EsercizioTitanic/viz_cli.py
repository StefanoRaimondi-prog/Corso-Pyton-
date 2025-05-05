# viz_cli.py
"""
Menu interattivo per esplorazione e grafici del dataset pulito
e per il grafico delle predizioni del Decision Tree.
"""
import pandas as pd
import matplotlib.pyplot as plt
from clean_data import clean_titanic_data

def show_menu():
    print("\n=== Titanic Data Visualization Menu ===")
    print("1. Mostra prime 10 righe")
    print("2. Informazioni sul dataset")
    print("3. Distribuzione di 'Survived'")
    print("4. Distribuzione di 'Pclass'")
    print("5. Heatmap delle correlazioni")
    print("6. Boxplot 'Age' vs 'Survived'")
    print("7. Elenca sopravvissuti reali")
    print("8. Grafico predizioni sopravvivenza (Decision Tree)")
    print("9. Esci")

def main():
    df = clean_titanic_data("train.csv")

    while True:
        show_menu()
        choice = input("Scegli un'opzione: ")
        if choice == '1':
            print(df.head(10))
        elif choice == '2':
            print(df.info())
        elif choice == '3':
            df['Survived'].value_counts().plot.bar()
            plt.title("Distribuzione di Survived")
            plt.show()
        elif choice == '4':
            df['Pclass'].value_counts().sort_index().plot.bar()
            plt.title("Distribuzione di Pclass")
            plt.show()
        elif choice == '5':
            corr = df.corr()
            plt.imshow(corr, cmap='coolwarm')
            plt.colorbar()
            plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
            plt.show()
        elif choice == '6':
            df.boxplot(column='Age', by='Survived')
            plt.title("Age vs Survived")
            plt.suptitle('')
            plt.show()
        elif choice == '7':
            survivors = df[df['Survived'] == 1]
            print("\n=== Elenco sopravvissuti reali ===")
            print(survivors)
        elif choice == '8':
            try:
                preds = pd.read_csv("predictions_dt.csv")
                counts = preds["PredLabel"].value_counts().sort_index()
                counts.index = ["Non sopravvissuto","Sopravvissuto"]
                counts.plot(kind="bar")
                plt.title("Predizioni di sopravvivenza (Decision Tree)")
                plt.show()
            except FileNotFoundError:
                print("File predictions_dt.csv non trovato.")
        elif choice == '9':
            print("Uscita programma. Arrivederci!")
            break
        else:
            print("Opzione non valida, riprova.")

if __name__ == '__main__':
    main()
