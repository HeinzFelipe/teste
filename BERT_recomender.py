from transformers import BertTokenizer, BertModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Função para extrair embeddings usando BERT
def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:,0,:].numpy()

# Carregar tokenizer e modelo do BERT
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Carregar o arquivo CSV e embeddings
df = pd.read_csv('/app/artigos.csv')
embeddings = np.load("/app/BERT_embeddings.npy")

def recommend_text(query):
    # Obter embedding da query e normalizar
    embedding_query = get_bert_embedding(query)
    embedding_query = embedding_query / np.linalg.norm(embedding_query)
    
    # Normalizar embeddings do conjunto de dados
    normalized_embeddings = embeddings / np.linalg.norm(embeddings, axis=1)[:, np.newaxis]
    
    # Calcular similaridades
    similarities = cosine_similarity(embedding_query, normalized_embeddings).squeeze()
    
    # Obter os índices das top 5 similaridades
    top_indices = similarities.argsort()[-5:][::-1]
    
    # Imprimir as top 5 similaridades e títulos correspondentes
    print("Top 5 similaridades:", similarities[top_indices])
    print("\nTítulos correspondentes:")
    for i, index in enumerate(top_indices, start=1):
        print(f"N.º {i} - {df['title'][index]}")
    
    return top_indices

class ReturnToQuery(Exception):
    pass

while True:
    try:
        query = input("\nDigite sua consulta (ou 'exit' para sair): ")
        
        if query.lower() == "exit":
            break

        top_indices = recommend_text(query)

        while True:
            choice = input("\nDigite o número da recomendação para ver o texto completo ou 'voltar' para inserir uma nova consulta: ")
            
            if choice.lower() == "voltar":
                raise ReturnToQuery
            
            if choice.isdigit() and 1 <= int(choice) <= 5:
                index = top_indices[int(choice)-1]
                print("\n" + df['text'][index])
    except ReturnToQuery:
        continue