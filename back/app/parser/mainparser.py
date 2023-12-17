from parsers.extraclassesparser import ExtraClassesParser
from parsers.groupsclassesparser import GroupsClassesParser
from parsers.groupsstudentsparser import GroupsStudentsParser


class MainParser:
    """
    Класс содержит в себе все парсеры, что позволяет получить к ним лёгкий доступ.
    """
    def __init__(self):
        self.ExtraClassesParser = ExtraClassesParser()
        self.GroupsClassesParser = GroupsClassesParser()
        self.GroupsStudentsParser = GroupsStudentsParser()

    def getExtraClassesJson(self, file_name: str):
        """
        Данный метод получает на вход имя файла, который содержит в себе список студентов, где указаны:\n
        - имя студента;
        - группа студента;
        - доп программу, которую выбрал студент.
        :param file_name: имя файла в формате csv (с гугла скачивается в формате csv).
        :return: файл, который содержит в себе: список доп программ; список групп, которые выбрали доп программу;
        список студентов, которые входят в группу.
        """
        output_json = self.ExtraClassesParser.getJson(file_name)
        return output_json

    def getGroupsClassesJson(self, folder_path: str):
        """
        Данный метод получает на вход путь к папке, в которой лежат расписания.
        :param folder_path: путь к папке, в которой лежат расписания.
        :return: файл, который содержит в себе список групп, для каждой выписаны свободные и занятые пары.
        """
        output_json = self.GroupsClassesParser.getJson(folder_path)
        return output_json

    def defGroupsStudentsJson(self, file_name: str):
        """
        Данный метод получает на вход имя файла, который содержит в себе список студентов, где указаны:\n
        - имя студента;
        - группа студента;
        - доп программу, которую выбрал студент.
        :param file_name: имя файла в формате csv (с гугла скачивается в формате csv).
        :return: файл, который содержит в себе: список учебных групп; для каждой группы список студентов, которые
        входят в эту группу.
        """
        output_json = self.GroupsStudentsParser.getJson(file_name)
        return output_json
