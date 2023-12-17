import pandas as pd


class GroupsStudentsParser:
    def __init__(self):
        self.csv_file = None
    
    def getJson(self, file_name):
        """
        Данный метод получает на вход имя файла, который содержит в себе списко студентов, где указаны:\n
        - имя студента;\n
        - группа студента;\n
        - доп программу, которую выбрал студент.
        :param file_name: имя файла в формате csv (с гугла скачивается в формате csv).
        :return: файл, который содержит в себе: список учебных групп; для каждой группы список студентов, которые
        входят в эту группу.
        """
        df = pd.read_csv(file_name)[['ФИО', 'Группа ООП 2023-2024', 'Программа ЦК']]
        groups = df['Группа ООП 2023-2024'].unique()
        grops_students_json = []
        for grop in groups:
            lst_stud = list(df[df['Группа ООП 2023-2024'] == grop]['ФИО'])
            grop_dict = {"name": grop, "students": lst_stud}
            grops_students_json.append({"group": grop_dict})
        
        return grops_students_json
      
