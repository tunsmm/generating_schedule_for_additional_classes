from config import GENERATED_SCHEDULE_DIR

from parser.mainparser import MainParser


def get_generated_schedule_name():
    filename = __generate_schedule()
    return filename

def __generate_schedule() -> str:
    main_parser = MainParser()

    parsed_extra_classes_data = main_parser.getExtraClassesJson()
    parsed_groups_classes_data = main_parser.getGroupsClassesJson()
    parsed_groups_students_data = main_parser.defGroupsStudentsJson()

    # TODO: Add algorithm working

    filename = 'result_schedule.xlsx'
    file_path = GENERATED_SCHEDULE_DIR / filename

    return file_path
