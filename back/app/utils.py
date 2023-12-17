from openpyxl import Workbook


def generate_excel(extra_classes: list, extra_groups: list, file_path: str):
    """
    Generate excel based on data like that 

    extra_classes:
    [
        {"weekday": 0, "class": 0, "groups": ["\u0421\u0418\u0418-1", "C\u0418\u0418-2"]}, 
        {"weekday": 0, "class": 1, "groups": ["\u0421\u0418\u0418-3"]}
    ]

    extra_groups:
    [
        {"name": "\u0421\u0418\u0418-1", "students": [
            {"group": "\u042d\u041f-362", "name": "6538ec43a04fb531ff864a26"}, 
            {"group": "\u042d\u041f-362", "name": "7832ac43a04fb545ff864a21"}]
        }
    ]
    """
    workbook = Workbook()

    sheet = workbook.active
    sheet.title = "extra_groups"

    sheet2 = workbook.create_sheet(title="extra_classes")

    # TODO: Add implementation of inserting values

    # sheet["A4"] = "row 4"

    workbook.save(file_path)
