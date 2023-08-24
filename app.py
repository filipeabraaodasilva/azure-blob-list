# IMPORTANDO BIBLIOTECAS DE TERCEIROS
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import pyodbc



# BIBLIOTECAS INTERNAS
# Super classe para realizar conexão com o banco
class Conexao:
    def __init__(self) -> None:
        self.__conn = pyodbc.connect(
            'Driver={SQL Server};'
            'Server=nome_servidor.database.windows.net;'
            'Database=banco_de_dados;'
            'Uid=usuario;'
            'Pwd=senha;'
        )


# Função para obter chaves para acesso ao Azure
class UnidadeCliente(Conexao):
    def __init__(self, id_unidade_cliente: str) -> None:
        super().__init__()
        self.__cursor = self._Conexao__conn.cursor()
        self.__cursor.execute("""
        SELECT      u.Id AS 'IdUnidade',
                    c.Id AS 'IdCliente',
                    u.Azure_NomeConta AS 'ContaAzure',
                    u.Azure_ChaveAcessoPrimario AS 'ChaveAzure'
        FROM        Schema.UnidadeCliente uc
        INNER JOIN  Schema.Unidade u ON u.Id = uc.IdUnidade AND uc.Id = ?
        INNER JOIN  Schema.Cliente c ON c.Id = uc.IdCliente
        """, id_unidade_cliente)

        self.__resultado = self.__cursor.fetchone()
        self.__cursor.close()
        self._Conexao__conn.close()
        
    @property
    def get_retorno(self) -> dict:
        dados = {
            "id_cliente": self.__resultado[1],
            "id_unidade": self.__resultado[0],
            "azure_conta": self.__resultado[2],
            "azure_chave": self.__resultado[3]
        }
        return dados


# Execução da aplicação
pasta_de_trabalho: str = input("INSIRA SUA PASTA DE TRABALHO: ")
id_unidade_cliente: str = input("\nINSIRA O IDUNIDADECLIENTE DESEJADO: ")

azure = UnidadeCliente(id_unidade_cliente)
azure_dados = azure.get_retorno

url: str = "https://{}.blob.core.windows.net".format(azure_dados["azure_conta"])
key: str = azure_dados["azure_chave"]

blob_service_client = BlobServiceClient(account_url=url, credential=key)

container = azure_dados["id_cliente"].lower()
container_client = blob_service_client.get_container_client(container)

blobs = container_client.list_blobs()

contador: int = 0

print("\nLISTANDO OS BLOBS DO CONTAINER {}.".format(container))

for blob in blobs:
    arquivo = blob.name
    
    with open(pasta_de_trabalho + "\\lista_de_arquivos_container_{}.txt".format(container), "a", encoding="utf-8") as lista:
        lista.write("{}\n".format(arquivo))
    
    contador += 1
    
print("\nFORAM LISTADOS {} ARQUIVO(S).".format(contador))
    