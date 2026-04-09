import qrcode

def generate_qr(machine_code):
    url = f"https://mantenimiento-ap.vercel.app/equipment/{machine_code}"
    img = qrcode.make(url)
    img.save(f"{machine_code}.png")
    return "QR generado"