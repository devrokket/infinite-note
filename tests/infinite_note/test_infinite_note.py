import sys
import infinite_note


def test_ping():
    sys.argv = ['foo', '10']
    infinite_note.ping()

