import os, fitz
 
doc = fitz.open("course.pdf")
os.makedirs("pages", exist_ok=True)
for i, page in enumerate(doc, 1):
    page.get_pixmap(dpi=130).save(f"pages/{i:03d}.jpg", jpg_quality=85)
    print(f"{i}/{len(doc)}", end="\r")
with open("pages/meta.js", "w") as f:
    f.write(f"window.BOOK_PAGES={len(doc)};")
print("\nДайын:", len(doc), "бет")
