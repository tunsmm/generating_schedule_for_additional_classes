from config import GENERATED_FILE_PATH, UPLOAD_DIR, WEEKDAYS_COUNT, CLASSES_COUNT, MAX_GROUP_CAPACITY

from alg.factories.timetablefactory import create_timetable_alg
from parser.mainparser import MainParser
from utils import generate_excel

time_table_alg = create_timetable_alg(MAX_GROUP_CAPACITY, WEEKDAYS_COUNT, CLASSES_COUNT)


def get_generated_schedule_name():
    filename = __generate_schedule()
    return filename


def __generate_schedule() -> str:
    main_parser = MainParser()

    file_path = UPLOAD_DIR / "studentsGroups" / "Iskhodny_spisok_xlsx.csv"
    parsed_extra_classes_data = main_parser.getExtraClassesJson(file_path)
    parsed_groups_students_data = main_parser.defGroupsStudentsJson(file_path)

    file_dir = UPLOAD_DIR / "schedules"
    parsed_groups_classes_data = main_parser.getGroupsClassesJson(file_dir)

    data_to_alg = {
        "classes": parsed_groups_classes_data,
        "main_groups": parsed_groups_classes_data,
        "extra_classes": parsed_extra_classes_data
    }

    extra_groups, extra_classes = time_table_alg.process(data_to_alg)

    file_path = GENERATED_FILE_PATH

    generate_excel(extra_classes, extra_groups, file_path)

    return file_path
