from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import zipfile
import pandas as pd

def gerar_pdf(df):
    df = df.loc[:, df.columns!='id']
    df = df.loc[:, df.columns!='usuario_cadastro']
    df = df.loc[:, df.columns!='is_active']
    df = df.loc[:, df.columns!='contrato']
    df = df.loc[:, df.columns!='vigencia']
    df = df.rename(columns={'nome_completo': 'Nome Completo', 'unidade': 'Unidade', 
    'contratada': 'Contratada', 'cnpj_contratada': 'CNPJ', 'cargo': 'Cargo'})
    df = df.sort_values('Nome Completo')
    df.insert(0, 'id', range(1, len(df) + 1))

    df.to_csv('uploads/transparencia.csv')
    
    # Configurar o estilo da tabela
    styles = getSampleStyleSheet()
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.black),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),  # Tamanho da fonte do cabeçalho para 10 pontos
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 7.5),  # Tamanho da fonte dos dados para 7.5 pontos
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ])

    # Configurar o arquivo PDF
    pdf_filename = 'uploads/transparencia.pdf'
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter, leftMargin=0, 
    rightMargin=0, topMargin=-1, bottomMargin=-5)

    # Definir larguras de colunas personalizadas
    col_widths = [10, 10, 10, 10, 10, 10, 10, 10]

    # Criar a tabela a partir do DataFrame
    table_data = [df.columns.to_list()] + df.values.tolist()
    table = Table(table_data)

    # Aplicar o estilo à tabela
    table.setStyle(style)

    # Adicionar a tabela ao PDF
    elements = []
    elements.append(table)
    doc.build(elements)

    # Nome do arquivo zip a ser criado
    zip_filename = 'uploads/transparencia.zip'

    # Arquivos a serem incluídos no zip
    arquivos = ['uploads/transparencia.pdf', 'uploads/transparencia.csv']

    # Cria um arquivo zip e adiciona os arquivos
    with zipfile.ZipFile(zip_filename, 'w') as zip:
        for arquivo in arquivos:
            zip.write(arquivo)

    return 
