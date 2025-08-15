import qrcode
import os

# Thông tin thiết bị
device_info = {
    "device_id": "TB001",
    "device_name": "Laptop Dell XPS 15",
    "model": "XPS 15 9520",
    "serial_number": "123456789-IT",
    "purchase_date": "15/08/2023",
    "owner": "Nguyễn Văn A",
    "status": "Đang sử dụng"
}


# Tạo URL GitHub Pages (thay bằng username GitHub của bạn)
github_username = "LPVincent01"  # Thay bằng username GitHub của bạn
repo_name = "QRCODE"        # Tên repo
device_id = "DEV001"            # ID thiết bị

url = f"https://{github_username}.github.io/{repo_name}/device.html?id={device_id}"

# Tạo QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Lưu QR Code
if not os.path.exists('output'):
    os.makedirs('output')
img.save(f"output/{device_info['device_id']}.png")

print(f"QR Code đã được tạo và lưu tại: output/{device_info['device_id']}.png")
print(f"URL: {url}")