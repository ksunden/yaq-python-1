import pathlib
import subprocess
import sys
import time
import math

import pytest

import yaqc
import yaqd_core
from yaqd_core import testing


config = pathlib.Path(__file__).parent / "config.toml"


@testing.run_daemon_entry_point("fake-triggered-sensor", config=config)
def test_defaults():
    c = yaqc.Client(39426)
    c.measure()
    while c.busy():
        time.sleep(0.1)
    out = c.get_measured()["random_walk"]
    assert -1 <= out <= 1


if __name__ == "__main__":
    test_defaults()