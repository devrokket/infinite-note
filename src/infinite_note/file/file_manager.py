import os.path

def save_question(msg, file_name='inf-question.txt'):
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
    home_dir = os.path.expanduser('~')
    return home_dir
