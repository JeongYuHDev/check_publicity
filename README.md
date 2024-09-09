# check_publicity

이 프로젝트는 텍스트 내 공인 여부를 확인하고 관리하는 도구를 제공합니다.

## 개요

`check_publicity` 프로젝트는 주어진 이름이나 문장에서 공인을 식별하고, 이에 대한 정확도를 평가하는 기능을 제공합니다.

## 주요 기능

- 이름의 공인 여부 식별
- 문장 내 공인 식별
- 인물 묘사 생성 및 분석
- 공인 식별 모델의 정확도 평가

## 파일 구조

### 핵심 코드 파일
이 프로젝트에서 최종적으로 사용되는 주요 코드 파일들은 다음과 같습니다:

1. `prompt.py`: AI 모델에 사용될 프롬프트를 정의하는 스크립트
2. `description_person.py`: 인물 묘사 관련 처리를 수행하는 스크립트
3. `check_sentence.py`: 문장 내 공인 여부를 확인하는 스크립트

### 보조 스크립트
- `publicity_detector.py`: 이름의 공인 여부를 확인하고 모델의 정확도를 평가하는 스크립트
- `make_sentence.py`: 테스트용 문장을 생성하는 스크립트
- `make_data.py`: 테스트 데이터를 생성하는 스크립트

### 노트북
- `team.ipynb`: 팀원 이름을 활용한 일반인 데이터 생성 및 처리를 위한 주피터 노트북

### testset/
테스트 데이터를 저장하는 폴더입니다.
- `public_name.csv`: 공인 이름 데이터
- `common_name.csv`: 일반인 이름 데이터
- `team_name.csv`: 팀원 이름 데이터
- `public_name_sentence.csv`: 공인 이름을 포함한 문장 데이터
- `common_name_sentence.csv`: 일반인 이름을 포함한 문장 데이터
- `team_name_sentence.csv`: 팀원 이름을 포함한 문장 데이터

### results/
프로젝트에서 생성된 결과 파일들을 저장하는 폴더입니다.
- `results.csv`: 공인 식별 결과, 실제 값과 예측 값, 정확도 등이 저장됩니다.
- `results_sentence.csv`: 문장 단위의 상세한 처리 결과가 저장됩니다.
- 기타 분석 결과 및 로그 파일들

## 사용 방법

1. 핵심 코드 파일 실행:
   - `prompt.py`: 프롬프트 정의 및 관리
   - `description_person.py`: 인물 묘사 생성 및 분석
   - `check_sentence.py`: 문장 내 공인 여부 확인

2. 보조 스크립트 실행:
   - `publicity_detector.py`: 공인 식별 및 정확도 평가
   - `make_sentence.py`: 테스트용 문장 생성
   - `make_data.py`: 테스트 데이터 생성

3. 결과 분석:
   - `results/` 폴더 내의 CSV 파일들을 확인하여 처리 결과를 분석합니다.

## 테스트

테스트 데이터는 `testset/` 폴더에 저장됩니다. 공인, 일반인, 팀원 이름 데이터를 포함하며, 이를 사용하여 모델의 정확도를 평가합니다.

## 결과 확인

모든 처리 결과는 `results/` 폴더에 저장했습니다. 주요 결과 파일은 다음과 같습니다:
- `results.csv`: 공인 식별 결과 요약
- `results_sentence.csv`: 문장 단위 처리 상세 결과

추가적인 분석 결과나 로그 파일들도 이 폴더에 저장했습니다
