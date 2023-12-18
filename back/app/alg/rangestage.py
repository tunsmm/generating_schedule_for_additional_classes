import numpy as np
from abc import ABC, abstractmethod

from alg.middlestage import MidProcessStage


class RangeProcessStage(ABC):
    def __init__(self, estimate_stage: MidProcessStage, weekdays=6, classes_count=6):
        self._rng = np.random.default_rng()
        self._estimate_stage = estimate_stage

        self._weekdays = weekdays
        self._classes_count = classes_count

    @abstractmethod
    def get_extra_timetables(self, data):
        pass

    @abstractmethod
    def compare_grater(self, point1, point2):
        return False

    def process_cell(self, weekday, class_num, extra_timetables):
        row = class_num
        column = weekday

        current_cells = {}
        for extra_timetable in extra_timetables:
            current_timetable = extra_timetables[extra_timetable]
            current_cells[extra_timetable] = current_timetable[weekday][class_num]

        i = 0
        operations = len(current_cells.keys())

        busy_students = set()
        while i < operations:
            max_cell_num, max_extratimetable = 0, ""
            for extra_timetable in current_cells:
                current_cell = current_cells[extra_timetable]
                current_value = current_cell["value"]
                if self.compare_grater(current_value, max_cell_num):
                    max_cell_num = current_value
                    max_extratimetable = extra_timetable

            if max_cell_num == 0:
                for extra_timetable in current_cells:
                    max_extratimetable = extra_timetable
                    break

            max_extratimetable_data = extra_timetables[max_extratimetable]

            cell_data = max_extratimetable_data[row][column]

            current_busy_students = cell_data["students"]
            for current_busy_student in current_busy_students:
                busy_students.add(current_busy_student)

            for extra_timetable in extra_timetables:
                if extra_timetable != max_extratimetable:
                    current_timetable = extra_timetables[extra_timetable]

                    current_students = current_timetable[row][column]["students"]

                    for busy_student in busy_students:
                        if busy_student in current_students:
                            current_students.remove(busy_student)

            extra_timetables = self._estimate_stage.update(extra_timetables)
            i += 1

        return extra_timetables

    def process(self, data):
        extra_timetables = self.get_extra_timetables(data)

        rows = self._classes_count
        columns = self._weekdays

        for i in range(rows):
            for j in range(columns):
                extra_timetables = self.process_cell(i, j, extra_timetables)

        return extra_timetables