import sys
import unittest
import logging

from internal.phase import Phase, PhaseCycler

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)

class TestPhaseCycler(unittest.TestCase):

    def test_phase_cycler(self):
        logger.addHandler(stream_handler)

        pc = PhaseCycler()
        self.assertTrue(pc.next() == Phase.DAY)
        self.assertTrue(pc.next() == Phase.NIGHT)

        logger.removeHandler(stream_handler)

if __name__ == '__main__':
    unittest.main()

