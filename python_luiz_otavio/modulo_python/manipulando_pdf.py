# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# pip install pypdf2
from pathlib import Path

from PyPDF2 import PdfReader

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdf'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230707.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)
# print(len(reader.pages))

# for page in reader.pages:
#     print(page)

page0 = reader.pages[0]
print(page0.extract_text())
