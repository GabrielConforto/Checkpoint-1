import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar a base de dados CSV
file_path = 'caminho/para/seu/arquivo.csv'  # Substitua pelo caminho para seu arquivo CSV
df = pd.read_csv(file_path)


# Gerar uma amostra aleatória de 4000 dados
np.random.seed(303)  # Definir o random_state
sample_df = df['url_length'].sample(n=4000, random_state=303)

# Calcular a média e a mediana
mean_url_length = sample_df.mean()
median_url_length = sample_df.median()

print(f"Média da comprimento das URLs: {mean_url_length:.2f}")
print(f"Mediana do comprimento das URLs: {median_url_length:.2f}")


plt.figure(figsize=(12, 6))
sns.histplot(sample_df, bins=30, kde=True)
plt.title('Distribuição do Comprimento das URLs')
plt.xlabel('Comprimento da URL')
plt.ylabel('Frequência')
plt.show()


