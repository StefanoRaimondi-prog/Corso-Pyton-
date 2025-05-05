# main.py

from clean_data import clean_titanic_data
from model import train_and_predict_dt
from viz_cli import main as viz_main

def menu():
    print("\n=== Titanic ML Menu ===")
    print("1. Train & Optimize Decision Tree")
    print("2. Visualize Data")
    print("3. Exit")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose (1/2/3): ").strip()
        if choice == '1':
            # Allena e genera predictions_dt.csv
            train_and_predict_dt()
        elif choice == '2':
            viz_main()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")
