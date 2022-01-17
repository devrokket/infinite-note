"""무한 노트

문제를 입력하고 풀고 오답노트를 관리한다.

Example:
    ``infinite_note`` 사용법은 아래와 같습니다.

        $ pip install infinite_note
        $ inf-note-input
        $ inf-note-count
        $ inf-note-challenge

추가적인 설명은 여기에!

Attributes:
    nnn (int): ``사용되지 않는`` 시범용 변수

Todo:
    * 무한한 모듈의 발전 ``꿈``꾸며!
    * ``Dreaming`` of infinite module development!

"""
import sys
"""
sys 모듈? 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
"""
from infinite_note.file.file_manager import save_msg2file, count_file_line, get_random_line, extract_all_line
# import infinite_note.file.file_manager as fm

nnn = 1


def join_comma_str(s1, s2) -> str:
    """두문자를 콤파로 붙이고 앞에 문제의 뉴라인 스트링을 지운다

    Args:
        s1:
        s2:

    Returns:

    """
    remove_new_line_s1 = s1.replace('\n', '')
    질문_콤마_답 = f"{remove_new_line_s1},{s2}"
    return 질문_콤마_답


def answer_question():
    """답을 받아서 질문과 짝을 지어준다.
    input("->") = answer 변수에 담는다.
    save_question(answer, INF_QUESTION_FILE_NAME) 파일에 저장한다.
    ? 질문과 답을 같이 배치한다.
    Returns:

    """
    질문 = output_question()
    답 = input("->")

    질문_콤마_답 = join_comma_str(질문, 답)

    save_msg2file(질문_콤마_답, file_name='inf-answer.txt')
    print('문제와 제출한 답안이 저장되었습니다')


def output_question() -> str:
    """문제 은행에서 한 문제를 꺼내서 화면에서 출력하고 리턴도 해준다."""
    질문 = get_random_line()
    print("아래 문제를 보고 답을 입력하세요")
    print(질문)
    return 질문


def count_question():
    count = count_file_line()
    print(f'총 저장된 문제는 ({count})건 입니다.')


def input_question():
    question = input("문제를 입력하세요:")
    save_msg2file(msg=question)
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
