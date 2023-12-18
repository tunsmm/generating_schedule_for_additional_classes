from abc import ABC, abstractmethod, abstractproperty
import json

import numpy as np


class ComposeProcessStage(ABC):
    @abstractmethod
    def get_timetables(self, data):
        pass

    @abstractmethod
    def process_timetable(self, current_timetable):
        pass

    def process(self, data):
        timetables = self.get_timetables(data)
        groups = {}
        result_timetables = {}

        for extra_class in timetables:
            current_timetable = timetables[extra_class]
            current_timetable, current_groups = self.process_timetable(current_timetable)
            groups[extra_class] = current_groups
            result_timetables[extra_class] = current_timetable

        return result_timetables, groups
