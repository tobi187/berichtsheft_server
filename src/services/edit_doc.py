from docxtpl import DocxTemplate
import io

BASE_TEMPLATE = r"C:\Users\fisch\Desktop\projects\web\berichtsheft_server\src\services\Berichtsheft_Template.docx"


def prepare_data(content):
    point = content["point"]
    if point:
        length = len(content["todos"].split("\n"))
        point = "\n".join([point for _ in range(length)])

    return {
        "name": content["name"],
        "department": content["department"],
        "nr": str(content["berichtNummer"]),
        "kw": content["date"],
        "todo": content["todos"],
        "weekly": content["weekly_theme"],
        "school": content["school"],
        "four": point
    }


def fill_doc(content):
    file_stream = io.BytesIO()
    doc = DocxTemplate(BASE_TEMPLATE)
    doc.render(
        prepare_data(content)
    )

    doc.save(file_stream)
    file_stream.seek(0)

    return file_stream.getvalue()
