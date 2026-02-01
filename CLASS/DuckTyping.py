# Duck typing : It is concept where the type of an object is determined by its behaviour, not by its class.
class InkJetPrinter:
    def printDocument(self,document):
        print("InkJet Printer printing : ",document)

class LaserPrinter:
    def printDocument(self,document):
        print("Laser Printer printing : ",document)

class PDFWriter:
    def printDocument(self,document):
        print(f"saving : {document} as PDF")

def StartPrinting(device):
    device.printDocument("Marvellous Notes")

def main():
    StartPrinting(InkJetPrinter())
    StartPrinting(LaserPrinter())
    StartPrinting(PDFWriter())

main()
