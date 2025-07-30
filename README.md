
# Simulações de Leilões de Espectro com Direito de Preferência

Este repositório contém um script em Python utilizado para simular o desempenho de quatro mecanismos de leilão de espectro, considerando diferentes estruturas de mercado (simétrica e assimétrica). As simulações avaliam os seguintes critérios: receita esperada do leiloeiro, eficiência alocativa e frequência de entrada de novos prestadores.

## Mecanismos Simulados

- **SPA (Second-Price Auction):** Leilão de segundo preço tradicional.
- **FPA (First-Price Auction):** Leilão de primeiro preço com função de lance ótima.
- **Mecanismo A:** Duas rodadas, com exclusividade para entrantes na primeira.
- **Mecanismo B:** Leilão com direito de preferência para entrantes.

## Estrutura do Código

- Geração de valores privados para incumbentes e entrantes.
- Simulação de 10.000 rodadas por mecanismo.
- Dois cenários: simétrico (entrantes ~ U[0,1]) e assimétrico (entrantes ~ U[0, θ]).
- Cálculo da receita média, eficiência e taxa de entrada.
- Geração de gráficos comparativos (PNG).

## Como Executar

1. Requisitos:
   - Python 3.x
   - `numpy`
   - `matplotlib`

2. Executar o script principal:
```bash
python simulacoes_leilao.py
```

3. Os gráficos serão salvos como arquivos `.png` no diretório atual.

## Resultados Gerados

- `grafico_receita.png`: Receita esperada por mecanismo e cenário.
- `grafico_eficiencia.png`: Eficiência alocativa média.
- `grafico_entrada.png`: Frequência de entrada (apenas Mecanismo B).

## Parâmetros

- `n_E = 3`: Número de entrantes
- `n_I = 3`: Número de incumbentes
- `n_sim = 10000`: Número de simulações por mecanismo
- `theta = 0.7`: Limite superior da distribuição de valores dos entrantes no cenário assimétrico

## Observações

- As simulações assumem valores privados independentes e distribuições uniformes.
- Para garantir reprodutibilidade, você pode definir uma semente aleatória (`np.random.seed()`).
- O código é parte integrante do artigo acadêmico sobre mecanismos de alocação de espectro com foco em promoção da entrada e eficiência.

## Autora

Priscila Evangelista de Souza  
Doutoranda em Economia Aplicada - Universidade de Brasília (UnB)  
E-mail: priscila@unb.br

