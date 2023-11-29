<h1 align="center"> Price Analisy - Batimento de preço </h1>
<h2> Descrição </h2>
Este projeto tem como objetivo realizar todo o processo de extração de preços do ElasticSearch para um arquivo CSV. O processo inclui a entrada de parâmetros, chamadas de API GET e exportação dos dados para um arquivo delimitado por ";".

<h2> Funcionalidades do projeto </h2>

- `Validação de Variáveis de Entrada:` : Para a chamada do programa é necessacio passar alguns parametro.
-- Ex: `py price_analysis.py https://elk-motor-oc-dev.ovd.com.br elastic G6U2j01xr70942e4pqAFqPlR C:\Users\ovd8439\PycharmProjects\pythonProject 10000 0`

### 
Antes de iniciar o processamento, o sistema valida as variáveis de entrada, garantindo que estão corretas e atendem aos requisitos necessários.

### Chamada de API GET:
Após a validação das variáveis, o sistema realiza uma chamada de API GET para o servidor especificado, recuperando os dados necessários para o processamento.

### Parsing de JSON:
Os dados recebidos da API, geralmente em formato JSON, são estruturados e organizados em linhas para facilitar a manipulação posterior.

### Gravação em CSV:
Os dados processados são gravados em um arquivo CSV, permitindo fácil importação e análise em ferramentas como planilhas eletrônicas.

### Logs Detalhados:
Todos os passos do processo são registrados em logs detalhados, facilitando a identificação e resolução de problemas caso ocorram.
