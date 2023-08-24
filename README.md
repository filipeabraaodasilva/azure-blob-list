# azure-blob-list
Aplicações criadas para listarem arquivos contidos em um container dentro do 'Azure Blob Storage'.

# app.py
Realiza consultas em banco de dados para obter credênciais de acesso a conta no Microsoft Azure e recebe os parâmetros 'Pasta de trabalho' (Local onde serão salvos os logs da aplicação e também o arquivo contendo os nomes dos arquivos).

# app_tmp.py
Recebe diretamente no código os parâmetros necessários para listagem dos blobs, sem a necessidade de passar por um banco de dados, recebe como parâmetro apenas a 'Pasta de trabalho' (Local onde serão salvos os logs da aplicação e também o arquivo contendo os nomes dos arquivos).
