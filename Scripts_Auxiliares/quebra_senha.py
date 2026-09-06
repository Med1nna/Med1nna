from pypdf import PdfReader, PdfWriter
from io import BytesIO
import getpass
import os

def remover_senha_pdf_sobrescrever():
    print("--- Removedor de Senha de PDF (Sobrescrevendo) ---")
    arquivo_entrada = input("Caminho do PDF protegido (ex: C:/fatura.pdf): ").strip()
    
    if not os.path.exists(arquivo_entrada):
        print("Erro: O arquivo não foi encontrado.")
        return

    # Como deve ficar (visível):
    senha = input("Digite a senha do PDF: ") 

    try:
        # Lê o PDF como dados brutos (bytes) para a memória e fecha o arquivo em disco
        with open(arquivo_entrada, "rb") as f:
            pdf_bytes = BytesIO(f.read())

        # O leitor agora usa a versão que está na memória
        reader = PdfReader(pdf_bytes)

        if not reader.is_encrypted:
            print("Aviso: Este PDF não está protegido por senha. Nenhuma alteração foi feita.")
            return

        # Tenta descriptografar
        resultado = reader.decrypt(senha)

        if resultado:
            writer = PdfWriter()

            # Copia as páginas descriptografadas
            for page in reader.pages:
                writer.add_page(page)

            # Sobrescreve o arquivo original com a versão sem senha
            with open(arquivo_entrada, "wb") as f:
                writer.write(f)
                
            print(f"\nSucesso! O arquivo original foi sobrescrito sem a senha em: {arquivo_entrada}")
        else:
            print("\nErro: A senha informada está incorreta. O arquivo não foi modificado.")

    except Exception as e:
        print(f"\nOcorreu um erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    remover_senha_pdf_sobrescrever()