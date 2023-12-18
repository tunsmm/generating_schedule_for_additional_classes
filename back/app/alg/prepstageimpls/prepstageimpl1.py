import numpy as np

from alg.preprocessstage import PreprocessStage


class PreprocessStageImpl1(PreprocessStage):
    def __init__(self, weekdays=6, classes_count=6):
        # self._classes_variant = {
        #     "1-2": 0,
        #     "3-4": 1,
        #     "5-6": 2,
        #     "7-8": 3,
        #     "9-10": 4,
        #     "11-12": 5,
        # }
        self._classes_variant = {
            "1": 0,
            "2": 1,
            "3": 2,
            "4": 3,
            "5": 4,
            "6": 5,
        }

        self._weekdays_variants = {
            'понедельник': 0,
            'вторник': 1,
            'среда': 2,
            'четверг': 3,
            'пятница': 4,
            'суббота': 5
        }

        self._even_variants = {
            'НЕЧЕТНАЯ': 0,
            'ЧЕТНАЯ': 1
        }

        self._main_groups = []
        self._classes = []
        self._extra_classes = []

        self._result_groups = np.empty(shape=(classes_count, weekdays), dtype=list)
        self._result_students = np.empty(shape=(classes_count, weekdays), dtype=list)
        for i, r_ in enumerate(self._result_groups):
            for j, r__ in enumerate(r_):
                self._result_groups[i][j] = []
                self._result_students[i][j] = []

    def _get_main_groups(self, data):
        """Метод, который необходимо переопределить для того, чтобы
        получить первичные данные о группах из тех, которые подаются блоку на вход.
        Данные должны быть преобразованы в JSON формат (словарь),
        далее эти данные будут использоваться для преобразования в более удобный вид
        в пределах этого блока для выполнения его работы.
        """
        result = data["main_groups"]
        return result

    def _parse_main_groups(self, data):
        """Метод, который должен быть переопределн для преобразования данных
        о группах (которые были результатом работы метода _get_main_groups),
        чтобы обработать"""
        student_groups_result = []
        for group in data:
            student_groups_result.append(group["group"])

        student_groups_result = self._parse_main_groups_prep(student_groups_result)
        return student_groups_result

    def _get_classes(self, data):
        result = data['classes']
        return result

    def _parse_classes(self, data):
        result = []

        weekdays_variants = self._weekdays_variants
        classes_variants = self._classes_variant

        middle_dict = {}
        for group in data:
            group_data = group["group"]
            group_name = group_data["name"]

            for free_class in group_data["free_classes"]:
                weekday_name = free_class["weekday"]
                class_name = free_class["class"]

                weekday_name = weekday_name.replace(" ", "").lower()
                class_name = class_name.replace(" ", "").lower()

                weekday = weekdays_variants[weekday_name]
                class_num = classes_variants[class_name]

                class_key = (class_num, weekday)

                if class_key not in middle_dict:
                    middle_dict[class_key] = set()

                middle_dict[class_key].add(group_name)

        for class_key in middle_dict:
            result.append({
                "weekday": class_key[1],
                "class": class_key[0],
                "groups": list(middle_dict[class_key])
            })

        return result

    def _get_extra_classes(self, data):
        result = data["extra_classes"]
        return result

    def _parse_extra_classes(self, data):
        extra_classes_result = []

        for extra_class in data:
            extra_class_data = extra_class["class"]
            extra_class_name = extra_class_data["name"]
            extra_class_groups = extra_class_data["groups"]

            extra_class_students = set()

            for group in extra_class_groups:
                group_data = group["group"]
                group_students = group_data["students"]
                for student in group_students:
                    extra_class_students.add(student)

            current_data = {
                "name": extra_class_name,
                "students": list(extra_class_students)
            }

            extra_classes_result.append(current_data)

        extra_classes_result = self._parse_extra_classes_prep(extra_classes_result)

        return extra_classes_result