# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# pip install pypdf2
from pathlib import Path

from PyPDF2 import PdfReader, PdfWriter

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
imagem0 = page0.images[2]
print(page0.extract_text())
print(imagem0)

# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)


writer = PdfWriter()
with open(PASTA_NOVA / 'renata.pdf', 'wb') as fp:
    for page in reader.pages:
        writer.add_page(page)
    writer.write(fp)  # type: ignore
