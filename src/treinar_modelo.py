import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

def treinar():
    # Dados fictícios para o classificador de texto
    X = ["Amei o atendimento, nota dez!", "Serviço excelente e rápido",
         "Odiei, nunca mais volto", "Horrível, suporte não ajuda",
         "O produto chegou no prazo", "Recebi o pacote ontem"]
    y = ["positivo", "positivo", "negativo", "negativo", "neutro", "neutro"]

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])

    print("Treinando modelo...")
    pipeline.fit(X, y)

    os.makedirs('modelos', exist_ok=True)
    
    joblib.dump(pipeline, "modelos/modelo_v1.joblib")
    print("Modelo salvo em modelos/modelo_v1.joblib")

if __name__ == "__main__":
    treinar()