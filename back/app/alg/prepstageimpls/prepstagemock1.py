import numpy as np

from alg.preprocessstage import PreprocessStage


class PreprocessStageMock1(PreprocessStage):
    """
    Класс заглушка для тестирования
    """

    def __init__(self, weekdays=6, classes_count=6):
        self._main_groups = []
        self._classes = []
        self._extra_classes = []

        days = weekdays
        self._result_groups = np.empty(shape=(classes_count, days), dtype=list)
        self._result_students = np.empty(shape=(classes_count, days), dtype=list)
        for i, r_ in enumerate(self._result_groups):
            for j, r__ in enumerate(r_):
                self._result_groups[i][j] = []
                self._result_students[i][j] = []

    def _get_main_groups(self, data):
        groups = []
        return groups

    def _parse_main_groups(self, data):
        groups = [{
            "name": "СП - 1П",
            "students": [
                "6538edcfa04fb531ff864b57",
                "6238edf3a04fb531ff864b72"
            ]
        },
            {
                "name": "ЛПл -1П",
                "students": [
                    "5538edcfa04fb531ff864b81",
                    "1238edf3a04fb531ff864b02"
                ]
            }]

        groups = self._parse_main_groups_prep(groups)
        return groups

    def _get_classes(self, data):
        result = []
        return result

    def _parse_classes(self, data):
        classes = [{
            "weekday": 0,
            "class": 0,
            "groups": [
                "СП - 1П", "ЛПл -1П"
            ]}, {
            "weekday": 0,
            "class": 1,
            "groups": [
                "СП - 1П"
            ]}, {
            "weekday": 0,
            "class": 2,
            "groups": [
                "СП - 1П"
            ]}, {
            "weekday": 0,
            "class": 3,
            "groups": [
                "ЛПл -1П"
            ]}, {
            "weekday": 0,
            "class": 4,
            "groups": [
                "СП - 1П", "ЛПл -1П"
            ]}, {
            "weekday": 0,
            "class": 5,
            "groups": [
                "ЛПл -1П"
            ]}
        ]
        return classes

    def _get_extra_classes(self, data):
        result = []
        return result

    def _parse_extra_classes(self, data):
        result = [{
            "name": "СИИ",
            "students": [
                "6538edcfa04fb531ff864b57",
                "6238edf3a04fb531ff864b72",
                "5538edcfa04fb531ff864b81",
                "5538edcfa04fb531ff864b82",
                "5538edcfa04fb531ff864b83"
            ]
        },
            {
                "name": "СУБД",
                "students": [
                    "5538edcfa04fb531ff864b81",
                    "6538edcfa04fb531ff864b57",
                    "1238edf3a04fb531ff864b02",
                    "1238edf3a04fb531ff864b05"
                ]
            },
            {
                "name": "ППЦП",
                "students": [
                    "6538edcfa04fb531ff864b57",
                    "1238edf3a04fb531ff864b50",
                    "1238edf3a04fb531ff864b99",
                    "1238edf3a04fb531ff864b22"
                ]
            }]

        result = self._parse_extra_classes_prep(result)
        return result
