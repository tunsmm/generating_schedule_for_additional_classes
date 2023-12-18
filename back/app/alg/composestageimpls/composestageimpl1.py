from alg.composestage import ComposeProcessStage


class ComposeProcessStageImpl1(ComposeProcessStage):
    def __init__(self, max_group_capacity=12):
        self._max_group_capacity = max_group_capacity

    def get_timetables(self, data):
        result = data
        return result

    def is_timetable_empty(self, current_timetable):
        for current_row in current_timetable:
            for current_cell in current_row:
                current_cell_students = current_cell["students"]
                if (len(current_cell_students) != 0):
                    return False
        return True

    def process_timetable(self, current_timetable):
        groups = []
        result_timetable = np.empty_like(current_timetable.copy())
        for i, row_data in enumerate(result_timetable):
            for j, cell_data in enumerate(row_data):
                result_timetable[i][j] = []

        group_num = 0
        while not self.is_timetable_empty(current_timetable):
            max_cell_row, max_cell_column, max_cell_value = 0, 0, 0
            for class_num, row_data in enumerate(current_timetable):
                for weekday_num, cell_data in enumerate(row_data):
                    students = cell_data["students"]
                    students_count = len(students)

                    if students_count > max_cell_value:
                        max_cell_value = students_count
                        max_cell_row = class_num
                        max_cell_column = weekday_num

            max_cell = current_timetable[max_cell_row][max_cell_column]
            new_group_students = []
            if max_cell_value > self._max_group_capacity:
                students = list(max_cell["students"])
                new_group_students = students[:self._max_group_capacity].copy()

            else:
                new_group_students = max_cell["students"].copy()
                current_timetable[max_cell_row][max_cell_column]["students"].clear()

            new_group = set(new_group_students)
            groups.append(new_group)
            group_num += 1
            for i, row_for_delete in enumerate(current_timetable):
                for j, cell_for_delete in enumerate(row_for_delete):
                    #                     print(i, j, current_timetable[i][j])
                    is_for_group = len(new_group_students) != 0
                    for student in new_group_students:
                        current_students_to_delete = current_timetable[i][j]["students"]
                        if len(current_students_to_delete) == 0:
                            is_for_group = False
                            break

                        if student in current_students_to_delete:
                            current_timetable[i][j]["students"].remove(student)
                        else:
                            if_for_group = False

                    if is_for_group == True:
                        result_timetable[i][j].append({"group_num": group_num, "students": new_group})

        #             print(current_timetable)

        return result_timetable, groups
