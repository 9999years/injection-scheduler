from datetime import datetime, timedelta
import math
from typing import List

FIRST_INJECTION = datetime(2019, 1, 9)
INJECTION_FREQUENCY = timedelta(days=7)

INSTRUCTION_FMT = 'Inject on {leg} leg, {place}. {vial}Good luck and stay safe!'
VIAL = 'Additionally, use a new vial this week. '  # only sometimes inserted
LEG_CYCLE: List[str] = ['left', 'right']
PLACE_CYCLE: List[str] = [
    'closer to knee',
    'near the middle (towards knee)',
    'near the middle (towards hip)',
    'closer to hip',
]


def injections_since(
        dt: datetime,
        start: datetime = FIRST_INJECTION,
        period: timedelta = INJECTION_FREQUENCY) -> int:
    """
    Number of injections between `start` and `dt`, assuming one injection per
    `period`.
    """
    return math.floor((dt - start) / period)


def location(count: int) -> str:
    """
    Location to inject in for the `count`th injection.
    """
    # Note: place is indexed with count/2 because it's not repetition to inject
    # on left leg, middle then right leg, middle
    return INSTRUCTION_FMT.format(
            leg=LEG_CYCLE[count % len(LEG_CYCLE)],
            place=PLACE_CYCLE[int(count / 2) % len(PLACE_CYCLE)],
            vial='' if count % 4 else VIAL)


def main():
    print(location(injections_since(datetime.now())))

if __name__ == '__main__':
    main()
