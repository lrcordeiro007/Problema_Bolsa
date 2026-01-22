import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

def treinar():
    # Dados fictícios para o classificador de texto
    X = ["erro no sistema", "como faço login?", "relato de uso", "problema técnico", "qual seu nome?"]
    y = ["reclamacao", "pergunta", "relato", "reclamacao", "pergunta"]

    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])

    print("Treinando modelo...")
    pipeline.fit(X, y)

    # Garante que a pasta modelos existe
    os.makedirs('modelos', exist_ok=True)
    
    # Salva o modelo
    joblib.dump(pipeline, "modelos/modelo_v1.joblib")
    print("Modelo salvo em modelos/modelo_v1.joblib")

if __name__ == "__main__":
    treinar()