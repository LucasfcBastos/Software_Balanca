from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from tkinter import filedialog
from components.database import *


def gerar_pdf_abate(id_abate):

    abates = listar_abate()
    abate = next((a for a in abates if a["id"] == int(id_abate)), None)

    if not abate:
        return False

    produtor = abate.get("produtor", {})
    industria = abate.get("industria", {})
    lotes = abate.get("lotes", [])

    data_formatada = abate.get("data_registro", "").replace("/", "-").replace(":", "-")
    nome_padrao = f"abate_{abate['id']}_{data_formatada}"

    caminho_pdf = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("Arquivo PDF", "*.pdf")],
        initialfile=nome_padrao,
        title="Salvar Relatório de Abate"
    )

    if not caminho_pdf:
        return False

    doc = SimpleDocTemplate(caminho_pdf)
    elementos = []
    styles = getSampleStyleSheet()

    # ===== TÍTULO =====
    elementos.append(Paragraph("<b>RELATÓRIO DE ABATE</b>", styles["Title"]))
    elementos.append(Spacer(1, 0.4 * inch))

    # ===== CABEÇALHO =====
    elementos.append(Paragraph(f"<b>PRODUTOR:</b> {produtor.get('nome','')}", styles["Normal"]))
    elementos.append(Paragraph(f"<b>INDÚSTRIA:</b> {industria.get('nome','')}", styles["Normal"]))
    elementos.append(Paragraph(f"<b>DATA:</b> {abate.get('data_registro','')}", styles["Normal"]))
    elementos.append(Spacer(1, 0.3 * inch))

    total_animais = 0
    total_kg = 0
    total_arroba = 0

    # ===== LOTES =====
    for i, lote in enumerate(lotes, start=1):

        elementos.append(Paragraph(f"<b>LOTE {i}: {lote.get('tipo','')}</b>", styles["Heading3"]))
        elementos.append(Spacer(1, 0.2 * inch))

        dados_tabela = [
            ["ID", "Lado A", "Lado B", "Total KG", "@"]
        ]

        for animal in lote.get("animais", []):

            dados_tabela.append([
                animal.get("id"),
                f"{animal.get('banda_a', 0):.2f}",
                f"{animal.get('banda_b', 0):.2f}",
                f"{animal.get('peso_total', 0):.2f}",
                f"{animal.get('peso_arroba', 0):.2f}",
            ])

            total_animais += 1
            total_kg += animal.get("peso_total", 0)
            total_arroba += animal.get("peso_arroba", 0)

        tabela = Table(dados_tabela, colWidths=[50, 80, 80, 80, 60])
        tabela.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
            ("GRID", (0,0), (-1,-1), 1, colors.black),
            ("ALIGN", (1,1), (-1,-1), "CENTER"),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ]))

        elementos.append(tabela)
        elementos.append(Spacer(1, 0.4 * inch))

    # ===== RESUMO =====
    elementos.append(Paragraph("<b>RESUMO</b>", styles["Heading2"]))
    elementos.append(Spacer(1, 0.2 * inch))

    media_kg = total_kg / total_animais if total_animais else 0
    media_arroba = total_arroba / total_animais if total_animais else 0

    resumo_data = [
        ["QUANT. BOVINO", "TOTAL KG", "MÉDIA KG", "TOTAL @", "MÉDIA @"],
        [
            total_animais,
            f"{total_kg:.2f}",
            f"{media_kg:.2f}",
            f"{total_arroba:.2f}",
            f"{media_arroba:.2f}"
        ]
    ]

    tabela_resumo = Table(resumo_data, colWidths=[100, 80, 80, 80, 80])
    tabela_resumo.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ]))

    elementos.append(tabela_resumo)

    doc.build(elementos)

    return caminho_pdf