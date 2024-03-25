# Week9. Recommender System Basic, Generative Basic
## Part 1. Recommender System Basic

`u.data` 데이터를 사용해 `tobigs_week9_movielens_withmf.ipynb` 파일의 빈칸을 채워주세요.

(실행하실때 이전 버전의 파일을 받으신 분들은 
`# from src.preprocess.ml100k import ML100k`
`# from src.models.mf import MF`
`# from src.utils.trainer import Trainer`
이렇게 3줄을 주석처리 하고 진행해주세요!!)

## Part 2. Generative Basic

`HW_GenBasic(20240313).ipynb` 파일에서,

- [ ] VAE(Variational Autoencoder) 구현하기
- [ ] (Optional) [Beta-VAE](https://openreview.net/forum?id=Sy2fzU9gl)를 참고하여,
  - [ ] Pre-made loss 변형하기
  - [ ] Sample 시각화하기
  - [ ] Sample data의 fidelity 개선 여부 확인하기

## 제출 방법
1. 본인의 이름으로 branch를 생성합니다.
2. `main`을 본인의 branch로 pull합니다.
3. **본인의 branch에서** 과제 디렉토리에 본인의 이름으로 디렉토리를 생성합니다.
4. 과제를 수행합니다. 디렉토리 구조:
   ```
   tobigs-21st
   └── Week1
       ├── EDA
       │   └── 김투빅
       │       └── example.md # 과제 파일
       └── Framework
           └── 김투빅
               └── example.md # 과제 파일
   ```
5. 변경된 본인의 branch를 commit, push합니다.
6. `이름(기수) - n주차 과제`라는 타이틀로 `Pull Request`를 등록합니다. 예) 김투빅(21기) - 1주차 과제

## 제출 기한
⏰ ~ 3/19(화) 23:59
