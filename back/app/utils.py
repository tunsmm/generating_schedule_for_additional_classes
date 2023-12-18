from openpyxl import Workbook


def generate_excel(extra_classes: list, extra_groups: list, file_path: str):
    """
    Generate excel based on data like that 

    extra_classes = [
        {"weekday": 0, "class": 0, "groups": [" СИИ-1", "СИИ-2"]}, 
        {"weekday": 0, "class": 1, "groups": ["СИИ-3"]}
    ]

    extra_groups = [
        {"name": "СИИ-2", "students": [
                {"group": "ЭП-362", "name": "6538ec43a04fb531ff864a26"}, 
                {"group": "ЭП-362", "name": "7832ac43a04fb545ff864a21"}
            ]
        }
    ]
    """
    workbook = Workbook()

    file_path = r"C:\Users\nekit\OneDrive\Desktop\result.xlsx"

    sheet = workbook.active
    sheet.title = "extra_groups"

    name_col = "A"
    main_col = "B"
    add_col = "C"

    sheet[f"{name_col}1"] = "Имя студента"
    sheet[f"{main_col}1"] = "Основная группа"
    sheet[f"{add_col}1"] = "Доп. группа"

    current_row = 2
    for group in extra_groups:
        add_name_group = group.get("name")
        students = group.get("students")
        for student in students:
            student_group = student.get("group")
            student_name = student.get("name")

            sheet[f"{name_col}{current_row}"] = student_name
            sheet[f"{main_col}{current_row}"] = student_group
            sheet[f"{add_col}{current_row}"] = add_name_group

            current_row += 1

    sheet2 = workbook.create_sheet(title="extra_classes")

    weekdays = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "E",
        5: "F",
        6: "G",
    }

    sheet2["A1"] = "Понедельник"
    sheet2["B1"] = "Вторник"
    sheet2["C1"] = "Среда"
    sheet2["D1"] = "Четверг"
    sheet2["E1"] = "Пятница"
    sheet2["F1"] = "Суббота"
    sheet2["G1"] = "Воскресенье"

    for class_ in extra_classes:
        weekday = class_.get("weekday")
        weekday = weekdays[weekday]

        pair = class_.get("class") + 2
        
        groups = class_.get("groups")
        groups = ", ".join(groups)

        sheet2[f"{weekday}{pair}"] = groups

    workbook.save(file_path)
