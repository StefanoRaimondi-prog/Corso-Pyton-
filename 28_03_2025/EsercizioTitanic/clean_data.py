# clean_data.py

import pandas as pd
import os

def clean_titanic_data(path: str = "train.csv") -> pd.DataFrame:
    """
    Carica train.csv, gestisce i missing, crea feature extra e codifica le categoriche.
    """
    # Percorso assoluto 
    if not os.path.isabs(path):
        path = os.path.join(os.path.dirname(__file__), path)
    df = pd.read_csv(path)

    # Drop colonne non utili
    df = df.drop(columns=['PassengerId','Ticket','Cabin'])

    # Estrai titolo da Name e raggruppa i rari
    df['Title'] = df['Name'].str.extract(r'([A-Za-z]+)\.', expand=False)
    rare = ['Lady','Countess','Capt','Col','Don','Dr','Major','Rev','Sir','Jonkheer','Dona']
    df['Title'] = df['Title'].replace(rare, 'Rare')
    df['Title'] = df['Title'].replace({'Mlle':'Miss','Ms':'Miss','Mme':'Mrs'})

    # Missing values
    df['Age']   = df['Age'].fillna(df['Age'].median())
    df['Fare']  = df['Fare'].fillna(df['Fare'].median())
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

    # Nuove feature 
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone']    = (df['FamilySize']==1).astype(int)

    # Encoding categoriche
    df['Sex'] = df['Sex'].map({'male':0,'female':1})
    df = pd.get_dummies(df, columns=['Embarked','Title'], drop_first=True)

    # Rimuovo Name (usato per Title) e mantengo solo i numeri
    df = df.drop(columns=['Name'])

    return df

if __name__ == "__main__":
    df_clean = clean_titanic_data("train.csv")
    print(df_clean.info())
    print(df_clean.head())
    df_clean.to_csv("train_clean.csv", index=False)
