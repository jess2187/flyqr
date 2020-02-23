import qrcode
from PIL import Image
from pdf2image import convert_from_path

class PDF_QR():
    def __init__(self, pdf_url, px = -1, py = -1, pwidth = 100, pheight = 100):
        self.pdf_url = pdf_url
        pdf_as_img = self.getBlankPDF()
        self.left_x = int(pdf_as_img.size[0]*px)
        self.width = int(pdf_as_img.size[0]*pwidth)
        self.top_y = int(pdf_as_img.size[1]*py)
        self.height = int(pdf_as_img.size[1]*pheight)
        if self.width != self.height:
            print("warning: non-square qr code will be created w/ dims", (self.width, self.height))

    def getBlankPDF(self):
        return convert_from_path(self.pdf_url)[0]

    def getQR_img(self, url):
        img = qrcode.make(url).convert('RGB').resize((self.width, self.height))
        return img

    def placeImageOnBlankPDF(self, url):
        add_img = self.getQR_img(url)
        blank_pdf = self.getBlankPDF()
        blank_pdf.paste(add_img, (self.left_x, self.top_y))
        return blank_pdf

    def generatePDF(self, list_of_urls, dest_url = "out.pdf"):
        imlist = []
        for url in list_of_urls:
            imlist.append(self.placeImageOnBlankPDF(url))
        imlist[0].save(dest_url, save_all = True, append_images=imlist[1:])

#qr = PDF_QR("blank_pdf.pdf", 0.4, 0.4, 0.2, 0.2)
#qr.generatePDF(ex_urls, dest_url="out.pdf")