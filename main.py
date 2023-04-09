# pip install qrcode

import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('https://github.com/Sh-Alexandr')
qr.make(fit=True)

img = qr.make_image(image_factory=StyledPilImage, embeded_image_path="logoGitHub.png")

img.save("qrcode.png")

