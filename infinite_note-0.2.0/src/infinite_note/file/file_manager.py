import os.path
import random

INF_QUESTION_FILE_NAME = 'inf-question.txt'

def save_question(msg, file_name=INF_QUESTION_FILE_NAME):
    """입력받은 메시지를 파일로 저장한다.
    1. 파일이 없으면 만든다. 만드는 위치는 홈디렉토리 아래이다.
    2. 파일이 있으면 파일 내용 맨 아래에 입력된 MSG 를 추가한다.

    Args:
        msg: 추가할 내용, 문제
        file_name: 저장파일 이름

    Returns:

    """

    home_dir = get_home_dir()
    with open(f"{home_dir}/{file_name}", "a") as f:
        f.write(msg + "\n")


def get_home_dir():
    """홈 디렉토리 경록 갖여오기

    Returns:

    """
    home_dir = os.path.expanduser('~')
    return home_dir


def count_file_line(file_name=INF_QUESTION_FILE_NAME) -> int:
    """홈데렉토리에 생성되는 파일의 라인 카운트 리턴

    Args:
        file_name:

    Returns:

    """
    l = extract_all_line(file_name)
    return len(l)


def delete_file(file_name):
    """파일 삭제 기능

    Args:
        file_name: 삭제할 파일 이름, 파일은 홈디렉토리에 있다고 가정한다.

    Returns: 파일이 없으면 False 반환

    """
    home_dir = get_home_dir()
    file_full_path = f"{home_dir}/{file_name}"
    # file_full_path = home_dir + "/" + file_name
    if os.path.isfile(file_full_path):
        os.remove(file_full_path)
        return True
    else:
        return False


def get_random_line(file_name=INF_QUESTION_FILE_NAME) -> str:
    """문제가 저장된 파일/디비에서 랜덤하게 하나의 문제를 뽑아준다

    Args:
        file_name: 문제가 저장된 파일명

    Returns:

    """
    list_lines = extract_all_line(file_name=file_name)
    return random.choice(list_lines)


def extract_all_line(file_name=INF_QUESTION_FILE_NAME) -> list:
    """파일 내용을 리스트로 반환"""
    home_dir = get_home_dir()
    with open(f"{home_dir}/{file_name}", "r") as f:
        list_lines = f.readlines()
        return list_lines
