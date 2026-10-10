
from PIL import Image

# Open texture
img = Image.open("texture.png").convert("RGB")
w, h = img.size

# Offset texture by half its dimensions
offset = Image.new("RGB", (w, h))

offset.paste(img.crop((0, 0, w//2, h//2)), (w//2, h//2))
offset.paste(img.crop((w//2, 0, w, h//2)), (0, h//2))
offset.paste(img.crop((0, h//2, w//2, h)), (w//2, 0))
offset.paste(img.crop((w//2, h//2, w, h)), (0, 0))

offset.save("offset_texture.png")
