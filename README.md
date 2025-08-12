# **SKN17-2ND-5Team**
> SK네트웍스 Family AI 캠프 17기 5팀 2ND PROJECT <br>
> 개발기간: 25.08.12 - 25.08.12

---
# 📚 Contents

<br>

1. [Introduce Team](#1-Introduce-Team)
2. [Project Overview](#2-Project-Overview)
3. [Technology Stack & Models](#3-Technology-Stack-&-Models)
<br>
<br>

---

# 1. Introduce Team

#### 💡 팀명: Hoonibus <img src="./images/hoonibus.png" align='center' width="70px"/> 
#### 💡팀원 소개:

<table align="center" width="100%">
  <tr>
    <td align="center">
      <a href="https://github.com/Hoonieboogie"><b>@한훈</b></a>
    </td>
    <td align="center">
      <a href="https://github.com/donghyun4957"><b>@최동현</b></a>
    </td>
    <td align="center">
      <a href="https://github.com/happyfrogg"><b>@맹지수</b></a>
    </td>
    <td align="center">
      <a href="https://github.com/Kicangel"><b>@김태완</b></a>
    </td>
    <td align="center">
      <a href="https://github.com/Taeyeon514"><b>@김태연</b></a>
    </td>
  </tr>
  <tr>
    <td align="center"><img src="./images/hh.png" width="100px" /></td>
    <td align="center"><img src="./images/dh.png" width="100px" /></td>
    <td align="center"><img src="./images/js.png" width="100px" /></td>
    <td align="center"><img src="./images/tw.png" width="100px" /></td>
    <td align="center"><img src="./images/ty.png" width="100px" /></td>
  </tr>
</table>

<br>

---


# 2. Project Overview
### ✅ 프로젝트명: 데이터 기반 신문 구독자 이탈 예측
### ✅ 프로젝트 소개
본 프로젝트는 전통 언론사가 직면한 구독자 이탈 문제를 데이터 기반으로 해결하고자 합니다.
온라인과 오프라인 신문 구독 데이터를 활용하여 구독자의 이탈 가능성을 예측하고, 이를 바탕으로 맞춤형 유지 전략을 수립함으로써 신문사의 지속 가능한 경영과 경쟁력 확보에 기여하는 것을 목표로 합니다.


<br>

### ✅ 프로젝트 필요성

<table align="center">
  <tr>
    <td align="center">
      <img src="./images/news.png" width="700" height="500">
    </td>
  </tr>
</table>

디지털 미디어의 급속한 확산과 스마트폰, 인터넷, 뉴스 플랫폼 및 동영상 기반 정보 채널의 성장으로, 사람들은 실시간·무료·맞춤형 콘텐츠를 손쉽게 접하게 되면서 전통적인 종이 신문 구독 환경과 정보 소비 패턴이 근본적으로 변화하였습니다.

종이신문은 인쇄·편집 등 다단계 검증 과정을 거쳐 높은 신뢰성을 유지하는 반면, 온라인 뉴스는 클릭 수와 조회 수에 집중하여 자극적이고 단편적인 내용이 많아지고 있습니다. 이에 따라 사실과 맥락을 깊이 전달하는 전통 언론의 역할이 더욱 중요해졌으며, 신문사는 존재 이유와 사업 구조를 재점검해야 하는 상황에 놓여 있습니다.

전통적인 구독 기반 수익 모델의 붕괴와 구독자 수 감소에 따른 매출 하락, 구조조정 및 인력 감축의 위기가 현실로 다가오는 가운데, 구독자 이탈을 사전에 예측하고 방지하는 전략은 신문사의 생존과 지속 가능성을 위한 필수 과제로 떠올랐습니다.

### ✅ 프로젝트 목표
- 구독자의 개인 특성을 면밀히 분석하고 이탈 가능성을 예측하는 머신러닝 모델 개발
- 이탈 위험 구독자를 조기에 식별하여 맞춤형 할인, 콘텐츠 추천 등 유지 전략 실행 지원
- 장기적으로 안정적인 구독 기반 확보 및 광고 수익, 브랜드 가치 향상 도모

<br>
<br>

---

# 3. Technology Stack & Models

## ✅ 기술 스택 및 사용한 모델

- **데이터 분석 & 전처리:**
    
    `Python`, `NumPy`, `Pandas`, `re` (정규표현식 활용)
    
- **데이터 시각화 (EDA):**
    
    `Matplotlib`, `Seaborn`
    
- **머신러닝 모델:**
    
    `Support Vector Classifier (SVC)`, `Decision Tree`, `Random Forest`, `Gradient Boosting`, `XGBoost`
    
- **웹 대시보드:**
    
    `Streamlit`


## 4. 데이터 선택 및 구조

### 4.1 데이터 출처
* 미국 신문 구독자 데이터
* 다양한 주요 변수 포함

**데이터 출처**
- KAGGLE

<br>

---

### 4.2 데이터 구조

#### **분석 타겟 컬럼**
- `Subcriber` : 구독자 이탈 여부 (분류 대상)

#### **주요 변수**
- `income` : 수입
- `ownership` : 자가 여부
- `ethnicity` : 민족
- `reward program` : 보상혜택 수령 횟수
- `nielsen prizem` : 사회적
- `age range` : 나이
- `deliveryperiod` : 배달 받는 요일
- `year of residence` : 거주기간
- `source channel` : 결제 플랫폼
- `weekly fee` : 주당 구독료

---

#### 4.3 데이터 기초 통계량

## 5. 데이터 전처리 및 통합

- 결측치 및 이상치 처리, 파생변수, 변수명 정제 등 전처리 수행

#### 데이터 조회

#### 수치형, 범주형 데이터 확인 [이미지 필요]

#### 데이터 결측치 조회 [이미지 필요]

#### 데이터 이상치 조회 [이미지 필요]

#### 이상치 처리 안함

- 거주기간, 보상 헤택 수령 횟수는 실제 시장 특성을 반영하는 것으로 판단하여 일부만 제거

#### 중복값 제거

#### 최종 남은 컬럼 요약



### 6. EDA

#### 이탈 잔류 전체 비율
### 카이제곱 검정, 크래머의 V

#### 집 소유 여부별 비율 (상대적 이탈률만 비교)
#### Ethnicity & Language 별 비율 (상대적 이탈률만 비교)
#### Age Range 별 이탈률
#### 소득 구간 별 이탈률
#### Source Channel 별
#### Delivery Period 별
#### Dummy for Children
- 뜯어봤다는 얘기 강조
#### 도시 및 County 별 
#### weekly fee 별
#### Nielsen Prizm별
#### 거주기간
#### 보상 프로그램 획득

### 얻은 결론
- 다 상관이 있다. feature 다 사용 결정
<br>

## 7. 머신러닝

### 7.1 학습을 위한 전처리

#### 나이, 소득 수치형 변환
- 그 이유에 대해 논문까지 첨부해가며 설명

#### 데이터 불균형
- SMOTENC 처리 사용 결정 그러나 실험은 안한 것과도 비교 분석
- SMOTENC 적용을 위해 사전 범주형 특성 라벨인코딩 진행
- SMOTEENC 결과 비율 변화 보여주기
- 수치형 변수 스탠다드 스케일링

### 7.2 머신러닝을 위한 모델 선정
- 머신러닝 모델 리스트

### 7.3 머신러닝 모델 학습
- GridSearchCV로 다양한 하이퍼파라미터 비교 및 최적 조합 탐색
- 교차검증을 통해 모델의 일반화 성능 평가
- 각 모델별 최고 성능 기준 최적 모델 선정
- 최적 모델 성능 고도화(threshold 포함)
- 최적 모델 기준 성능지표 게산(classication report, ROC curve)

### 7.4 최적 모델 성능에 대한 고찰
- feature importance
- 변수 중요도와 크래머의 V 값간의 경향성이 일치하는 비교
- threshold가 0.3 일때 성능이 최적이었는가에 대한 고찰

## 8. 한계점
- 캐글데이터 쓴거 -> 실제 raw가 아니다보니 데이터 관련성이 미리 설계되었을 가능성
- smote -> 라이브러리에 의존한 무지성 증강. 증강에 대한 사전평가 아쉽다
- 광범위한 하이퍼파라미터 튜닝 -> 7.3 성능 고도화 단계에서 훨씬 성능이 증가한 경우도 봤다. (시간 제약, 서포트벡터머신 900분)