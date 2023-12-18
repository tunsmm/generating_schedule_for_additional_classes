class PostProcessData:
    def __init__(self, main_groups):
        self._main_groups = main_groups

    def extra_groups_process(self, groups):
        pass

    def get_group_name(self, group_prefix, group_num):
        return group_prefix + "--" + str(group_num)

    def extra_classes_process(self, timetables):
        result = []

        groups_dict = {}
        classes_dict = {}

        groups_result = []
        classes_result = []

        for extra_class_timetable in timetables:
            group_prefix = extra_class_timetable
            current_timetable = timetables[extra_class_timetable]

            for class_num, row_data in enumerate(current_timetable):
                for weekday, cell_data in enumerate(row_data):
                    current_cell_groups = []
                    for num, group in enumerate(cell_data):
                        group_num = group["group_num"]
                        group_name = self.get_group_name(group_prefix, group_num)
                        if group_name not in groups_dict:
                            students = group["students"]
                            students_data = []
                            for student in students:
                                students_data.append({
                                    "group": "",
                                    "name": student
                                })
                            data_to_add = students_data
                            groups_dict[group_name] = data_to_add

                        current_cell_groups.append(group_name)

                    class_key = (class_num, weekday)
                    if class_key not in classes_dict:
                        classes_dict[class_key] = []

                    for g in current_cell_groups:
                        classes_dict[class_key].append(g)

        for group in groups_dict:
            groups_result.append({
                "name": group,
                "students": groups_dict[group]
            })

        for classes_key in classes_dict:
            classes_result.append({
                "weekday": classes_key[1],
                "class": classes_key[0],
                "groups": classes_dict[classes_key]
            })

        return groups_result, classes_result

    def process(self, data):
        groups = data[1]
        timetables = data[0]

        extra_groups_result, extra_classes_result = self.extra_classes_process(timetables)
        return extra_groups_result, extra_classes_result
