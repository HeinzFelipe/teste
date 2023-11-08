from transformers import BertTokenizer, BertModel
import torch
import pandas as pd
import numpy as np

# Carregar tokenizer e modelo do BERT
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

# Função para extrair embeddings usando BERT
def get_bert_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding="max_length", max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:,0,:].numpy()

# Carregar o arquivo CSV
df = pd.read_csv('/app/artigos.csv')

# Extrair embeddings para todos os textos (ajuste o número conforme necessário)
embeddings = []
for text in df['text']:
    embedding = get_bert_embedding(text)
    embeddings.append(embedding)

# Salvar os embeddings em um arquivo para posterior uso
embeddings = np.array(embeddings).squeeze()
np.save("/app/BERT_embeddings.npy", embeddings)
