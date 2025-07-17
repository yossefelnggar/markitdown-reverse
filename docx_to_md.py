from docx import Document
from markdownify import markdownify as md

# تحميل ملف Word (تأكد إن الملف موجود في نفس المجلد وده اسمه)
doc = Document("output.docx")

# جمع كل النصوص من الفقرات
full_text = "\n".join([para.text for para in doc.paragraphs])

# تحويل إلى Markdown
markdown_text = md(full_text)

# حفظ الناتج
with open("converted_back.md", "w", encoding="utf-8") as f:
    f.write(markdown_text)

print("✅ تم تحويل Word إلى Markdown!")
