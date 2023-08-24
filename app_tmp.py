# IMPORTANDO BIBLIOTECAS DE TERCEIROS
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient



# Execução da aplicação
pasta_de_trabalho: str = input("\nINSIRA SUA PASTA DE TRABALHO: ")
nome_container: str = input("\nINSIRA O NOME DO CONTAINER DESEJADO: ")

conta: str = "account"
chave: str = "key"

url: str = "https://{}.blob.core.windows.net".format(conta)

blob_service_client = BlobServiceClient(account_url=url, credential=key)

container_client = blob_service_client.get_container_client(nome_container)

blobs = container_client.list_blobs()

print("\nLISTANDO OS BLOBS DO CONTAINER {}.".format(nome_container))

contador: int = 0

for blob in blobs:
    arquivo = blob.name
    
    with open(pasta_de_trabalho + "\\lista_de_arquivos_do_container_{}.txt".format(nome_container), "a", encoding="utf-8") as lista:
        lista.write("{}\n".format(arquivo))
    
    contador += 1
    
print("\nFORAM LISTADOS {} ARQUIVO(S).".format(contador))
