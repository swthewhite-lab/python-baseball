# 미션 - 숫자 야구

> [!NOTE]  
> 이 코드는 원래 [java-baseball-6](https://github.com/woowacourse-precourse/java-baseball-6)에서 제공된 **Java 기반의 숫자야구 게임**을 **Python**에 맞게 변환한 과제입니다. 프로젝트 구조, 요구 사항, 기능 구현 방식은 원본 저장소를 바탕으로 Python 환경에 맞추어 수정하였습니다.
> 
---

## 🔍 진행 방식

- 미션은 **기능 요구 사항, 프로그래밍 요구 사항, 과제 진행 요구 사항** 세 가지로 구성되어 있다.
- 세 개의 요구 사항을 만족하기 위해 노력한다. 특히 기능을 구현하기 전에 기능 목록을 만든다.
- 기능 요구 사항에 기재되지 않은 내용은 스스로 판단하여 구현한다.

## 📮 미션 제출 방법

- 미션 구현을 완료한 후 GitHub을 통해 제출해야 합니다.
    - **Pull Request로 최종 제출**

## 🚨 과제 제출 전 체크 리스트 - 0점 방지

- 기능 구현을 모두 정상적으로 했더라도 **요구 사항에 명시된 출력값 형식을 지키지 않을 경우 0점 처리**됩니다.
- 기능 구현을 완료한 뒤 아래 가이드에 따라 테스트를 실행하고 모든 테스트가 성공하는지 확인합니다.
- **테스트가 실패할 경우 0점 처리**되므로, 반드시 확인 후 제출해야 합니다.

### 테스트 실행 가이드

- 터미널에서 `python --version`을 실행하여 Python 버전이 3.9 이상인지 확인합니다.
- `pytest` 명령어를 사용하여 모든 테스트가 아래와 같이 통과하는지 확인합니다.

```
=========================== test session starts ============================
...
========================= 100% passing in Xs =============================
```

---

## 🚀 기능 요구 사항

기본적으로 1부터 9까지 서로 다른 수로 이루어진 3자리의 수를 맞추는 게임입니다.

- 같은 수가 같은 자리에 있으면 스트라이크, 다른 자리에 있으면 볼, 같은 수가 전혀 없으면 낫싱이라는 힌트를 얻고, 그 힌트를 이용해 컴퓨터의 수를 맞추면 승리합니다.
    - 예) 상대방(컴퓨터)의 수가 425일 때
        - 123을 제시한 경우: 1스트라이크
        - 456을 제시한 경우: 1볼 1스트라이크
        - 789를 제시한 경우: 낫싱
- 컴퓨터는 1에서 9까지 서로 다른 임의의 수 3개를 선택합니다. 플레이어는 컴퓨터가 생각하고 있는 3개의 숫자를 입력하며, 컴퓨터는 입력한 숫자에 대한 결과를 출력합니다.
- 위 과정을 반복해 3개의 숫자를 모두 맞히면 게임이 종료됩니다.
- 게임 종료 후 게임을 다시 시작하거나 완전히 종료할 수 있습니다.
- 잘못된 값을 입력할 경우 `ValueError`를 발생시킨 후 프로그램을 종료해야 합니다.

### 입출력 요구 사항

#### 입력

- 서로 다른 3자리의 수
- 게임이 끝난 후 재시작/종료를 구분하는 1과 2 중 하나의 수

#### 출력

- 입력한 수에 대한 결과를 볼, 스트라이크 개수로 표시

```
1볼 1스트라이크
```

- 하나도 없는 경우

```
낫싱
```

- 3개의 숫자를 모두 맞힐 경우

```
3스트라이크
3개의 숫자를 모두 맞히셨습니다! 게임 종료
```

- 게임 시작 문구 출력

```
숫자 야구 게임을 시작합니다.
```

#### 실행 결과 예시

```
숫자 야구 게임을 시작합니다.
숫자를 입력해주세요 : 123
1볼 1스트라이크
숫자를 입력해주세요 : 145
1볼
숫자를 입력해주세요 : 671
2볼
숫자를 입력해주세요 : 216
1스트라이크
숫자를 입력해주세요 : 713
3스트라이크
3개의 숫자를 모두 맞히셨습니다! 게임 종료
게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.
1
숫자를 입력해주세요 : 123
1볼
...
```

---

## 🎯 프로그래밍 요구 사항

- Python 3.9 이상에서 실행 가능해야 합니다. **정상적으로 동작하지 않을 경우 0점 처리**됩니다.
- 프로그램 실행의 시작점은 `main.py`의 `main()` 함수입니다.
- 외부 라이브러리는 사용하지 않습니다.
- [PEP8](https://www.python.org/dev/peps/pep-0008/) Python 코드 스타일을 준수하며 프로그래밍합니다.
- 프로그램 종료 시 `sys.exit()`를 호출하지 않습니다.
- 프로그램 구현이 완료되면 테스트 코드가 성공해야 합니다. **테스트가 실패할 경우 0점 처리**됩니다.

### 라이브러리

- Python의 `random` 모듈을 사용하여 임의의 수를 생성합니다.
    - Random 값 추출은 `random.sample()`을 활용합니다.
    - 사용자가 입력하는 값은 `input()`을 활용합니다.

#### 사용 예시

```python
import random

computer = random.sample(range(1, 10), 3)
```

---

## ✏️ 과제 진행 요구 사항

- 미션은 [python-baseball](https://github.com/swthewhite-lab/python-baseball) 저장소를 Fork & Clone해 시작합니다.
- **기능을 구현하기 전 `docs/README.md`에 구현할 기능 목록을 정리**해 추가합니다.
- **Git의 커밋 단위는 기능 목록 단위**로 추가합니다.
