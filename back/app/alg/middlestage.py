from abc import ABC, abstractmethod

class MidProcessStage(ABC):
    @abstractmethod
    def get_free_students(self, data):
        pass

    @abstractmethod
    def form_extra_classes_timetables(self, free_students):
        pass

    @abstractmethod
    def update(self, extra_timetables):
        pass

    def process(self, data):
        free_students = self.get_free_students(data)

        result = self.form_extra_classes_timetables(free_students)
        return result