from promptpay import qrcode
from PIL import Image
# generate a payload
id_or_phone_number = '0655059606'
payload = qrcode.generate_payload(id_or_phone_number)
payload_with_amount = qrcode.generate_payload(id_or_phone_number, 10)

# export to PIL image
img = qrcode.to_image(payload)
img23 = qrcode.to_image(payload_with_amount )
img23.save('qrcode.png')
images = Image.open('qrcode.png')
images.show()