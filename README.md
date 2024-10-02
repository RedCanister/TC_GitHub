# TC_GitHub

TC_Github é um projeto que utiliza dados da API do GitHub para realizar a classificação dos repositórios públicos (de forma aleatória) , e que depois os usa como referência para uma previsão sobre o número de estrelas de cada repositório através de um app feito com o streamlit.


## Descrição

No desenvolvimento desse projeto, utilizando a linguagem Python nós começamos realizando a análise de dados da API de eventos do GitHub que alimenta um aplicativo interativo onde o usuário tem a capacidade de definir os dados gerais do seu, ou do repositório do Github de outro usuário, e baseado nisso, prever quantas estrelas esse repositório conseguiria ao longo do tempo (como estrelas em potencial, baseado na classificação de outros repositório criados e que possuem um número de estrelas em potencial). 

Primeiro testamos a regressão com diversos modelos de maneira crua, começamos a trabalhar naquele que melhor performou sem tratamento nenhum e depois o implementamos.

conseguimos melhorar em muito a performance mas acredito que devido a extrema variância da classe alvo, não tínhamos um resultado ruim, mas não era excelente, por isso tivemos a ideia de criar uma nova classe, que seria o intervalo entre estrelas, diminuindo assim sua variância. O que no final, também permitiu o desenvolvimento do app feito pelo streamlit na sua forma atual.

Escolhemos o modelo de Árvore de Decisão, pois foi a mesma que melhor performou na regressão dos dados tendo as estrelas como alvo e com ela conseguimos um resultado surpreendente, mesmo simplificando a eta de pré-processamento.

A idéia inicial para esse Tech Challenge era de criar um dashboard que descreveria uma previsão ao longo do tempo das próximas ações de cada usuário que fosse registrado na API de eventos, mas essa versão acabou sendo complicada para o escopo do exercício.

Vocês podem saber mais sobre a API do Github aqui: https://docs.github.com/pt/rest?apiVersion=2022-11-28


## Contribuidores

- Octavio Ruiz Thomas
- Jorge Kayodê Lima Trindade


## Instalação

### Pré-requisitos

- Python 3.12 ou superior
- Instalação de dependências pelo requirements.txt
- VSCode ou Google Colab

### Passos para instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/RedCanister/TC_GitHub.git
   cd tc_embrapa
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate ** No windows use `venv\Scripts\activate
   ```

   ```
   Para usuários do VSCode, é possível utilizar o atalho Ctrl + Shift + P para realizar a instalação rápido do ambiente virtual.
    Na barra de pesquise escreva:
    1. Python: Create Environment
    2. Venv
    3. A Versão mais recente do Python
    4. Selecione o requirements.txt 
   ```

3. Instale as dependências:
   ```bash
   cd ./TC_App
   pip install -r requirements.txt
   ```

4. Inicie a aplicação pelo terminal:
   ```bash
   streamlit run app.py
   ```


# Gráficos

![Gráficos da acurácia do modelo inicial com 40k registros](https://github.com/user-attachments/assets/4eb4ba2f-7245-4f27-8d78-81210001675f)

![Gráficos da acurácia do modelo inicial com 1k registros](https://github.com/user-attachments/assets/07d6da2d-5d64-4661-b583-b79509b037c3)


# Vídeo de apresentação

