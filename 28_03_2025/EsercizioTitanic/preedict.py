# predict.py

import pandas as pd
import joblib
from clean_data import clean_titanic_data

def predict_single(sample: dict, model_path: str = "titanic_model.joblib") -> int:
    """
    Accetta un dict con le stesse colonne di train.csv,
    restituisce 0/1 a indicare sopravvivenza predetta.
    """
    # Costruisci un DataFrame da un solo campione
    df = pd.DataFrame([sample])
    # Applica la stessa pulizia
    df_clean = clean_titanic_data(path=None)  # modifica clean_data per accettare DataFrame in input se vuoi
    # Oppure: adatta clean_data per pulire anche piccole tabelle
    
    # Carica il modello
    clf = joblib.load(model_path)
    # Predict
    return int(clf.predict(df_clean)[0])

if __name__ == "__main__":
    # Esempio di utilizzo:
    example = {
      "PassengerId": 892, "Pclass": 3, "Name": "Test User", "Sex": "male",
      "Age": 30, "SibSp": 0, "Parch": 0, "Ticket": "12345", "Fare": 7.25, "Cabin": None, "Embarked": "S"
    }
    pred = predict_single(example)
    print("Predizione sopravvivenza (0=no, 1=sì):", pred)
