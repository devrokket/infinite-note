from infinite_note.file import file_manager


def test_save_question():
    msg = "테스트 문제 추가"
    file_manager.save_question(msg)