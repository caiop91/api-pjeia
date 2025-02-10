import requests
import json
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtém a chave de API da variável de ambiente
API_KEY = os.getenv("PJEIA_API_KEY")
API_URL = "https://pjeia-backend.vercel.app/api/v1/external/completions"

def read_document():
    try:
        with open("documento.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("❌ Erro: arquivo documento.txt não encontrado")
        return None

def main():
    # Verifica se a chave de API está configurada
    if not API_KEY:
        print("❌ Erro: Chave de API não encontrada. Configure a variável de ambiente PJEIA_API_KEY")
        return

    # Lê o documento
    document_content = read_document()
    if not document_content:
        return

    # Pega o prompt do usuário
    user_prompt = input("Digite seu prompt: ")

    # Monta o prompt final
    final_prompt = f"{user_prompt}\n\n###\ndocumento anexado pelo usuário:\n{document_content}"

    # Configuração da requisição
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": API_KEY
    }
    
    data = {
        "prompt": final_prompt
    }

    try:
        # Faz a requisição
        print("\n🔄 Enviando requisição...")
        response = requests.post(API_URL, headers=headers, json=data, stream=True)
        
        if response.status_code == 429:
            print("❌ Erro: Limite de requisições excedido. Tente novamente mais tarde.")
            return
            
        if response.status_code != 200:
            print(f"❌ Erro: {response.json().get('error', 'Erro desconhecido')}")
            return

        # Processa a resposta em streaming
        print("\n🤖 Resposta do PJeIA:\n")
        for line in response.iter_lines():
            if line:
                line = line.decode('utf-8')
                if line.startswith("data: "):
                    content = line[6:]  # Remove o prefixo "data: "
                    if content == "[DONE]":
                        break
                    try:
                        chunk = json.loads(content)
                        print(chunk["content"], end="", flush=True)
                    except json.JSONDecodeError:
                        continue

    except requests.exceptions.RequestException as e:
        print(f"\n❌ Erro na requisição: {str(e)}")
    except KeyboardInterrupt:
        print("\n\n⚠️ Operação cancelada pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {str(e)}")

if __name__ == "__main__":
    main() 