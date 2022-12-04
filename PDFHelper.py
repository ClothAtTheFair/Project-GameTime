import PyPDF2
from fpdf import FPDF

class PDFHelper:
    def __init__(self, PDFName, pageNums):
        self.pdfName = PDFName
        self.pageNums = pageNums

    def readPDF(self):
        pdfFileObj = open(self.pdfName, 'rb')
        self.pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        self.pageNums = self.pdfReader.numPages

    def mergePDF(self, pdfList, outputPDF):

        pdfMerger = PyPDF2.PdfFileMerger()
        for pdf in pdfList:
            pdfMerger.append(pdf)

        #writing combined pdf to output
        with open(outputPDF, 'wb') as f:
            pdfMerger.write(f)

    # This method only splits the pdf in half, for now
    def splitPDF(self, pdf, index):

        #TODO: Change this to readPDF method
        pdfFileObj = open(pdf, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        start = 0
        end = index

        for i in range(end):
            pdfWriter = PyPDF2.PdfFileWriter()
            outputPDF = pdf.split('.pdf')[0] + str(i) + '.pdf'

            for page in range(start, end):
                pdfWriter.add_page(pdfReader.get_page(page))

            with open(outputPDF, "wb") as f:
                pdfWriter.write(f)

        pdfFileObj.close()

    #split key sections into separate pdfs
    def splitOnTopic(self, pdf, topic):
        pass

    def writeContentToNewPDF(self, outputPDF, content):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)

        #create a cell for the content
        pdf.cell(200, 10, txt = content, ln = 1, align = 'L')

        pdf.output(outputPDF)

    def writeTXTFileToNewPDF(self, outputPDF, txtFile):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 15)

        f = open(txtFile, "r")

        for x in f:
            pdf.cell(200, 10, txt = x, ln = 1, align = 'L')

        pdf.output(outputPDF)


        