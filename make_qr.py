import qrcode

# 👇 把这个改成你自己的 GitHub Pages 链接
url = "https://ning-d.github.io/conference-globe/"

img = qrcode.make(url)
img.save("globe_qr.png")

print("✅ 已生成二维码: globe_qr.png")
