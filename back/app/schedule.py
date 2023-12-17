from config import GENERATED_SCHEDULE_DIR, UPLOAD_DIR

from parser.mainparser import MainParser
from utils import generate_excel


def get_generated_schedule_name():
    filename = __generate_schedule()
    return filename

def __generate_schedule() -> str:
    main_parser = MainParser()

    file_path = UPLOAD_DIR / "studentsGroups" / "Исходный список.xlsx"
    parsed_extra_classes_data = main_parser.getExtraClassesJson(file_path)
    parsed_groups_students_data = main_parser.defGroupsStudentsJson(file_path)

    file_dir = UPLOAD_DIR / "schedules"
    parsed_groups_classes_data = main_parser.getGroupsClassesJson(file_dir)

    # TODO: Add algorithm working
    extra_classes, extra_groups = None, None  # Here is your algorithm result

    filename = 'result_schedule.xlsx'
    file_path = GENERATED_SCHEDULE_DIR / filename

    # TODO: Add generating excel
    generate_excel(extra_classes, extra_groups, file_path)

    return file_path
