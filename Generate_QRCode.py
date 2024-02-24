#GENERATE QRCODE 

#IMPORT LIBRARY
import qrcode as qr
print("GENERATE QRCODE BY JUST GIVING ANY LINK!")

print()

ver=int(input("ENTER THE SIZE OF QRCODE:"))
b_size=int(input("ENTER THE SIZE OF INNER BOX:"))
bor=int(input("ENTER THE SIZE OF OUTER BORDER:"))

print()

link=input("PLEASE PROVIDE A LINK:")

print()

inner_color=input("ENTER COLOR FOR INNER PORTION:")
b_color=input("ENTER COLOR FOR BACK PORTION:")


qr_code=qr.QRCode(version=ver,box_size=b_size,border=bor)
qr_code.add_data(link)
qr_code.make(fit=True)
img=qr_code.make_image(fill=inner_color,back_color=b_color)
img.save("practice7.png")
