from reportlab.graphics.barcode import code128
from reportlab.graphics.barcode import code93
from reportlab.graphics.barcode import code39
from reportlab.graphics.barcode import usps
from reportlab.graphics.barcode import usps4s
from reportlab.graphics.barcode import ecc200datamatrix
from reportlab.lib.pagesizes import A10
from reportlab.lib.units import cm, mm, inch
from reportlab.pdfgen import canvas

class MyEZBarcode():
    def __init__(self, parent):
        pass

    def createBarCodes(txt):
        """
        Create barcode examples and embed in a PDF
        """
        file_name = "./output/{}_mini_label.pdf".format(txt)
        len, wid = A10
        A10_landscape = (wid, len)
        canvs = canvas.Canvas(file_name, pagesize=A10_landscape)
        # canvas.setFontSize(size = 12)
        print("page size = ", A10_landscape)
        print(canvs.getAvailableFonts())
        code = txt
        x = -15
        y = 30
        print(x, y)

        barcode= code128.Code128(code)

        canvs.saveState()
        canvs.translate(0 * cm, 1 * cm)  # bottom left corner of the barcode
        canvs.scale(5.2 * cm / barcode.width, 1.5 * cm / barcode.height)  # resize (15 cm and 2 cm)
        barcode.drawOn(canvs, -17, 0)
        canvs.restoreState()
        canvs.setFontSize(size = 12)
        canvs.drawString(x+32, y-12, str(code))
        canvs.save()
#
# if __name__ == "__main__":
#     MyEZBarcode.createBarCodes("1291-11-23")







