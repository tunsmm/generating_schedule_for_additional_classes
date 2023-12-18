import pandas as pd


class ExtraClassesParser:
    def __init__(self):
        self.csv_file = None
    
    def getJson(self, file_name: str):
        """
        Данный метод получает на вход имя файла, который содержит в себе списко студентов, где указаны:\n
        - имя студента;\n
        - группа студента;\n
        - доп программу, которую выбрал студент.
        :param file_name: имя файла в формате csv (с гугла скачивается в формате csv).
        :return: файл, который содержит в себе: список доп программ; список групп, которые выбрали доп программу;
        список студентов, которые входят в группу.
        """

        # Читаем нужные нам столбцы. Из таблицы выделяем уникальные ученбые группы
        # и уникальные дополнительные программы.
        df = pd.read_csv(file_name)[['ФИО', 'Группа ООП 2023-2024', 'Программа ЦК']]
        groups = df['Группа ООП 2023-2024'].unique()
        classes = df['Программа ЦК'].unique()

        # итоговый список
        my_json = []
        # список групп, входящих в доп программу
        class_groups = []
        # список студентов, которые входят в учебную группу и выбрали данную доп программу
        group_students = []
        # словарь, в который помещаем название группы и студентов данной группы, выбравших данную доп программу
        group_dict = []
        # словарь, который содержит в себе все доп программы с их группами и студентами
        classes_dict = []
        
        for class_ in classes:
            class_groups = []
            class_df = df[df['Программа ЦК'] == class_]
            groups = class_df['Группа ООП 2023-2024'].unique()

            for group in groups:
                class_group_df = class_df[class_df['Группа ООП 2023-2024'] == group]
                group_students = list(class_group_df['ФИО'])
                group_dict = {'group': {'name': group, 'students': group_students}}
                class_groups.append(group_dict)

            classes_dict = {'class': {'name': class_, 'groups': class_groups}}
            my_json.append(classes_dict)
        
        return my_json
