from spire.doc import Document, ToPdfParameterList, PdfConformanceLevel


def format_converter(input_path):
    document = Document()
    document.LoadFromFile(input_path)
    parameters = ToPdfParameterList()
    parameters.PdfConformanceLevel = PdfConformanceLevel.Pdf_A1A
    document.SaveToFile('data.pdf', parameters)
    document.Close()
