import sys
import infinite_note


def test_ping():
    sys.argv = ['foo', '10']
    infinite_note.ping()


def test_j():
    q = "나는 문제\n"
    a = "그리고 답"
    j = infinite_note.join_comma_str(s1=q, s2=a)

    assert j == "나는 문제,그리고 답"
