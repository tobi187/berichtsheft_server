from docxtpl import DocxTemplate

BASE_TEMPLATE = ""


def fill_doc():
    doc = DocxTemplate(BASE_TEMPLATE)
    doc.render({
        "aaa": "bbbb"
    })

    with open("/home/tobi/projects/web/berichtsheft_server/src/test.docx", "wb") as f:
        f.write(doc.docx)
