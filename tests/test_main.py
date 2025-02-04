import pytest
from unittest.mock import patch
from baseball.main import main


# 게임 종료 후 재시작 테스트
def test_게임종료_후_재시작(capsys):
    # 랜덤값 임의 정의
    with patch('random.sample', side_effect=[[1, 3, 5], [5, 8, 9]]):
        # 입력값 모의 처리
        with patch('builtins.input', side_effect=["246", "135", "1", "597", "589", "2"]):
            main()

        # 출력값 캡처
        캡처된_출력 = capsys.readouterr().out

         # 결과 검증
        assert all(예상_출력 in 캡처된_출력 for 예상_출력 in ["낫싱", "3스트라이크", "1볼 1스트라이크", "3스트라이크", "게임 종료"])


# 예외 테스트
def test_예외_테스트():
    with pytest.raises(ValueError):
        # 잘못된 입력 처리
        with patch('builtins.input', side_effect=["1234"]):
            main()
