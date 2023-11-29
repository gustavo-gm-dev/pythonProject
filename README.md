<h1 align="center"> Price Analisy - Batimento de preço </h1>
<h2> Descrição </h2>
Este projeto tem como objetivo realizar todo o processo de extração de preços do ElasticSearch para um arquivo CSV. O processo inclui a entrada de parâmetros, chamadas de API GET e exportação dos dados para um arquivo delimitado por ";".

<h2> Funcionalidades do projeto </h2>
    
- `Validação de Variáveis de Entrada:` : Para a chamada do programa é necessacio passar alguns parametro, segue exemplo a seguir:
  - Comando: ```py price_analysis.py endpoint user pass diretorio registros ultimo_registro```
  - `py` = Programa que será chamado
  - `price_analysis.py` = Nome do programa que será executado
  - `endpoint` = Link do endpoint do elasticSearch que será efetuado a chamada da API
  - `user` = Usuario do elasitcSearch
  - `pass` = Senha do elastciSearch
  - `diretorio` = Diretorio que o arquivo CSV será gravado
  - `registros` = Quantidade de registro que será consumido por chamada (size)
  - `ultimo_registro` = Comando utilizado para recuperar a próxima página de ocorrências usando um conjunto de valores de classificação da página anterior. (search_after)
- `Chamada de API GET` :  Após a validação das variáveis, o sistema realiza uma chamada de API GET para o servidor especificado, recuperando os dados necessários para o processamento.
- `Parsing de JSON` : Os dados recebidos da API, geralmente em formato JSON, são estruturados e organizados em linhas para facilitar a manipulação posterior.
- `Gravação em CSV` : Os dados processados são gravados em um arquivo CSV, permitindo fácil importação e análise em ferramentas como planilhas eletrônicas.
- `Logs Detalhados` : Todos os passos do processo são registrados em logs detalhados, facilitando a identificação e resolução de problemas caso ocorram.
