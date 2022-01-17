"""무한 노트

문제를 입력하고 풀고 오답노트를 관리한다.

Example:
    ``infinite_note`` 사용법은 아래와 같습니다.

        $ pip install infinite_note
        $ inf-note-input

추가적인 설명은 여기에!

Attributes:
    nnn (int): ``사용되지 않는`` 시범용 변수

Todo:
    * 무한한 모듈의 발전 ``꿈``꾸며!
    * ``Dreaming`` of infinite module development!

"""
import sys
from infinite_note.file.file_manager import save_question, count_file_line, get_random_line

nnn = 1


def output_question():
    q = get_random_line()
    print("아래 문제를 보고 답을 입력하세요")
    print(q)
    a = input("->")


def count_question():
    count = count_file_line()
    print(f'총 저장된 문제는 ({count})건 입니다.')


def input_question():
    question = input("문제를 입력하세요:")
    save_question(msg=question)
    print(f'입력하신 문제({question})를 저장 하였습니다.')
    count_question()


def ping():
    """Example function with PEP 484 type annotations.

    Returns:
        리턴 없이 화면 print

    """
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(f"{'p' * n}ong")
    else:
        print('pong')


if __name__ == "__main__":
    ping()
