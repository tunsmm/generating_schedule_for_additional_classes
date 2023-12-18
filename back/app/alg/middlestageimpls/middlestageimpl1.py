import numpy as np

from alg.middlestage import MidProcessStage


class MidProcessStageImpl1(MidProcessStage):
    def __init__(self, weekdays_count=6, classes_count=6):
        self._weekdays_count = weekdays_count
        self._classes_count = classes_count

    def get_free_students(self, data):
        students = data["free_students"]
        return students

    def _create_extra_timetable(self):
        rows = self._classes_count
        columns = self._weekdays_count
        result = np.empty(shape=(rows, columns), dtype=object)
        for i, r_ in enumerate(result):
            for j, r__ in enumerate(r_):
                result[i][j] = {
                    "value": 0,
                    "students": set()
                }

        return result

    def form_extra_classes_timetables(self, free_students):
        extra_results = {}

        for class_num, class_data in enumerate(free_students):
            for weekday_num, class_cell in enumerate(class_data):
                for stud in class_cell:
                    student = stud["student"]
                    stud_extra_classes = stud["extra_classes"]

                    for extra_class in stud_extra_classes:

                        if extra_class not in extra_results:
                            extra_timetable_data = self._create_extra_timetable()
                            extra_results[extra_class] = extra_timetable_data
                        else:
                            extra_results[extra_class][class_num][weekday_num]["value"] += 1
                            extra_results[extra_class][class_num][weekday_num]["students"].add(student)

        return extra_results

    def update(self, extra_timetables):
        for extra_timetable in extra_timetables:
            current_timetable = extra_timetables[extra_timetable]

            for i, current_row in enumerate(current_timetable):
                for j, current_cell in enumerate(current_row):
                    students = current_cell["students"]
                    current_value = len(students)
                    extra_timetables[extra_timetable][i][j]["value"] = current_value
        #                     if i == 0 and j == 0:
        #                         print(current_cell)

        return extra_timetables