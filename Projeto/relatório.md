##### 2025-01-05
# Relatório Final
---
### Algoritmos e Técnicas de Programação
### Sistema de Consulta e Análise de Publicações Científicas
### Docente: José Carlos Ramalho
### Autores:
* Adriana Monteiro (a107201)
* Beatriz Neiva (a107241)
* Catarina Marantes (a107158)

## Conteúdo
### 1. Introdução 
### 2. Descrição do Projeto
2.1 Requisitos do sistema

2.2 Requisitos técnicos
### 3. Conceção e desenho do sistema
3.1 Estrutura de dados utilizados  

3.2 Explicação do código
### 4. Conclusão

## 1. Introdução
Este relatório, elaborado no contexto da unidade curricular "Algoritmos e Técnicas de Programação", descreve o desenvolvimento de um projeto cuja finalidade é desenvolver um sistema que permite criar, atualizar e analisar publicações científicas.
O sistema foi desenvolvido em Python, utilizando as estruturas de dados mais apropriadas e as bibliotecas necessárias (como o matplotlib) para garantir o funcionamento correto da aplicação. Para proporcionar uma interação mais intuitiva, foi implementada uma interface gráfica, neste caso, utilizando o FreeSimpleGUI. Esta interface permite ao utilizador visualizar um menu que reúne todas as funcionalidades disponíveis, possibilitando o uso completo dos componentes criados no código para a organização das suas tarefas.  

## 2. Descrição do projeto

Neste projeto, desenvolveu-se um sistema em Python para gerir publicações científicas. Utilizando um dataset de publicações, implementou-se funcionalidades que permitem a pesquisa de artigos com base em filtros relevantes, como data de publicação, palavras-chave e autores. Além disso, criou-se mecanismos para gerar relatórios detalhados, que incluem gráficos ilustrativos, a fim de analisar métricas relacionadas tanto aos artigos quanto aos seus autores.
### 2.1 Requesitos do Sistema

Os requisitos deste sistema incluem a criação de funções para: 

1. **Carregamento da Base de Dados**: O programa no arranque carrega para memória o dataset guardado no ficheiro de suporte à aplicação;

2. **Criação de Publicações**: O utilizador pode criar um artigo especificando um título, resumo, palavras-chave, DOI, uma lista de autores e sua afiliação correspondente, url para o ficheiro PDF do artigo, data de publicação e url do artigo;

3. **Atualização de Publicações**: O sistema permite a atualização da informação de uma publicação, nomeadamente a data de publicação, o resumo, palavras-chave, autores e afiliações; 

4. **Consulta de Publicações**: O sistema permite pesquisar publicações. Esta pesquisa permite filtros por título, autor, afiliação, data de publicação e palavras-chave. É ainda possível ordenar as publicações encontradas pelos títulos e pela data de publicação; 

5. **Análise de publicações por Autor**: O sistema permite listar os autores e aceder aos artigos de cada autor da lista. Os autores aparecem ordenados pela frequência dos seus artigos publicados e/ou por ordem alfabética;

6. **Análise de publicações por palavras-chave**: O sistema permite a pesquisa e visualização das palavras-chave do dataset. As palavras-chave devem estar ordenadas pelo seu número de ocorrências nos artigos e/ou por ordem alfabética. O sistema permite também visualizar a lista das publicações associadas a cada palavra-chave;

7. **Estatísticas de Publicação**:
O sistema apresenta relatórios que incluam os seguintes gráficos:
- Distribuição de publicações por ano.
- Distribuição de publicações por mês de um determinado ano.
- Número de publicações por autor (top 20 autores).
- Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave).
- Distribuição de palavras-chave mais frequente por ano.

8. **Armazenamento dos Dados**: Quando o utilizador decidir sair da aplicação ou tiver selecionado o armazenamento dos dados, a aplicação guarda os dados em memória no ficheiro de suporte;

9. **Importação de Dados**: Em qualquer momento, é possível importar novos registos dum outro ficheiro que tenha a mesma estrutura do ficheiro de suporte;

10. **Exportação parcial de dados**: Em qualquer momento, é possível exportar para ficheiro os registos resultantes de uma pesquisa (apenas o subconjunto retornado pela pesquisa).

### 2.2 Requisitos técnicos

Os requisitos técnicos deste projeto incluem:

1. O sistema ser implementado em Python.

2. Utilizar estruturas de dados apropriadas para armazenar a informação sobre as publicações.

3. Implementar uma interface de linha de comando (CLI) e uma interface gráfica para a interação dos utilizadores.

4. Integrar funcionalidades de gráficos usando bibliotecas Python, como matplotlib.

5. Implementar um mecanismo de armazenamento persistente para guardar as publicações, por exemplo um ficheiro JSON.

## 3. Conceção e desenho do sistema
### 3.1 Estrutura de dados utilizados 

O código é composto por uma lista de dicionários para armazenamento e manipulação de dados.
Cada dicionário é uma publicação composto por: resumo, palavras-chaves, autores, doi, pdf, data de publicação, título e url.
Os autores são definidos com uma lista de dicionários, em que cada dicionário inclui o nome do autor, a afiliação e, em certos casos, o orcid correspondente.

Utilizou-se a biblioteca Json para guardar dados das tarefas em arquivos JSON.
O utilizador pode aceder às funções base do sistema, como modificar publicações (adicionar ou eliminar), importar e consultar informações do ficheiro fornecido através do terminal do VScode.

### 3.2 Explicação do código

O funcionamento do código depende de várias funções específicas, cada uma associada a uma janela que será exibida na interface gráfica.

**Função para mostrar a janela inicial do sistema:**

*main_menu*

    O código define uma função denomimada main_menu, que cria uma interface gráfica para um menu principal utilizando a biblioteca FreeSimpleGUI, que facilita a criação de layouts por meio de uma lista de listas, onde cada sublista representa uma linha da interface. São utilizados widgets como sg.Text para exibir texto e sg.Button para criar botões que respondem a eventos.
    A janela é apresentada pelo método sg.Window(), com uma interface gráfica intuitiva e botões que facilitam a interação do utilizador.
    Este menu serve como ponto de navegação para diversas funcionalidades do sistema. 


![Captura de ecrã 2025-01-02 150954.png](<attachment:Captura de ecrã 2025-01-02 150954.png>)


**Função de ajuda:**

*help*

    A função help melhora a experiência do utilizador ao fornecer um guia rápido e acessível dentro da interface gráfica. Ela permite que o utilizador compreenda facilmente o propósito de cada funcionalidade do sistema.

![image.png](attachment:image.png)

**Função para criar uma nova publicação:**

*criarPub*

    A função criarPub é projetada para criar uma nova publicação no sistema. Para isso, são usadas várias bibliotecas e conceitos-chave. A **biblioteca os** é utilizada para verificar se o arquivo de publicações existe, enquanto a biblioteca json permite carregar e manipular dados estruturados em formato JSON, convertendo strings em listas de dicionários, é utilizada também a biblioteca FreeSimpleGUI.

![image-2.png](attachment:image-2.png)

**Função para consultar uma publicação:**

*consultarPub*

    Esta função fornece uma solução prática e intuitiva para pesquisar e visualizar publicações num sistema baseado em arquivos JSON.
    Diferente dos métodos anteriormente utilizados, nesta função usamos um campo de seleção (sg.Combo) para escolher o filtro (título, autores, afiliação, palavras-chave ou data).

![image-3.png](attachment:image-3.png)


**Função para listar uma publicação:**

*listarPub*

    A interface usada apresenta:
        - Um campo de seleção (sg.Combo) com critérios de filtro como "Título", "Resumo", "Autores", etc.
        - Um campo de entrada de texto (sg.InputText) para que o utilizador insira o identificador.
        - Um botão Consultar para realizar a procura.
        - Uma caixa de listagem (sg.Listbox) para exibir os resultados encontrados.
        - Um botão Cancelar para fechar a janela.

![image-4.png](attachment:image-4.png)

**Função para eliminar uma publicação:**

*elimPub*

    Esta função começa por criar uma janela para que o utilizador insira o título da publicação que pretende eliminar, verificando se ela existe. Caso encontrada, solicita confirmação para excluir, atualiza o arquivo com os dados modificados e exibe mensagens de sucesso ou erro. A operação pode ser cancelada a qualquer momento, e a interface é fechada ao final.

![image-5.png](attachment:image-5.png)

**Função para gerar relatórios estatísticos das publicações:**

*relEsta*

    A função relEstat gera relatórios e visualizações estatísticas sobre um conjunto de publicações armazenadas num arquivo JSON. Ela permite ao utilizador interagir com os dados de forma intuitiva, oferecendo opções para criar gráficos baseados em diferentes parâmetros, como anos, autores, palavras-chave e meses.

**1. gerarGraficoPorAno**

    Esta função cria e exibe um gráfico de barras que mostra quantas publicações ocorreram a cada ano, com base nos dados fornecidos no dicionário contagem_anos.

explicação detalhada:

- plt.figure(figsize=(10, 6)): Cria uma figura de gráfico com o tamanho especificado (10x6 polegadas).
- plt.bar(anos, publicacoes, color='skyblue'): Gera um gráfico de barras, onde os anos são colocados no eixo X e o número de publicações no eixo Y. A cor das barras será "skyblue" (azul claro).
- plt.title("Distribuição de Publicações por Ano"): Define o título do gráfico como "Distribuição de Publicações por Ano".
- plt.xlabel("Ano"): Define o rótulo do eixo X como "Ano".
- plt.ylabel("Número de Publicações"): Define o rótulo do eixo Y como "Número de Publicações".
- plt.xticks(rotation=45): Provoca uma rotação sobre as marcas (ticks) do eixo X (os anos) de 45 graus, para melhorar a legibilidade, especialmente se os anos forem muitos ou longos.
- plt.tight_layout(): Ajusta o layout do gráfico para garantir que tudo seja bem ajustado na área visível e não seja cortado.
- plt.show(): Exibe o gráfico gerado.

![Captura de ecrã 2025-01-02 154953.png](<attachment:Captura de ecrã 2025-01-02 154953.png>)

**2. gerarGraficoPorMesAno**

    A função cria e exibe um gráfico de barras que mostra o número de publicações em cada mês de um ano específico, com base nos dados fornecidos no dicionário contagem_meses. Ela filtra as publicações para o ano escolhido e, em seguida, cria um gráfico de barras para mostrar a distribuição de publicações ao longo dos meses desse ano.

Em seguida temos o ano de 2024 como exemplo:

![Captura de ecrã 2025-01-02 155012.png](<attachment:Captura de ecrã 2025-01-02 155012.png>)


**3. gerarGraficoPorAutor**

    Esta função cria e exibe um gráfico de barras horizontais que mostra o número de publicações de cada autor, usando os dados fornecidos na lista top_autores.

![Captura de ecrã 2025-01-02 155050.png](<attachment:Captura de ecrã 2025-01-02 155050.png>)

**4. gerarGraficoPalavrasChave**

    Esta função cria e exibe um gráfico de barras horizontais que mostra as 20 palavras-chave mais frequentes, baseando-se nos dados fornecidos no dicionário contagem_palavras_chave.

![Captura de ecrã 2025-01-02 155101.png](<attachment:Captura de ecrã 2025-01-02 155101.png>)

**4. gerarGraficoPalavrasAno**

    A função gerarGraficoPalavrasAno cria um gráfico de barras horizontais mostrando as 20 palavras-chave mais frequentes para um ano específico, utilizando um dicionário de palavras-chave por ano.

![Captura de ecrã 2025-01-02 155117.png](<attachment:Captura de ecrã 2025-01-02 155117.png>)


**Função para listar os autores das publicações:**

*listAutores*

    A função listAutores exibe uma lista de autores e os títulos das suas publicações. Inicialmente, verifica se o arquivo existe e, caso esteja válido e não vazio, carrega os dados. Em seguida, percorre as publicações para identificar os autores, associando os seus nomes aos títulos das publicações ou "Título Desconhecido" caso o título esteja ausente. Os autores são organizados por ordem alfabética, criando uma lista que inclui o nome do autor seguido pelos títulos. A função exibe uma interface gráfica com um título, uma lista interativa que mostra os autores e as suas publicações, e um botão "Fechar" para encerrar. Um loop mantém a interface ativa até que o utilizador clique em "Fechar" ou feche a janela, momento em que a função encerra e fecha a interface.

Em seguida temos o inicio da interface que aparece ao utilizador

![image-6.png](attachment:image-6.png)

**Função para importar publicações**:

*importarPubs*

A função é responsável por importar publicações de maneira controlada, garantindo a integridade dos dados existentes e fornecendo feedback ao utilizador durante cada etapa.

**Função para exportar para ficheiro toda a informação em memória:**

*exportarDados*

    A função exportarDados permite que o utilizador exporte publicações do sistema para um arquivo JSON, aplicando filtros opcionais para selecionar quais dados serão exportados.

## 4. Conclusão

O desenvolvimento do projeto que funciona como Sistema de Consulta e Análise de Publicações Científicas exigiu a aplicação de todo o conhecimento adquirido ao longo do semestre. Recorremos ainda à informação disponível no *W3Schools* e a informações adicionais na internet para atender aos objetivos do projeto. 

Apesar de ainda existirem aspetos a melhorar, o processo de criação deste sistema permitiu reforçar e aprofundar as nossas habilidades em programação. Além disso, tivemos a oportunidade de desenvolver uma solução prática e funcional, que pode ser útil no quotidiano e acessível a qualquer utilizador.


