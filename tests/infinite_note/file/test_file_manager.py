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
    # 파일유무 확인
    file_full_path = f"{home_dir}/{file_name}"
    return_value = os.path.isfile(file_full_path)
    assert return_value

    # 한줄증가 확인


def test_count_file_line():
    # given
    msg = "테스트 문제 추가"
    file_name = "inf-test-count.txt"
    file_manager.delete_file(file_name)

    # when
    file_manager.save_question(msg=f"{msg}-1", file_name=file_name)
    file_manager.save_question(msg=f"{msg}-2", file_name=file_name)
    file_manager.save_question(msg=f"{msg}-3", file_name=file_name)

    # then
    count = file_manager.count_file_line(file_name=file_name)
    assert count == 3


def test_delete_file():
    file_name = "inf-nothing.txt"
    r = file_manager.delete_file(file_name)
    assert not r

    file_manager.save_question(msg="any", file_name=file_name)
    r = file_manager.delete_file(file_name)
    assert r


def test_get_random_line():
    l = file_manager.extract_all_line()

    for i in range(10):
        r = file_manager.get_random_line()
        assert r in l
        assert len(r) > 10




