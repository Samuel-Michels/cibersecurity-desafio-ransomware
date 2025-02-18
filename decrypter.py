import os
import pyaes

def decrypt_file(file_name, key):
    try:
        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Descriptografar o arquivo
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        # Criar o arquivo descriptografado
        new_file_name = file_name.replace(".ransomwaretroll", "")
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo '{new_file_name}' descriptografado com sucesso!")
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")

# Nome do arquivo e chave de descriptografia
file_name = "teste.txt.ransomwaretroll"
key = b"testeransomwares"

# Chamar a função de descriptografia
decrypt_file(file_name, key)
