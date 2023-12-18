from alg.composestage import ComposeProcessStage
from alg.middlestage import MidProcessStage
from alg.poststage import PostProcessData
from alg.preprocessstage import PreprocessStage
from alg.rangestage import RangeProcessStage


class TimetableAlg:
    def __init__(self, pre_stage: PreprocessStage,
                 mid_stage: MidProcessStage,
                 range_stage: RangeProcessStage,
                 compose_stage: ComposeProcessStage,
                 post_stage: PostProcessData):
        self._pre_stage = pre_stage
        self._mid_stage = mid_stage
        self._range_stage = range_stage
        self._compose_stage = compose_stage
        self._post_stage = post_stage

    def process(self, data):
        prep_result = self._pre_stage.process(data)[0]
        data_for_second_stage = {"free_students": prep_result}
        r = self._mid_stage.process(data_for_second_stage)
        timetables = self._range_stage.process(r)
        final = self._compose_stage.process(timetables.copy())
        result = self._post_stage.process(final)
        return result
