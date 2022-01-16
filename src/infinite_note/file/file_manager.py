
def save_question(msg):
    """입력받은 메시지를 파일로 저장한다.
    1. 파일이 없으면 만든다.
    2. 파일이 있으면 파일 내용 맨 아래에 입력된 MSG 를 추가한다.

    Args:
        msg:

    Returns:

    """
    import os.path
    home_dir = os.path.expanduser('~')
    with open(f"{home_dir}/inf-question.txt", "a") as f:
        f.write(msg + "\n")
