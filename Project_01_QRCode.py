import qrcode as qc

# image = qc.make("https://deepak-kumar62.github.io/PackShifts_website_clone/")
# image.save("Deepak_Website.png")
from PIL import Image

qr = qc.QRCode(version=5,
               error_correction=qc.constants.ERROR_CORRECT_H,
               box_size=5, border=2, )

qr.add_data("https://deepak-kumar62.github.io/PackShifts_website_clone/")
qr.make(fit=True)
image = qr.make_image(fill_color="pink", back_color="white")
image.save("Deepak_Website_QRCode.png")
