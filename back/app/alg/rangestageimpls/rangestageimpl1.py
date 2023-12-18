from alg.middlestage import MidProcessStage
from alg.rangestage import RangeProcessStage


class RangeProcessStageWithRandImpl(RangeProcessStage):
    def __init__(self, estimate_stage: MidProcessStage, weekdays=6, classes_count=6):
        super().__init__(estimate_stage, weekdays, classes_count)

    def get_extra_timetables(self, data):
        return data

    def compare_grater(self, point1, point2):
        if point1 > point2:
            return True

        if point1 == point2:
            r = self._rng.random()
            if r > 0.5:
                return True
            else:
                return False

        return False