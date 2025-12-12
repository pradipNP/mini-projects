import qrcode

data = input("Enter the url: ")

img = qrcode.make(data)

img.save("qrcode.png")

print("QR code saved as qrcode.png")