from typing import List
from datetime import datetime

from injection_scheduler import *

SCHEDULE = [
    'Inject on left leg, closer to knee. Additionally, use a new vial this week. Good luck and stay safe!',
    'Inject on right leg, closer to knee. Good luck and stay safe!',
    'Inject on left leg, near the middle (towards knee). Good luck and stay safe!',
    'Inject on right leg, near the middle (towards knee). Good luck and stay safe!',
    'Inject on left leg, near the middle (towards hip). Additionally, use a new vial this week. Good luck and stay safe!',
    'Inject on right leg, near the middle (towards hip). Good luck and stay safe!',
    'Inject on left leg, closer to hip. Good luck and stay safe!',
    'Inject on right leg, closer to hip. Good luck and stay safe!',
    'Inject on left leg, closer to knee. Additionally, use a new vial this week. Good luck and stay safe!',
    'Inject on right leg, closer to knee. Good luck and stay safe!',
    'Inject on left leg, near the middle (towards knee). Good luck and stay safe!',
    'Inject on right leg, near the middle (towards knee). Good luck and stay safe!',
    'Inject on left leg, near the middle (towards hip). Additionally, use a new vial this week. Good luck and stay safe!',
    'Inject on right leg, near the middle (towards hip). Good luck and stay safe!',
    'Inject on left leg, closer to hip. Good luck and stay safe!',
    'Inject on right leg, closer to hip. Good luck and stay safe!',
    'Inject on left leg, closer to knee. Additionally, use a new vial this week. Good luck and stay safe!',
    'Inject on right leg, closer to knee. Good luck and stay safe!',
    'Inject on left leg, near the middle (towards knee). Good luck and stay safe!',
    'Inject on right leg, near the middle (towards knee). Good luck and stay safe!',
]

def get_schedule(size: int = 20) -> List[str]:
    return [location(i) for i in range(size)]

def test_location():
    for ct, txt in zip(range(20), SCHEDULE):
        assert txt == location(ct)

def test_injections_since():
    assert 6 == injections_since(datetime(2019, 2, 24))
    assert 0 == injections_since(datetime(2019, 1, 9))
    assert 0 == injections_since(datetime(2019, 1, 10))
    assert 0 == injections_since(datetime(2019, 1, 11))
    assert 0 == injections_since(datetime(2019, 1, 15))
    assert 1 == injections_since(datetime(2019, 1, 16))
    assert 1 == injections_since(datetime(2019, 1, 17))
