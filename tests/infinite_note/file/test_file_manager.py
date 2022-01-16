from infinite_note.file import file_manager
import os


def test_save_question():
    # given
    msg = "테스트 문제 추가"
    file_name = "inf-test.txt"
    home_dir = file_manager.get_home_dir()

    # when
    file_manager.save_question(msg=msg, file_name=file_name)

    # then
    file_full_path = f"{home_dir}/{file_name}"
    return_value = os.path.isfile(file_full_path)
    assert return_value




