import webbrowser
import os
from filestack import Client

class PDFPrintout:
    """
    object that contains a PDF version of the bill
    """

    def __init__(self, fileName):
        self.fileName = fileName


    def generate(self, bill, house):
        from fpdf import FPDF

        pdf = FPDF(orientation="portrait", unit="pt", format="A4")
        pdf.add_page()

        # Add an image
       # pdf.images("house.png", w=20, l=30)

        # Add some text
        pdf.set_font(family="Times", size=24, style="B")

        pdf.cell(w=0, h=50, txt="Flatmates Bill", border=1, align="C", ln=1)

        pdf.cell(w=100, h=50, txt="Period:", border=1, align="L")
        pdf.cell(w=170, h=50, txt=bill.period, border=1, align="C")

        pdf.cell(w=110, h=50, txt="Address:", border=1, align="C")
        pdf.cell(w=0, h=50, txt=house.address, border=1, align="C", ln=1)

        pdf.cell(w=100, h=30, txt="Name", border=1, align="C")
        pdf.cell(w=0, h=30, txt="Amount", border=1, align="R", ln=1)

        for flatmate in house.listOfFlatmates:

            pdf.set_font(family="Times", size=16)
            pdf.cell(w=100, h=30, txt=flatmate.name, border=1, align="C")
            pdf.set_font(family="Times", size=8)
            pdf.cell(w=350, h=30, txt=flatmate.the_maths, border=1, align="C")
            pdf.set_font(family="Times", size=16)
            pdf.cell(w=0, h=30, txt="£"+str(round(flatmate.pays(bill, house),2)), border=1, align="R", ln=1)

        # pdf.cell(w=100, h=30, txt=flatMate2.name, border=1, align="C")
        # pdf.set_font(family="Times", size=8)
        # pdf.cell(w=350, h=30, txt=flatMate2.the_maths , border=1, align="C")
        # pdf.set_font(family="Times", size=16)
        # pdf.cell(w=0, h=30, txt="£"+str(round(flatMate2.pays(bill,house),2)) , border=1, align="R", ln=1)

        pdf.cell(w=0, h=30, txt=f"Total: £{bill.amount}", border=1, align="R", ln=1)

        os.chdir("files")
        pdf.output(self.fileName)
        webbrowser.open(self.fileName)

class FileSharer:

    def __init__(self, filepath, api_key="A1cGdfaMGQZuze08wm1CDz"):
        self.filepath=filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_file_link = client.upload(filepath=self.filepath)
        return new_file_link.url