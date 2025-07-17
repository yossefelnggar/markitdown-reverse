from docx import Document

# افتح ملف Markdown
with open("example.md", "r", encoding="utf-8") as file:
    lines = file.readlines()

# أنشئ مستند Word جديد
doc = Document()

# أضف كل سطر كفقرة
for line in lines:
    doc.add_paragraph(line.strip())

# احفظ الملف
doc.save("output.docx")

print("✅ تم التحويل من Markdown إلى Word!")
