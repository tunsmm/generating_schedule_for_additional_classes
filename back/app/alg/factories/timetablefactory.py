from alg.prepstageimpls.prepstageimpl1 import PreprocessStageImpl1
from alg.middlestageimpls.middlestageimpl1 import MidProcessStageImpl1
from alg.rangestageimpls.rangestageimpl1 import RangeProcessStageWithRandImpl
from alg.composestageimpls.composestageimpl1 import ComposeProcessStageImpl1
from alg.poststage import PostProcessData

from alg.timetablealg import TimetableAlg


def create_timetable_alg(max_group_capacity=12, weekdays=6, classes_count=6):
    prep_stage_impl = PreprocessStageImpl1(weekdays, classes_count)
    mid_stage = MidProcessStageImpl1(weekdays, classes_count)
    range_stage = RangeProcessStageWithRandImpl(mid_stage, weekdays, classes_count)
    compose_stage = ComposeProcessStageImpl1(max_group_capacity)
    post_stage = PostProcessData([])

    time_table_alg = TimetableAlg(prep_stage_impl, mid_stage, range_stage, compose_stage, post_stage)
    return time_table_alg
