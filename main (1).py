import qrcode

# User se input le lo
data = input("Enter your URL or any text: ")

# QR code generate karo
qr = qrcode.make(data)

# Save as image file
qr.save("my_qr.png")

print("QR Code generated and saved as my_qr.png!")