# Week5. KNN & Clustering, SVM & SVR

## Part 1. KNN & Clustering
### KNN
`tobigs21_KNN_과제_000.ipynb`에 주어진 데이터(`blackfriday.csv`)로 주석과 함께 아래 항목을 포함해 자유롭게 분석하기

- [ ] Preprocessing / EDA
- [ ] KNN 구현 & 파라미터 튜닝
- [ ] Evaluation

### Clustering
`tobigs21_Clustering_과제_000.ipynb`에 주어진 데이터(`Mall_Customers.csv`)로 주석과 함께 아래 항목을 포함해 자유롭게 분석하기

- [ ] Preprocessing / EDA
- [ ] Clustering
- [ ] Evaluation

## Part 2. SVM & SVR
`Week5_SVM_Assignment.ipynb`에 아래 조건을 지켜 Multiclass SVM 구현하기

- [ ] Scikit-learn의 SVM 사용 금지
- [ ] Iris 데이터 클래스 one-hot encoding
- [ ] 각각 Binary SVM 학습 후 결과 조합해 Multiclass SVM 구현하기
- [ ] One vs. one, One vs. rest 방법 중 하나 자유롭게 구현하기
- [ ] 투표 결과가 동점으로 나온 경우 아래 방법 중 하나를 이용해 경우 판별하기
  - decision_function 활용하기
  - 가장 개수가 많은 클래스를 사용하기
  - 랜덤으로 하나를 뽑기
- [ ] 클래스의 수와 무관한 Multiclass SVM 만들기

## 제출 방법
1. 본인의 이름으로 branch를 생성합니다.
2. `main`을 본인의 branch로 pull합니다.
3. **본인의 branch에서** 과제 디렉토리에 본인의 이름으로 디렉토리를 생성합니다.
4. 과제를 수행합니다. 디렉토리 구조:
   ```
   tobigs-21st
   └── Week1
       ├── EDA
       │   └── 김투빅
       │       └── example.md # 과제 파일
       └── Framework
           └── 김투빅
               └── example.md # 과제 파일
   ```
5. 변경된 본인의 branch를 commit, push합니다.
6. `이름(기수) - n주차 과제`라는 타이틀로 `Pull Request`를 등록합니다. 예) 김투빅(21기) - 1주차 과제

## 제출 기한
⏰ ~ 2/20(화) 23:59
