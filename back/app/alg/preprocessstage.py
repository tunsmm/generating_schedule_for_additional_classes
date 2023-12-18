from abc import ABC, abstractmethod, abstractproperty
import json

import numpy as np


class PreprocessStage(ABC):
    @abstractmethod
    def _get_main_groups(self, data):
        """Метод, который необходимо переопределить для того, чтобы
        получить первичные данные о группах из тех, которые подаются блоку на вход.
        Данные должны быть преобразованы в JSON формат (словарь),
        далее эти данные будут использоваться для преобразования в более удобный вид
        в пределах этого блока для выполнения его работы.
        """
        result = []
        return result

    @abstractmethod
    def _parse_main_groups(self, data):
        """Метод, который должен быть переопределн для преобразования данных
        о группах (которые были результатом работы метода _get_main_groups),
        чтобы обработать"""
        # TODO: Дописать преобразования данных с пред.слоя
        pass

    def _parse_main_groups_prep(self, data):
        result = {}
        for group in data:
            group_name = group['name']
            group_students = group['students']
            result[group_name] = group_students

        return result

    @abstractmethod
    def _get_classes(self, data):
        result = data['classes']
        return result

    @abstractmethod
    def _parse_classes(self, data):
        result = []
        # TODO: Дописать преобразования данных с пред.слоя
        return result

    @abstractmethod
    def _get_extra_classes(self, data):
        result = []
        return result

    @abstractmethod
    def _parse_extra_classes(self, data):
        # TODO: Дописать преобразования данных с пред.слоя
        pass

    def _parse_extra_classes_prep(self, data):
        result = {}
        for extra_class in data:
            class_name = extra_class['name']
            students = extra_class['students']

            result[class_name] = students

        return result

    def find_student_extra_classes(self, extra_classes, student):
        result = []
        for extra_class in extra_classes:
            students = extra_classes[extra_class]
            for stud in students:
                if stud == student:
                    result.append(extra_class)

        return result

    def _get_result_students(self, main_groups, classes, extra_classes):
        for _class in classes:
            row = _class['class']
            column = _class['weekday']
            groups = _class['groups']

            self._result_groups[row][column] = groups

        for i, cl_i in enumerate(self._result_groups):
            for j, cl_j in enumerate(cl_i):
                stud_list = []
                for group in cl_j:
                    if group not in main_groups:
                        continue
                    students = main_groups[group]
                    for stud in students:
                        stud_extra_classes = self.find_student_extra_classes(extra_classes, stud)
                        stud_list.append({"student": stud, "group": group, "extra_classes": stud_extra_classes})

                self._result_students[i][j] = stud_list

        return self._result_students

    def process(self, data):
        init_classes = self._get_classes(data)
        init_extra_classes = self._get_extra_classes(data)
        init_main_groups = self._get_main_groups(data)

        classes = self._parse_classes(init_classes)
        extra_classes = self._parse_extra_classes(init_extra_classes)
        main_groups = self._parse_main_groups(init_main_groups)

        result_students = self._get_result_students(main_groups, classes, extra_classes)
        return result_students, extra_classes
