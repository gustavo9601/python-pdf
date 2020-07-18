import fitz

# pip install PyMuPDF
# https://pypi.org/project/PyMuPDF/

pdf_documento = 'test_2.pdf'
documento = fitz.open(pdf_documento)
print("Cantidad de paginas", documento.pageCount)
print("Metadata", documento.metadata)

# .loadPage(# pagina desde 0)
pagina = documento.loadPage(2)
textPagina = pagina.getText('text')
#textPagina = pagina.getText('text').encode('utf8')
print("textPagina", textPagina)

for numberPage in range(0, documento.pageCount):
    print(numberPage, documento.loadPage(numberPage).getText('text'))
