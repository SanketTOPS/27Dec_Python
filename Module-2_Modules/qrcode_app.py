import qrcode

# url = "http://topshrms.in/"

data = "Hello Students! I'm Sanket from TOPS"

qr = qrcode.make(data)
qr.save("data.png")
