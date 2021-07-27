# STARBUCKS

# 프로젝트 개요

## INDEX

   * **데이터 탐색**
   * **데이터 전처리**
   * **데이터 분석 및 시각화**
   * **분석 결론**
   * **가설 검정**
   * **최종 결론**


## 팀원 소개

| 팀원 | 담당 역할|
|------|----------|
|이종원[팀장] |데이터 전처리, 데이터 분석, 보고서 작성|
|김도환|데이터 전처리, 데이터 시각화|
|성호경|데이터 시각화, 가설검정, PPT 제작|
|이현우|데이터 분석, 가설검정, 발표|
|오승훈|데이터 전처리, 데이터 분석, PPT 제작|

## 데이터 소개

* **출처** : 캐글 데이터 - Starbucks Customer Data. 
    - https://www.kaggle.com/ihormuliar/starbucks-customer-data 
    
![kaggle](./image/kaggle.PNG)


## 분석 방향

### 주제 : 스타벅스 고객의 특성 파악과 향후 프로모션 전략에 대한 제안

#### 스타벅스 고객의 특성 
   * **1. 스타벅스 가입 고객들의 특성**

#### 향후 프로모션 전략 제안
   * **1. 총 순 수익 관점에서 우수한 프로모션을 파악하고 향후 프로모션 전략에 반영**
      * ex) 예상 결론 : 현재 이러이러한 프로모션 전략이 총 순 수익 관점에서 우수하니. 앞으로 이런 프로모션을 자주 진행하자.
<br><br>
   * **2. 주력 고객층을 확보하기 위한 프로모션 전략 제안**
      * ex) 예상 결론 : 총 소비금액이 큰 `주력 고객층`이 자주참여 하는 프로모션 전략은 (~~ 이러이러) 하니. 주력 고객층을 확보하기 위해서는 ~ 이런 프로모션 전략을 취해야 한다. 
<br><br>
   * **3. 신규 고객층을 확보하기 위한 프로모션 전략 제안**
       * ex) 신규 고객 일수록 거래 빈도와 프로모션 참여 비율이 높은 결과가 나왔다. 신규 고객들이 선호하는 프로모션 전략을 파악하고 앞으로 그 프로모션을 취하자.

# 데이터 탐색

## 필요 라이브러리 로드 및 환경 설정

### 라이브러리 로드


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import datetime
```

### 환경 설정


```python
# 그래프 스타일(seaborn-whitegrid)
plt.style.use('seaborn-whitegrid')

# 폰트설정, 마이너스 폰트 설정
plt.rc('font', family= "Malgun Gothic")
plt.rc('axes', unicode_minus=False)

# 모든 열을 다 보이게 하는 설정
pd.set_option('max_columns', None)
```

## 데이터 로드


```python
profile = pd.read_csv('./profile.csv')
portfolio = pd.read_csv('./portfolio.csv')
transcript = pd.read_csv('./transcript.csv')
```

## profile.csv 데이터 탐색

* Dimensional data about each person, including their age, salary, and gender. There is one unique customer for each record.

|열 이름 | 의미| 특징|
|--------|-----|----|
| ***gender*** | 성별|  2175개의 결측치 |
|***age*** | 나이 | 2175개의 결측치 |
|***id*** | 아이디(고객 고유번호)| 17000명|
|***become_member_on*** | 어플 계정을 만든 날짜|2013/7/29 ~ 2018/7/26|
|***income*** | 수입|2175개의 결측치|

* **특징**
    * ***특징1*** : ***2175개의 결측치***가 존재하고, id, age(118:NA), income이 ***동시에 결측***됨.<br><br>
    * ***특징 2*** : gender 3개, income 값의 분포가 생각보다 적었다. 91개
    * ***특징 3*** : ***[gender]*** 결측치를 제외한 gender는, F, M, O 3개로 나뉨.
        - M : 8484 명, F : 6129 명, O : 212 명, nan : 2175명
            + O는 성소수자로 편입.
    * ***특징 4*** : **[age]**  평균 나이 : 54.4 세, 최대 : 101세, 최소 18세
    * ***특징 5*** : **[age]**  50대가 1등 ~ 10등 차지
    * ***특징 6*** :**[became_member_on]** 2013/7/29 ~ 2018/7/26일 까지.
    * ***특징 7*** :**[became_member_on]** 신규 어플 계정 가입자수가 크게 감소함.
    * ***특징 8*** :**[id]** 테이블의 key 값으로 17000명의 고객이 재 .
    * ***특징 9*** :**[income]**  수입의 분포가 91개로 그렇게 크지 않다. (측정치 14825개, 결측치는 2175개)
    * ***특징 10*** :**[income]**  평균 65404, 최소 30000, 최대 120000

----------------------------------------
### 전체적으로 살펴보기


```python
display(profile.head())
display(profile.tail())
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>gender</th>
      <th>age</th>
      <th>id</th>
      <th>became_member_on</th>
      <th>income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>NaN</td>
      <td>118</td>
      <td>68be06ca386d4c31939f3a4f0e3dd783</td>
      <td>20170212</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>F</td>
      <td>55</td>
      <td>0610b486422d4921ae7d2bf64640c50b</td>
      <td>20170715</td>
      <td>112000.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>NaN</td>
      <td>118</td>
      <td>38fe809add3b4fcf9315a9694bb96ff5</td>
      <td>20180712</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>F</td>
      <td>75</td>
      <td>78afa995795e4d85b5d9ceeca43f5fef</td>
      <td>20170509</td>
      <td>100000.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>NaN</td>
      <td>118</td>
      <td>a03223e636434f42ac4c3df47e8bac43</td>
      <td>20170804</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>gender</th>
      <th>age</th>
      <th>id</th>
      <th>became_member_on</th>
      <th>income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16995</th>
      <td>16995</td>
      <td>F</td>
      <td>45</td>
      <td>6d5f3a774f3d4714ab0c092238f3a1d7</td>
      <td>20180604</td>
      <td>54000.0</td>
    </tr>
    <tr>
      <th>16996</th>
      <td>16996</td>
      <td>M</td>
      <td>61</td>
      <td>2cb4f97358b841b9a9773a7aa05a9d77</td>
      <td>20180713</td>
      <td>72000.0</td>
    </tr>
    <tr>
      <th>16997</th>
      <td>16997</td>
      <td>M</td>
      <td>49</td>
      <td>01d26f638c274aa0b965d24cefe3183f</td>
      <td>20170126</td>
      <td>73000.0</td>
    </tr>
    <tr>
      <th>16998</th>
      <td>16998</td>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481194dcd9400aec7c9ae6366</td>
      <td>20160307</td>
      <td>50000.0</td>
    </tr>
    <tr>
      <th>16999</th>
      <td>16999</td>
      <td>F</td>
      <td>62</td>
      <td>e4052622e5ba45a8b96b59aba68cf068</td>
      <td>20170722</td>
      <td>82000.0</td>
    </tr>
  </tbody>
</table>
</div>


**특징1** : **2175개의 결측치**가 존재하고, gender, age(118:NA), income이 **동시에 결측**됨
  - (번호표시) 데이터 전처리 과정에서 **데이터 삭제**. 전체 데이터의 약 13%정도(계산다시)


```python
profile.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 17000 entries, 0 to 16999
    Data columns (total 6 columns):
     #   Column            Non-Null Count  Dtype  
    ---  ------            --------------  -----  
     0   Unnamed: 0        17000 non-null  int64  
     1   gender            14825 non-null  object 
     2   age               17000 non-null  int64  
     3   id                17000 non-null  object 
     4   became_member_on  17000 non-null  int64  
     5   income            14825 non-null  float64
    dtypes: float64(1), int64(3), object(2)
    memory usage: 797.0+ KB
    


```python
profile[profile['age']==118]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>gender</th>
      <th>age</th>
      <th>id</th>
      <th>became_member_on</th>
      <th>income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>NaN</td>
      <td>118</td>
      <td>68be06ca386d4c31939f3a4f0e3dd783</td>
      <td>20170212</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>NaN</td>
      <td>118</td>
      <td>38fe809add3b4fcf9315a9694bb96ff5</td>
      <td>20180712</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>NaN</td>
      <td>118</td>
      <td>a03223e636434f42ac4c3df47e8bac43</td>
      <td>20170804</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>NaN</td>
      <td>118</td>
      <td>8ec6ce2a7e7949b1bf142def7d0e0586</td>
      <td>20170925</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>NaN</td>
      <td>118</td>
      <td>68617ca6246f4fbc85e91a2a49552598</td>
      <td>20171002</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>16980</th>
      <td>16980</td>
      <td>NaN</td>
      <td>118</td>
      <td>5c686d09ca4d475a8f750f2ba07e0440</td>
      <td>20160901</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16982</th>
      <td>16982</td>
      <td>NaN</td>
      <td>118</td>
      <td>d9ca82f550ac4ee58b6299cf1e5c824a</td>
      <td>20160415</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16989</th>
      <td>16989</td>
      <td>NaN</td>
      <td>118</td>
      <td>ca45ee1883624304bac1e4c8a114f045</td>
      <td>20180305</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16991</th>
      <td>16991</td>
      <td>NaN</td>
      <td>118</td>
      <td>a9a20fa8b5504360beb4e7c8712f8306</td>
      <td>20160116</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16994</th>
      <td>16994</td>
      <td>NaN</td>
      <td>118</td>
      <td>c02b10e8752c4d8e9b73f918558531f7</td>
      <td>20151211</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>2175 rows × 6 columns</p>
</div>



***특징 2*** : gender 3개, income 값의 분포가 생각보다 적었다. 91개


```python
profile.nunique()
```




    Unnamed: 0          17000
    gender                  3
    age                    85
    id                  17000
    became_member_on     1716
    income                 91
    dtype: int64



--------------------------------
### gender : 고객 성별

* ***특징 3*** : 결측치를 제외한 gender는, F, M, O 3개로 나뉨. 
    - `M` : 8484 명, `F` : 6129 명, `O` : 212 명, nan : 2175명
    - `O` :를 제 3의 성별로 인식하기로 함.


```python
print('gender :', profile['gender'].unique())
print(profile['gender'].fillna(1).value_counts())
sns.countplot(data=profile, x='gender').set_title('고객 성별 분포');
```

    gender : [nan 'F' 'M' 'O']
    M    8484
    F    6129
    1    2175
    O     212
    Name: gender, dtype: int64
    


    
![png](output_22_1.png)
    


---------------------------------------
### age : 고객 나이
* ***특징 4*** : 평균 나이 : 54.4 세, 최대 : 101세, 최소 18세, 결측치 118세
* ***특징 5*** : 50대가 1등 ~ 10등 차지


```python
# 결측치 제거 데이터
age = profile[profile['age']!=118]
```


```python
print('기술통계값',age['age'].describe(), sep='\n') 
profile['age'].value_counts().head(10)
```

    기술통계값
    count    14825.000000
    mean        54.393524
    std         17.383705
    min         18.000000
    25%         42.000000
    50%         55.000000
    75%         66.000000
    max        101.000000
    Name: age, dtype: float64
    




    118    2175
    58      408
    53      372
    51      363
    54      359
    59      359
    57      353
    52      351
    55      350
    56      342
    Name: age, dtype: int64




```python
plt.figure(figsize=(20, 7))
sns.countplot(data=age, x='age')
```




    <AxesSubplot:xlabel='age', ylabel='count'>




    
![png](output_26_1.png)
    


---------------------------------------
### became_member_on : 어플 계정을 만든 날짜
* ***특징 6*** : 2013/7/29 ~ 2018/7/26일 까지.
* ***특징 7*** : 신규 어플 계정 가입자수가 크게 감소함.


```python
profile['became_member_on']=pd.to_datetime(profile['became_member_on'], format='%Y%m%d')
```


```python
profile['became_member_on'].describe()
```

    <ipython-input-161-406b1a2d7433>:1: FutureWarning: Treating datetime data as categorical rather than numeric in `.describe` is deprecated and will be removed in a future version of pandas. Specify `datetime_is_numeric=True` to silence this warning and adopt the future behavior now.
      profile['became_member_on'].describe()
    




    count                   17000
    unique                   1716
    top       2017-12-07 00:00:00
    freq                       43
    first     2013-07-29 00:00:00
    last      2018-07-26 00:00:00
    Name: became_member_on, dtype: object




```python
plt.figure(figsize=(25, 7))
plt.xticks(rotation=90)  
sns.countplot(data=profile, x='became_member_on').set_title('일자별 어플계정 생성 수');
```


    
![png](output_30_0.png)
    


---------------------------------------
### id : 고객 아이디

* ***특징 8*** : 테이블의 key 값으로 17000명의 고객이 존재.
  - 비 직관적인 데이터 -> 중복을 허용하지 않는 선[10 자리]로 자른다.

---------------------------------------
### income : 고객 수입

* ***특징 8*** : 수입의 분포가 91개로 그렇게 크지 않다. (측정치 14825개, 결측치는 2175개)
* ***특징 9*** : 평균 65404, 최소 30000, 최대 120000


```python
print(profile['income'].isnull().value_counts())
profile['income'].describe()
```

    False    14825
    True      2175
    Name: income, dtype: int64
    




    count     14825.000000
    mean      65404.991568
    std       21598.299410
    min       30000.000000
    25%       49000.000000
    50%       64000.000000
    75%       80000.000000
    max      120000.000000
    Name: income, dtype: float64




```python
plt.figure(figsize=(20, 5))
plt.xticks(rotation =90)
sns.countplot(data=profile, x='income').set_title('고객 수입 분포');
```


    
![png](output_34_0.png)
    


----------------------------------------
## portfolio.csv 데이터 탐색

* Information about the promotional offers that are possible to receive, and basic information about each one including the promotional type, duration of the promotion, reward, and how the promotion was distributed to customers
* 홍보제안이 제공될 수 있는 정보와 홍보유형, 홍보기간, 보상, 고객에게 홍보가 어떻게 배포되었는지를 포함한 각 홍보제안의 기본정보

|열 이름 | 의미| 특징|
|--------|-----|----|
|<span style="color:red">***reward***</span>| 쿠폰 사용 금액(달러) |  bogo(1+1)의 reward는 difficulty와 같다.|
|***channel*** | 홍보가 어떤 수단을 통해 배포되었는가 | web, email, mobile, social|
|<span style="color:red">***difficulty***</span>|쿠폰을 받기 위한 최소 금액(달러)|There is also a difficulty score, the dollar amount that must be spent for the offer to be completed.|
|***duration*** | UNKOWN, 이벤트 진행기간 |
|***offer_type*** | 프로모션 유형|Bogo : 보고 쿠폰(Buy One Get One) 1+1 쿠폰, Informational : 정보제공, Discount : 할인|
| ***id***|프로모션 id ||

* **특징**
   * **특징1** : **[id]** id 값이 비 직관적이다. 전처리시, 10자리로 자른다.
   * **특징2** : **[offer_type]** 정보성 프로모션(offer_type : informational)은 difficulty가 0이다.
   * **특징3** : **[channels]** 홍보수단(channels)이 list로 묶여 있다. 이를 풀어줘야 한다.



```python
portfolio
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>10</td>
      <td>['email', 'mobile', 'social']</td>
      <td>10</td>
      <td>7</td>
      <td>bogo</td>
      <td>ae264e3637204a6fb9bb56bc8210ddfd</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>4d5c57ea9a6940dd891ad53e9dbe8da0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>0</td>
      <td>4</td>
      <td>informational</td>
      <td>3f207df678b143eea3cee63160fa8bed</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>9b98b8c7a33c4b65b9aebfe6a799e6d9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>['web', 'email']</td>
      <td>20</td>
      <td>10</td>
      <td>discount</td>
      <td>0b1e1539f2cc45b7b9fa7c272da2e1d7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>3</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>7</td>
      <td>7</td>
      <td>discount</td>
      <td>2298d6c36e964ae4a3e7e9706d1fb8c2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>2</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>10</td>
      <td>discount</td>
      <td>fafdcd668e3743c1bb461111dcafc2a4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>0</td>
      <td>['email', 'mobile', 'social']</td>
      <td>0</td>
      <td>3</td>
      <td>informational</td>
      <td>5a8bc65990b245e5a138643cd4eb9837</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>5</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>5</td>
      <td>5</td>
      <td>bogo</td>
      <td>f19421c1d4aa40978ebb69ca19b0e20d</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>2</td>
      <td>['web', 'email', 'mobile']</td>
      <td>10</td>
      <td>7</td>
      <td>discount</td>
      <td>2906b810c7d4411798c6938adc9daaa5</td>
    </tr>
  </tbody>
</table>
</div>



----------------------------------------
## Transcript.csv 데이터 탐색

* Records show the different steps of promotional offers that a customer received. The different values of receiving a promotion are receiving, viewing, and completing. You also see the different transactions that a person made in the time since he became a customer. With all records, you see the day that they interacted with Starbucks and the amount that it is worth.

|열 이름 | 의미| 특징|
|--------|-----|----|
| ***person*** | 고객 id |  |
|***event*** | 진행</span>상황(record) : transaction, offer viewed, offer received,  offer completed| |
|***value*** |프로모션 id, 거래금액(transaction amount)|`{key : value}` 형태로 존재 |
|***time***| time in hours| |

* **특징**
    * ***특징 1*** :**[person]**  결측치가 없다, 17000명의 고객의 정보가 있다. 한 고객은 한번 이상의 거래(프로모션 참여) 기록을 가지고 있다. 
    * ***특징 2*** :**[person]** 한 고객의 프로모션 참여 빈도 최대 51회, 최소1회, 평균 18회, 중앙값 17회 
    * ***특징 3*** : **[event]** `offer received`(76277건), `offer viewed`(57725건), `offer completed`(33579건), `transaction`(138953건) 값만 존재.
    * ***특징 4*** : **[event]** 'transaction'은 **[value]**의 key값이 amount이다. 나머지는 프로모션 id와 연관
    * ***특징 5*** : **[event]** `{'offer_id': '2906b810c7d4411798c6938adc9daaa5', 'reward': 2}`를 portfoio와 비교해보니 reward개수가 같았다.

---------------------------------------
### 전체적으로 살펴보기


```python
display(transcript.head())
display(transcript.tail())
transcript.info()
transcript.nunique()
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>78afa995795e4d85b5d9ceeca43f5fef</td>
      <td>offer received</td>
      <td>{'offer id': '9b98b8c7a33c4b65b9aebfe6a799e6d9'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>a03223e636434f42ac4c3df47e8bac43</td>
      <td>offer received</td>
      <td>{'offer id': '0b1e1539f2cc45b7b9fa7c272da2e1d7'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>e2127556f4f64592b11af22de27a7932</td>
      <td>offer received</td>
      <td>{'offer id': '2906b810c7d4411798c6938adc9daaa5'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>8ec6ce2a7e7949b1bf142def7d0e0586</td>
      <td>offer received</td>
      <td>{'offer id': 'fafdcd668e3743c1bb461111dcafc2a4'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>68617ca6246f4fbc85e91a2a49552598</td>
      <td>offer received</td>
      <td>{'offer id': '4d5c57ea9a6940dd891ad53e9dbe8da0'}</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>306529</th>
      <td>306529</td>
      <td>b3a1272bc9904337b331bf348c3e8c17</td>
      <td>transaction</td>
      <td>{'amount': 1.5899999999999999}</td>
      <td>714</td>
    </tr>
    <tr>
      <th>306530</th>
      <td>306530</td>
      <td>68213b08d99a4ae1b0dcb72aebd9aa35</td>
      <td>transaction</td>
      <td>{'amount': 9.53}</td>
      <td>714</td>
    </tr>
    <tr>
      <th>306531</th>
      <td>306531</td>
      <td>a00058cf10334a308c68e7631c529907</td>
      <td>transaction</td>
      <td>{'amount': 3.61}</td>
      <td>714</td>
    </tr>
    <tr>
      <th>306532</th>
      <td>306532</td>
      <td>76ddbd6576844afe811f1a3c0fbb5bec</td>
      <td>transaction</td>
      <td>{'amount': 3.5300000000000002}</td>
      <td>714</td>
    </tr>
    <tr>
      <th>306533</th>
      <td>306533</td>
      <td>c02b10e8752c4d8e9b73f918558531f7</td>
      <td>transaction</td>
      <td>{'amount': 4.05}</td>
      <td>714</td>
    </tr>
  </tbody>
</table>
</div>


    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 306534 entries, 0 to 306533
    Data columns (total 5 columns):
     #   Column      Non-Null Count   Dtype 
    ---  ------      --------------   ----- 
     0   Unnamed: 0  306534 non-null  int64 
     1   person      306534 non-null  object
     2   event       306534 non-null  object
     3   value       306534 non-null  object
     4   time        306534 non-null  int64 
    dtypes: int64(2), object(3)
    memory usage: 11.7+ MB
    




    Unnamed: 0    306534
    person         17000
    event              4
    value           5121
    time             120
    dtype: int64



---------------------------------------
### person : 고객 id


* ***특징 1*** :**[person]**  결측치가 없다, 17000명의 고객의 정보가 있다. 한 고객은 한번 이상의 거래(프로모션 참여) 기록을 가지고 있다. 
* ***특징 2*** :**[person]** 한 고객의 프로모션 참여 빈도 최대 51회, 최소1회, 평균 18회, 중앙값 17회


```python
len(transcript['person'].unique())
```




    17000




```python
print('max', transcript['person'].value_counts().max())
print('min', transcript['person'].value_counts().min())
print('mean', transcript['person'].value_counts().mean())
print('median', transcript['person'].value_counts().median())
```

    max 51
    min 1
    mean 18.031411764705883
    median 17.0
    

---------------------------------------
### event : 진행상황, 거래, 이벤트 제안 수신, 이벤트 조회, 이벤트 완판


* ***특징 3*** : **[event]** `offer received`(76277건), `offer viewed`(57725건), `offer completed`(33579건), `transaction`(138953건) 값만 존재.


```python
transcript['event'].unique()
```




    array(['offer received', 'offer viewed', 'transaction', 'offer completed'],
          dtype=object)




```python
print(transcript['event'].value_counts())
transcript['event'].value_counts().plot.bar(rot=0, color='g', title='EVENT');
```

    transaction        138953
    offer received      76277
    offer viewed        57725
    offer completed     33579
    Name: event, dtype: int64
    


    
![png](output_45_1.png)
    


* ***특징 4*** : **[event]** 'transaction'은 **[value]**의 key값이 amount이다. 나머지는 프로모션 id와 연관
<br><br>
* ***특징 5*** : **[event]** key값이 'offer id'인 부분을 value만 따로 뽑아서 **portfolio.csv**의 **[id]**와 조인하면 더 많은 내용을 분석할 수 있을거 같다.


```python
display(transcript[transcript['event']=='transaction'].sample(6))
display(transcript[transcript['event']=='offer received'].sample(6))
display(transcript[transcript['event']=='offer viewed'].sample(6))
display(transcript[transcript['event']=='offer completed'].sample(6))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>98279</th>
      <td>98279</td>
      <td>70f0cba2dfeb48d2817d789ba39b1939</td>
      <td>transaction</td>
      <td>{'amount': 3.48}</td>
      <td>264</td>
    </tr>
    <tr>
      <th>31024</th>
      <td>31024</td>
      <td>6676062b996d42499314026f12c2efac</td>
      <td>transaction</td>
      <td>{'amount': 19.47}</td>
      <td>48</td>
    </tr>
    <tr>
      <th>275140</th>
      <td>275140</td>
      <td>171c7f6ef14c416a87ac8907c58202ed</td>
      <td>transaction</td>
      <td>{'amount': 1.01}</td>
      <td>606</td>
    </tr>
    <tr>
      <th>189649</th>
      <td>189649</td>
      <td>5eade4be36b747868769ca1899919f8f</td>
      <td>transaction</td>
      <td>{'amount': 1.65}</td>
      <td>462</td>
    </tr>
    <tr>
      <th>187800</th>
      <td>187800</td>
      <td>28681c16026943e68f26feaccab0907f</td>
      <td>transaction</td>
      <td>{'amount': 2.93}</td>
      <td>456</td>
    </tr>
    <tr>
      <th>297738</th>
      <td>297738</td>
      <td>c2215f480a39490e8830b7700cf6f7b7</td>
      <td>transaction</td>
      <td>{'amount': 17.3}</td>
      <td>672</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>57078</th>
      <td>57078</td>
      <td>bde68ea39f4449f1818922a3077d3ff4</td>
      <td>offer received</td>
      <td>{'offer id': '5a8bc65990b245e5a138643cd4eb9837'}</td>
      <td>168</td>
    </tr>
    <tr>
      <th>63434</th>
      <td>63434</td>
      <td>2999a95f137240ed802890b38f0466e5</td>
      <td>offer received</td>
      <td>{'offer id': 'f19421c1d4aa40978ebb69ca19b0e20d'}</td>
      <td>168</td>
    </tr>
    <tr>
      <th>251705</th>
      <td>251705</td>
      <td>07e7d74b98e9496eae8226d4af05f33b</td>
      <td>offer received</td>
      <td>{'offer id': '2906b810c7d4411798c6938adc9daaa5'}</td>
      <td>576</td>
    </tr>
    <tr>
      <th>121696</th>
      <td>121696</td>
      <td>84a43ae3265546f7a39950f9d321ca71</td>
      <td>offer received</td>
      <td>{'offer id': '2906b810c7d4411798c6938adc9daaa5'}</td>
      <td>336</td>
    </tr>
    <tr>
      <th>3834</th>
      <td>3834</td>
      <td>5d02e48e7b974a69875d0c6ab097928e</td>
      <td>offer received</td>
      <td>{'offer id': 'ae264e3637204a6fb9bb56bc8210ddfd'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>114344</th>
      <td>114344</td>
      <td>9e481b621a724dd098378e497483ea21</td>
      <td>offer received</td>
      <td>{'offer id': '9b98b8c7a33c4b65b9aebfe6a799e6d9'}</td>
      <td>336</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>28683</th>
      <td>28683</td>
      <td>28cded7dcbaf492f8b61b7ff56348b34</td>
      <td>offer viewed</td>
      <td>{'offer id': '0b1e1539f2cc45b7b9fa7c272da2e1d7'}</td>
      <td>42</td>
    </tr>
    <tr>
      <th>89613</th>
      <td>89613</td>
      <td>8ce65a3b2b79468980312b5a61b77e29</td>
      <td>offer viewed</td>
      <td>{'offer id': '4d5c57ea9a6940dd891ad53e9dbe8da0'}</td>
      <td>228</td>
    </tr>
    <tr>
      <th>66608</th>
      <td>66608</td>
      <td>9ebe696078b742b389f486bd3a98ca56</td>
      <td>offer viewed</td>
      <td>{'offer id': 'ae264e3637204a6fb9bb56bc8210ddfd'}</td>
      <td>168</td>
    </tr>
    <tr>
      <th>102233</th>
      <td>102233</td>
      <td>133d2f38d79b40b6a047374a4e1b1cdc</td>
      <td>offer viewed</td>
      <td>{'offer id': 'fafdcd668e3743c1bb461111dcafc2a4'}</td>
      <td>282</td>
    </tr>
    <tr>
      <th>274394</th>
      <td>274394</td>
      <td>462bee4de62b4c5bad10ae72d93616ec</td>
      <td>offer viewed</td>
      <td>{'offer id': 'fafdcd668e3743c1bb461111dcafc2a4'}</td>
      <td>600</td>
    </tr>
    <tr>
      <th>217102</th>
      <td>217102</td>
      <td>ec7764ae29b0430a9b291c00c1cfa757</td>
      <td>offer viewed</td>
      <td>{'offer id': '5a8bc65990b245e5a138643cd4eb9837'}</td>
      <td>504</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>199360</th>
      <td>199360</td>
      <td>7bb31864f78149fdb3eb9d49d05b3b1c</td>
      <td>offer completed</td>
      <td>{'offer_id': 'fafdcd668e3743c1bb461111dcafc2a4...</td>
      <td>492</td>
    </tr>
    <tr>
      <th>34774</th>
      <td>34774</td>
      <td>c15ed45a455d416daa0cb30aa7f8f9b1</td>
      <td>offer completed</td>
      <td>{'offer_id': 'fafdcd668e3743c1bb461111dcafc2a4...</td>
      <td>66</td>
    </tr>
    <tr>
      <th>267007</th>
      <td>267007</td>
      <td>910a58abd30c4df596b3904b4471c626</td>
      <td>offer completed</td>
      <td>{'offer_id': 'ae264e3637204a6fb9bb56bc8210ddfd...</td>
      <td>588</td>
    </tr>
    <tr>
      <th>37570</th>
      <td>37570</td>
      <td>6985f5feb03d419591be91df02575ed6</td>
      <td>offer completed</td>
      <td>{'offer_id': 'fafdcd668e3743c1bb461111dcafc2a4...</td>
      <td>78</td>
    </tr>
    <tr>
      <th>279535</th>
      <td>279535</td>
      <td>cb4a0508e95e41b8a57c59d69a20f06d</td>
      <td>offer completed</td>
      <td>{'offer_id': 'f19421c1d4aa40978ebb69ca19b0e20d...</td>
      <td>618</td>
    </tr>
    <tr>
      <th>269951</th>
      <td>269951</td>
      <td>fff7576017104bcc8677a8d63322b5e1</td>
      <td>offer completed</td>
      <td>{'offer_id': 'fafdcd668e3743c1bb461111dcafc2a4...</td>
      <td>594</td>
    </tr>
  </tbody>
</table>
</div>


### value : 프로모션 ID, 트랜잭션 금액

* ***특징 4*** : **[event]** 'transaction'은 **[value]**의 key값이 amount이다. 나머지는 프로모션 id와 연관
* ***특징 6*** : **[value]** `{'offer_id': '2906b810c7d4411798c6938adc9daaa5', 'reward': 2}`를 portfoio와 비교해보니 reward개수가 같았다.
    - key값은 'offer_id', 'offer id', 'amount' 이렇게 3개가 존재한다.<br><br>

* <span style="color:red"> ***체크 포인트 8***</span> : **[value]**  전처리시 value값에 대하여 다음과 같이 처리
     - reward 부분 제거
     - key와 value를 분리한다.
     - amount 소수점 두자리로 변경


```python
transcript
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>78afa995795e4d85b5d9ceeca43f5fef</td>
      <td>offer received</td>
      <td>{'offer id': '9b98b8c7a33c4b65b9aebfe6a799e6d9'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>a03223e636434f42ac4c3df47e8bac43</td>
      <td>offer received</td>
      <td>{'offer id': '0b1e1539f2cc45b7b9fa7c272da2e1d7'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>e2127556f4f64592b11af22de27a7932</td>
      <td>offer received</td>
      <td>{'offer id': '2906b810c7d4411798c6938adc9daaa5'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>8ec6ce2a7e7949b1bf142def7d0e0586</td>
      <td>offer received</td>
      <td>{'offer id': 'fafdcd668e3743c1bb461111dcafc2a4'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>68617ca6246f4fbc85e91a2a49552598</td>
      <td>offer received</td>
      <td>{'offer id': '4d5c57ea9a6940dd891ad53e9dbe8da0'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>306529</th>
      <td>306529</td>
      <td>b3a1272bc9904337b331bf348c3e8c17</td>
      <td>transaction</td>
      <td>{'amount': 1.5899999999999999}</td>
      <td>714</td>
    </tr>
    <tr>
      <th>306530</th>
      <td>306530</td>
      <td>68213b08d99a4ae1b0dcb72aebd9aa35</td>
      <td>transaction</td>
      <td>{'amount': 9.53}</td>
      <td>714</td>
    </tr>
    <tr>
      <th>306531</th>
      <td>306531</td>
      <td>a00058cf10334a308c68e7631c529907</td>
      <td>transaction</td>
      <td>{'amount': 3.61}</td>
      <td>714</td>
    </tr>
    <tr>
      <th>306532</th>
      <td>306532</td>
      <td>76ddbd6576844afe811f1a3c0fbb5bec</td>
      <td>transaction</td>
      <td>{'amount': 3.5300000000000002}</td>
      <td>714</td>
    </tr>
    <tr>
      <th>306533</th>
      <td>306533</td>
      <td>c02b10e8752c4d8e9b73f918558531f7</td>
      <td>transaction</td>
      <td>{'amount': 4.05}</td>
      <td>714</td>
    </tr>
  </tbody>
</table>
<p>306534 rows × 5 columns</p>
</div>




```python
portfolio
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>10</td>
      <td>['email', 'mobile', 'social']</td>
      <td>10</td>
      <td>7</td>
      <td>bogo</td>
      <td>ae264e3637204a6fb9bb56bc8210ddfd</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>4d5c57ea9a6940dd891ad53e9dbe8da0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>0</td>
      <td>4</td>
      <td>informational</td>
      <td>3f207df678b143eea3cee63160fa8bed</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>9b98b8c7a33c4b65b9aebfe6a799e6d9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>['web', 'email']</td>
      <td>20</td>
      <td>10</td>
      <td>discount</td>
      <td>0b1e1539f2cc45b7b9fa7c272da2e1d7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>3</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>7</td>
      <td>7</td>
      <td>discount</td>
      <td>2298d6c36e964ae4a3e7e9706d1fb8c2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>2</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>10</td>
      <td>discount</td>
      <td>fafdcd668e3743c1bb461111dcafc2a4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>0</td>
      <td>['email', 'mobile', 'social']</td>
      <td>0</td>
      <td>3</td>
      <td>informational</td>
      <td>5a8bc65990b245e5a138643cd4eb9837</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>5</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>5</td>
      <td>5</td>
      <td>bogo</td>
      <td>f19421c1d4aa40978ebb69ca19b0e20d</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>2</td>
      <td>['web', 'email', 'mobile']</td>
      <td>10</td>
      <td>7</td>
      <td>discount</td>
      <td>2906b810c7d4411798c6938adc9daaa5</td>
    </tr>
  </tbody>
</table>
</div>




```python
transcript[transcript['event']!='transaction']['value'].value_counts()
```




    {'offer id': '2298d6c36e964ae4a3e7e9706d1fb8c2'}                  14983
    {'offer id': 'fafdcd668e3743c1bb461111dcafc2a4'}                  14924
    {'offer id': '4d5c57ea9a6940dd891ad53e9dbe8da0'}                  14891
    {'offer id': 'f19421c1d4aa40978ebb69ca19b0e20d'}                  14835
    {'offer id': 'ae264e3637204a6fb9bb56bc8210ddfd'}                  14374
    {'offer id': '5a8bc65990b245e5a138643cd4eb9837'}                  14305
    {'offer id': '9b98b8c7a33c4b65b9aebfe6a799e6d9'}                  11848
    {'offer id': '3f207df678b143eea3cee63160fa8bed'}                  11761
    {'offer id': '2906b810c7d4411798c6938adc9daaa5'}                  11750
    {'offer id': '0b1e1539f2cc45b7b9fa7c272da2e1d7'}                  10331
    {'offer_id': 'fafdcd668e3743c1bb461111dcafc2a4', 'reward': 2}      5317
    {'offer_id': '2298d6c36e964ae4a3e7e9706d1fb8c2', 'reward': 3}      5156
    {'offer_id': '9b98b8c7a33c4b65b9aebfe6a799e6d9', 'reward': 5}      4354
    {'offer_id': 'f19421c1d4aa40978ebb69ca19b0e20d', 'reward': 5}      4296
    {'offer_id': '2906b810c7d4411798c6938adc9daaa5', 'reward': 2}      4017
    {'offer_id': 'ae264e3637204a6fb9bb56bc8210ddfd', 'reward': 10}     3688
    {'offer_id': '0b1e1539f2cc45b7b9fa7c272da2e1d7', 'reward': 5}      3420
    {'offer_id': '4d5c57ea9a6940dd891ad53e9dbe8da0', 'reward': 10}     3331
    Name: value, dtype: int64



### time : time in hours

+ Time in hours, The data begins at time(시점 0으로 부터 시작 기간). [2021/05/18]
+ Time을 하루 24시간으로 나누면 1일 ~ 30일이 나온다. 여기서  일주일 간격으로 peak를 찍는 모습을 보였다.
+ 데이터 전처리시 Time을 일별로 변환한 데이터의 컬럼을 추가해보자 
+ 데이터를 보면 6 단위로 증가함.


```python
plt.figure(figsize=(15, 5))
sns.countplot(x = transcript['time']/24)
plt.xticks(rotation=90);
```


    
![png](output_53_0.png)
    



```python
transcript.groupby(by= 'time')[['time']].count()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>time</th>
    </tr>
    <tr>
      <th>time</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15561</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2506</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2215</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2015</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1921</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th>690</th>
      <td>1260</td>
    </tr>
    <tr>
      <th>696</th>
      <td>1326</td>
    </tr>
    <tr>
      <th>702</th>
      <td>1115</td>
    </tr>
    <tr>
      <th>708</th>
      <td>1048</td>
    </tr>
    <tr>
      <th>714</th>
      <td>1130</td>
    </tr>
  </tbody>
</table>
<p>120 rows × 1 columns</p>
</div>



-------------------------------------------
# 데이터 전처리 

----------------------------------------
## profile.csv 전처리

|열 이름 | 의미| 특징|
|--------|-----|----|
| ***gender*** | 고객 성별|  2175개의 결측치 |
|***age*** | 고객 나이(bining필요) | 2175개의 결측치 |
|***id*** | 고객 아이디(고객 고유번호)| key값|
|***become_member_on*** | 어플 계정을 만든 날짜|
|***income*** | 고객 수입|2175개의 결측치|


```python
# 지수표현 처리[profile의 income 부분이 지수로 표현되면 아래 실행]
# pd.options.display.float_format = '{:.1f}'.format
```

**데이터 깊은 복사 : profile_data**


```python
profile_data = profile.copy()
```

-------------------------------------------
### 결측치 제거, Unnamed: 0 컬럼 제거
* **특징1** : **2175개의 결측치**가 존재하고, gender, age(118:NA), income이 **동시에 결측**됨
    - 2175개의 결측치 제거


```python
profile_data = profile_data.dropna(axis=0)
del profile_data['Unnamed: 0']
print(profile_data.shape)
```

    (14825, 5)
    


```python
profile_data.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>id</th>
      <th>became_member_on</th>
      <th>income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>55</td>
      <td>0610b486422d4921ae7d2bf64640c50b</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>75</td>
      <td>78afa995795e4d85b5d9ceeca43f5fef</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
    </tr>
  </tbody>
</table>
</div>



-------------------------------------------
### gender 관련 전처리

+ 각각의 성별로 데이터를 모아서 변수로 생성한다.
    - 나중에 성별에 따른 데이터를 분석 가능


```python
gender_m = profile_data[profile_data['gender'] == 'M']
gender_f = profile_data[profile_data['gender'] == 'F']
gender_o = profile_data[profile_data['gender'] == 'O']
```


```python
print(gender_m.shape, gender_f.shape, gender_o.shape )
```

    (8484, 5) (6129, 5) (212, 5)
    

-------------------------------------------
### age 관련 전처리

### [age_units10] 10을 간격으로 나눔
* 나이대별로 구간 나누기
   + 0세 ~ 19세 : '10'
   + 20세 ~ 29세 : '20'
   + 30세 ~ 39세 : '30'
   + 40세 ~ 49세 : '40'
   + 50세 ~ 59세 : '50'
   + 60세 ~ 69세 : '60'
   + 70세 ~ 79세 : '70'
   + 80세 ~ 89세 : '80'
   + 90세 ~ 99세 : '90'
   + 100세 ~ 117세 : '100'


```python
profile_data['age_units10'] = pd.cut(x= profile_data['age'], bins=[0, 20, 30, 40, 50, 60, 70, 80, 90, 100, 118], 
       labels=['10','20', '30', '40', '50', '60', '70', '80', '90', '100'], include_lowest = True, right=False)
```


```python
# 정수형으로 변환
profile_data = profile_data.astype({'age_units10':'int'})
profile_data.sample(4)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10373</th>
      <td>M</td>
      <td>66</td>
      <td>f5236217d594472a9e8c53800e6c3144</td>
      <td>2018-03-23</td>
      <td>71000.0</td>
      <td>60</td>
    </tr>
    <tr>
      <th>399</th>
      <td>F</td>
      <td>56</td>
      <td>06b99e8cc24b426f8a578c749974b88a</td>
      <td>2018-01-23</td>
      <td>109000.0</td>
      <td>50</td>
    </tr>
    <tr>
      <th>3760</th>
      <td>M</td>
      <td>63</td>
      <td>6b715ac1dfaa41b49a463cabb73cbe52</td>
      <td>2018-03-15</td>
      <td>51000.0</td>
      <td>60</td>
    </tr>
    <tr>
      <th>16467</th>
      <td>M</td>
      <td>48</td>
      <td>e856cd5b7ad84f6c9d2e9f5d5a8bf02c</td>
      <td>2018-07-17</td>
      <td>32000.0</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>



### [age_units5] 5을 간격으로 나눔


```python
profile_data['age_units5'] = pd.cut(x= profile_data['age'], 
        bins=[0, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 118], 
       labels=['10','15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80', '85', '90', '95', '100'], 
                                     include_lowest = True, right=False)
# 정수형으로 변환
profile_data = profile_data.astype({'age_units5':'int'})
profile_data.sample(4)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10809</th>
      <td>M</td>
      <td>80</td>
      <td>3cc18472ed634128b409baa2a48700f4</td>
      <td>2017-12-05</td>
      <td>81000.0</td>
      <td>80</td>
      <td>80</td>
    </tr>
    <tr>
      <th>6988</th>
      <td>M</td>
      <td>75</td>
      <td>fb99c38cdceb4f92bf004f4c3e95fff4</td>
      <td>2018-02-23</td>
      <td>42000.0</td>
      <td>70</td>
      <td>75</td>
    </tr>
    <tr>
      <th>16527</th>
      <td>F</td>
      <td>46</td>
      <td>7dc9f81c5d1542b192c3af2bc70924e1</td>
      <td>2017-10-12</td>
      <td>31000.0</td>
      <td>40</td>
      <td>45</td>
    </tr>
    <tr>
      <th>8806</th>
      <td>M</td>
      <td>36</td>
      <td>b28226cae51c4caf88dade33add552a2</td>
      <td>2017-09-09</td>
      <td>90000.0</td>
      <td>30</td>
      <td>35</td>
    </tr>
  </tbody>
</table>
</div>



-------------------------------------------
### id 관련 전처리

#### id 값을 10자리로 축소
 + id 값이 불필요하게 너무 길다. 분석의 편리를 위해 중복되지 않는 선에서 10자리로 줄인다.
     - 줄인 후에도 14825개 데이터 유지


```python
profile_data['id'] = profile_data['id'].str[:10]
display(profile_data.head(3))
profile_data['id'].nunique()
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
    </tr>
    <tr>
      <th>5</th>
      <td>M</td>
      <td>68</td>
      <td>e2127556f4</td>
      <td>2018-04-26</td>
      <td>70000.0</td>
      <td>60</td>
      <td>65</td>
    </tr>
  </tbody>
</table>
</div>





    14825



#### [person_id] transcript 와 join을 위해 id값 변경


```python
profile_data = profile_data.rename({'id':'person_id'},axis='columns')
profile_data.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
    </tr>
  </tbody>
</table>
</div>



-------------------------------------------
### became_member_on 관련 전처리

#### [year], [month], [day] 컬럼 추가
 + 어플 가입 일자를 연(year), 월(month), 일(day)로 구분하여 데이터 분석을 확장시킨다.


```python
profile_data['join_year'] = profile_data['became_member_on'].dt.year
profile_data['join_month'] = profile_data['became_member_on'].dt.month
profile_data['join_day'] = profile_data['became_member_on'].dt.day
```


```python
profile_data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 14825 entries, 1 to 16999
    Data columns (total 10 columns):
     #   Column            Non-Null Count  Dtype         
    ---  ------            --------------  -----         
     0   gender            14825 non-null  object        
     1   age               14825 non-null  int64         
     2   person_id         14825 non-null  object        
     3   became_member_on  14825 non-null  datetime64[ns]
     4   income            14825 non-null  float64       
     5   age_units10       14825 non-null  int64         
     6   age_units5        14825 non-null  int64         
     7   join_year         14825 non-null  int64         
     8   join_month        14825 non-null  int64         
     9   join_day          14825 non-null  int64         
    dtypes: datetime64[ns](1), float64(1), int64(6), object(2)
    memory usage: 1.2+ MB
    

#### [now], [join_period]

 + 마지막일자(2021/06/01) 기준으로 어플 가입 일자 추가.


```python
profile_data['now'] = datetime.date.today()
profile_data['now'] = pd.to_datetime(profile_data['now'])
profile_data['join_period'] = profile_data['now'] - profile_data["became_member_on"]
display(profile_data.head(3))

# [join_day]의 days 제거 
profile_data = profile_data.astype({'join_period':'str'})
profile_data['join_period'] = profile_data['join_period'].str[:4]

# 다시 정수형으로 변환
profile_data = profile_data.astype({'join_period':'int'})

# 결과 확인 
display(profile_data.head(3))
profile_data.dtypes
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437 days</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504 days</td>
    </tr>
    <tr>
      <th>5</th>
      <td>M</td>
      <td>68</td>
      <td>e2127556f4</td>
      <td>2018-04-26</td>
      <td>70000.0</td>
      <td>60</td>
      <td>65</td>
      <td>2018</td>
      <td>4</td>
      <td>26</td>
      <td>2021-06-21</td>
      <td>1152 days</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
    </tr>
    <tr>
      <th>5</th>
      <td>M</td>
      <td>68</td>
      <td>e2127556f4</td>
      <td>2018-04-26</td>
      <td>70000.0</td>
      <td>60</td>
      <td>65</td>
      <td>2018</td>
      <td>4</td>
      <td>26</td>
      <td>2021-06-21</td>
      <td>1152</td>
    </tr>
  </tbody>
</table>
</div>





    gender                      object
    age                          int64
    person_id                   object
    became_member_on    datetime64[ns]
    income                     float64
    age_units10                  int64
    age_units5                   int64
    join_year                    int64
    join_month                   int64
    join_day                     int64
    now                 datetime64[ns]
    join_period                  int32
    dtype: object




```python
import numpy as np
import pandas as pd 
```


```python
df = pd.read_csv('./profile_processing.csv')
df[['person_id', 'became_member_on', 'join_year', 'join_month', 'join_day']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>e2127556f4</td>
      <td>2018-04-26</td>
      <td>2018</td>
      <td>4</td>
      <td>26</td>
    </tr>
    <tr>
      <th>3</th>
      <td>389bc3fa69</td>
      <td>2018-02-09</td>
      <td>2018</td>
      <td>2</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2eeac8d8fe</td>
      <td>2017-11-11</td>
      <td>2017</td>
      <td>11</td>
      <td>11</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>14820</th>
      <td>6d5f3a774f</td>
      <td>2018-06-04</td>
      <td>2018</td>
      <td>6</td>
      <td>4</td>
    </tr>
    <tr>
      <th>14821</th>
      <td>2cb4f97358</td>
      <td>2018-07-13</td>
      <td>2018</td>
      <td>7</td>
      <td>13</td>
    </tr>
    <tr>
      <th>14822</th>
      <td>01d26f638c</td>
      <td>2017-01-26</td>
      <td>2017</td>
      <td>1</td>
      <td>26</td>
    </tr>
    <tr>
      <th>14823</th>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
    </tr>
    <tr>
      <th>14824</th>
      <td>e4052622e5</td>
      <td>2017-07-22</td>
      <td>2017</td>
      <td>7</td>
      <td>22</td>
    </tr>
  </tbody>
</table>
<p>14825 rows × 5 columns</p>
</div>



### profile_processing.csv로 저장


```python
profile_data.to_csv('profile_processing.csv',index=False)
```

**확인**


```python
pd.read_csv('./profile_processing.csv')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
    </tr>
    <tr>
      <th>2</th>
      <td>M</td>
      <td>68</td>
      <td>e2127556f4</td>
      <td>2018-04-26</td>
      <td>70000.0</td>
      <td>60</td>
      <td>65</td>
      <td>2018</td>
      <td>4</td>
      <td>26</td>
      <td>2021-06-21</td>
      <td>1152</td>
    </tr>
    <tr>
      <th>3</th>
      <td>M</td>
      <td>65</td>
      <td>389bc3fa69</td>
      <td>2018-02-09</td>
      <td>53000.0</td>
      <td>60</td>
      <td>65</td>
      <td>2018</td>
      <td>2</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1228</td>
    </tr>
    <tr>
      <th>4</th>
      <td>M</td>
      <td>58</td>
      <td>2eeac8d8fe</td>
      <td>2017-11-11</td>
      <td>51000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>11</td>
      <td>11</td>
      <td>2021-06-21</td>
      <td>1318</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>14820</th>
      <td>F</td>
      <td>45</td>
      <td>6d5f3a774f</td>
      <td>2018-06-04</td>
      <td>54000.0</td>
      <td>40</td>
      <td>45</td>
      <td>2018</td>
      <td>6</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1113</td>
    </tr>
    <tr>
      <th>14821</th>
      <td>M</td>
      <td>61</td>
      <td>2cb4f97358</td>
      <td>2018-07-13</td>
      <td>72000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2018</td>
      <td>7</td>
      <td>13</td>
      <td>2021-06-21</td>
      <td>1074</td>
    </tr>
    <tr>
      <th>14822</th>
      <td>M</td>
      <td>49</td>
      <td>01d26f638c</td>
      <td>2017-01-26</td>
      <td>73000.0</td>
      <td>40</td>
      <td>45</td>
      <td>2017</td>
      <td>1</td>
      <td>26</td>
      <td>2021-06-21</td>
      <td>1607</td>
    </tr>
    <tr>
      <th>14823</th>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>50000.0</td>
      <td>80</td>
      <td>80</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
      <td>2021-06-21</td>
      <td>1932</td>
    </tr>
    <tr>
      <th>14824</th>
      <td>F</td>
      <td>62</td>
      <td>e4052622e5</td>
      <td>2017-07-22</td>
      <td>82000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2017</td>
      <td>7</td>
      <td>22</td>
      <td>2021-06-21</td>
      <td>1430</td>
    </tr>
  </tbody>
</table>
<p>14825 rows × 12 columns</p>
</div>



----------------------------------------
## portfolio.csv 전처리

|열 이름 | 의미| 특징|
|--------|-----|----|
|<span style="color:red">***reward***</span>| 쿠폰 사용 금액(달러) |  bogo(1+1)의 reward는 difficulty와 같다.|
|***channel*** | 홍보가 어떤 수단을 통해 배포되었는가 | web, email, mobile, social|
|<span style="color:red">***difficulty***</span>|쿠폰을 받기 위한 최소 금액(달러)|There is also a difficulty score, the dollar amount that must be spent for the offer to be completed.|
|***duration*** | UNKOWN, 이벤트 진행기간 |
|***offer_type*** | 프로모션 유형|Bogo : 보고 쿠폰(Buy One Get One) 1+1 쿠폰, Informational : 정보제공, Discount : 할인|
| ***id***|프로모션 id ||

-------------------------------------------
### Unnamed: 0 컬럼 제거


```python
portfolio_data = portfolio.copy()
del portfolio_data['Unnamed: 0']
portfolio_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>['email', 'mobile', 'social']</td>
      <td>10</td>
      <td>7</td>
      <td>bogo</td>
      <td>ae264e3637204a6fb9bb56bc8210ddfd</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>4d5c57ea9a6940dd891ad53e9dbe8da0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>0</td>
      <td>4</td>
      <td>informational</td>
      <td>3f207df678b143eea3cee63160fa8bed</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>9b98b8c7a33c4b65b9aebfe6a799e6d9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>['web', 'email']</td>
      <td>20</td>
      <td>10</td>
      <td>discount</td>
      <td>0b1e1539f2cc45b7b9fa7c272da2e1d7</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>7</td>
      <td>7</td>
      <td>discount</td>
      <td>2298d6c36e964ae4a3e7e9706d1fb8c2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>10</td>
      <td>discount</td>
      <td>fafdcd668e3743c1bb461111dcafc2a4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>['email', 'mobile', 'social']</td>
      <td>0</td>
      <td>3</td>
      <td>informational</td>
      <td>5a8bc65990b245e5a138643cd4eb9837</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>5</td>
      <td>5</td>
      <td>bogo</td>
      <td>f19421c1d4aa40978ebb69ca19b0e20d</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2</td>
      <td>['web', 'email', 'mobile']</td>
      <td>10</td>
      <td>7</td>
      <td>discount</td>
      <td>2906b810c7d4411798c6938adc9daaa5</td>
    </tr>
  </tbody>
</table>
</div>



--------------------------------------
### channel 관련 전처리

* **특징3** : **[channels]** 홍보수단(channels)이 list로 묶여 있다. 이를 풀어줘야 한다.
* (미확인) : channels 부분을 직접 사용할거 같지 않아서 풀지 않았다.


```python
portfolio_data.head(4)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>['email', 'mobile', 'social']</td>
      <td>10</td>
      <td>7</td>
      <td>bogo</td>
      <td>ae264e3637204a6fb9bb56bc8210ddfd</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>4d5c57ea9a6940dd891ad53e9dbe8da0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>0</td>
      <td>4</td>
      <td>informational</td>
      <td>3f207df678b143eea3cee63160fa8bed</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>9b98b8c7a33c4b65b9aebfe6a799e6d9</td>
    </tr>
  </tbody>
</table>
</div>



#### [email], [web], [mobile], [social] 각 홍보수단 별로 카운트 컬럼 생성


```python
portfolio_data['email'] = portfolio_data['channels'].str.count('email')
portfolio_data['web'] = portfolio_data['channels'].str.count('web')
portfolio_data['mobile'] = portfolio_data['channels'].str.count('mobile')
portfolio_data['social'] = portfolio_data['channels'].str.count('social')
portfolio_data.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>id</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>['email', 'mobile', 'social']</td>
      <td>10</td>
      <td>7</td>
      <td>bogo</td>
      <td>ae264e3637204a6fb9bb56bc8210ddfd</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>4d5c57ea9a6940dd891ad53e9dbe8da0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>0</td>
      <td>4</td>
      <td>informational</td>
      <td>3f207df678b143eea3cee63160fa8bed</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



#### [channel_num] 몇개의 홍보수단을 사용했는지 보여줌


```python
portfolio_data['channel_num'] = portfolio_data['email'] + portfolio_data['web'] + portfolio_data['mobile'] + portfolio_data['social']
portfolio_data.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>id</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
      <th>channel_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>['email', 'mobile', 'social']</td>
      <td>10</td>
      <td>7</td>
      <td>bogo</td>
      <td>ae264e3637204a6fb9bb56bc8210ddfd</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>4d5c57ea9a6940dd891ad53e9dbe8da0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>0</td>
      <td>4</td>
      <td>informational</td>
      <td>3f207df678b143eea3cee63160fa8bed</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



-------------------------------
###  id관련 전처리

#### 앞의 10자리로 변환 


```python
portfolio_data['id'] = portfolio_data['id'].str[:10]
```

#### [offer_id] profile.csv의 person_id와 구분


```python
portfolio_data = portfolio_data.rename({'id' : 'offer_id'}, axis='columns')
portfolio_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>offer_id</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
      <th>channel_num</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>['email', 'mobile', 'social']</td>
      <td>10</td>
      <td>7</td>
      <td>bogo</td>
      <td>ae264e3637</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>4d5c57ea9a</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>0</td>
      <td>4</td>
      <td>informational</td>
      <td>3f207df678</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>9b98b8c7a3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>['web', 'email']</td>
      <td>20</td>
      <td>10</td>
      <td>discount</td>
      <td>0b1e1539f2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>7</td>
      <td>7</td>
      <td>discount</td>
      <td>2298d6c36e</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>10</td>
      <td>discount</td>
      <td>fafdcd668e</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>['email', 'mobile', 'social']</td>
      <td>0</td>
      <td>3</td>
      <td>informational</td>
      <td>5a8bc65990</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>5</td>
      <td>5</td>
      <td>bogo</td>
      <td>f19421c1d4</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2</td>
      <td>['web', 'email', 'mobile']</td>
      <td>10</td>
      <td>7</td>
      <td>discount</td>
      <td>2906b810c7</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



----------------------------------
### [r_minus_d] reward, difficulty 관련 전처리

|열 이름 | 의미| 특징|
|--------|-----|----|
|<span style="color:red">***reward***</span>| 쿠폰 사용 금액(달러) |  bogo(1+1)의 reward는 difficulty와 같다.|
|<span style="color:red">***difficulty***</span>|쿠폰을 받기 위한 최소 금액(달러)|There is also a difficulty score, the dollar amount that must be spent for the offer to be completed.|


```python
portfolio_data['r_minus_d'] = portfolio_data['reward'] - portfolio_data['difficulty'] 
portfolio_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>offer_id</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
      <th>channel_num</th>
      <th>r_minus_d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>['email', 'mobile', 'social']</td>
      <td>10</td>
      <td>7</td>
      <td>bogo</td>
      <td>ae264e3637</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>4d5c57ea9a</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>0</td>
      <td>4</td>
      <td>informational</td>
      <td>3f207df678</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>9b98b8c7a3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>['web', 'email']</td>
      <td>20</td>
      <td>10</td>
      <td>discount</td>
      <td>0b1e1539f2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>-15</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>7</td>
      <td>7</td>
      <td>discount</td>
      <td>2298d6c36e</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>-4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>10</td>
      <td>discount</td>
      <td>fafdcd668e</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>-8</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>['email', 'mobile', 'social']</td>
      <td>0</td>
      <td>3</td>
      <td>informational</td>
      <td>5a8bc65990</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>5</td>
      <td>5</td>
      <td>bogo</td>
      <td>f19421c1d4</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2</td>
      <td>['web', 'email', 'mobile']</td>
      <td>10</td>
      <td>7</td>
      <td>discount</td>
      <td>2906b810c7</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>-8</td>
    </tr>
  </tbody>
</table>
</div>



### portfolio_processing.csv로 저장


```python
portfolio_data.to_csv('portfolio_processing.csv', index=False)
```

**확인**


```python
pd.read_csv('portfolio_processing.csv')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>offer_id</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
      <th>channel_num</th>
      <th>r_minus_d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>['email', 'mobile', 'social']</td>
      <td>10</td>
      <td>7</td>
      <td>bogo</td>
      <td>ae264e3637</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>4d5c57ea9a</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>0</td>
      <td>4</td>
      <td>informational</td>
      <td>3f207df678</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>9b98b8c7a3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>['web', 'email']</td>
      <td>20</td>
      <td>10</td>
      <td>discount</td>
      <td>0b1e1539f2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>-15</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>7</td>
      <td>7</td>
      <td>discount</td>
      <td>2298d6c36e</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>-4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>10</td>
      <td>discount</td>
      <td>fafdcd668e</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>-8</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>['email', 'mobile', 'social']</td>
      <td>0</td>
      <td>3</td>
      <td>informational</td>
      <td>5a8bc65990</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>5</td>
      <td>5</td>
      <td>bogo</td>
      <td>f19421c1d4</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2</td>
      <td>['web', 'email', 'mobile']</td>
      <td>10</td>
      <td>7</td>
      <td>discount</td>
      <td>2906b810c7</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>-8</td>
    </tr>
  </tbody>
</table>
</div>



----------------------------------------
## Transcript.csv 전처리

|열 이름 | 의미| 특징|
|--------|-----|----|
| ***person*** | 고객 id |  |
|***event*** | 진행상황(record) : 거래, 이벤트 제안 수신, 이벤트 조회, 이벤트 완판| |
|***value*** |프로모션 id, 거래금액(transaction amount)|`{key : value}` 형태로 존재 |
|***time*** | time in hours(이벤트 남은 기간??)| |


-------------------------------------------
### 결측치 제거, Unnamed: 0 컬럼 제거


```python
transcript_data = transcript.copy()
del transcript_data['Unnamed: 0']
transcript_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>78afa995795e4d85b5d9ceeca43f5fef</td>
      <td>offer received</td>
      <td>{'offer id': '9b98b8c7a33c4b65b9aebfe6a799e6d9'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a03223e636434f42ac4c3df47e8bac43</td>
      <td>offer received</td>
      <td>{'offer id': '0b1e1539f2cc45b7b9fa7c272da2e1d7'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>e2127556f4f64592b11af22de27a7932</td>
      <td>offer received</td>
      <td>{'offer id': '2906b810c7d4411798c6938adc9daaa5'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8ec6ce2a7e7949b1bf142def7d0e0586</td>
      <td>offer received</td>
      <td>{'offer id': 'fafdcd668e3743c1bb461111dcafc2a4'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>68617ca6246f4fbc85e91a2a49552598</td>
      <td>offer received</td>
      <td>{'offer id': '4d5c57ea9a6940dd891ad53e9dbe8da0'}</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>306529</th>
      <td>b3a1272bc9904337b331bf348c3e8c17</td>
      <td>transaction</td>
      <td>{'amount': 1.5899999999999999}</td>
      <td>714</td>
    </tr>
    <tr>
      <th>306530</th>
      <td>68213b08d99a4ae1b0dcb72aebd9aa35</td>
      <td>transaction</td>
      <td>{'amount': 9.53}</td>
      <td>714</td>
    </tr>
    <tr>
      <th>306531</th>
      <td>a00058cf10334a308c68e7631c529907</td>
      <td>transaction</td>
      <td>{'amount': 3.61}</td>
      <td>714</td>
    </tr>
    <tr>
      <th>306532</th>
      <td>76ddbd6576844afe811f1a3c0fbb5bec</td>
      <td>transaction</td>
      <td>{'amount': 3.5300000000000002}</td>
      <td>714</td>
    </tr>
    <tr>
      <th>306533</th>
      <td>c02b10e8752c4d8e9b73f918558531f7</td>
      <td>transaction</td>
      <td>{'amount': 4.05}</td>
      <td>714</td>
    </tr>
  </tbody>
</table>
<p>306534 rows × 4 columns</p>
</div>



-------------------------------
###  value 관련 전처리

#### [group], [id] 컬럼 생성

* ***특징 6*** : **[value]** `{'offer_id': '2906b810c7d4411798c6938adc9daaa5', 'reward': 2}`를 portfoio와 비교해보니 reward개수가 같았다


**value를 group과 id로 분할한다**


```python
# value값 나눠서 offer_id로 나누기
transcript_data[['group', 'id']] = transcript_data['value'].str.split(':', n=1, expand=True)
display(transcript_data.head(3))

# 중괄호 및 필요없는 문자 제거
transcript_data['group'] = transcript_data['group'].str.strip('{')
transcript_data['id'] = transcript_data['id'].str.strip('}')
transcript_data['group'] = transcript_data['group'].str.strip("''")
transcript_data['group'] = transcript_data['group'].str.replace('offer_id', 'offer id')  ## (미확인) 부분 해결
transcript_data['id'] = transcript_data['id'].str.strip("''")

display(transcript_data.head(2))
display(transcript_data.tail(2))
display(transcript_data[transcript_data['id'].str.contains('reward')].head(2))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
      <th>group</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>78afa995795e4d85b5d9ceeca43f5fef</td>
      <td>offer received</td>
      <td>{'offer id': '9b98b8c7a33c4b65b9aebfe6a799e6d9'}</td>
      <td>0</td>
      <td>{'offer id'</td>
      <td>'9b98b8c7a33c4b65b9aebfe6a799e6d9'}</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a03223e636434f42ac4c3df47e8bac43</td>
      <td>offer received</td>
      <td>{'offer id': '0b1e1539f2cc45b7b9fa7c272da2e1d7'}</td>
      <td>0</td>
      <td>{'offer id'</td>
      <td>'0b1e1539f2cc45b7b9fa7c272da2e1d7'}</td>
    </tr>
    <tr>
      <th>2</th>
      <td>e2127556f4f64592b11af22de27a7932</td>
      <td>offer received</td>
      <td>{'offer id': '2906b810c7d4411798c6938adc9daaa5'}</td>
      <td>0</td>
      <td>{'offer id'</td>
      <td>'2906b810c7d4411798c6938adc9daaa5'}</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
      <th>group</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>78afa995795e4d85b5d9ceeca43f5fef</td>
      <td>offer received</td>
      <td>{'offer id': '9b98b8c7a33c4b65b9aebfe6a799e6d9'}</td>
      <td>0</td>
      <td>offer id</td>
      <td>'9b98b8c7a33c4b65b9aebfe6a799e6d9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a03223e636434f42ac4c3df47e8bac43</td>
      <td>offer received</td>
      <td>{'offer id': '0b1e1539f2cc45b7b9fa7c272da2e1d7'}</td>
      <td>0</td>
      <td>offer id</td>
      <td>'0b1e1539f2cc45b7b9fa7c272da2e1d7</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
      <th>group</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>306532</th>
      <td>76ddbd6576844afe811f1a3c0fbb5bec</td>
      <td>transaction</td>
      <td>{'amount': 3.5300000000000002}</td>
      <td>714</td>
      <td>amount</td>
      <td>3.5300000000000002</td>
    </tr>
    <tr>
      <th>306533</th>
      <td>c02b10e8752c4d8e9b73f918558531f7</td>
      <td>transaction</td>
      <td>{'amount': 4.05}</td>
      <td>714</td>
      <td>amount</td>
      <td>4.05</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
      <th>group</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12658</th>
      <td>9fa9ae8f57894cc9a3b8a9bbe0fc1b2f</td>
      <td>offer completed</td>
      <td>{'offer_id': '2906b810c7d4411798c6938adc9daaa5...</td>
      <td>0</td>
      <td>offer id</td>
      <td>'2906b810c7d4411798c6938adc9daaa5', 'reward': 2</td>
    </tr>
    <tr>
      <th>12672</th>
      <td>fe97aa22dd3e48c8b143116a8403dd52</td>
      <td>offer completed</td>
      <td>{'offer_id': 'fafdcd668e3743c1bb461111dcafc2a4...</td>
      <td>0</td>
      <td>offer id</td>
      <td>'fafdcd668e3743c1bb461111dcafc2a4', 'reward': 2</td>
    </tr>
  </tbody>
</table>
</div>


***특징 6*** : **[value]** `{'offer_id': '2906b810c7d4411798c6938adc9daaa5', 'reward': 2}`를 portfoio와 비교해보니 reward개수가 같았다

**reward를 삭제해준다**


```python
reward = transcript_data['id'].str.contains('reward')
transcript_data.loc[reward, 'id'] = transcript_data.loc[reward, 'id'].str.split(",", expand=True)[0]
transcript_data['id'] = transcript_data['id'].str.replace("'", "")
```

**재확인**


```python
display(transcript_data[reward].head(2))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person</th>
      <th>event</th>
      <th>value</th>
      <th>time</th>
      <th>group</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12658</th>
      <td>9fa9ae8f57894cc9a3b8a9bbe0fc1b2f</td>
      <td>offer completed</td>
      <td>{'offer_id': '2906b810c7d4411798c6938adc9daaa5...</td>
      <td>0</td>
      <td>offer id</td>
      <td>2906b810c7d4411798c6938adc9daaa5</td>
    </tr>
    <tr>
      <th>12672</th>
      <td>fe97aa22dd3e48c8b143116a8403dd52</td>
      <td>offer completed</td>
      <td>{'offer_id': 'fafdcd668e3743c1bb461111dcafc2a4...</td>
      <td>0</td>
      <td>offer id</td>
      <td>fafdcd668e3743c1bb461111dcafc2a4</td>
    </tr>
  </tbody>
</table>
</div>


**value제거**


```python
del transcript_data['value']
```


```python
display(transcript_data)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>78afa995795e4d85b5d9ceeca43f5fef</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>9b98b8c7a33c4b65b9aebfe6a799e6d9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a03223e636434f42ac4c3df47e8bac43</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>0b1e1539f2cc45b7b9fa7c272da2e1d7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>e2127556f4f64592b11af22de27a7932</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>2906b810c7d4411798c6938adc9daaa5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8ec6ce2a7e7949b1bf142def7d0e0586</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>fafdcd668e3743c1bb461111dcafc2a4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>68617ca6246f4fbc85e91a2a49552598</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>4d5c57ea9a6940dd891ad53e9dbe8da0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>306529</th>
      <td>b3a1272bc9904337b331bf348c3e8c17</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>1.5899999999999999</td>
    </tr>
    <tr>
      <th>306530</th>
      <td>68213b08d99a4ae1b0dcb72aebd9aa35</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>9.53</td>
    </tr>
    <tr>
      <th>306531</th>
      <td>a00058cf10334a308c68e7631c529907</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>3.61</td>
    </tr>
    <tr>
      <th>306532</th>
      <td>76ddbd6576844afe811f1a3c0fbb5bec</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>3.5300000000000002</td>
    </tr>
    <tr>
      <th>306533</th>
      <td>c02b10e8752c4d8e9b73f918558531f7</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>4.05</td>
    </tr>
  </tbody>
</table>
<p>306534 rows × 5 columns</p>
</div>


**[offer_id] id값을 5자리로 축약하고 offer_id로 컬럼명 변경**


```python
offer = transcript_data['group'] == 'offer id'
transcript_data.loc[offer, 'id'] = transcript_data.loc[offer, 'id'].str.replace(" ", "").str[:10]
transcript_data = transcript_data.rename({'id':'offer_id'},axis='columns')
```


```python
display(transcript_data)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>78afa995795e4d85b5d9ceeca43f5fef</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a03223e636434f42ac4c3df47e8bac43</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>0b1e1539f2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>e2127556f4f64592b11af22de27a7932</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>2906b810c7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8ec6ce2a7e7949b1bf142def7d0e0586</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>fafdcd668e</td>
    </tr>
    <tr>
      <th>4</th>
      <td>68617ca6246f4fbc85e91a2a49552598</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>306529</th>
      <td>b3a1272bc9904337b331bf348c3e8c17</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>1.5899999999999999</td>
    </tr>
    <tr>
      <th>306530</th>
      <td>68213b08d99a4ae1b0dcb72aebd9aa35</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>9.53</td>
    </tr>
    <tr>
      <th>306531</th>
      <td>a00058cf10334a308c68e7631c529907</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>3.61</td>
    </tr>
    <tr>
      <th>306532</th>
      <td>76ddbd6576844afe811f1a3c0fbb5bec</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>3.5300000000000002</td>
    </tr>
    <tr>
      <th>306533</th>
      <td>c02b10e8752c4d8e9b73f918558531f7</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>4.05</td>
    </tr>
  </tbody>
</table>
<p>306534 rows × 5 columns</p>
</div>


#### group = amount인 컬럼의 id 값을 소수점 두자리로 변환


```python
amount = transcript_data['group']=='amount' 
transcript_data.loc[amount, 'offer_id'] = transcript_data.loc[amount, 'offer_id'].astype(float).round(2)
```


```python
transcript_data.loc[amount, :]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12654</th>
      <td>02c083884c7d45b39cc68e1314fec56c</td>
      <td>transaction</td>
      <td>0</td>
      <td>amount</td>
      <td>0.83</td>
    </tr>
    <tr>
      <th>12657</th>
      <td>9fa9ae8f57894cc9a3b8a9bbe0fc1b2f</td>
      <td>transaction</td>
      <td>0</td>
      <td>amount</td>
      <td>34.56</td>
    </tr>
    <tr>
      <th>12659</th>
      <td>54890f68699049c2a04d415abc25e717</td>
      <td>transaction</td>
      <td>0</td>
      <td>amount</td>
      <td>13.23</td>
    </tr>
    <tr>
      <th>12670</th>
      <td>b2f1cd155b864803ad8334cdf13c4bd2</td>
      <td>transaction</td>
      <td>0</td>
      <td>amount</td>
      <td>19.51</td>
    </tr>
    <tr>
      <th>12671</th>
      <td>fe97aa22dd3e48c8b143116a8403dd52</td>
      <td>transaction</td>
      <td>0</td>
      <td>amount</td>
      <td>18.97</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>306529</th>
      <td>b3a1272bc9904337b331bf348c3e8c17</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>1.59</td>
    </tr>
    <tr>
      <th>306530</th>
      <td>68213b08d99a4ae1b0dcb72aebd9aa35</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>9.53</td>
    </tr>
    <tr>
      <th>306531</th>
      <td>a00058cf10334a308c68e7631c529907</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>3.61</td>
    </tr>
    <tr>
      <th>306532</th>
      <td>76ddbd6576844afe811f1a3c0fbb5bec</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>3.53</td>
    </tr>
    <tr>
      <th>306533</th>
      <td>c02b10e8752c4d8e9b73f918558531f7</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>4.05</td>
    </tr>
  </tbody>
</table>
<p>138953 rows × 5 columns</p>
</div>



-------------------------------
###  person 관련 전처리

#### [person_id]로 컬럼명 변경


```python
transcript_data = transcript_data.rename({'person':'person_id'},axis='columns')
```

#### 앞의 10자리로 축약


```python
transcript_data['person_id'] = transcript_data['person_id'].str[:10]
```


```python
display(transcript_data.head())
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person_id</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>78afa99579</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a03223e636</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>0b1e1539f2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>e2127556f4</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>2906b810c7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8ec6ce2a7e</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>fafdcd668e</td>
    </tr>
    <tr>
      <th>4</th>
      <td>68617ca624</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
    </tr>
  </tbody>
</table>
</div>


-------------------------------
### time 관련 전처리

+ Time in hours, The data begins at time(시점 0으로 부터 시작 기간)
+ Time을 하루 24시간으로 나누면 1일 ~ 30일이 나온다. 여기서  일주일 간격으로 peak를 찍는 모습을 보였다.
+ 데이터를 보면 6 단위로 증가함.

####  [day] 컬럼 생성
 - 시간을 24로 나누고 내림하여 일(day) 생성
 - 숫자형으로 변환


```python
transcript_data['day'] = np.floor(transcript_data['time']/24).astype(int)
```

#### [week] 컬럼 생성
  - day를 7로 나누고 내림하여 주(week) 생성


```python
transcript_data['week'] = np.floor(transcript_data['day']/7).astype(int)
```

#### [time_korea] 컬럼 생성
  - 6시간 단위로 움직이는 특징
  - 0:자정, 6:오전6시, 12:정오, 18:오후6시 


```python
자정 = (transcript_data['time']%24 == 0)
오전6시 = (transcript_data['time']%24 == 6)
정오 = (transcript_data['time']%24 == 12)
오후6시 = (transcript_data['time']%24 == 18)
```


```python
transcript_data.loc[자정, 'time_korea'] = '자정'
transcript_data.loc[오전6시, 'time_korea'] = '오전6시'
transcript_data.loc[정오, 'time_korea'] = '정오'
transcript_data.loc[오후6시, 'time_korea'] = '오후6시'
```


```python
display(transcript_data.sample(5))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person_id</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
      <th>day</th>
      <th>week</th>
      <th>time_korea</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40555</th>
      <td>7ebc1c5f81</td>
      <td>offer viewed</td>
      <td>90</td>
      <td>offer id</td>
      <td>5a8bc65990</td>
      <td>3</td>
      <td>0</td>
      <td>오후6시</td>
    </tr>
    <tr>
      <th>138113</th>
      <td>a331d5262b</td>
      <td>offer viewed</td>
      <td>366</td>
      <td>offer id</td>
      <td>f19421c1d4</td>
      <td>15</td>
      <td>2</td>
      <td>오전6시</td>
    </tr>
    <tr>
      <th>52015</th>
      <td>eeb1816aa0</td>
      <td>transaction</td>
      <td>156</td>
      <td>amount</td>
      <td>6.46</td>
      <td>6</td>
      <td>0</td>
      <td>정오</td>
    </tr>
    <tr>
      <th>292358</th>
      <td>3f99f807bf</td>
      <td>transaction</td>
      <td>654</td>
      <td>amount</td>
      <td>10.92</td>
      <td>27</td>
      <td>3</td>
      <td>오전6시</td>
    </tr>
    <tr>
      <th>45561</th>
      <td>b991355e11</td>
      <td>offer completed</td>
      <td>120</td>
      <td>offer id</td>
      <td>2906b810c7</td>
      <td>5</td>
      <td>0</td>
      <td>자정</td>
    </tr>
  </tbody>
</table>
</div>


--------------------------------------
### portfolio_processing.csv로 저장


```python
transcript_data.to_csv('transcript_processing.csv', index=False)
```

**확인**


```python
pd.read_csv('./transcript_processing.csv')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person_id</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
      <th>day</th>
      <th>week</th>
      <th>time_korea</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>78afa99579</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a03223e636</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>0b1e1539f2</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>2</th>
      <td>e2127556f4</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>2906b810c7</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8ec6ce2a7e</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>fafdcd668e</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>4</th>
      <td>68617ca624</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>306529</th>
      <td>b3a1272bc9</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>1.59</td>
      <td>29</td>
      <td>4</td>
      <td>오후6시</td>
    </tr>
    <tr>
      <th>306530</th>
      <td>68213b08d9</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>9.53</td>
      <td>29</td>
      <td>4</td>
      <td>오후6시</td>
    </tr>
    <tr>
      <th>306531</th>
      <td>a00058cf10</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>3.61</td>
      <td>29</td>
      <td>4</td>
      <td>오후6시</td>
    </tr>
    <tr>
      <th>306532</th>
      <td>76ddbd6576</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>3.53</td>
      <td>29</td>
      <td>4</td>
      <td>오후6시</td>
    </tr>
    <tr>
      <th>306533</th>
      <td>c02b10e875</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>4.05</td>
      <td>29</td>
      <td>4</td>
      <td>오후6시</td>
    </tr>
  </tbody>
</table>
<p>306534 rows × 8 columns</p>
</div>



--------------------------------------
## 데이터 병합(merge)

- 기본 데이터
  + profile_data : 17000명 - 2175명 = 14875명
  + portfolio_data : 프로모션 10개
  + transcript_data : 고객 거래 내용 306534가지<br><br>
 
- **병합 데이터** 
  + profile_data + transcript_data (inner) : 272762
      - 사라진 데이터 33772개, 결측치로 제거한 고객수 2175명
          + 한 명당 15.5회 거래한 것으로 사료, 이 데이터가 merge시 빠짐<br><br>
          
  + pr_tr + portfolio (inner) : 148805
      - event가 transaction인 부분은 offer_id가 숫자(거래량)이다. 프로모션 id 값이 아니다.
      - offer_id가 숫자로 이루어진 부분 제거됨.

  + pr_tr + portfolio (outer) : 272762
      - **`final[final['group']=='amount']`** : 123957개
      - **`final[final['group']=='offer id']`** : 148805개

* 결론 
    1. 병합시 (profile_data + transcript_data)를 inner로 조인하고
    2. portfolio_data를 outer 조인한다.


```python
display(profile_data)
display(portfolio_data)
display(transcript_data)

pr_tr = pd.merge(profile_data, transcript_data, on = 'person_id', how='inner')
final_in = pd.merge(pr_tr, portfolio_data, on = 'offer_id', how ='inner')
final_out = pd.merge(pr_tr, portfolio_data, on = 'offer_id', how ='outer')
display(pr_tr)
display(final_in)
display(final_out)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
    </tr>
    <tr>
      <th>5</th>
      <td>M</td>
      <td>68</td>
      <td>e2127556f4</td>
      <td>2018-04-26</td>
      <td>70000.0</td>
      <td>60</td>
      <td>65</td>
      <td>2018</td>
      <td>4</td>
      <td>26</td>
      <td>2021-06-21</td>
      <td>1152</td>
    </tr>
    <tr>
      <th>8</th>
      <td>M</td>
      <td>65</td>
      <td>389bc3fa69</td>
      <td>2018-02-09</td>
      <td>53000.0</td>
      <td>60</td>
      <td>65</td>
      <td>2018</td>
      <td>2</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1228</td>
    </tr>
    <tr>
      <th>12</th>
      <td>M</td>
      <td>58</td>
      <td>2eeac8d8fe</td>
      <td>2017-11-11</td>
      <td>51000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>11</td>
      <td>11</td>
      <td>2021-06-21</td>
      <td>1318</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>16995</th>
      <td>F</td>
      <td>45</td>
      <td>6d5f3a774f</td>
      <td>2018-06-04</td>
      <td>54000.0</td>
      <td>40</td>
      <td>45</td>
      <td>2018</td>
      <td>6</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1113</td>
    </tr>
    <tr>
      <th>16996</th>
      <td>M</td>
      <td>61</td>
      <td>2cb4f97358</td>
      <td>2018-07-13</td>
      <td>72000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2018</td>
      <td>7</td>
      <td>13</td>
      <td>2021-06-21</td>
      <td>1074</td>
    </tr>
    <tr>
      <th>16997</th>
      <td>M</td>
      <td>49</td>
      <td>01d26f638c</td>
      <td>2017-01-26</td>
      <td>73000.0</td>
      <td>40</td>
      <td>45</td>
      <td>2017</td>
      <td>1</td>
      <td>26</td>
      <td>2021-06-21</td>
      <td>1607</td>
    </tr>
    <tr>
      <th>16998</th>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>50000.0</td>
      <td>80</td>
      <td>80</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
      <td>2021-06-21</td>
      <td>1932</td>
    </tr>
    <tr>
      <th>16999</th>
      <td>F</td>
      <td>62</td>
      <td>e4052622e5</td>
      <td>2017-07-22</td>
      <td>82000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2017</td>
      <td>7</td>
      <td>22</td>
      <td>2021-06-21</td>
      <td>1430</td>
    </tr>
  </tbody>
</table>
<p>14825 rows × 12 columns</p>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>offer_id</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
      <th>channel_num</th>
      <th>r_minus_d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>['email', 'mobile', 'social']</td>
      <td>10</td>
      <td>7</td>
      <td>bogo</td>
      <td>ae264e3637</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>4d5c57ea9a</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>0</td>
      <td>4</td>
      <td>informational</td>
      <td>3f207df678</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>9b98b8c7a3</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>['web', 'email']</td>
      <td>20</td>
      <td>10</td>
      <td>discount</td>
      <td>0b1e1539f2</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
      <td>-15</td>
    </tr>
    <tr>
      <th>5</th>
      <td>3</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>7</td>
      <td>7</td>
      <td>discount</td>
      <td>2298d6c36e</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>-4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>10</td>
      <td>discount</td>
      <td>fafdcd668e</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>-8</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>['email', 'mobile', 'social']</td>
      <td>0</td>
      <td>3</td>
      <td>informational</td>
      <td>5a8bc65990</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>5</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>5</td>
      <td>5</td>
      <td>bogo</td>
      <td>f19421c1d4</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2</td>
      <td>['web', 'email', 'mobile']</td>
      <td>10</td>
      <td>7</td>
      <td>discount</td>
      <td>2906b810c7</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>-8</td>
    </tr>
  </tbody>
</table>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>person_id</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
      <th>day</th>
      <th>week</th>
      <th>time_korea</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>78afa99579</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>1</th>
      <td>a03223e636</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>0b1e1539f2</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>2</th>
      <td>e2127556f4</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>2906b810c7</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8ec6ce2a7e</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>fafdcd668e</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>4</th>
      <td>68617ca624</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>306529</th>
      <td>b3a1272bc9</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>1.59</td>
      <td>29</td>
      <td>4</td>
      <td>오후6시</td>
    </tr>
    <tr>
      <th>306530</th>
      <td>68213b08d9</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>9.53</td>
      <td>29</td>
      <td>4</td>
      <td>오후6시</td>
    </tr>
    <tr>
      <th>306531</th>
      <td>a00058cf10</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>3.61</td>
      <td>29</td>
      <td>4</td>
      <td>오후6시</td>
    </tr>
    <tr>
      <th>306532</th>
      <td>76ddbd6576</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>3.53</td>
      <td>29</td>
      <td>4</td>
      <td>오후6시</td>
    </tr>
    <tr>
      <th>306533</th>
      <td>c02b10e875</td>
      <td>transaction</td>
      <td>714</td>
      <td>amount</td>
      <td>4.05</td>
      <td>29</td>
      <td>4</td>
      <td>오후6시</td>
    </tr>
  </tbody>
</table>
<p>306534 rows × 8 columns</p>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
      <th>day</th>
      <th>week</th>
      <th>time_korea</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>transaction</td>
      <td>18</td>
      <td>amount</td>
      <td>21.51</td>
      <td>0</td>
      <td>0</td>
      <td>오후6시</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>transaction</td>
      <td>144</td>
      <td>amount</td>
      <td>32.28</td>
      <td>6</td>
      <td>0</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>offer received</td>
      <td>408</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>17</td>
      <td>2</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>offer received</td>
      <td>504</td>
      <td>offer id</td>
      <td>3f207df678</td>
      <td>21</td>
      <td>3</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>4</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>transaction</td>
      <td>528</td>
      <td>amount</td>
      <td>23.22</td>
      <td>22</td>
      <td>3</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>272757</th>
      <td>F</td>
      <td>62</td>
      <td>e4052622e5</td>
      <td>2017-07-22</td>
      <td>82000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2017</td>
      <td>7</td>
      <td>22</td>
      <td>2021-06-21</td>
      <td>1430</td>
      <td>offer completed</td>
      <td>480</td>
      <td>offer id</td>
      <td>f19421c1d4</td>
      <td>20</td>
      <td>2</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>272758</th>
      <td>F</td>
      <td>62</td>
      <td>e4052622e5</td>
      <td>2017-07-22</td>
      <td>82000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2017</td>
      <td>7</td>
      <td>22</td>
      <td>2021-06-21</td>
      <td>1430</td>
      <td>transaction</td>
      <td>486</td>
      <td>amount</td>
      <td>19.47</td>
      <td>20</td>
      <td>2</td>
      <td>오전6시</td>
    </tr>
    <tr>
      <th>272759</th>
      <td>F</td>
      <td>62</td>
      <td>e4052622e5</td>
      <td>2017-07-22</td>
      <td>82000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2017</td>
      <td>7</td>
      <td>22</td>
      <td>2021-06-21</td>
      <td>1430</td>
      <td>offer viewed</td>
      <td>546</td>
      <td>offer id</td>
      <td>f19421c1d4</td>
      <td>22</td>
      <td>3</td>
      <td>오후6시</td>
    </tr>
    <tr>
      <th>272760</th>
      <td>F</td>
      <td>62</td>
      <td>e4052622e5</td>
      <td>2017-07-22</td>
      <td>82000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2017</td>
      <td>7</td>
      <td>22</td>
      <td>2021-06-21</td>
      <td>1430</td>
      <td>offer received</td>
      <td>576</td>
      <td>offer id</td>
      <td>3f207df678</td>
      <td>24</td>
      <td>3</td>
      <td>자정</td>
    </tr>
    <tr>
      <th>272761</th>
      <td>F</td>
      <td>62</td>
      <td>e4052622e5</td>
      <td>2017-07-22</td>
      <td>82000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2017</td>
      <td>7</td>
      <td>22</td>
      <td>2021-06-21</td>
      <td>1430</td>
      <td>transaction</td>
      <td>690</td>
      <td>amount</td>
      <td>24.71</td>
      <td>28</td>
      <td>4</td>
      <td>오후6시</td>
    </tr>
  </tbody>
</table>
<p>272762 rows × 19 columns</p>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
      <th>day</th>
      <th>week</th>
      <th>time_korea</th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
      <th>channel_num</th>
      <th>r_minus_d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>offer received</td>
      <td>408</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>17</td>
      <td>2</td>
      <td>자정</td>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>offer completed</td>
      <td>528</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>22</td>
      <td>3</td>
      <td>자정</td>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
      <td>offer viewed</td>
      <td>6</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>0</td>
      <td>0</td>
      <td>오전6시</td>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
      <td>offer completed</td>
      <td>132</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>5</td>
      <td>0</td>
      <td>정오</td>
      <td>5</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5</td>
      <td>7</td>
      <td>bogo</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>148800</th>
      <td>F</td>
      <td>45</td>
      <td>6d5f3a774f</td>
      <td>2018-06-04</td>
      <td>54000.0</td>
      <td>40</td>
      <td>45</td>
      <td>2018</td>
      <td>6</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1113</td>
      <td>offer received</td>
      <td>336</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>14</td>
      <td>2</td>
      <td>자정</td>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>148801</th>
      <td>F</td>
      <td>45</td>
      <td>6d5f3a774f</td>
      <td>2018-06-04</td>
      <td>54000.0</td>
      <td>40</td>
      <td>45</td>
      <td>2018</td>
      <td>6</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1113</td>
      <td>offer viewed</td>
      <td>402</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>16</td>
      <td>2</td>
      <td>오후6시</td>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>148802</th>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>50000.0</td>
      <td>80</td>
      <td>80</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
      <td>2021-06-21</td>
      <td>1932</td>
      <td>offer received</td>
      <td>336</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>14</td>
      <td>2</td>
      <td>자정</td>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>148803</th>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>50000.0</td>
      <td>80</td>
      <td>80</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
      <td>2021-06-21</td>
      <td>1932</td>
      <td>offer viewed</td>
      <td>342</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>14</td>
      <td>2</td>
      <td>오전6시</td>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>148804</th>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>50000.0</td>
      <td>80</td>
      <td>80</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
      <td>2021-06-21</td>
      <td>1932</td>
      <td>offer completed</td>
      <td>360</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>15</td>
      <td>2</td>
      <td>자정</td>
      <td>10</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10</td>
      <td>5</td>
      <td>bogo</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>4</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>148805 rows × 30 columns</p>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
      <th>day</th>
      <th>week</th>
      <th>time_korea</th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
      <th>channel_num</th>
      <th>r_minus_d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>transaction</td>
      <td>18</td>
      <td>amount</td>
      <td>21.51</td>
      <td>0</td>
      <td>0</td>
      <td>오후6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>58</td>
      <td>fcb6487bac</td>
      <td>2017-03-10</td>
      <td>71000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>3</td>
      <td>10</td>
      <td>2021-06-21</td>
      <td>1564</td>
      <td>transaction</td>
      <td>594</td>
      <td>amount</td>
      <td>21.51</td>
      <td>24</td>
      <td>3</td>
      <td>오후6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>56</td>
      <td>0f792a0ea8</td>
      <td>2016-02-14</td>
      <td>70000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2016</td>
      <td>2</td>
      <td>14</td>
      <td>2021-06-21</td>
      <td>1954</td>
      <td>transaction</td>
      <td>594</td>
      <td>amount</td>
      <td>21.51</td>
      <td>24</td>
      <td>3</td>
      <td>오후6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>41</td>
      <td>3915674b75</td>
      <td>2018-02-11</td>
      <td>89000.0</td>
      <td>40</td>
      <td>40</td>
      <td>2018</td>
      <td>2</td>
      <td>11</td>
      <td>2021-06-21</td>
      <td>1226</td>
      <td>transaction</td>
      <td>678</td>
      <td>amount</td>
      <td>21.51</td>
      <td>28</td>
      <td>4</td>
      <td>오전6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>F</td>
      <td>76</td>
      <td>7b249c93b5</td>
      <td>2016-06-04</td>
      <td>64000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2016</td>
      <td>6</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1843</td>
      <td>transaction</td>
      <td>6</td>
      <td>amount</td>
      <td>21.51</td>
      <td>0</td>
      <td>0</td>
      <td>오전6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>272757</th>
      <td>M</td>
      <td>30</td>
      <td>d77c7af5dd</td>
      <td>2017-12-23</td>
      <td>38000.0</td>
      <td>30</td>
      <td>30</td>
      <td>2017</td>
      <td>12</td>
      <td>23</td>
      <td>2021-06-21</td>
      <td>1276</td>
      <td>transaction</td>
      <td>432</td>
      <td>amount</td>
      <td>319.83</td>
      <td>18</td>
      <td>2</td>
      <td>자정</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>272758</th>
      <td>F</td>
      <td>63</td>
      <td>0b250fe9fa</td>
      <td>2016-03-04</td>
      <td>85000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2016</td>
      <td>3</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1935</td>
      <td>transaction</td>
      <td>486</td>
      <td>amount</td>
      <td>42.38</td>
      <td>20</td>
      <td>2</td>
      <td>오전6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>272759</th>
      <td>M</td>
      <td>56</td>
      <td>d087c473b4</td>
      <td>2016-10-23</td>
      <td>51000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2016</td>
      <td>10</td>
      <td>23</td>
      <td>2021-06-21</td>
      <td>1702</td>
      <td>transaction</td>
      <td>438</td>
      <td>amount</td>
      <td>423.4</td>
      <td>18</td>
      <td>2</td>
      <td>오전6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>272760</th>
      <td>F</td>
      <td>75</td>
      <td>392d23b2c9</td>
      <td>2016-07-16</td>
      <td>78000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2016</td>
      <td>7</td>
      <td>16</td>
      <td>2021-06-21</td>
      <td>1801</td>
      <td>transaction</td>
      <td>570</td>
      <td>amount</td>
      <td>38.33</td>
      <td>23</td>
      <td>3</td>
      <td>오후6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>272761</th>
      <td>M</td>
      <td>57</td>
      <td>76ddbd6576</td>
      <td>2016-07-09</td>
      <td>40000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2016</td>
      <td>7</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1808</td>
      <td>transaction</td>
      <td>168</td>
      <td>amount</td>
      <td>112.6</td>
      <td>7</td>
      <td>1</td>
      <td>자정</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>272762 rows × 30 columns</p>
</div>



```python
display(final_out[final_out['group']=='offer id'])
display(final_out[final_out['group']=='amount'])
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
      <th>day</th>
      <th>week</th>
      <th>time_korea</th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
      <th>channel_num</th>
      <th>r_minus_d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>offer received</td>
      <td>408</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>17</td>
      <td>2</td>
      <td>자정</td>
      <td>5.0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>41</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>offer completed</td>
      <td>528</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>22</td>
      <td>3</td>
      <td>자정</td>
      <td>5.0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>42</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
      <td>5.0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>43</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
      <td>offer viewed</td>
      <td>6</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>0</td>
      <td>0</td>
      <td>오전6시</td>
      <td>5.0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>44</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
      <td>offer completed</td>
      <td>132</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>5</td>
      <td>0</td>
      <td>정오</td>
      <td>5.0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>149565</th>
      <td>F</td>
      <td>45</td>
      <td>6d5f3a774f</td>
      <td>2018-06-04</td>
      <td>54000.0</td>
      <td>40</td>
      <td>45</td>
      <td>2018</td>
      <td>6</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1113</td>
      <td>offer received</td>
      <td>336</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>14</td>
      <td>2</td>
      <td>자정</td>
      <td>10.0</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>149566</th>
      <td>F</td>
      <td>45</td>
      <td>6d5f3a774f</td>
      <td>2018-06-04</td>
      <td>54000.0</td>
      <td>40</td>
      <td>45</td>
      <td>2018</td>
      <td>6</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1113</td>
      <td>offer viewed</td>
      <td>402</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>16</td>
      <td>2</td>
      <td>오후6시</td>
      <td>10.0</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>149567</th>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>50000.0</td>
      <td>80</td>
      <td>80</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
      <td>2021-06-21</td>
      <td>1932</td>
      <td>offer received</td>
      <td>336</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>14</td>
      <td>2</td>
      <td>자정</td>
      <td>10.0</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>149568</th>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>50000.0</td>
      <td>80</td>
      <td>80</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
      <td>2021-06-21</td>
      <td>1932</td>
      <td>offer viewed</td>
      <td>342</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>14</td>
      <td>2</td>
      <td>오전6시</td>
      <td>10.0</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>149569</th>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>50000.0</td>
      <td>80</td>
      <td>80</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
      <td>2021-06-21</td>
      <td>1932</td>
      <td>offer completed</td>
      <td>360</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>15</td>
      <td>2</td>
      <td>자정</td>
      <td>10.0</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>148805 rows × 30 columns</p>
</div>



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
      <th>day</th>
      <th>week</th>
      <th>time_korea</th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
      <th>channel_num</th>
      <th>r_minus_d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>transaction</td>
      <td>18</td>
      <td>amount</td>
      <td>21.51</td>
      <td>0</td>
      <td>0</td>
      <td>오후6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>58</td>
      <td>fcb6487bac</td>
      <td>2017-03-10</td>
      <td>71000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>3</td>
      <td>10</td>
      <td>2021-06-21</td>
      <td>1564</td>
      <td>transaction</td>
      <td>594</td>
      <td>amount</td>
      <td>21.51</td>
      <td>24</td>
      <td>3</td>
      <td>오후6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>56</td>
      <td>0f792a0ea8</td>
      <td>2016-02-14</td>
      <td>70000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2016</td>
      <td>2</td>
      <td>14</td>
      <td>2021-06-21</td>
      <td>1954</td>
      <td>transaction</td>
      <td>594</td>
      <td>amount</td>
      <td>21.51</td>
      <td>24</td>
      <td>3</td>
      <td>오후6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>F</td>
      <td>41</td>
      <td>3915674b75</td>
      <td>2018-02-11</td>
      <td>89000.0</td>
      <td>40</td>
      <td>40</td>
      <td>2018</td>
      <td>2</td>
      <td>11</td>
      <td>2021-06-21</td>
      <td>1226</td>
      <td>transaction</td>
      <td>678</td>
      <td>amount</td>
      <td>21.51</td>
      <td>28</td>
      <td>4</td>
      <td>오전6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>F</td>
      <td>76</td>
      <td>7b249c93b5</td>
      <td>2016-06-04</td>
      <td>64000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2016</td>
      <td>6</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1843</td>
      <td>transaction</td>
      <td>6</td>
      <td>amount</td>
      <td>21.51</td>
      <td>0</td>
      <td>0</td>
      <td>오전6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>272757</th>
      <td>M</td>
      <td>30</td>
      <td>d77c7af5dd</td>
      <td>2017-12-23</td>
      <td>38000.0</td>
      <td>30</td>
      <td>30</td>
      <td>2017</td>
      <td>12</td>
      <td>23</td>
      <td>2021-06-21</td>
      <td>1276</td>
      <td>transaction</td>
      <td>432</td>
      <td>amount</td>
      <td>319.83</td>
      <td>18</td>
      <td>2</td>
      <td>자정</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>272758</th>
      <td>F</td>
      <td>63</td>
      <td>0b250fe9fa</td>
      <td>2016-03-04</td>
      <td>85000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2016</td>
      <td>3</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1935</td>
      <td>transaction</td>
      <td>486</td>
      <td>amount</td>
      <td>42.38</td>
      <td>20</td>
      <td>2</td>
      <td>오전6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>272759</th>
      <td>M</td>
      <td>56</td>
      <td>d087c473b4</td>
      <td>2016-10-23</td>
      <td>51000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2016</td>
      <td>10</td>
      <td>23</td>
      <td>2021-06-21</td>
      <td>1702</td>
      <td>transaction</td>
      <td>438</td>
      <td>amount</td>
      <td>423.4</td>
      <td>18</td>
      <td>2</td>
      <td>오전6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>272760</th>
      <td>F</td>
      <td>75</td>
      <td>392d23b2c9</td>
      <td>2016-07-16</td>
      <td>78000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2016</td>
      <td>7</td>
      <td>16</td>
      <td>2021-06-21</td>
      <td>1801</td>
      <td>transaction</td>
      <td>570</td>
      <td>amount</td>
      <td>38.33</td>
      <td>23</td>
      <td>3</td>
      <td>오후6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>272761</th>
      <td>M</td>
      <td>57</td>
      <td>76ddbd6576</td>
      <td>2016-07-09</td>
      <td>40000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2016</td>
      <td>7</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1808</td>
      <td>transaction</td>
      <td>168</td>
      <td>amount</td>
      <td>112.6</td>
      <td>7</td>
      <td>1</td>
      <td>자정</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>123957 rows × 30 columns</p>
</div>


**파일명 다시 final로 변경**


```python
pr_tr = pd.merge(profile_data, transcript_data, on = 'person_id', how='inner')
final = pd.merge(pr_tr, portfolio_data, on = 'offer_id', how ='outer')
```

## 최종 파일로 저장


```python
final.to_csv('final.csv', index=False)
```

----------------
# 데이터 분석 및 시각화

**파일 로드**


```python
profile = pd.read_csv('./profile_processing.csv')
portfolio = pd.read_csv('./portfolio_processing.csv')
transcript = pd.read_csv('./transcript_processing.csv')
final = pd.read_csv('./final.csv')
```

    C:\Users\asus\AppData\Roaming\Python\Python38\site-packages\IPython\core\interactiveshell.py:3155: DtypeWarning: Columns (15,20,23) have mixed types.Specify dtype option on import or set low_memory=False.
      has_raised = await self.run_ast_nodes(code_ast.body, cell_name,
    

**파일 정리**


```python
final2 = final.copy()
```

**추가 컬럼 생성 : 소득 구간 나눠주기**


```python
final2['income_rank'] = pd.cut(x= final2['income'], bins= [29000, 50000, 75000, 100000, 121000], 
                     labels =['income_4th', 'income_3th', 'income_2th', 'income_1th'])
```


```python
profile['income_rank'] = pd.cut(x= profile['income'], bins= [29000, 50000, 75000, 100000, 121000], 
                     labels =['income_4th', 'income_3th', 'income_2th', 'income_1th'])
```


```python
final2.columns
```




    Index(['gender', 'age', 'person_id', 'became_member_on', 'income',
           'age_units10', 'age_units5', 'join_year', 'join_month', 'join_day',
           'now', 'join_period', 'event', 'time', 'group', 'offer_id', 'day',
           'week', 'time_korea', 'reward', 'channels', 'difficulty', 'duration',
           'offer_type', 'email', 'web', 'mobile', 'social', 'channel_num',
           'r_minus_d', 'income_rank'],
          dtype='object')



## 전체 분석 윤곽 설정

* **[기본 데이터]**
    * **고객(profile)** : 성별, 나이, 수입, 가입일자
    * **프로모션(portfolio)** : reward, difficulty, channel, offer_type(bogo, discount, informational), duration
    * **거래 데이터(transcript)** : event(transaction(거래금액), offer view, offer receive, offer completed

### 주제 : 스타벅스 고객의 특성 파악과 향후 프로모션 전략에 대한 제안

#### 스타벅스 고객의 특성 
   * **1. 스타벅스 가입 고객들의 특성**

#### 향후 프로모션 전략 제안
   * **2. 총 순 수익 관점에서 우수한 프로모션을 파악하고 향후 프로모션 전략에 반영**
      * ex) 예상 결론 : 현재 이러이러한 프로모션 전략이 총 순 수익 관점에서 우수하니. 앞으로 이런 프로모션을 자주 진행하자.
<br><br>
   * **3. 주력 고객층을 확보하기 위한 프로모션 전략 제안**
      * ex) 예상 결론 : 총 소비금액이 큰 `주력 고객층`이 자주참여 하는 프로모션 전략은 (~~ 이러이러) 하니. 주력 고객층을 확보하기 위해서는 ~ 이런 프로모션 전략을 취해야 한다. 
<br><br>
   * **4. 프로모션 참여 매니아들을 위한 프로모션 전략 제안**
       * ex) 예상 결론 : 기존 고객들 중 ~ 이러이러 한 고객들이 프로모션 참여도가 높았다. 이 고객들이 선호하는 프로모션 전략을 파악해서 향후 반영하자. 
<br><br>
   * **5. 신규 고객층을 확보하기 위한 프로모션 전략 제안**
       * ex) 신규 고객 일수록 거래 빈도와 프로모션 참여 비율이 높은 결과가 나왔다. 신규 고객들이 선호하는 프로모션 전략을 파악하고 앞으로 그 프로모션을 취하자.

### 흐름

* **1. 스타벅스 고객들의 특성을 분석하자.**
    - 성별, 나이, 가입일자, 수입등의 특성 분석.
<br><br>    
* **2. 고객 거래 데이터중 transaction 부분을 활용하여 `주력 고객층`을 선정해보자.**
    - 거래 빈도가 많은 고객층(성별, 연령, 가입일자, 수입)
    - 평균 거래금액이 큰 고객층 파악.
    - **`거래 총량`이 큰 고객층 -> `주력 고객층`으로 설정**
<br><br>

* **3. 어떤 프로모션이 `총 순 수익`관점에서 우수한가?**
     * event
          - **`offer received`** : difficulty를 지불하고 bogo 쿠폰 및 할인권을 지급받음
          - **`offer completed`** : 쿠폰 및 할인권을 사용함.(reward)를 받음.
          - **`offer view`** : 이 정보는 분석에 제외한다.

     * offer_type
          - **`informational`** : 정보성 프로모션, 총 순수익과 관련이 없으므로 제거한다.<br><br>
     * profit(순이익) : difficulty - reward
     * **`total_difficulty(총 이익)`** = **`difficulty * offer_received`**
     * **`total_reward(총 지출)`** = **`total_reward * offer_completed`**
     * **`total_profit(총 순이익)`** = **`total_difficulty - total_reward`** = **`(difficulty * offer_received) - (total_reward * offer_completed)`**
          <br>   

* **4. `주력고객층`이 선호하는 프로모션 전략을 파악해보자**
    - **2번**에서 선정한 `주력고객층`이 높은 빈도로 참여하는 프로모션 전략을 파악해보고. 이를 앞으로의 프로모션 전략에 반영해보자.
<br><br>
* **5. 2018년도의 가입한 고객을 `신규고객` 이라고 지정하고. `신규고객`을 유치하기 위해서 프로모션 전략을 반영한다고 할 때. `신규고객`이 자주 참여하는 프로모션 전략을 파악해서. 향후에 그 프로모션 전략을 취한다.**
    - 가입일자가 최근이 될 수록 거래 & 프로모션 참여도가 높았다.

## 스타벅스 고객들의 특성

### 스타벅스 어플 가입 고객들의 특성


```python
print(profile.groupby(by='age_units10').count()['person_id']/len(profile))
print(profile.groupby(by='gender').count()['person_id']/len(profile))
print(profile.groupby(by='join_year').count()['person_id']/len(profile))
print(final2.groupby(by='income_rank').nunique()['person_id']/len(profile))
```

    age_units10
    10     0.013828
    20     0.092344
    30     0.102934
    40     0.155750
    50     0.238853
    60     0.201754
    70     0.120202
    80     0.056054
    90     0.017133
    100    0.001147
    Name: person_id, dtype: float64
    gender
    F    0.413423
    M    0.572277
    O    0.014300
    Name: person_id, dtype: float64
    join_year
    2013    0.018482
    2014    0.044654
    2015    0.107723
    2016    0.203980
    2017    0.377673
    2018    0.247487
    Name: person_id, dtype: float64
    income_rank
    income_4th    0.272108
    income_3th    0.434132
    income_2th    0.225902
    income_1th    0.067858
    Name: person_id, dtype: float64
    


```python
0.201754+0.238853+0.155750
```




    0.596357



[1차원 분석]

* **나이 분포**
    - 50대(23.9%), 60대(20.1%)가 가장 많고, 40대,50대, 60대가 전체 고객의 60%를 차지한다.
    - 생각보다 나이대가 있으신 분이 많은 부분을 차지했다.
    
* **성별 분포**
    - 남성 57.2%, 여성 41.3%, 성소수자 1.5%를 차지했다.
 
* **가입 일자 분포**
    - 점점 가입자수가 증가하는 모습을 보였다.

* **수입 분포**
    - 50000 ~ 75000 구간인 income_3th의 소득을 갖는 고객이 43.4%로 가장 많았다.


```python
profile.groupby(by='age_units10').count()['person_id']/len(profile)
```




    age_units10
    10     0.013828
    20     0.092344
    30     0.102934
    40     0.155750
    50     0.238853
    60     0.201754
    70     0.120202
    80     0.056054
    90     0.017133
    100    0.001147
    Name: person_id, dtype: float64




```python
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14,9))
(profile.groupby(by='age_units10').count()['person_id']/len(profile)).plot.bar(ax=axes[0][0], rot=0, title='고객 나이별 분포', color='g', alpha=0.8)
(profile.groupby(by='gender').count()['person_id']/len(profile)).plot.bar(ax=axes[0][1], rot=0, title='고객 성별별 분포', color = 'grey', alpha =0.8)
(profile.groupby(by='join_year').count()['person_id']/len(profile)).plot.bar(ax=axes[1][0], rot=0, title='고객 연도별 분포', color='grey', alpha=0.8)
(profile.groupby(by='income_rank').count()['person_id']/len(profile)).plot.bar(ax=axes[1][1], rot=0, title='고객 수입별 분포',  color='g', alpha=0.8)
```




    <AxesSubplot:title={'center':'고객 수입별 분포'}, xlabel='income_rank'>




    
![png](output_169_1.png)
    



```python
display(profile.head(3))
final2.head(3)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
      <th>income_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>income_1th</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
      <td>income_2th</td>
    </tr>
    <tr>
      <th>2</th>
      <td>M</td>
      <td>68</td>
      <td>e2127556f4</td>
      <td>2018-04-26</td>
      <td>70000.0</td>
      <td>60</td>
      <td>65</td>
      <td>2018</td>
      <td>4</td>
      <td>26</td>
      <td>2021-06-21</td>
      <td>1152</td>
      <td>income_3th</td>
    </tr>
  </tbody>
</table>
</div>





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
      <th>day</th>
      <th>week</th>
      <th>time_korea</th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
      <th>channel_num</th>
      <th>r_minus_d</th>
      <th>income_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>transaction</td>
      <td>18</td>
      <td>amount</td>
      <td>21.51</td>
      <td>0</td>
      <td>0</td>
      <td>오후6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>income_1th</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>58</td>
      <td>fcb6487bac</td>
      <td>2017-03-10</td>
      <td>71000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>3</td>
      <td>10</td>
      <td>2021-06-21</td>
      <td>1564</td>
      <td>transaction</td>
      <td>594</td>
      <td>amount</td>
      <td>21.51</td>
      <td>24</td>
      <td>3</td>
      <td>오후6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>income_3th</td>
    </tr>
    <tr>
      <th>2</th>
      <td>F</td>
      <td>56</td>
      <td>0f792a0ea8</td>
      <td>2016-02-14</td>
      <td>70000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2016</td>
      <td>2</td>
      <td>14</td>
      <td>2021-06-21</td>
      <td>1954</td>
      <td>transaction</td>
      <td>594</td>
      <td>amount</td>
      <td>21.51</td>
      <td>24</td>
      <td>3</td>
      <td>오후6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>income_3th</td>
    </tr>
  </tbody>
</table>
</div>



[2차원 분석]

* 같은 성별 집단 내에서 여성고객이 남성고객보다 소득 구간이 높은 구간에 있는 비율이 높았다.


```python
fig, axes = plt.subplots(ncols=2, figsize=(14,6))
(profile.groupby(by=['gender', 'income_rank']).count()['person_id'].unstack('gender')/len(profile)).plot.bar(ax= axes[0], rot=0)
(profile.groupby(by=['gender', 'income_rank']).count()['person_id'].unstack('income_rank')/len(profile)).plot.bar(ax=axes[1], rot=0)

```




    <AxesSubplot:xlabel='gender'>




    
![png](output_172_1.png)
    


* 시간이 지날수록 새로가입한 고객 중 남성 고객의 비율이 증가하고 있다.


```python
fig, axes1 = plt.subplots(nrows=1, ncols=2, figsize=(14,4))
(profile.groupby(by=['gender', 'join_year']).count()['person_id'].unstack('gender')/len(profile)).plot.bar(ax= axes1[0], rot=0)
(profile.groupby(by=['gender', 'join_year']).count()['person_id'].unstack('join_year')/len(profile)).plot.bar(ax= axes1[1], rot=0)
```




    <AxesSubplot:xlabel='gender'>




    
![png](output_174_1.png)
    



```python
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14,6))
(profile.groupby(by=['join_year', 'age_units10']).count()['person_id'].unstack('join_year')/len(profile)).plot.bar(ax=axes[0], rot=0)
(profile.groupby(by=['join_year', 'age_units10']).count()['person_id'].unstack('age_units10')/len(profile)).plot.bar(ax=axes[1], rot=0)

```




    <AxesSubplot:xlabel='join_year'>




    
![png](output_175_1.png)
    


### 주력 고객층 선정

#### 고객 거래 데이터중 transaction 부분을 활용하여 거래 총 금액이 큰 주력 고객층을 선정해보자


```python
final.sample(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
      <th>day</th>
      <th>week</th>
      <th>time_korea</th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
      <th>channel_num</th>
      <th>r_minus_d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>163337</th>
      <td>F</td>
      <td>74</td>
      <td>a4dbdeea34</td>
      <td>2017-12-03</td>
      <td>42000.0</td>
      <td>70</td>
      <td>70</td>
      <td>2017</td>
      <td>12</td>
      <td>3</td>
      <td>2021-06-21</td>
      <td>1296</td>
      <td>transaction</td>
      <td>414</td>
      <td>amount</td>
      <td>1.89</td>
      <td>17</td>
      <td>2</td>
      <td>오전6시</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>33328</th>
      <td>F</td>
      <td>54</td>
      <td>35d9949d3e</td>
      <td>2017-04-15</td>
      <td>53000.0</td>
      <td>50</td>
      <td>50</td>
      <td>2017</td>
      <td>4</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1528</td>
      <td>offer viewed</td>
      <td>594</td>
      <td>offer id</td>
      <td>5a8bc65990</td>
      <td>24</td>
      <td>3</td>
      <td>오후6시</td>
      <td>0.0</td>
      <td>['email', 'mobile', 'social']</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>informational</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>125895</th>
      <td>F</td>
      <td>70</td>
      <td>1561efceb8</td>
      <td>2016-10-26</td>
      <td>94000.0</td>
      <td>70</td>
      <td>70</td>
      <td>2016</td>
      <td>10</td>
      <td>26</td>
      <td>2021-06-21</td>
      <td>1699</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>0b1e1539f2</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
      <td>5.0</td>
      <td>['web', 'email']</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>discount</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>-15.0</td>
    </tr>
  </tbody>
</table>
</div>



**필요한 컬럼 쇼핑**


```python
cols = ['gender', 'age', 'person_id', 'age_units10', 'join_year', 'event', 'group', 'offer_id']
transaction = final[cols].copy()
```


```python
## 고객 결제 총금액 구하는 부분
transaction = transaction[transaction['group']=='amount']
transaction = transaction.astype({'offer_id':float})
transaction_amount = transaction.groupby(by='person_id').sum()[['offer_id']]

## 고객 데이터와 merge
customer_buy = pd.merge(profile, transaction_amount, left_on = 'person_id', right_index=True)
customer_buy = customer_buy.rename(columns ={'offer_id' : 'total_buy'})
customer_buy.head(4)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
      <th>income_rank</th>
      <th>total_buy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>income_1th</td>
      <td>77.01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
      <td>income_2th</td>
      <td>159.27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>M</td>
      <td>68</td>
      <td>e2127556f4</td>
      <td>2018-04-26</td>
      <td>70000.0</td>
      <td>60</td>
      <td>65</td>
      <td>2018</td>
      <td>4</td>
      <td>26</td>
      <td>2021-06-21</td>
      <td>1152</td>
      <td>income_3th</td>
      <td>57.73</td>
    </tr>
    <tr>
      <th>3</th>
      <td>M</td>
      <td>65</td>
      <td>389bc3fa69</td>
      <td>2018-02-09</td>
      <td>53000.0</td>
      <td>60</td>
      <td>65</td>
      <td>2018</td>
      <td>2</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1228</td>
      <td>income_3th</td>
      <td>36.43</td>
    </tr>
  </tbody>
</table>
</div>




```python
customer_buy.to_csv('customer_buy.csv', index=0)
```


```python
pd.read_csv('customer_buy.csv')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
      <th>income_rank</th>
      <th>total_buy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>income_1th</td>
      <td>77.01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
      <td>income_2th</td>
      <td>159.27</td>
    </tr>
    <tr>
      <th>2</th>
      <td>M</td>
      <td>68</td>
      <td>e2127556f4</td>
      <td>2018-04-26</td>
      <td>70000.0</td>
      <td>60</td>
      <td>65</td>
      <td>2018</td>
      <td>4</td>
      <td>26</td>
      <td>2021-06-21</td>
      <td>1152</td>
      <td>income_3th</td>
      <td>57.73</td>
    </tr>
    <tr>
      <th>3</th>
      <td>M</td>
      <td>65</td>
      <td>389bc3fa69</td>
      <td>2018-02-09</td>
      <td>53000.0</td>
      <td>60</td>
      <td>65</td>
      <td>2018</td>
      <td>2</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1228</td>
      <td>income_3th</td>
      <td>36.43</td>
    </tr>
    <tr>
      <th>4</th>
      <td>M</td>
      <td>58</td>
      <td>2eeac8d8fe</td>
      <td>2017-11-11</td>
      <td>51000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>11</td>
      <td>11</td>
      <td>2021-06-21</td>
      <td>1318</td>
      <td>income_3th</td>
      <td>15.62</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>14487</th>
      <td>F</td>
      <td>45</td>
      <td>6d5f3a774f</td>
      <td>2018-06-04</td>
      <td>54000.0</td>
      <td>40</td>
      <td>45</td>
      <td>2018</td>
      <td>6</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1113</td>
      <td>income_3th</td>
      <td>20.03</td>
    </tr>
    <tr>
      <th>14488</th>
      <td>M</td>
      <td>61</td>
      <td>2cb4f97358</td>
      <td>2018-07-13</td>
      <td>72000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2018</td>
      <td>7</td>
      <td>13</td>
      <td>2021-06-21</td>
      <td>1074</td>
      <td>income_3th</td>
      <td>25.97</td>
    </tr>
    <tr>
      <th>14489</th>
      <td>M</td>
      <td>49</td>
      <td>01d26f638c</td>
      <td>2017-01-26</td>
      <td>73000.0</td>
      <td>40</td>
      <td>45</td>
      <td>2017</td>
      <td>1</td>
      <td>26</td>
      <td>2021-06-21</td>
      <td>1607</td>
      <td>income_3th</td>
      <td>39.74</td>
    </tr>
    <tr>
      <th>14490</th>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>50000.0</td>
      <td>80</td>
      <td>80</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
      <td>2021-06-21</td>
      <td>1932</td>
      <td>income_4th</td>
      <td>189.67</td>
    </tr>
    <tr>
      <th>14491</th>
      <td>F</td>
      <td>62</td>
      <td>e4052622e5</td>
      <td>2017-07-22</td>
      <td>82000.0</td>
      <td>60</td>
      <td>60</td>
      <td>2017</td>
      <td>7</td>
      <td>22</td>
      <td>2021-06-21</td>
      <td>1430</td>
      <td>income_2th</td>
      <td>143.02</td>
    </tr>
  </tbody>
</table>
<p>14492 rows × 14 columns</p>
</div>




```python
total_buy = customer_buy['total_buy'].sum()
```

* 50대 ~ 60대의 고객들이 전체 고객중 44%를 차지하며 가장 많은 비율을 차지하고 있다.
* 50대  ~ 60대의 고객들이 전체 매출의 47.9%를 차지하고 있다.

**인원수 비율**


```python
pie_profile = profile.groupby(by='age_units10').count()['person_id']/len(profile)
plt.figure(figsize =(8, 8));
plt.pie(pie_profile, labels=pie_profile.index, autopct = '%0.2f%%', 
        colors = ['Gray', 'Gray', 'Gray', 'Gray', 
                  'ForestGreen', 'ForestGreen', 'Gray', 'Gray', 'Gray', 'Gray']);
plt.legend(pie_profile.index);
```


    
![png](output_186_0.png)
    


**매출 비율**


```python
pie_buy = customer_buy.groupby(by='age_units10').sum()['total_buy']/total_buy

plt.figure(figsize =(8, 8));
plt.pie(pie_buy, labels=pie_profile.index, autopct = '%0.2f%%',
        colors = ['ForestGreen', 'ForestGreen','ForestGreen', 'ForestGreen', 
                  'Gray', 'Gray', 'ForestGreen', 'ForestGreen', 'ForestGreen', 'ForestGreen']);
# plt.legend(pie_buy.index);
```


    
![png](output_188_0.png)
    



```python
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,6), sharey=True)
(customer_buy.groupby(by='age_units10').sum()['total_buy']/total_buy).plot.bar(ax=axes[0], title='각 연령층 구매금액 비율', color='green')
(profile.groupby(by='age_units10').count()['person_id']/len(profile)).plot.bar(ax=axes[1], rot=0, color='grey', title='고객 나이별 분포')
```




    <AxesSubplot:title={'center':'고객 나이별 분포'}, xlabel='age_units10'>




    
![png](output_189_1.png)
    


* 여성이 남성보다 분포는 적은데 더 많은 금액을 쓰는 것을 볼 수 있다. 즉, 남성보다 여성이 돈을 더 많이 쓴다.
    
    -> 성별로 타켓을 잡는다면 여성을 주력 고객으로 잡는 것이 좋다.


```python
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,6), sharey=True)
(customer_buy.groupby(by='gender').sum()['total_buy']/total_buy).plot.bar(ax=axes[0], color='green', title='각 성별별 구매금액 비율')
(profile.groupby(by='gender').count()['person_id']/len(profile)).plot.bar(ax=axes[1], rot=0, color='grey', title='고객 성별별 분포')
```




    <AxesSubplot:title={'center':'고객 성별별 분포'}, xlabel='gender'>




    
![png](output_191_1.png)
    


* 50대 여성, 60대 여성이 비율에 비해 큰 금액을 지출하고 있는 것을 알 수 있다.


```python
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,6), sharey=True)
(customer_buy.groupby(by=['gender', 'age_units10']).sum()['total_buy'].unstack('gender')/total_buy).plot.bar(ax=axes[0], title='각 성별별 구매금액 비율')
(profile.groupby(by=['gender', 'age_units10']).count()['person_id'].unstack('gender')/len(profile)).plot.bar(ax=axes[1], rot=0, title='고객 성별별 분포')
```




    <AxesSubplot:title={'center':'고객 성별별 분포'}, xlabel='age_units10'>




    
![png](output_193_1.png)
    



```python
# display(customer_buy.groupby(by=['gender', 'age_units10']).sum()['total_buy'].unstack('gender')/total_buy)
# display(profile.groupby(by=['gender', 'age_units10']).count()['person_id'].unstack('gender')/len(profile))
print('50, 60대 여성 총 매출 비율 :', 0.133753 + 0.114888)
print('50, 60대 여성 총 인원 비율 :', 0.105228 + 0.091062)
```

    50, 60대 여성 총 매출 비율 : 0.248641
    50, 60대 여성 총 인원 비율 : 0.19629000000000002
    

#### (결론) 주력 고객층 선정

* 50대 ~60대의 고객들이 전체 고객중 44%를 차지하며 가장 많은 비율을 차지하고 있고, 전체 매출의 47.9%를 차지하고 있다.
* 여성이 남성보다 더 큰 금액을 소비하고 있는 모습을 보여준다.
* 주력 고객층 선정
    - 대집단 : 전체 고객중 44%를 차지하며 47.9%의 매출을 올리고 있는 **50대, 60대 고객**을 스타벅스의 주력 고객으로 선정하자.
    - 소집단 : 전체 고객 중 19.6% 차지하며 24.8%의 매출을 올리고 있는 **50대, 60대 여성**을 주력고객으로 지정하자.
        * 향후에 프로모션 타케팅을 진행할때, 소집단과 대집단이 동일하면 좋겠다. 

**아래**
* 아래 그림은 income rank 별로 전체 소비에서 각 그룹이 차지하는 소비 비율(왼쪽)
* income rank별로 전체 소비에서 각 그룹이 차지하는 인원 비율(오른쪽)을 살펴 본 것이다.

* income rank가 높을 수록 소비 금액이 큰 것을 알 수 있다.


```python
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,6), sharey=True)
(customer_buy.groupby(by=['income_rank', 'gender']).sum()['total_buy'].unstack('gender')/total_buy).plot.bar(ax=axes[0], rot=0, 
                                                                                                             title = '각 수입 집단 별 소비 비율',color=['green', 'gray', 'saddlebrown'])
(profile.groupby(by=['income_rank', 'gender']).count()['person_id'].unstack('gender')/len(profile)).plot.bar(ax=axes[1], rot=0, 
                                                                                                             title='각 수입 집단 별 인원수', color=['green', 'gray', 'saddlebrown'])
```




    <AxesSubplot:title={'center':'각 수입 집단 별 인원수'}, xlabel='income_rank'>




    
![png](output_197_1.png)
    


#### 각 집단별  인원 비율 대비 구매 금액 비율

   * (각 집단의 구매 총금액/전체 집단 구매 총금액) / (각 집단의 인원 수/ 전체 인원수 )
   * 전반적으로 나이대가 높고, 소득구간이 높은 고객들이 소비금액이 컸다.


```python
## 각 집단별 구매 금액 비율
buy_ratio_table = customer_buy.groupby(by=['income_rank', 'gender', 'age_units10']).sum()['total_buy'].unstack('age_units10')/total_buy
## 각 집단별 인원수 비율
people_ratio_table = profile.groupby(by=['income_rank', 'gender', 'age_units10' ]).count()['person_id'].unstack('age_units10')/len(profile)
## 각 집단별 인원수 대비 구매 금액.
ratio = buy_ratio_table/people_ratio_table

plt.figure(figsize=(10, 10))
sns.heatmap(ratio,
           cmap='Greens', annot=True, fmt='f', linewidths=0.5)
```




    <AxesSubplot:xlabel='age_units10', ylabel='income_rank-gender'>




    
![png](output_199_1.png)
    


## 향후 프로모션 전략 제안

**고객 거래 데이터중 promotion 부분을 활용하여 어떤 프로모션이 매력적인지 파악해보고, 프로모션에 잘 참여하는 고객층을 파악해보자.**

### 총 순 수익 관점에서 우수한 프로모션
**어떤 프로모션이 `총 순 수익`관점에서 우수한가?**


```python
promotion = final2[final2['group']!='amount'].copy()
```


```python
promotion
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>became_member_on</th>
      <th>income</th>
      <th>age_units10</th>
      <th>age_units5</th>
      <th>join_year</th>
      <th>join_month</th>
      <th>join_day</th>
      <th>now</th>
      <th>join_period</th>
      <th>event</th>
      <th>time</th>
      <th>group</th>
      <th>offer_id</th>
      <th>day</th>
      <th>week</th>
      <th>time_korea</th>
      <th>reward</th>
      <th>channels</th>
      <th>difficulty</th>
      <th>duration</th>
      <th>offer_type</th>
      <th>email</th>
      <th>web</th>
      <th>mobile</th>
      <th>social</th>
      <th>channel_num</th>
      <th>r_minus_d</th>
      <th>income_rank</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>40</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>offer received</td>
      <td>408</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>17</td>
      <td>2</td>
      <td>자정</td>
      <td>5.0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>income_1th</td>
    </tr>
    <tr>
      <th>41</th>
      <td>F</td>
      <td>55</td>
      <td>0610b48642</td>
      <td>2017-07-15</td>
      <td>112000.0</td>
      <td>50</td>
      <td>55</td>
      <td>2017</td>
      <td>7</td>
      <td>15</td>
      <td>2021-06-21</td>
      <td>1437</td>
      <td>offer completed</td>
      <td>528</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>22</td>
      <td>3</td>
      <td>자정</td>
      <td>5.0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>income_1th</td>
    </tr>
    <tr>
      <th>42</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
      <td>offer received</td>
      <td>0</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>0</td>
      <td>0</td>
      <td>자정</td>
      <td>5.0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>income_2th</td>
    </tr>
    <tr>
      <th>43</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
      <td>offer viewed</td>
      <td>6</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>0</td>
      <td>0</td>
      <td>오전6시</td>
      <td>5.0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>income_2th</td>
    </tr>
    <tr>
      <th>44</th>
      <td>F</td>
      <td>75</td>
      <td>78afa99579</td>
      <td>2017-05-09</td>
      <td>100000.0</td>
      <td>70</td>
      <td>75</td>
      <td>2017</td>
      <td>5</td>
      <td>9</td>
      <td>2021-06-21</td>
      <td>1504</td>
      <td>offer completed</td>
      <td>132</td>
      <td>offer id</td>
      <td>9b98b8c7a3</td>
      <td>5</td>
      <td>0</td>
      <td>정오</td>
      <td>5.0</td>
      <td>['web', 'email', 'mobile']</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>income_2th</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>149565</th>
      <td>F</td>
      <td>45</td>
      <td>6d5f3a774f</td>
      <td>2018-06-04</td>
      <td>54000.0</td>
      <td>40</td>
      <td>45</td>
      <td>2018</td>
      <td>6</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1113</td>
      <td>offer received</td>
      <td>336</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>14</td>
      <td>2</td>
      <td>자정</td>
      <td>10.0</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>income_3th</td>
    </tr>
    <tr>
      <th>149566</th>
      <td>F</td>
      <td>45</td>
      <td>6d5f3a774f</td>
      <td>2018-06-04</td>
      <td>54000.0</td>
      <td>40</td>
      <td>45</td>
      <td>2018</td>
      <td>6</td>
      <td>4</td>
      <td>2021-06-21</td>
      <td>1113</td>
      <td>offer viewed</td>
      <td>402</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>16</td>
      <td>2</td>
      <td>오후6시</td>
      <td>10.0</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>income_3th</td>
    </tr>
    <tr>
      <th>149567</th>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>50000.0</td>
      <td>80</td>
      <td>80</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
      <td>2021-06-21</td>
      <td>1932</td>
      <td>offer received</td>
      <td>336</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>14</td>
      <td>2</td>
      <td>자정</td>
      <td>10.0</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>income_4th</td>
    </tr>
    <tr>
      <th>149568</th>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>50000.0</td>
      <td>80</td>
      <td>80</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
      <td>2021-06-21</td>
      <td>1932</td>
      <td>offer viewed</td>
      <td>342</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>14</td>
      <td>2</td>
      <td>오전6시</td>
      <td>10.0</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>income_4th</td>
    </tr>
    <tr>
      <th>149569</th>
      <td>F</td>
      <td>83</td>
      <td>9dc1421481</td>
      <td>2016-03-07</td>
      <td>50000.0</td>
      <td>80</td>
      <td>80</td>
      <td>2016</td>
      <td>3</td>
      <td>7</td>
      <td>2021-06-21</td>
      <td>1932</td>
      <td>offer completed</td>
      <td>360</td>
      <td>offer id</td>
      <td>4d5c57ea9a</td>
      <td>15</td>
      <td>2</td>
      <td>자정</td>
      <td>10.0</td>
      <td>['web', 'email', 'mobile', 'social']</td>
      <td>10.0</td>
      <td>5.0</td>
      <td>bogo</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>income_4th</td>
    </tr>
  </tbody>
</table>
<p>148805 rows × 31 columns</p>
</div>




```python
cols = ['gender', 'age', 'person_id', 'age_units10', 'join_year', 'event', 'group', 'offer_id', 'reward', 'difficulty', 'r_minus_d', 'duration', 'offer_type']
promotion= promotion[cols].copy()
promotion.sample(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>age</th>
      <th>person_id</th>
      <th>age_units10</th>
      <th>join_year</th>
      <th>event</th>
      <th>group</th>
      <th>offer_id</th>
      <th>reward</th>
      <th>difficulty</th>
      <th>r_minus_d</th>
      <th>duration</th>
      <th>offer_type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>43410</th>
      <td>M</td>
      <td>66</td>
      <td>b27c2e80e2</td>
      <td>60</td>
      <td>2016</td>
      <td>offer completed</td>
      <td>offer id</td>
      <td>ae264e3637</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>bogo</td>
    </tr>
    <tr>
      <th>130225</th>
      <td>M</td>
      <td>66</td>
      <td>9a6c9d73cc</td>
      <td>60</td>
      <td>2018</td>
      <td>offer received</td>
      <td>offer id</td>
      <td>0b1e1539f2</td>
      <td>5.0</td>
      <td>20.0</td>
      <td>-15.0</td>
      <td>10.0</td>
      <td>discount</td>
    </tr>
    <tr>
      <th>111760</th>
      <td>F</td>
      <td>53</td>
      <td>6951ddadd1</td>
      <td>50</td>
      <td>2018</td>
      <td>offer viewed</td>
      <td>offer id</td>
      <td>2298d6c36e</td>
      <td>3.0</td>
      <td>7.0</td>
      <td>-4.0</td>
      <td>7.0</td>
      <td>discount</td>
    </tr>
  </tbody>
</table>
</div>



* event
    - **`offer received`** : difficulty를 지불하고 bogo 쿠폰 및 할인권을 지급받음
    - **`offer completed`** : 쿠폰 및 할인권을 사용함.(reward)를 받음.
    - **`offer view`** : 이 정보는 분석에 제외한다.

* offer_type
    - **`informational`** : 정보성 프로모션, 총 순수익과 관련이 없으므로 제거한다.


* profit(순이익) : difficulty - reward

* **`total_difficulty(총 이익)`** = **`difficulty * offer_received`**
* **`total_reward(총 지출)`** = **`total_reward * offer_completed`**
* **`total_profit(총 순이익)`** = **`total_difficulty - total_reward`** = **`(difficulty * offer_received) - (total_reward * offer_completed)`**


```python
promotion = promotion[promotion['offer_type']!='informational']
promotion = promotion[promotion['event']!='offer viewed']
promotion['event'].value_counts()
promotion.groupby(by=['offer_id','offer_type', 'event']).count()['person_id'].unstack('event').plot.bar()
```




    <AxesSubplot:xlabel='offer_id,offer_type'>




    
![png](output_206_1.png)
    


**offer received와 offer completed로 나누기**


```python
promotion_received  = promotion[promotion['event']=='offer received']
promotion_completed  = promotion[promotion['event']=='offer completed']
```


```python
total_difficulty = promotion_received.groupby(by=['offer_id']).sum()['difficulty']
total_reward = promotion_completed.groupby(by=['offer_id']).sum()['reward']

total = pd.DataFrame([total_difficulty, total_reward]).T
total.columns = ['total_difficulty', 'total_reward']
total['total_profit'] = total['total_difficulty'] - total['total_reward']
```

**portfoilo 데이터와 병합**

* **completed_count** : 쿠폰을 사용당한 숫자
* **received_count** : 쿠폰을 지급한 숫자
* **completed_ratio(%)** : 쿠폰을 받고, 쿠폰을 사용한 비율 


```python
result = pd.merge(portfolio, total, left_on='offer_id', right_index=True)
result = result[['offer_id', 'offer_type', 'difficulty', 'reward', 'total_difficulty', 'total_reward', 'total_profit', 'duration']]

result['receive_count'] = result['total_difficulty']/result['difficulty']
result['completed_count'] = result['total_reward']/result['reward']
result['completed_ratio(%)'] = (result['completed_count']/result['receive_count']*100).round(2)
result_sort = result.sort_values('total_profit', ascending=False).set_index(['offer_id', 'offer_type'])
result_sort
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>difficulty</th>
      <th>reward</th>
      <th>total_difficulty</th>
      <th>total_reward</th>
      <th>total_profit</th>
      <th>duration</th>
      <th>receive_count</th>
      <th>completed_count</th>
      <th>completed_ratio(%)</th>
    </tr>
    <tr>
      <th>offer_id</th>
      <th>offer_type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0b1e1539f2</th>
      <th>discount</th>
      <td>20</td>
      <td>5</td>
      <td>134520.0</td>
      <td>16930.0</td>
      <td>117590.0</td>
      <td>10</td>
      <td>6726.0</td>
      <td>3386.0</td>
      <td>50.34</td>
    </tr>
    <tr>
      <th>2906b810c7</th>
      <th>discount</th>
      <td>10</td>
      <td>2</td>
      <td>66310.0</td>
      <td>7822.0</td>
      <td>58488.0</td>
      <td>7</td>
      <td>6631.0</td>
      <td>3911.0</td>
      <td>58.98</td>
    </tr>
    <tr>
      <th>fafdcd668e</th>
      <th>discount</th>
      <td>10</td>
      <td>2</td>
      <td>66520.0</td>
      <td>10006.0</td>
      <td>56514.0</td>
      <td>10</td>
      <td>6652.0</td>
      <td>5003.0</td>
      <td>75.21</td>
    </tr>
    <tr>
      <th>4d5c57ea9a</th>
      <th>bogo</th>
      <td>10</td>
      <td>10</td>
      <td>65930.0</td>
      <td>33100.0</td>
      <td>32830.0</td>
      <td>5</td>
      <td>6593.0</td>
      <td>3310.0</td>
      <td>50.20</td>
    </tr>
    <tr>
      <th>2298d6c36e</th>
      <th>discount</th>
      <td>7</td>
      <td>3</td>
      <td>46585.0</td>
      <td>14658.0</td>
      <td>31927.0</td>
      <td>7</td>
      <td>6655.0</td>
      <td>4886.0</td>
      <td>73.42</td>
    </tr>
    <tr>
      <th>ae264e3637</th>
      <th>bogo</th>
      <td>10</td>
      <td>10</td>
      <td>66830.0</td>
      <td>36570.0</td>
      <td>30260.0</td>
      <td>7</td>
      <td>6683.0</td>
      <td>3657.0</td>
      <td>54.72</td>
    </tr>
    <tr>
      <th>9b98b8c7a3</th>
      <th>bogo</th>
      <td>5</td>
      <td>5</td>
      <td>33425.0</td>
      <td>20940.0</td>
      <td>12485.0</td>
      <td>7</td>
      <td>6685.0</td>
      <td>4188.0</td>
      <td>62.65</td>
    </tr>
    <tr>
      <th>f19421c1d4</th>
      <th>bogo</th>
      <td>5</td>
      <td>5</td>
      <td>32880.0</td>
      <td>20515.0</td>
      <td>12365.0</td>
      <td>5</td>
      <td>6576.0</td>
      <td>4103.0</td>
      <td>62.39</td>
    </tr>
  </tbody>
</table>
</div>




```python
result_sort.to_csv('result_sort.csv')
```


```python
pd.read_csv('result_sort.csv')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>offer_id</th>
      <th>offer_type</th>
      <th>difficulty</th>
      <th>reward</th>
      <th>total_difficulty</th>
      <th>total_reward</th>
      <th>total_profit</th>
      <th>duration</th>
      <th>receive_count</th>
      <th>completed_count</th>
      <th>completed_ratio(%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0b1e1539f2</td>
      <td>discount</td>
      <td>20</td>
      <td>5</td>
      <td>134520.0</td>
      <td>16930.0</td>
      <td>117590.0</td>
      <td>10</td>
      <td>6726.0</td>
      <td>3386.0</td>
      <td>50.34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2906b810c7</td>
      <td>discount</td>
      <td>10</td>
      <td>2</td>
      <td>66310.0</td>
      <td>7822.0</td>
      <td>58488.0</td>
      <td>7</td>
      <td>6631.0</td>
      <td>3911.0</td>
      <td>58.98</td>
    </tr>
    <tr>
      <th>2</th>
      <td>fafdcd668e</td>
      <td>discount</td>
      <td>10</td>
      <td>2</td>
      <td>66520.0</td>
      <td>10006.0</td>
      <td>56514.0</td>
      <td>10</td>
      <td>6652.0</td>
      <td>5003.0</td>
      <td>75.21</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4d5c57ea9a</td>
      <td>bogo</td>
      <td>10</td>
      <td>10</td>
      <td>65930.0</td>
      <td>33100.0</td>
      <td>32830.0</td>
      <td>5</td>
      <td>6593.0</td>
      <td>3310.0</td>
      <td>50.20</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2298d6c36e</td>
      <td>discount</td>
      <td>7</td>
      <td>3</td>
      <td>46585.0</td>
      <td>14658.0</td>
      <td>31927.0</td>
      <td>7</td>
      <td>6655.0</td>
      <td>4886.0</td>
      <td>73.42</td>
    </tr>
    <tr>
      <th>5</th>
      <td>ae264e3637</td>
      <td>bogo</td>
      <td>10</td>
      <td>10</td>
      <td>66830.0</td>
      <td>36570.0</td>
      <td>30260.0</td>
      <td>7</td>
      <td>6683.0</td>
      <td>3657.0</td>
      <td>54.72</td>
    </tr>
    <tr>
      <th>6</th>
      <td>9b98b8c7a3</td>
      <td>bogo</td>
      <td>5</td>
      <td>5</td>
      <td>33425.0</td>
      <td>20940.0</td>
      <td>12485.0</td>
      <td>7</td>
      <td>6685.0</td>
      <td>4188.0</td>
      <td>62.65</td>
    </tr>
    <tr>
      <th>7</th>
      <td>f19421c1d4</td>
      <td>bogo</td>
      <td>5</td>
      <td>5</td>
      <td>32880.0</td>
      <td>20515.0</td>
      <td>12365.0</td>
      <td>5</td>
      <td>6576.0</td>
      <td>4103.0</td>
      <td>62.39</td>
    </tr>
  </tbody>
</table>
</div>




```python

```

#### (결론) 총 순수익이 우수한 프로모션

* 각 프로모션을 참여(received)된 횟수는 비슷하다. 하지만 실제 쿠폰을 사용한 것은 discount가 더 많다. 
* bogo 전략보다, discount 전략이 총 수익 관점에서 좋다.


```python
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(13,5))

result_sort['total_profit'].plot.bar(ax= axes[0], title ='총 순이익(달러)', color ='grey')
result_sort[['completed_count', 'receive_count']].plot.bar(ax= axes[1], title ='쿠폰 지급 및 사용')
result_sort['completed_ratio(%)'].plot.bar(ax= axes[2], title ='쿠폰 사용 비율', color ='green')
```




    <AxesSubplot:title={'center':'쿠폰 사용 비율'}, xlabel='offer_id,offer_type'>




    
![png](output_216_1.png)
    


* reward가 클 수록 completed_ratio가 감소하는 경향을 보였다. (상관관계 -0.69)
* 0b1e1539f2이 프로모션이 총 수익 관점에서 좋다.
    - 각 프로모션의 참여 빈도가 비슷하며, difficulty가 큼과 동시에 reward 사용 빈도가 적은 것이 total profit에 일조한 것으로 보인다.

#### 총 수익 관점에서 프로모션 제안 
* 총 수익 관점에서 향후 프로모션을 진행할 때 discount전략을 사용하고, reward를 증가시키더라도 difficulty를 높히는 프로모션을 추천한다.


```python
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(13,5))
axes[1] = plt.scatter(x=result_sort['reward'], y = result_sort['completed_ratio(%)'], color ='g')
sns.heatmap(result_sort.corr(),cmap='Greens', ax=axes[0], annot=True, linewidths=2)

```




    <AxesSubplot:>




    
![png](output_218_1.png)
    



```python
sns.heatmap(result_sort[['difficulty','reward', 'total_profit', 'duration','completed_ratio(%)']].corr(),cmap='Greens', annot=True, linewidths=2)
```




    <AxesSubplot:>




    
![png](output_219_1.png)
    


### 주력 고객층이 선호하는 프로모션 전략을 파악해보자

* 주력 고객층 선정
    - 대집단 : 전체 고객중 44%를 차지하며 47.9%의 매출을 올리고 있는 **50대, 60대 고객**을 스타벅스의 주력 고객으로 선정하자.
    - 소집단 : 전체 고객 중 19.6% 차지하며 24.8%의 매출을 올리고 있는 **50대, 60대 여성**을 주력고객으로 지정하자.

**소집단 : 전체 고객 중 19.6% 차지하며 24.8%의 매출을 올리고 있는 `50대, 60대 여성`을 주력고객으로 지정하자.**


```python
female = (promotion['gender']=='F')
age_50_60 = (promotion['age_units10'].isin([50, 60]))

small_group = promotion.loc[female&age_50_60]
f_50_60 = small_group.groupby(by=['offer_id','event']).count()['person_id'].unstack('event')
f_50_60.style.background_gradient(cmap ='Greens', subset='offer received')
```




<style  type="text/css" >
#T_bc1cc_row0_col1{
            background-color:  #208843;
            color:  #000000;
        }#T_bc1cc_row1_col1,#T_bc1cc_row6_col1{
            background-color:  #daf0d4;
            color:  #000000;
        }#T_bc1cc_row2_col1{
            background-color:  #b0dfaa;
            color:  #000000;
        }#T_bc1cc_row3_col1{
            background-color:  #f7fcf5;
            color:  #000000;
        }#T_bc1cc_row4_col1{
            background-color:  #acdea6;
            color:  #000000;
        }#T_bc1cc_row5_col1{
            background-color:  #cfecc9;
            color:  #000000;
        }#T_bc1cc_row7_col1{
            background-color:  #00441b;
            color:  #f1f1f1;
        }</style><table id="T_bc1cc_" ><thead>    <tr>        <th class="index_name level0" >event</th>        <th class="col_heading level0 col0" >offer completed</th>        <th class="col_heading level0 col1" >offer received</th>    </tr>    <tr>        <th class="index_name level0" >offer_id</th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_bc1cc_level0_row0" class="row_heading level0 row0" >0b1e1539f2</th>
                        <td id="T_bc1cc_row0_col0" class="data row0 col0" >858</td>
                        <td id="T_bc1cc_row0_col1" class="data row0 col1" >1335</td>
            </tr>
            <tr>
                        <th id="T_bc1cc_level0_row1" class="row_heading level0 row1" >2298d6c36e</th>
                        <td id="T_bc1cc_row1_col0" class="data row1 col0" >1049</td>
                        <td id="T_bc1cc_row1_col1" class="data row1 col1" >1281</td>
            </tr>
            <tr>
                        <th id="T_bc1cc_level0_row2" class="row_heading level0 row2" >2906b810c7</th>
                        <td id="T_bc1cc_row2_col0" class="data row2 col0" >912</td>
                        <td id="T_bc1cc_row2_col1" class="data row2 col1" >1295</td>
            </tr>
            <tr>
                        <th id="T_bc1cc_level0_row3" class="row_heading level0 row3" >4d5c57ea9a</th>
                        <td id="T_bc1cc_row3_col0" class="data row3 col0" >843</td>
                        <td id="T_bc1cc_row3_col1" class="data row3 col1" >1265</td>
            </tr>
            <tr>
                        <th id="T_bc1cc_level0_row4" class="row_heading level0 row4" >9b98b8c7a3</th>
                        <td id="T_bc1cc_row4_col0" class="data row4 col0" >949</td>
                        <td id="T_bc1cc_row4_col1" class="data row4 col1" >1296</td>
            </tr>
            <tr>
                        <th id="T_bc1cc_level0_row5" class="row_heading level0 row5" >ae264e3637</th>
                        <td id="T_bc1cc_row5_col0" class="data row5 col0" >908</td>
                        <td id="T_bc1cc_row5_col1" class="data row5 col1" >1285</td>
            </tr>
            <tr>
                        <th id="T_bc1cc_level0_row6" class="row_heading level0 row6" >f19421c1d4</th>
                        <td id="T_bc1cc_row6_col0" class="data row6 col0" >917</td>
                        <td id="T_bc1cc_row6_col1" class="data row6 col1" >1281</td>
            </tr>
            <tr>
                        <th id="T_bc1cc_level0_row7" class="row_heading level0 row7" >fafdcd668e</th>
                        <td id="T_bc1cc_row7_col0" class="data row7 col0" >1130</td>
                        <td id="T_bc1cc_row7_col1" class="data row7 col1" >1357</td>
            </tr>
    </tbody></table>




```python
f_50_60.to_csv('f_50_60.csv')
```


```python
pd.read_csv('f_50_60.csv')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>offer_id</th>
      <th>offer completed</th>
      <th>offer received</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0b1e1539f2</td>
      <td>858</td>
      <td>1335</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2298d6c36e</td>
      <td>1049</td>
      <td>1281</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2906b810c7</td>
      <td>912</td>
      <td>1295</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4d5c57ea9a</td>
      <td>843</td>
      <td>1265</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9b98b8c7a3</td>
      <td>949</td>
      <td>1296</td>
    </tr>
    <tr>
      <th>5</th>
      <td>ae264e3637</td>
      <td>908</td>
      <td>1285</td>
    </tr>
    <tr>
      <th>6</th>
      <td>f19421c1d4</td>
      <td>917</td>
      <td>1281</td>
    </tr>
    <tr>
      <th>7</th>
      <td>fafdcd668e</td>
      <td>1130</td>
      <td>1357</td>
    </tr>
  </tbody>
</table>
</div>



#### (소집단 : 결론) 주력고객(50대 ~ 60대 여성)은 모든 프로모션에 골고루 참여하지만, 그나마 선호하는 프로모션은 discount 프로모션(fafdcd668e, 0b1e1539f2)이다.


```python
cols = ['offer_id', 'offer_type', 'difficulty', 'reward', 'duration']
result = pd.merge(portfolio[cols], f_50_60, left_on = 'offer_id', right_index=True).sort_values(by = 'offer received', ascending=False)
result.style.background_gradient(cmap ='Greens', subset='offer received')
```




<style  type="text/css" >
#T_a6ef5_row0_col6{
            background-color:  #00441b;
            color:  #f1f1f1;
        }#T_a6ef5_row1_col6{
            background-color:  #208843;
            color:  #000000;
        }#T_a6ef5_row2_col6{
            background-color:  #acdea6;
            color:  #000000;
        }#T_a6ef5_row3_col6{
            background-color:  #b0dfaa;
            color:  #000000;
        }#T_a6ef5_row4_col6{
            background-color:  #cfecc9;
            color:  #000000;
        }#T_a6ef5_row5_col6,#T_a6ef5_row6_col6{
            background-color:  #daf0d4;
            color:  #000000;
        }#T_a6ef5_row7_col6{
            background-color:  #f7fcf5;
            color:  #000000;
        }</style><table id="T_a6ef5_" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >offer_id</th>        <th class="col_heading level0 col1" >offer_type</th>        <th class="col_heading level0 col2" >difficulty</th>        <th class="col_heading level0 col3" >reward</th>        <th class="col_heading level0 col4" >duration</th>        <th class="col_heading level0 col5" >offer completed</th>        <th class="col_heading level0 col6" >offer received</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_a6ef5_level0_row0" class="row_heading level0 row0" >6</th>
                        <td id="T_a6ef5_row0_col0" class="data row0 col0" >fafdcd668e</td>
                        <td id="T_a6ef5_row0_col1" class="data row0 col1" >discount</td>
                        <td id="T_a6ef5_row0_col2" class="data row0 col2" >10</td>
                        <td id="T_a6ef5_row0_col3" class="data row0 col3" >2</td>
                        <td id="T_a6ef5_row0_col4" class="data row0 col4" >10</td>
                        <td id="T_a6ef5_row0_col5" class="data row0 col5" >1130</td>
                        <td id="T_a6ef5_row0_col6" class="data row0 col6" >1357</td>
            </tr>
            <tr>
                        <th id="T_a6ef5_level0_row1" class="row_heading level0 row1" >4</th>
                        <td id="T_a6ef5_row1_col0" class="data row1 col0" >0b1e1539f2</td>
                        <td id="T_a6ef5_row1_col1" class="data row1 col1" >discount</td>
                        <td id="T_a6ef5_row1_col2" class="data row1 col2" >20</td>
                        <td id="T_a6ef5_row1_col3" class="data row1 col3" >5</td>
                        <td id="T_a6ef5_row1_col4" class="data row1 col4" >10</td>
                        <td id="T_a6ef5_row1_col5" class="data row1 col5" >858</td>
                        <td id="T_a6ef5_row1_col6" class="data row1 col6" >1335</td>
            </tr>
            <tr>
                        <th id="T_a6ef5_level0_row2" class="row_heading level0 row2" >3</th>
                        <td id="T_a6ef5_row2_col0" class="data row2 col0" >9b98b8c7a3</td>
                        <td id="T_a6ef5_row2_col1" class="data row2 col1" >bogo</td>
                        <td id="T_a6ef5_row2_col2" class="data row2 col2" >5</td>
                        <td id="T_a6ef5_row2_col3" class="data row2 col3" >5</td>
                        <td id="T_a6ef5_row2_col4" class="data row2 col4" >7</td>
                        <td id="T_a6ef5_row2_col5" class="data row2 col5" >949</td>
                        <td id="T_a6ef5_row2_col6" class="data row2 col6" >1296</td>
            </tr>
            <tr>
                        <th id="T_a6ef5_level0_row3" class="row_heading level0 row3" >9</th>
                        <td id="T_a6ef5_row3_col0" class="data row3 col0" >2906b810c7</td>
                        <td id="T_a6ef5_row3_col1" class="data row3 col1" >discount</td>
                        <td id="T_a6ef5_row3_col2" class="data row3 col2" >10</td>
                        <td id="T_a6ef5_row3_col3" class="data row3 col3" >2</td>
                        <td id="T_a6ef5_row3_col4" class="data row3 col4" >7</td>
                        <td id="T_a6ef5_row3_col5" class="data row3 col5" >912</td>
                        <td id="T_a6ef5_row3_col6" class="data row3 col6" >1295</td>
            </tr>
            <tr>
                        <th id="T_a6ef5_level0_row4" class="row_heading level0 row4" >0</th>
                        <td id="T_a6ef5_row4_col0" class="data row4 col0" >ae264e3637</td>
                        <td id="T_a6ef5_row4_col1" class="data row4 col1" >bogo</td>
                        <td id="T_a6ef5_row4_col2" class="data row4 col2" >10</td>
                        <td id="T_a6ef5_row4_col3" class="data row4 col3" >10</td>
                        <td id="T_a6ef5_row4_col4" class="data row4 col4" >7</td>
                        <td id="T_a6ef5_row4_col5" class="data row4 col5" >908</td>
                        <td id="T_a6ef5_row4_col6" class="data row4 col6" >1285</td>
            </tr>
            <tr>
                        <th id="T_a6ef5_level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_a6ef5_row5_col0" class="data row5 col0" >2298d6c36e</td>
                        <td id="T_a6ef5_row5_col1" class="data row5 col1" >discount</td>
                        <td id="T_a6ef5_row5_col2" class="data row5 col2" >7</td>
                        <td id="T_a6ef5_row5_col3" class="data row5 col3" >3</td>
                        <td id="T_a6ef5_row5_col4" class="data row5 col4" >7</td>
                        <td id="T_a6ef5_row5_col5" class="data row5 col5" >1049</td>
                        <td id="T_a6ef5_row5_col6" class="data row5 col6" >1281</td>
            </tr>
            <tr>
                        <th id="T_a6ef5_level0_row6" class="row_heading level0 row6" >8</th>
                        <td id="T_a6ef5_row6_col0" class="data row6 col0" >f19421c1d4</td>
                        <td id="T_a6ef5_row6_col1" class="data row6 col1" >bogo</td>
                        <td id="T_a6ef5_row6_col2" class="data row6 col2" >5</td>
                        <td id="T_a6ef5_row6_col3" class="data row6 col3" >5</td>
                        <td id="T_a6ef5_row6_col4" class="data row6 col4" >5</td>
                        <td id="T_a6ef5_row6_col5" class="data row6 col5" >917</td>
                        <td id="T_a6ef5_row6_col6" class="data row6 col6" >1281</td>
            </tr>
            <tr>
                        <th id="T_a6ef5_level0_row7" class="row_heading level0 row7" >1</th>
                        <td id="T_a6ef5_row7_col0" class="data row7 col0" >4d5c57ea9a</td>
                        <td id="T_a6ef5_row7_col1" class="data row7 col1" >bogo</td>
                        <td id="T_a6ef5_row7_col2" class="data row7 col2" >10</td>
                        <td id="T_a6ef5_row7_col3" class="data row7 col3" >10</td>
                        <td id="T_a6ef5_row7_col4" class="data row7 col4" >5</td>
                        <td id="T_a6ef5_row7_col5" class="data row7 col5" >843</td>
                        <td id="T_a6ef5_row7_col6" class="data row7 col6" >1265</td>
            </tr>
    </tbody></table>



**대집단 : 전체 고객중 44%를 차지하며 47.9%의 매출을 올리고 있는 `50대, 60대 고객`을 스타벅스의 주력 고객으로 선정하자.**


```python
age_50_60 = (promotion['age_units10'].isin([50, 60]))

big_group = promotion.loc[age_50_60]
age_50_60 = big_group.groupby(by=['offer_id','event']).count()['person_id'].unstack('event')
age_50_60.style.background_gradient(cmap ='Greens', subset='offer received')
```




<style  type="text/css" >
#T_78d78_row0_col1{
            background-color:  #00441b;
            color:  #f1f1f1;
        }#T_78d78_row1_col1{
            background-color:  #d6efd0;
            color:  #000000;
        }#T_78d78_row2_col1{
            background-color:  #58b668;
            color:  #000000;
        }#T_78d78_row3_col1{
            background-color:  #f7fcf5;
            color:  #000000;
        }#T_78d78_row4_col1{
            background-color:  #258d47;
            color:  #000000;
        }#T_78d78_row5_col1{
            background-color:  #73c476;
            color:  #000000;
        }#T_78d78_row6_col1{
            background-color:  #f3faf0;
            color:  #000000;
        }#T_78d78_row7_col1{
            background-color:  #127c39;
            color:  #f1f1f1;
        }</style><table id="T_78d78_" ><thead>    <tr>        <th class="index_name level0" >event</th>        <th class="col_heading level0 col0" >offer completed</th>        <th class="col_heading level0 col1" >offer received</th>    </tr>    <tr>        <th class="index_name level0" >offer_id</th>        <th class="blank" ></th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_78d78_level0_row0" class="row_heading level0 row0" >0b1e1539f2</th>
                        <td id="T_78d78_row0_col0" class="data row0 col0" >1645</td>
                        <td id="T_78d78_row0_col1" class="data row0 col1" >2986</td>
            </tr>
            <tr>
                        <th id="T_78d78_level0_row1" class="row_heading level0 row1" >2298d6c36e</th>
                        <td id="T_78d78_row1_col0" class="data row1 col0" >2166</td>
                        <td id="T_78d78_row1_col1" class="data row1 col1" >2905</td>
            </tr>
            <tr>
                        <th id="T_78d78_level0_row2" class="row_heading level0 row2" >2906b810c7</th>
                        <td id="T_78d78_row2_col0" class="data row2 col0" >1883</td>
                        <td id="T_78d78_row2_col1" class="data row2 col1" >2943</td>
            </tr>
            <tr>
                        <th id="T_78d78_level0_row3" class="row_heading level0 row3" >4d5c57ea9a</th>
                        <td id="T_78d78_row3_col0" class="data row3 col0" >1597</td>
                        <td id="T_78d78_row3_col1" class="data row3 col1" >2886</td>
            </tr>
            <tr>
                        <th id="T_78d78_level0_row4" class="row_heading level0 row4" >9b98b8c7a3</th>
                        <td id="T_78d78_row4_col0" class="data row4 col0" >1918</td>
                        <td id="T_78d78_row4_col1" class="data row4 col1" >2960</td>
            </tr>
            <tr>
                        <th id="T_78d78_level0_row5" class="row_heading level0 row5" >ae264e3637</th>
                        <td id="T_78d78_row5_col0" class="data row5 col0" >1754</td>
                        <td id="T_78d78_row5_col1" class="data row5 col1" >2936</td>
            </tr>
            <tr>
                        <th id="T_78d78_level0_row6" class="row_heading level0 row6" >f19421c1d4</th>
                        <td id="T_78d78_row6_col0" class="data row6 col0" >1906</td>
                        <td id="T_78d78_row6_col1" class="data row6 col1" >2889</td>
            </tr>
            <tr>
                        <th id="T_78d78_level0_row7" class="row_heading level0 row7" >fafdcd668e</th>
                        <td id="T_78d78_row7_col0" class="data row7 col0" >2317</td>
                        <td id="T_78d78_row7_col1" class="data row7 col1" >2967</td>
            </tr>
    </tbody></table>




```python
age_50_60.to_csv('age_50_60.csv')
pd.read_csv ('age_50_60.csv')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>offer_id</th>
      <th>offer completed</th>
      <th>offer received</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0b1e1539f2</td>
      <td>1645</td>
      <td>2986</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2298d6c36e</td>
      <td>2166</td>
      <td>2905</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2906b810c7</td>
      <td>1883</td>
      <td>2943</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4d5c57ea9a</td>
      <td>1597</td>
      <td>2886</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9b98b8c7a3</td>
      <td>1918</td>
      <td>2960</td>
    </tr>
    <tr>
      <th>5</th>
      <td>ae264e3637</td>
      <td>1754</td>
      <td>2936</td>
    </tr>
    <tr>
      <th>6</th>
      <td>f19421c1d4</td>
      <td>1906</td>
      <td>2889</td>
    </tr>
    <tr>
      <th>7</th>
      <td>fafdcd668e</td>
      <td>2317</td>
      <td>2967</td>
    </tr>
  </tbody>
</table>
</div>




```python
cols = ['offer_id', 'offer_type', 'difficulty', 'reward', 'duration']
result = pd.merge(portfolio[cols], age_50_60, left_on = 'offer_id', right_index=True).sort_values(by = 'offer received', ascending=False)
result.style.background_gradient(cmap ='Greens', subset='offer received')
```




<style  type="text/css" >
#T_09383_row0_col6{
            background-color:  #00441b;
            color:  #f1f1f1;
        }#T_09383_row1_col6{
            background-color:  #127c39;
            color:  #f1f1f1;
        }#T_09383_row2_col6{
            background-color:  #258d47;
            color:  #000000;
        }#T_09383_row3_col6{
            background-color:  #58b668;
            color:  #000000;
        }#T_09383_row4_col6{
            background-color:  #73c476;
            color:  #000000;
        }#T_09383_row5_col6{
            background-color:  #d6efd0;
            color:  #000000;
        }#T_09383_row6_col6{
            background-color:  #f3faf0;
            color:  #000000;
        }#T_09383_row7_col6{
            background-color:  #f7fcf5;
            color:  #000000;
        }</style><table id="T_09383_" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >offer_id</th>        <th class="col_heading level0 col1" >offer_type</th>        <th class="col_heading level0 col2" >difficulty</th>        <th class="col_heading level0 col3" >reward</th>        <th class="col_heading level0 col4" >duration</th>        <th class="col_heading level0 col5" >offer completed</th>        <th class="col_heading level0 col6" >offer received</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_09383_level0_row0" class="row_heading level0 row0" >4</th>
                        <td id="T_09383_row0_col0" class="data row0 col0" >0b1e1539f2</td>
                        <td id="T_09383_row0_col1" class="data row0 col1" >discount</td>
                        <td id="T_09383_row0_col2" class="data row0 col2" >20</td>
                        <td id="T_09383_row0_col3" class="data row0 col3" >5</td>
                        <td id="T_09383_row0_col4" class="data row0 col4" >10</td>
                        <td id="T_09383_row0_col5" class="data row0 col5" >1645</td>
                        <td id="T_09383_row0_col6" class="data row0 col6" >2986</td>
            </tr>
            <tr>
                        <th id="T_09383_level0_row1" class="row_heading level0 row1" >6</th>
                        <td id="T_09383_row1_col0" class="data row1 col0" >fafdcd668e</td>
                        <td id="T_09383_row1_col1" class="data row1 col1" >discount</td>
                        <td id="T_09383_row1_col2" class="data row1 col2" >10</td>
                        <td id="T_09383_row1_col3" class="data row1 col3" >2</td>
                        <td id="T_09383_row1_col4" class="data row1 col4" >10</td>
                        <td id="T_09383_row1_col5" class="data row1 col5" >2317</td>
                        <td id="T_09383_row1_col6" class="data row1 col6" >2967</td>
            </tr>
            <tr>
                        <th id="T_09383_level0_row2" class="row_heading level0 row2" >3</th>
                        <td id="T_09383_row2_col0" class="data row2 col0" >9b98b8c7a3</td>
                        <td id="T_09383_row2_col1" class="data row2 col1" >bogo</td>
                        <td id="T_09383_row2_col2" class="data row2 col2" >5</td>
                        <td id="T_09383_row2_col3" class="data row2 col3" >5</td>
                        <td id="T_09383_row2_col4" class="data row2 col4" >7</td>
                        <td id="T_09383_row2_col5" class="data row2 col5" >1918</td>
                        <td id="T_09383_row2_col6" class="data row2 col6" >2960</td>
            </tr>
            <tr>
                        <th id="T_09383_level0_row3" class="row_heading level0 row3" >9</th>
                        <td id="T_09383_row3_col0" class="data row3 col0" >2906b810c7</td>
                        <td id="T_09383_row3_col1" class="data row3 col1" >discount</td>
                        <td id="T_09383_row3_col2" class="data row3 col2" >10</td>
                        <td id="T_09383_row3_col3" class="data row3 col3" >2</td>
                        <td id="T_09383_row3_col4" class="data row3 col4" >7</td>
                        <td id="T_09383_row3_col5" class="data row3 col5" >1883</td>
                        <td id="T_09383_row3_col6" class="data row3 col6" >2943</td>
            </tr>
            <tr>
                        <th id="T_09383_level0_row4" class="row_heading level0 row4" >0</th>
                        <td id="T_09383_row4_col0" class="data row4 col0" >ae264e3637</td>
                        <td id="T_09383_row4_col1" class="data row4 col1" >bogo</td>
                        <td id="T_09383_row4_col2" class="data row4 col2" >10</td>
                        <td id="T_09383_row4_col3" class="data row4 col3" >10</td>
                        <td id="T_09383_row4_col4" class="data row4 col4" >7</td>
                        <td id="T_09383_row4_col5" class="data row4 col5" >1754</td>
                        <td id="T_09383_row4_col6" class="data row4 col6" >2936</td>
            </tr>
            <tr>
                        <th id="T_09383_level0_row5" class="row_heading level0 row5" >5</th>
                        <td id="T_09383_row5_col0" class="data row5 col0" >2298d6c36e</td>
                        <td id="T_09383_row5_col1" class="data row5 col1" >discount</td>
                        <td id="T_09383_row5_col2" class="data row5 col2" >7</td>
                        <td id="T_09383_row5_col3" class="data row5 col3" >3</td>
                        <td id="T_09383_row5_col4" class="data row5 col4" >7</td>
                        <td id="T_09383_row5_col5" class="data row5 col5" >2166</td>
                        <td id="T_09383_row5_col6" class="data row5 col6" >2905</td>
            </tr>
            <tr>
                        <th id="T_09383_level0_row6" class="row_heading level0 row6" >8</th>
                        <td id="T_09383_row6_col0" class="data row6 col0" >f19421c1d4</td>
                        <td id="T_09383_row6_col1" class="data row6 col1" >bogo</td>
                        <td id="T_09383_row6_col2" class="data row6 col2" >5</td>
                        <td id="T_09383_row6_col3" class="data row6 col3" >5</td>
                        <td id="T_09383_row6_col4" class="data row6 col4" >5</td>
                        <td id="T_09383_row6_col5" class="data row6 col5" >1906</td>
                        <td id="T_09383_row6_col6" class="data row6 col6" >2889</td>
            </tr>
            <tr>
                        <th id="T_09383_level0_row7" class="row_heading level0 row7" >1</th>
                        <td id="T_09383_row7_col0" class="data row7 col0" >4d5c57ea9a</td>
                        <td id="T_09383_row7_col1" class="data row7 col1" >bogo</td>
                        <td id="T_09383_row7_col2" class="data row7 col2" >10</td>
                        <td id="T_09383_row7_col3" class="data row7 col3" >10</td>
                        <td id="T_09383_row7_col4" class="data row7 col4" >5</td>
                        <td id="T_09383_row7_col5" class="data row7 col5" >1597</td>
                        <td id="T_09383_row7_col6" class="data row7 col6" >2886</td>
            </tr>
    </tbody></table>



#### (대집단 : 결론) 주력고객(50대 ~ 60대)은 모든 프로모션에 골고루 참여하지만, 그나마 선호하는 프로모션은 discount 프로모션(fafdcd668e, 0b1e1539f2)이다.

#### 주력 고객층은 대집단, 소집단 모두 discount프로모션을 선호하고 그중에 fafdcd668e, 0b1e1539f2 이 프로모션을 공통적으로 선호하는 모습을 보였다. 총 순수익에 영향력을 강하게 행사하는 주력 고객을 위해서 위 프로모션을 추천한다.

------------------
### 신규고객이 선호하는 프로모션 전략을 파악해보자

* **2018년도의 가입한 고객**을 **`신규고객`** 이라고 지정하고. `신규고객`을 유치하기 위해서 프로모션 전략을 반영한다고 할 때. **`신규고객`**이 자주 참여하는 프로모션 전략을 파악해서. 향후에 그 프로모션 전략을 취한다.

#### (주제 정당화 조건) 가입일자가 고객의 프로모션 참여, 거래 빈도에 영향을 주는가?

**가입일자(join_year)별 event 응답 횟수**


```python
B = final2.copy()
result_B = B.groupby(by=['join_year', 'event'])['offer_id'].count().unstack()[['transaction', 'offer received', 'offer completed']]
display(result_B)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>event</th>
      <th>transaction</th>
      <th>offer received</th>
      <th>offer completed</th>
    </tr>
    <tr>
      <th>join_year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013</th>
      <td>3408</td>
      <td>1226</td>
      <td>561</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>8183</td>
      <td>2973</td>
      <td>1321</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>17574</td>
      <td>7150</td>
      <td>4319</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>31167</td>
      <td>13520</td>
      <td>8928</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>44081</td>
      <td>25125</td>
      <td>12119</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>19544</td>
      <td>16507</td>
      <td>5196</td>
    </tr>
  </tbody>
</table>
</div>


**연도별 가입자수**


```python
join_year = B.groupby(by=['join_year'])[['offer_id']].nunique()
display(join_year)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>offer_id</th>
    </tr>
    <tr>
      <th>join_year</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013</th>
      <td>1369</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>2035</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>3640</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>4144</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>4284</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>3465</td>
    </tr>
  </tbody>
</table>
</div>


**연도별 가입자들의 평균 응답 수**


```python
## 각 연도별 거래 빈도를 각 연도별 가입자 수로 나눠준다.
arr_result_B = np.array(result_B)
arr_join_day = np.array(join_year)
arr_div = arr_result_B / arr_join_day

result_div = result_B.copy()

for i in range(result_div.shape[0]) :
    for j in range(result_div.shape[1]) :
        result_div.iloc[i, j] = arr_div[i, j]
result_div['total'] = result_div.sum(axis=1)
result_div
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>event</th>
      <th>transaction</th>
      <th>offer received</th>
      <th>offer completed</th>
      <th>total</th>
    </tr>
    <tr>
      <th>join_year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2013</th>
      <td>2.489408</td>
      <td>0.895544</td>
      <td>0.409788</td>
      <td>3.794741</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>4.021130</td>
      <td>1.460934</td>
      <td>0.649140</td>
      <td>6.131204</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>4.828022</td>
      <td>1.964286</td>
      <td>1.186538</td>
      <td>7.978846</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>7.520994</td>
      <td>3.262548</td>
      <td>2.154440</td>
      <td>12.937983</td>
    </tr>
    <tr>
      <th>2017</th>
      <td>10.289683</td>
      <td>5.864846</td>
      <td>2.828898</td>
      <td>18.983427</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>5.640404</td>
      <td>4.763925</td>
      <td>1.499567</td>
      <td>11.903896</td>
    </tr>
  </tbody>
</table>
</div>



**시각화**


```python
result_B.plot.bar(rot=0, title = '연도별 프로모션&거래 참여 횟수', figsize=(10, 3));
join_year.plot.bar(rot=0, color='green', title = '연도별 가입 고객 수', figsize=(10, 3));
result_div.plot.bar(rot=0,title='연도별 인당 평균 프로모션&거래 참여 횟수', figsize=(10,3));
```


    
![png](output_242_0.png)
    



    
![png](output_242_1.png)
    



    
![png](output_242_2.png)
    


#### (주제 정당화 조건 : 결론) 가입일자가 최근에 가까울 수록 거래 + 프로모션 참여 빈도가 높았다. 

   * 측정일자 2013년 7월 26일 ~ 2018년 7월 26일 

#### 신규 고객이 선호하는 프로모션 전략은 무었인가.


```python
promotion_2018 = promotion[promotion['join_year']==2018]
group_2018 = promotion_2018.groupby(by = 'offer_id').count()[['person_id']]
group_2018 = group_2018.sort_values(by='person_id', ascending=False) 
group_2018.style.background_gradient(cmap ='Greens')
```




<style  type="text/css" >
#T_7ad81_row0_col0{
            background-color:  #00441b;
            color:  #f1f1f1;
        }#T_7ad81_row1_col0{
            background-color:  #005723;
            color:  #f1f1f1;
        }#T_7ad81_row2_col0{
            background-color:  #4bb062;
            color:  #000000;
        }#T_7ad81_row3_col0{
            background-color:  #76c578;
            color:  #000000;
        }#T_7ad81_row4_col0{
            background-color:  #7fc97f;
            color:  #000000;
        }#T_7ad81_row5_col0{
            background-color:  #84cc83;
            color:  #000000;
        }#T_7ad81_row6_col0{
            background-color:  #9cd797;
            color:  #000000;
        }#T_7ad81_row7_col0{
            background-color:  #f7fcf5;
            color:  #000000;
        }</style><table id="T_7ad81_" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >person_id</th>    </tr>    <tr>        <th class="index_name level0" >offer_id</th>        <th class="blank" ></th>    </tr></thead><tbody>
                <tr>
                        <th id="T_7ad81_level0_row0" class="row_heading level0 row0" >fafdcd668e</th>
                        <td id="T_7ad81_row0_col0" class="data row0 col0" >2547</td>
            </tr>
            <tr>
                        <th id="T_7ad81_level0_row1" class="row_heading level0 row1" >2298d6c36e</th>
                        <td id="T_7ad81_row1_col0" class="data row1 col0" >2516</td>
            </tr>
            <tr>
                        <th id="T_7ad81_level0_row2" class="row_heading level0 row2" >9b98b8c7a3</th>
                        <td id="T_7ad81_row2_col0" class="data row2 col0" >2336</td>
            </tr>
            <tr>
                        <th id="T_7ad81_level0_row3" class="row_heading level0 row3" >2906b810c7</th>
                        <td id="T_7ad81_row3_col0" class="data row3 col0" >2281</td>
            </tr>
            <tr>
                        <th id="T_7ad81_level0_row4" class="row_heading level0 row4" >ae264e3637</th>
                        <td id="T_7ad81_row4_col0" class="data row4 col0" >2269</td>
            </tr>
            <tr>
                        <th id="T_7ad81_level0_row5" class="row_heading level0 row5" >f19421c1d4</th>
                        <td id="T_7ad81_row5_col0" class="data row5 col0" >2260</td>
            </tr>
            <tr>
                        <th id="T_7ad81_level0_row6" class="row_heading level0 row6" >0b1e1539f2</th>
                        <td id="T_7ad81_row6_col0" class="data row6 col0" >2225</td>
            </tr>
            <tr>
                        <th id="T_7ad81_level0_row7" class="row_heading level0 row7" >4d5c57ea9a</th>
                        <td id="T_7ad81_row7_col0" class="data row7 col0" >2021</td>
            </tr>
    </tbody></table>




```python
cols = ['offer_id', 'offer_type', 'difficulty', 'reward', 'duration']
result = pd.merge(portfolio[cols], group_2018, left_on = 'offer_id', right_index=True).sort_values(by = 'person_id', ascending=False)
result.style.background_gradient(cmap ='Greens', subset='person_id')
```




<style  type="text/css" >
#T_9150f_row0_col5{
            background-color:  #00441b;
            color:  #f1f1f1;
        }#T_9150f_row1_col5{
            background-color:  #005723;
            color:  #f1f1f1;
        }#T_9150f_row2_col5{
            background-color:  #4bb062;
            color:  #000000;
        }#T_9150f_row3_col5{
            background-color:  #76c578;
            color:  #000000;
        }#T_9150f_row4_col5{
            background-color:  #7fc97f;
            color:  #000000;
        }#T_9150f_row5_col5{
            background-color:  #84cc83;
            color:  #000000;
        }#T_9150f_row6_col5{
            background-color:  #9cd797;
            color:  #000000;
        }#T_9150f_row7_col5{
            background-color:  #f7fcf5;
            color:  #000000;
        }</style><table id="T_9150f_" ><thead>    <tr>        <th class="blank level0" ></th>        <th class="col_heading level0 col0" >offer_id</th>        <th class="col_heading level0 col1" >offer_type</th>        <th class="col_heading level0 col2" >difficulty</th>        <th class="col_heading level0 col3" >reward</th>        <th class="col_heading level0 col4" >duration</th>        <th class="col_heading level0 col5" >person_id</th>    </tr></thead><tbody>
                <tr>
                        <th id="T_9150f_level0_row0" class="row_heading level0 row0" >6</th>
                        <td id="T_9150f_row0_col0" class="data row0 col0" >fafdcd668e</td>
                        <td id="T_9150f_row0_col1" class="data row0 col1" >discount</td>
                        <td id="T_9150f_row0_col2" class="data row0 col2" >10</td>
                        <td id="T_9150f_row0_col3" class="data row0 col3" >2</td>
                        <td id="T_9150f_row0_col4" class="data row0 col4" >10</td>
                        <td id="T_9150f_row0_col5" class="data row0 col5" >2547</td>
            </tr>
            <tr>
                        <th id="T_9150f_level0_row1" class="row_heading level0 row1" >5</th>
                        <td id="T_9150f_row1_col0" class="data row1 col0" >2298d6c36e</td>
                        <td id="T_9150f_row1_col1" class="data row1 col1" >discount</td>
                        <td id="T_9150f_row1_col2" class="data row1 col2" >7</td>
                        <td id="T_9150f_row1_col3" class="data row1 col3" >3</td>
                        <td id="T_9150f_row1_col4" class="data row1 col4" >7</td>
                        <td id="T_9150f_row1_col5" class="data row1 col5" >2516</td>
            </tr>
            <tr>
                        <th id="T_9150f_level0_row2" class="row_heading level0 row2" >3</th>
                        <td id="T_9150f_row2_col0" class="data row2 col0" >9b98b8c7a3</td>
                        <td id="T_9150f_row2_col1" class="data row2 col1" >bogo</td>
                        <td id="T_9150f_row2_col2" class="data row2 col2" >5</td>
                        <td id="T_9150f_row2_col3" class="data row2 col3" >5</td>
                        <td id="T_9150f_row2_col4" class="data row2 col4" >7</td>
                        <td id="T_9150f_row2_col5" class="data row2 col5" >2336</td>
            </tr>
            <tr>
                        <th id="T_9150f_level0_row3" class="row_heading level0 row3" >9</th>
                        <td id="T_9150f_row3_col0" class="data row3 col0" >2906b810c7</td>
                        <td id="T_9150f_row3_col1" class="data row3 col1" >discount</td>
                        <td id="T_9150f_row3_col2" class="data row3 col2" >10</td>
                        <td id="T_9150f_row3_col3" class="data row3 col3" >2</td>
                        <td id="T_9150f_row3_col4" class="data row3 col4" >7</td>
                        <td id="T_9150f_row3_col5" class="data row3 col5" >2281</td>
            </tr>
            <tr>
                        <th id="T_9150f_level0_row4" class="row_heading level0 row4" >0</th>
                        <td id="T_9150f_row4_col0" class="data row4 col0" >ae264e3637</td>
                        <td id="T_9150f_row4_col1" class="data row4 col1" >bogo</td>
                        <td id="T_9150f_row4_col2" class="data row4 col2" >10</td>
                        <td id="T_9150f_row4_col3" class="data row4 col3" >10</td>
                        <td id="T_9150f_row4_col4" class="data row4 col4" >7</td>
                        <td id="T_9150f_row4_col5" class="data row4 col5" >2269</td>
            </tr>
            <tr>
                        <th id="T_9150f_level0_row5" class="row_heading level0 row5" >8</th>
                        <td id="T_9150f_row5_col0" class="data row5 col0" >f19421c1d4</td>
                        <td id="T_9150f_row5_col1" class="data row5 col1" >bogo</td>
                        <td id="T_9150f_row5_col2" class="data row5 col2" >5</td>
                        <td id="T_9150f_row5_col3" class="data row5 col3" >5</td>
                        <td id="T_9150f_row5_col4" class="data row5 col4" >5</td>
                        <td id="T_9150f_row5_col5" class="data row5 col5" >2260</td>
            </tr>
            <tr>
                        <th id="T_9150f_level0_row6" class="row_heading level0 row6" >4</th>
                        <td id="T_9150f_row6_col0" class="data row6 col0" >0b1e1539f2</td>
                        <td id="T_9150f_row6_col1" class="data row6 col1" >discount</td>
                        <td id="T_9150f_row6_col2" class="data row6 col2" >20</td>
                        <td id="T_9150f_row6_col3" class="data row6 col3" >5</td>
                        <td id="T_9150f_row6_col4" class="data row6 col4" >10</td>
                        <td id="T_9150f_row6_col5" class="data row6 col5" >2225</td>
            </tr>
            <tr>
                        <th id="T_9150f_level0_row7" class="row_heading level0 row7" >1</th>
                        <td id="T_9150f_row7_col0" class="data row7 col0" >4d5c57ea9a</td>
                        <td id="T_9150f_row7_col1" class="data row7 col1" >bogo</td>
                        <td id="T_9150f_row7_col2" class="data row7 col2" >10</td>
                        <td id="T_9150f_row7_col3" class="data row7 col3" >10</td>
                        <td id="T_9150f_row7_col4" class="data row7 col4" >5</td>
                        <td id="T_9150f_row7_col5" class="data row7 col5" >2021</td>
            </tr>
    </tbody></table>



#### (결론) 신규고객은 discount 프로모션을 선호하는 모습을 보여준다. (fafdcd668e[discount], 2298d6c36e[discount])이 두 프로모션을 선호한다.

## 분석 결론 : 전반적으로 BOGO보다 DISCOUNT가 더 좋다.

###  주력 고객층

* 50대 ~60대의 고객들이 전체 고객중 44%를 차지하며 가장 많은 비율을 차지하고 있고, 전체 매출의 47.9%를 차지하고 있다.
* 여성이 남성보다 더 큰 금액을 소비하고 있는 모습을 보여준다.
* 주력 고객층 선정
    - 대집단 : 전체 고객중 44%를 차지하며 47.9%의 매출을 올리고 있는 **50대, 60대 고객**을 스타벅스의 주력 고객으로 선정하자.
    - 소집단 : 전체 고객 중 19.6% 차지하며 24.8%의 매출을 올리고 있는 **50대, 60대 여성**을 주력고객으로 지정하자.

### 총 순 수익 관점에서 우수한 프로모션

* 각 프로모션을 참여(received)된 횟수는 비슷하다. 하지만 실제 쿠폰을 사용한 것은 discount가 더 많다. 
* bogo 전략보다, discount 전략이 총 수익 관점에서 좋다.

* reward가 클 수록 completed_ratio가 감소하는 경향을 보였다. (상관관계 -0.69)
* **`0b1e1539f2[discount]`**이 프로모션이 총 수익 관점에서 좋다.
    - 각 프로모션의 참여 빈도가 비슷하며, difficulty가 큼과 동시에 reward 사용 빈도가 적은 것이 total profit에 일조한 것으로 보인다.
* 총 수익 관점에서 향후 프로모션을 진행할 때 discount전략을 사용하고, reward를 증가시키더라도 difficulty를 높히는 프로모션을 추천한다.


###  주력 고객층이 선호하는 프로모션
* 주력 고객층은 대집단, 소집단 모두 discount프로모션을 선호하고 그중에 **`fafdcd668e[discount]`**, **`0b1e1539f2[discount]`** 이 프로모션을 공통적으로 선호하는 모습을 보였다.
* 총 순수익에 영향력을 강하게 행사하는 주력 고객을 위해서 위 프로모션을 추천한다.

### 신규 고객층이 선호하는 프로모션
* 신규고객은 discount 프로모션을 선호하는 모습을 보여준다. (**`fafdcd668e[discount]`**, **`2298d6c36e[discount]`**)이 두 프로모션을 선호한다.
* 거래 빈도가 평균보다 높은 신규 고객층을 확보하기 위해서 신규 고객층이 선호하는 위 두가지의 discount 전략을 진행한다. 

--------------------------------------------
# 가설 검정

## 남성과 여성의 평균 소비금액이 다른가?

### 가설 설정
* **귀무가설** : 남성과 여성의 평균 소비금액은 차이가 없다.
* **대립가설** : 남성과 여성의 평균 소비금액에 차이가 있다.

### 가설 검정 
* **독립표본 T 검정**
    - 두 독립적인 표본의 평균에 대한 차이를 검정

* **등분산 검정**
    - var.test() -> `p-value < 0.05` : 두 표본의 분산이 다르다.

* **이분산 독립표본 검정**
    - welch's T test -> `p-value < 0.05` : 대립가설 채택

### 결론
* **남성과 여성의 평균 소비금액에 차이가 존재한다.**

## 여성의 연령 별 평균 소비금액이 다른가?

### 가설 설정
* **귀무가설** : 연령 별 평균 소비금액은 같다.
* **대립가설** : 연령 별 평균 소비금액은 다르다.

### 가설 검정 
* **ANOVA 검정**
    - 10대의 평균 소비금액은 너무나도 명확히 차이나서 제외
    - 100대의 경우 표본의 크기가 14로 중심극한정리를 따르지 않고, 정규성을 만족하지 않아서 제외.

* **등분산 검정**
    - bartlett.test -> `p-value < 0.05` : 두 표본의 분산이 다르다.
    - ANOVA를 사용할 수 없다.
    
* **Kruskal-walis test**
    - Kruskal-walis test -> `p-value < 0.05` : 대립가설 채택
    - **연령 별 평균 소비금액은 다르다.**
    
### 사후 검정

* **Wilcoxson ranksum test**
   * bonferonni correction 으로 p-value를 보정
   * 8개의 표본을 2개씩 검정(28개의 경우의수)
   * 보정 된 p-value = 0.00178
   
   * **분석 결론 : `50대와 60대의 평균 소비금액이 가장 높다`**
   
   * **사후 검정** : 20~40 대와의 검정에서 p-value가 0.00178보다 낮으므로 대립가설을 채택하고, 70대 ~ 90대 와의 검정에서는 0.00178보다 높은 p-value를 얻으므로 귀무가설을 채택한다.
    
### 결론
* **주 고객층 50 ~ 60대 여성은 20 ~ 40대 여성과의 평균 소비금액의 차이가 유의미하지만, 70~90대와의 차이는 유의미하지 않다.**

## 주력 고객층(소집단), 50대 ~ 60대 여성 고객은 특정 프로모션에 더 많이 참여가는가?

### 가설 설정
* **귀무가설** : 프로모션 참여 분포는 같다
* **대립가설** : 특정 프로모션에 대한 더 큰 참여가 있다.

### 가설 검정 
* **카이제곱 검정**
    - 8개의 프로모션에 대하여 균일 분포(각 프로모션 참여 확률 : 0.125)를 가정한다.
    - 0.125의 균일분포를 따르는지 검정.
    - `p-value > 0.05` : 귀무가설 채택
    
### 결론
* 50대 ~ 60대 여성의 프로모션 참여 분포는 같고 특정 프로모션에 대한 선호도는 없다.

## 주력 고객층(대집단) 50~60대 고객은 특정 프로모션에 더 많이 참여하는가?

### 가설 설정
* **귀무가설** : 프로모션 참여 분포는 같다.
* **대립가설** : 특정 프로모션에 대한 더 큰 참여가 있다.

### 가설 검정 
* **카이제곱 검정**
    - 8개의 프로모션에 대하여 균일 분포(각 프로모션 참여 확률 : 0.125)를 가정한다.
    - 0.125의 균일분포를 따르는지 검정.
    - `p-value > 0.05` : 귀무가설 채택
    
### 결론
* 50대 ~ 60대 고객의 프로모션 참여 분포는 같고 특정 프로모션에 대한 선호도는 없다.

## 신규 고객은 특정 프로모션에 더 많이 참여하는가?

### 가설 설정
* **귀무가설** : 프로모션 참여 분포는 같다.
* **대립가설** : 특정 프로모션에 대한 더 큰 참여가 있다.

### 가설 검정 
* **카이제곱 검정**
    - 8개의 프로모션에 대하여 균일 분포(각 프로모션 참여 확률 : 0.125)를 가정한다.
    - 0.125의 균일분포를 따르는지 검정.
    - `p-value < 0.05` : 귀무가설 채택
    
### 결론
* 신규고객들은 특정 프로모션에 대한 선호도가 존재한다.

# 최종 결론

## 수익성, 신규고객 관점에서 BOGO 보다 DISCOUNT 전략이 유의미한 수준으로 좋다
* 남성 고객이 여성 고객보다 많지만, 소비 금액은 여성 고객이 더 많다.
* 여성 고객 중 50대 이상 여성 고객이 다른 고객층에 비해 소비 금액이 크므로 주력 고객층으로 선정한다.
* 주력 고객층이 특별하게 선호하는 프로모션은 없다. 따라서 수익성이 좋은 discount 프로모션이 가장 좋은 프로모션이다.
* 신규 고객은 프로모션 참여나 거래 빈도 측면에서 주요한 고객층이고 이들은 discount 프로모션을 특히 선호한다.

# [부록] SQL을 활용하여 전처리

* 아래 python을 활용하여 전처리 한 과정을 SQL문법을 활용하여 진행해봄
* 이 부분은 **4.데이터 전처리** 과정을 복기한 것 입니다.

* **기본 상황**
  + 'starbucks'라는 이름의 데이터베이스는 미리 생성을 해놓고 csv파일을 워크벤치를 통해 미리 import를 시켜놓은 상태에서 응용
    + profile.csv
    + portfolio.csv
    + transcript.csv  

**라이브러리**


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import datetime
import scipy.io
import csv
import pymysql
```

## MySQL 연동


```python
conn = pymysql.connect(host="127.0.0.1", user="root", password="whdgk12345",database="starbuckss", charset="utf8")
# 결과를 Dict 형태로 변환
cur = conn.cursor(pymysql.cursors.DictCursor)
```

## profile.csv 전처리


```python
sql = "alter table profile drop no"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from profile limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'gender': '',
      'age': 118,
      'id': '68be06ca386d4c31939f3a4f0e3dd783',
      'became_member_on': 20170212,
      'income': ''},
     {'gender': 'F',
      'age': 55,
      'id': '0610b486422d4921ae7d2bf64640c50b',
      'became_member_on': 20170715,
      'income': '112000.0'},
     {'gender': '',
      'age': 118,
      'id': '38fe809add3b4fcf9315a9694bb96ff5',
      'became_member_on': 20180712,
      'income': ''},
     {'gender': 'F',
      'age': 75,
      'id': '78afa995795e4d85b5d9ceeca43f5fef',
      'became_member_on': 20170509,
      'income': '100000.0'},
     {'gender': '',
      'age': 118,
      'id': 'a03223e636434f42ac4c3df47e8bac43',
      'became_member_on': 20170804,
      'income': ''}]



### null 값 제거


```python
sql = "select count(age) from profile where gender = ''"
cur.execute(sql)

for a in cur:
    print(a)
```

    {'count(age)': 2175}
    


```python
sql = "delete from profile where gender = ''"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from profile limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'gender': 'F',
      'age': 55,
      'id': '0610b486422d4921ae7d2bf64640c50b',
      'became_member_on': 20170715,
      'income': '112000.0'},
     {'gender': 'F',
      'age': 75,
      'id': '78afa995795e4d85b5d9ceeca43f5fef',
      'became_member_on': 20170509,
      'income': '100000.0'},
     {'gender': 'M',
      'age': 68,
      'id': 'e2127556f4f64592b11af22de27a7932',
      'became_member_on': 20180426,
      'income': '70000.0'},
     {'gender': 'M',
      'age': 65,
      'id': '389bc3fa690240e798340f5a15918d5c',
      'became_member_on': 20180209,
      'income': '53000.0'},
     {'gender': 'M',
      'age': 58,
      'id': '2eeac8d8feae4a8cad5a6af0499a211d',
      'became_member_on': 20171111,
      'income': '51000.0'}]



### 연령대 나누는 [age_units10] 추가


```python
sql = "alter table profile add age_units10 int default null"
cur.execute(sql)
conn.commit()
```


```python
sql = "update profile set age_units10 = 10 where age < 20"
cur.execute(sql)
conn.commit()
sql = "update profile set age_units10 = 20 where age >= 20 and age < 30"
cur.execute(sql)
conn.commit()
sql = "update profile set age_units10 = 30 where age >= 30 and age <40"
cur.execute(sql)
conn.commit()
sql = "update profile set age_units10 = 40 where age >= 40 and age < 50"
cur.execute(sql)
conn.commit()
sql = "update profile set age_units10 = 50 where age >= 50 and age < 60"
cur.execute(sql)
conn.commit()
sql = "update profile set age_units10 = 60 where age >= 60 and age < 70"
cur.execute(sql)
conn.commit()
sql = "update profile set age_units10 = 70 where age >= 70 and age < 80"
cur.execute(sql)
conn.commit()
sql = "update profile set age_units10 = 80 where age >= 80 and age < 90"
cur.execute(sql)
conn.commit()
sql = "update profile set age_units10 = 90 where age >= 90 and age < 100"
cur.execute(sql)
conn.commit()
sql = "update profile set age_units10 = 100 where age >= 100"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from profile limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'gender': 'F',
      'age': 55,
      'id': '0610b486422d4921ae7d2bf64640c50b',
      'became_member_on': 20170715,
      'income': '112000.0',
      'age_units10': 50},
     {'gender': 'F',
      'age': 75,
      'id': '78afa995795e4d85b5d9ceeca43f5fef',
      'became_member_on': 20170509,
      'income': '100000.0',
      'age_units10': 70},
     {'gender': 'M',
      'age': 68,
      'id': 'e2127556f4f64592b11af22de27a7932',
      'became_member_on': 20180426,
      'income': '70000.0',
      'age_units10': 60},
     {'gender': 'M',
      'age': 65,
      'id': '389bc3fa690240e798340f5a15918d5c',
      'became_member_on': 20180209,
      'income': '53000.0',
      'age_units10': 60},
     {'gender': 'M',
      'age': 58,
      'id': '2eeac8d8feae4a8cad5a6af0499a211d',
      'became_member_on': 20171111,
      'income': '51000.0',
      'age_units10': 50}]



#### age_units10을 추가할 때 생긴 null값 행 제거


```python
sql = "delete from profile where age is null"
cur.execute(sql)
conn.commit()
```

### id 값을 10자리로 축소


```python
sql = "update profile set id = (select substr(id,1,10))"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from profile limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'gender': 'F',
      'age': 55,
      'id': '0610b48642',
      'became_member_on': 20170715,
      'income': '112000.0',
      'age_units10': 50},
     {'gender': 'F',
      'age': 75,
      'id': '78afa99579',
      'became_member_on': 20170509,
      'income': '100000.0',
      'age_units10': 70},
     {'gender': 'M',
      'age': 68,
      'id': 'e2127556f4',
      'became_member_on': 20180426,
      'income': '70000.0',
      'age_units10': 60},
     {'gender': 'M',
      'age': 65,
      'id': '389bc3fa69',
      'became_member_on': 20180209,
      'income': '53000.0',
      'age_units10': 60},
     {'gender': 'M',
      'age': 58,
      'id': '2eeac8d8fe',
      'became_member_on': 20171111,
      'income': '51000.0',
      'age_units10': 50}]



### became_member_on 나누기

**year, month, day 컬럼 추가**


```python
sql = "alter table profile add year int default null"
cur.execute(sql)
conn.commit()

sql = "alter table profile add month int default null"
cur.execute(sql)
conn.commit()

sql = "alter table profile add day int default null"
cur.execute(sql)
conn.commit()
```

#### became_member_on 타입 변경


```python
sql = "alter table profile modify became_member_on date"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from profile limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'gender': 'F',
      'age': 55,
      'id': '0610b48642',
      'became_member_on': datetime.date(2017, 7, 15),
      'income': '112000.0',
      'age_units10': 50,
      'year': None,
      'month': None,
      'day': None},
     {'gender': 'F',
      'age': 75,
      'id': '78afa99579',
      'became_member_on': datetime.date(2017, 5, 9),
      'income': '100000.0',
      'age_units10': 70,
      'year': None,
      'month': None,
      'day': None},
     {'gender': 'M',
      'age': 68,
      'id': 'e2127556f4',
      'became_member_on': datetime.date(2018, 4, 26),
      'income': '70000.0',
      'age_units10': 60,
      'year': None,
      'month': None,
      'day': None},
     {'gender': 'M',
      'age': 65,
      'id': '389bc3fa69',
      'became_member_on': datetime.date(2018, 2, 9),
      'income': '53000.0',
      'age_units10': 60,
      'year': None,
      'month': None,
      'day': None},
     {'gender': 'M',
      'age': 58,
      'id': '2eeac8d8fe',
      'became_member_on': datetime.date(2017, 11, 11),
      'income': '51000.0',
      'age_units10': 50,
      'year': None,
      'month': None,
      'day': None}]



### join_year, join_month, join_day 데이터 추가

**컬럼명 변경**


```python
sql = "alter table profile change year join_year int"
cur.execute(sql)
conn.commit()

sql = "alter table profile change month join_month int"
cur.execute(sql)
conn.commit()

sql = "alter table profile change day join_day int"
cur.execute(sql)
conn.commit()
```


```python
sql = "update profile set join_year = date_format(became_member_on,'%Y')"
cur.execute(sql)
conn.commit()

sql = "update profile set join_month = date_format(became_member_on,'%m')"
cur.execute(sql)
conn.commit()

sql = "update profile set join_day = date_format(became_member_on,'%d')"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from profile limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'gender': 'F',
      'age': 55,
      'id': '0610b48642',
      'became_member_on': datetime.date(2017, 7, 15),
      'income': '112000.0',
      'age_units10': 50,
      'join_year': 2017,
      'join_month': 7,
      'join_day': 15},
     {'gender': 'F',
      'age': 75,
      'id': '78afa99579',
      'became_member_on': datetime.date(2017, 5, 9),
      'income': '100000.0',
      'age_units10': 70,
      'join_year': 2017,
      'join_month': 5,
      'join_day': 9},
     {'gender': 'M',
      'age': 68,
      'id': 'e2127556f4',
      'became_member_on': datetime.date(2018, 4, 26),
      'income': '70000.0',
      'age_units10': 60,
      'join_year': 2018,
      'join_month': 4,
      'join_day': 26},
     {'gender': 'M',
      'age': 65,
      'id': '389bc3fa69',
      'became_member_on': datetime.date(2018, 2, 9),
      'income': '53000.0',
      'age_units10': 60,
      'join_year': 2018,
      'join_month': 2,
      'join_day': 9},
     {'gender': 'M',
      'age': 58,
      'id': '2eeac8d8fe',
      'became_member_on': datetime.date(2017, 11, 11),
      'income': '51000.0',
      'age_units10': 50,
      'join_year': 2017,
      'join_month': 11,
      'join_day': 11}]



### 현재 날짜 추가


```python
sql = "alter table profile add now date"
cur.execute(sql)
conn.commit()
```


```python
sql = "update profile set now = date_format(now(),'%Y-%m-%d')"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from profile limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'gender': 'F',
      'age': 55,
      'id': '0610b48642',
      'became_member_on': datetime.date(2017, 7, 15),
      'income': '112000.0',
      'age_units10': 50,
      'join_year': 2017,
      'join_month': 7,
      'join_day': 15,
      'now': datetime.date(2021, 6, 22)},
     {'gender': 'F',
      'age': 75,
      'id': '78afa99579',
      'became_member_on': datetime.date(2017, 5, 9),
      'income': '100000.0',
      'age_units10': 70,
      'join_year': 2017,
      'join_month': 5,
      'join_day': 9,
      'now': datetime.date(2021, 6, 22)},
     {'gender': 'M',
      'age': 68,
      'id': 'e2127556f4',
      'became_member_on': datetime.date(2018, 4, 26),
      'income': '70000.0',
      'age_units10': 60,
      'join_year': 2018,
      'join_month': 4,
      'join_day': 26,
      'now': datetime.date(2021, 6, 22)},
     {'gender': 'M',
      'age': 65,
      'id': '389bc3fa69',
      'became_member_on': datetime.date(2018, 2, 9),
      'income': '53000.0',
      'age_units10': 60,
      'join_year': 2018,
      'join_month': 2,
      'join_day': 9,
      'now': datetime.date(2021, 6, 22)},
     {'gender': 'M',
      'age': 58,
      'id': '2eeac8d8fe',
      'became_member_on': datetime.date(2017, 11, 11),
      'income': '51000.0',
      'age_units10': 50,
      'join_year': 2017,
      'join_month': 11,
      'join_day': 11,
      'now': datetime.date(2021, 6, 22)}]



### 회원 가입 후 지금까지의 일 수 추가


```python
sql = "alter table profile add join_period int"
cur.execute(sql)
conn.commit()
```


```python
sql = "update profile set join_period = to_days(now) - to_days(became_member_on)"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from profile limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'gender': 'F',
      'age': 55,
      'id': '0610b48642',
      'became_member_on': datetime.date(2017, 7, 15),
      'income': '112000.0',
      'age_units10': 50,
      'join_year': 2017,
      'join_month': 7,
      'join_day': 15,
      'now': datetime.date(2021, 6, 22),
      'join_period': 1438},
     {'gender': 'F',
      'age': 75,
      'id': '78afa99579',
      'became_member_on': datetime.date(2017, 5, 9),
      'income': '100000.0',
      'age_units10': 70,
      'join_year': 2017,
      'join_month': 5,
      'join_day': 9,
      'now': datetime.date(2021, 6, 22),
      'join_period': 1505},
     {'gender': 'M',
      'age': 68,
      'id': 'e2127556f4',
      'became_member_on': datetime.date(2018, 4, 26),
      'income': '70000.0',
      'age_units10': 60,
      'join_year': 2018,
      'join_month': 4,
      'join_day': 26,
      'now': datetime.date(2021, 6, 22),
      'join_period': 1153},
     {'gender': 'M',
      'age': 65,
      'id': '389bc3fa69',
      'became_member_on': datetime.date(2018, 2, 9),
      'income': '53000.0',
      'age_units10': 60,
      'join_year': 2018,
      'join_month': 2,
      'join_day': 9,
      'now': datetime.date(2021, 6, 22),
      'join_period': 1229},
     {'gender': 'M',
      'age': 58,
      'id': '2eeac8d8fe',
      'became_member_on': datetime.date(2017, 11, 11),
      'income': '51000.0',
      'age_units10': 50,
      'join_year': 2017,
      'join_month': 11,
      'join_day': 11,
      'now': datetime.date(2021, 6, 22),
      'join_period': 1319}]



### person 이름 변경


```python
sql = "alter table profile change id person_id text"
cur.execute(sql)
conn.commit()
```

### profile.csv 전체 조회


```python
sql = "select * from profile limit 5"
cur.execute(sql)
result = cur.fetchall()
result
```




    [{'gender': 'F',
      'age': 55,
      'person_id': '0610b48642',
      'became_member_on': datetime.date(2017, 7, 15),
      'income': '112000.0',
      'age_units10': 50,
      'join_year': 2017,
      'join_month': 7,
      'join_day': 15,
      'now': datetime.date(2021, 6, 22),
      'join_period': 1438},
     {'gender': 'F',
      'age': 75,
      'person_id': '78afa99579',
      'became_member_on': datetime.date(2017, 5, 9),
      'income': '100000.0',
      'age_units10': 70,
      'join_year': 2017,
      'join_month': 5,
      'join_day': 9,
      'now': datetime.date(2021, 6, 22),
      'join_period': 1505},
     {'gender': 'M',
      'age': 68,
      'person_id': 'e2127556f4',
      'became_member_on': datetime.date(2018, 4, 26),
      'income': '70000.0',
      'age_units10': 60,
      'join_year': 2018,
      'join_month': 4,
      'join_day': 26,
      'now': datetime.date(2021, 6, 22),
      'join_period': 1153},
     {'gender': 'M',
      'age': 65,
      'person_id': '389bc3fa69',
      'became_member_on': datetime.date(2018, 2, 9),
      'income': '53000.0',
      'age_units10': 60,
      'join_year': 2018,
      'join_month': 2,
      'join_day': 9,
      'now': datetime.date(2021, 6, 22),
      'join_period': 1229},
     {'gender': 'M',
      'age': 58,
      'person_id': '2eeac8d8fe',
      'became_member_on': datetime.date(2017, 11, 11),
      'income': '51000.0',
      'age_units10': 50,
      'join_year': 2017,
      'join_month': 11,
      'join_day': 11,
      'now': datetime.date(2021, 6, 22),
      'join_period': 1319}]



## portfolio.csv 전처리

### channels 전처리
+ email,web,mobile,social 별로 카운트 컬럼 생성


```python
sql = "alter table portfolio drop no"
cur.execute(sql)
conn.commit()
```


```python
sql = "alter table portfolio add email int default 0"
cur.execute(sql)
conn.commit()

sql = "alter table portfolio add web int default 0"
cur.execute(sql)
conn.commit()

sql = "alter table portfolio add mobile int default 0"
cur.execute(sql)
conn.commit()

sql = "alter table portfolio add social int default 0"
cur.execute(sql)
conn.commit()
```

**채널 별 카운트**


```python
sql = "update portfolio set email = 1 where channels like '%email%'"
cur.execute(sql)
conn.commit()

sql = "update portfolio set web = 1 where channels like '%web%'"
cur.execute(sql)
conn.commit()

sql = "update portfolio set mobile = 1 where channels like '%mobile%'"
cur.execute(sql)
conn.commit()

sql = "update portfolio set social = 1 where channels like '%social%'"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from portfolio limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'reward': 10,
      'channels': "['email', 'mobile', 'social']",
      'difficulty': 10,
      'duration': 7,
      'offer_type': 'bogo',
      'id': 'ae264e3637204a6fb9bb56bc8210ddfd',
      'email': 1,
      'web': 0,
      'mobile': 1,
      'social': 1},
     {'reward': 10,
      'channels': "['web', 'email', 'mobile', 'social']",
      'difficulty': 10,
      'duration': 5,
      'offer_type': 'bogo',
      'id': '4d5c57ea9a6940dd891ad53e9dbe8da0',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 1},
     {'reward': 0,
      'channels': "['web', 'email', 'mobile']",
      'difficulty': 0,
      'duration': 4,
      'offer_type': 'informational',
      'id': '3f207df678b143eea3cee63160fa8bed',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 0},
     {'reward': 5,
      'channels': "['web', 'email', 'mobile']",
      'difficulty': 5,
      'duration': 7,
      'offer_type': 'bogo',
      'id': '9b98b8c7a33c4b65b9aebfe6a799e6d9',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 0},
     {'reward': 5,
      'channels': "['web', 'email']",
      'difficulty': 20,
      'duration': 10,
      'offer_type': 'discount',
      'id': '0b1e1539f2cc45b7b9fa7c272da2e1d7',
      'email': 1,
      'web': 1,
      'mobile': 0,
      'social': 0}]



**홍보수단의 개수 카운트 : channels_num** 


```python
sql = "alter table portfolio add channels_num int default 0"
cur.execute(sql)
conn.commit()
```


```python
sql = "update portfolio set channels_num = email + web + mobile + social"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from portfolio limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'reward': 10,
      'channels': "['email', 'mobile', 'social']",
      'difficulty': 10,
      'duration': 7,
      'offer_type': 'bogo',
      'id': 'ae264e3637204a6fb9bb56bc8210ddfd',
      'email': 1,
      'web': 0,
      'mobile': 1,
      'social': 1,
      'channels_num': 3},
     {'reward': 10,
      'channels': "['web', 'email', 'mobile', 'social']",
      'difficulty': 10,
      'duration': 5,
      'offer_type': 'bogo',
      'id': '4d5c57ea9a6940dd891ad53e9dbe8da0',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 1,
      'channels_num': 4},
     {'reward': 0,
      'channels': "['web', 'email', 'mobile']",
      'difficulty': 0,
      'duration': 4,
      'offer_type': 'informational',
      'id': '3f207df678b143eea3cee63160fa8bed',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 0,
      'channels_num': 3},
     {'reward': 5,
      'channels': "['web', 'email', 'mobile']",
      'difficulty': 5,
      'duration': 7,
      'offer_type': 'bogo',
      'id': '9b98b8c7a33c4b65b9aebfe6a799e6d9',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 0,
      'channels_num': 3},
     {'reward': 5,
      'channels': "['web', 'email']",
      'difficulty': 20,
      'duration': 10,
      'offer_type': 'discount',
      'id': '0b1e1539f2cc45b7b9fa7c272da2e1d7',
      'email': 1,
      'web': 1,
      'mobile': 0,
      'social': 0,
      'channels_num': 2}]



### id 값을 10자리로 축소


```python
sql = "alter table portfolio change id offer_id text"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from portfolio limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'reward': 10,
      'channels': "['email', 'mobile', 'social']",
      'difficulty': 10,
      'duration': 7,
      'offer_type': 'bogo',
      'offer_id': 'ae264e3637204a6fb9bb56bc8210ddfd',
      'email': 1,
      'web': 0,
      'mobile': 1,
      'social': 1,
      'channels_num': 3},
     {'reward': 10,
      'channels': "['web', 'email', 'mobile', 'social']",
      'difficulty': 10,
      'duration': 5,
      'offer_type': 'bogo',
      'offer_id': '4d5c57ea9a6940dd891ad53e9dbe8da0',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 1,
      'channels_num': 4},
     {'reward': 0,
      'channels': "['web', 'email', 'mobile']",
      'difficulty': 0,
      'duration': 4,
      'offer_type': 'informational',
      'offer_id': '3f207df678b143eea3cee63160fa8bed',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 0,
      'channels_num': 3},
     {'reward': 5,
      'channels': "['web', 'email', 'mobile']",
      'difficulty': 5,
      'duration': 7,
      'offer_type': 'bogo',
      'offer_id': '9b98b8c7a33c4b65b9aebfe6a799e6d9',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 0,
      'channels_num': 3},
     {'reward': 5,
      'channels': "['web', 'email']",
      'difficulty': 20,
      'duration': 10,
      'offer_type': 'discount',
      'offer_id': '0b1e1539f2cc45b7b9fa7c272da2e1d7',
      'email': 1,
      'web': 1,
      'mobile': 0,
      'social': 0,
      'channels_num': 2}]



### reward - difficulty : r_minus_d


```python
sql = "alter table portfolio add r_minus_d int default 0"
cur.execute(sql)
conn.commit()
```


```python
sql = "update portfolio set r_minus_d = reward - difficulty"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from portfolio limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'reward': 10,
      'channels': "['email', 'mobile', 'social']",
      'difficulty': 10,
      'duration': 7,
      'offer_type': 'bogo',
      'offer_id': 'ae264e3637204a6fb9bb56bc8210ddfd',
      'email': 1,
      'web': 0,
      'mobile': 1,
      'social': 1,
      'channels_num': 3,
      'r_minus_d': 0},
     {'reward': 10,
      'channels': "['web', 'email', 'mobile', 'social']",
      'difficulty': 10,
      'duration': 5,
      'offer_type': 'bogo',
      'offer_id': '4d5c57ea9a6940dd891ad53e9dbe8da0',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 1,
      'channels_num': 4,
      'r_minus_d': 0},
     {'reward': 0,
      'channels': "['web', 'email', 'mobile']",
      'difficulty': 0,
      'duration': 4,
      'offer_type': 'informational',
      'offer_id': '3f207df678b143eea3cee63160fa8bed',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 0,
      'channels_num': 3,
      'r_minus_d': 0},
     {'reward': 5,
      'channels': "['web', 'email', 'mobile']",
      'difficulty': 5,
      'duration': 7,
      'offer_type': 'bogo',
      'offer_id': '9b98b8c7a33c4b65b9aebfe6a799e6d9',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 0,
      'channels_num': 3,
      'r_minus_d': 0},
     {'reward': 5,
      'channels': "['web', 'email']",
      'difficulty': 20,
      'duration': 10,
      'offer_type': 'discount',
      'offer_id': '0b1e1539f2cc45b7b9fa7c272da2e1d7',
      'email': 1,
      'web': 1,
      'mobile': 0,
      'social': 0,
      'channels_num': 2,
      'r_minus_d': -15}]



### portfolio.csv 전체 조회


```python
sql = "select * from portfolio limit 5"
cur.execute(sql)
result = cur.fetchall()
result
```




    [{'reward': 10,
      'channels': "['email', 'mobile', 'social']",
      'difficulty': 10,
      'duration': 7,
      'offer_type': 'bogo',
      'offer_id': 'ae264e3637204a6fb9bb56bc8210ddfd',
      'email': 1,
      'web': 0,
      'mobile': 1,
      'social': 1,
      'channels_num': 3,
      'r_minus_d': 0},
     {'reward': 10,
      'channels': "['web', 'email', 'mobile', 'social']",
      'difficulty': 10,
      'duration': 5,
      'offer_type': 'bogo',
      'offer_id': '4d5c57ea9a6940dd891ad53e9dbe8da0',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 1,
      'channels_num': 4,
      'r_minus_d': 0},
     {'reward': 0,
      'channels': "['web', 'email', 'mobile']",
      'difficulty': 0,
      'duration': 4,
      'offer_type': 'informational',
      'offer_id': '3f207df678b143eea3cee63160fa8bed',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 0,
      'channels_num': 3,
      'r_minus_d': 0},
     {'reward': 5,
      'channels': "['web', 'email', 'mobile']",
      'difficulty': 5,
      'duration': 7,
      'offer_type': 'bogo',
      'offer_id': '9b98b8c7a33c4b65b9aebfe6a799e6d9',
      'email': 1,
      'web': 1,
      'mobile': 1,
      'social': 0,
      'channels_num': 3,
      'r_minus_d': 0},
     {'reward': 5,
      'channels': "['web', 'email']",
      'difficulty': 20,
      'duration': 10,
      'offer_type': 'discount',
      'offer_id': '0b1e1539f2cc45b7b9fa7c272da2e1d7',
      'email': 1,
      'web': 1,
      'mobile': 0,
      'social': 0,
      'channels_num': 2,
      'r_minus_d': -15}]



## transcript.csv 전처리


```python
sql = "alter table transcript drop no"
cur.execute(sql)
conn.commit()
```

### value를 group과 id로 분할

**컬럼 생성**
   + sql에서의 group은 예약어이기 때문에 오류가 남으로 offer_group으로 지정


```python
sql = "alter table transcript add offer_group text"
cur.execute(sql)
conn.commit()

sql = "alter table transcript add offer_id text"
cur.execute(sql)
conn.commit()
```

**value 데이터 복사**


```python
sql = "update transcript set offer_group = value"
cur.execute(sql)
conn.commit()

sql = "update transcript set offer_id = value"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from transcript limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'person': '78afa995795e4d85b5d9ceeca43f5fef',
      'EVENT': 'offer received',
      'VALUE': "{'offer id': '9b98b8c7a33c4b65b9aebfe6a799e6d9'}",
      'TIME': 0,
      'offer_group': "{'offer id': '9b98b8c7a33c4b65b9aebfe6a799e6d9'}",
      'offer_id': "{'offer id': '9b98b8c7a33c4b65b9aebfe6a799e6d9'}"},
     {'person': 'a03223e636434f42ac4c3df47e8bac43',
      'EVENT': 'offer received',
      'VALUE': "{'offer id': '0b1e1539f2cc45b7b9fa7c272da2e1d7'}",
      'TIME': 0,
      'offer_group': "{'offer id': '0b1e1539f2cc45b7b9fa7c272da2e1d7'}",
      'offer_id': "{'offer id': '0b1e1539f2cc45b7b9fa7c272da2e1d7'}"},
     {'person': 'e2127556f4f64592b11af22de27a7932',
      'EVENT': 'offer received',
      'VALUE': "{'offer id': '2906b810c7d4411798c6938adc9daaa5'}",
      'TIME': 0,
      'offer_group': "{'offer id': '2906b810c7d4411798c6938adc9daaa5'}",
      'offer_id': "{'offer id': '2906b810c7d4411798c6938adc9daaa5'}"},
     {'person': '8ec6ce2a7e7949b1bf142def7d0e0586',
      'EVENT': 'offer received',
      'VALUE': "{'offer id': 'fafdcd668e3743c1bb461111dcafc2a4'}",
      'TIME': 0,
      'offer_group': "{'offer id': 'fafdcd668e3743c1bb461111dcafc2a4'}",
      'offer_id': "{'offer id': 'fafdcd668e3743c1bb461111dcafc2a4'}"},
     {'person': '68617ca6246f4fbc85e91a2a49552598',
      'EVENT': 'offer received',
      'VALUE': "{'offer id': '4d5c57ea9a6940dd891ad53e9dbe8da0'}",
      'TIME': 0,
      'offer_group': "{'offer id': '4d5c57ea9a6940dd891ad53e9dbe8da0'}",
      'offer_id': "{'offer id': '4d5c57ea9a6940dd891ad53e9dbe8da0'}"}]



**문자열 분할**

* **offer_group 부분**


```python
sql = "update transcript set offer_group = (select substring_index(offer_group,':',1))"
cur.execute(sql)
conn.commit()

sql = "update transcript set offer_group = replace(offer_group,'{','')"
cur.execute(sql)
conn.commit()

sql = "update transcript set offer_group = replace(offer_group,'''','')"
cur.execute(sql)
conn.commit()
```

**id 부분**


```python
sql = "update transcript set offer_id = (select substring_index(substring_index(offer_id,':',4), ':', -1))"
cur.execute(sql)
conn.commit()

sql = "update transcript set offer_id = replace(offer_id,'}','')"
cur.execute(sql)
conn.commit()

sql = "update transcript set offer_id = replace(offer_id,'''','')"
cur.execute(sql)
conn.commit()

sql = "update transcript set offer_id = replace(offer_id,' ','')"
cur.execute(sql)
conn.commit()
```

**vlaue 제거**


```python
sql = "alter table transcript drop value"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from transcript limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'person': '78afa995795e4d85b5d9ceeca43f5fef',
      'EVENT': 'offer received',
      'TIME': 0,
      'offer_group': 'offer id',
      'offer_id': '9b98b8c7a33c4b65b9aebfe6a799e6d9'},
     {'person': 'a03223e636434f42ac4c3df47e8bac43',
      'EVENT': 'offer received',
      'TIME': 0,
      'offer_group': 'offer id',
      'offer_id': '0b1e1539f2cc45b7b9fa7c272da2e1d7'},
     {'person': 'e2127556f4f64592b11af22de27a7932',
      'EVENT': 'offer received',
      'TIME': 0,
      'offer_group': 'offer id',
      'offer_id': '2906b810c7d4411798c6938adc9daaa5'},
     {'person': '8ec6ce2a7e7949b1bf142def7d0e0586',
      'EVENT': 'offer received',
      'TIME': 0,
      'offer_group': 'offer id',
      'offer_id': 'fafdcd668e3743c1bb461111dcafc2a4'},
     {'person': '68617ca6246f4fbc85e91a2a49552598',
      'EVENT': 'offer received',
      'TIME': 0,
      'offer_group': 'offer id',
      'offer_id': '4d5c57ea9a6940dd891ad53e9dbe8da0'}]



### offer_id값 10자리로 축소


```python
sql = "update transcript set offer_id = (select substr(offer_id,1,10))"
cur.execute(sql)
conn.commit()
```

###  amount의 값을 실수형 2자리로 변경


```python
sql = "update transcript set offer_id = (select round(offer_id,2)) where offer_group = 'amount'"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from transcript where offer_group = 'amount' limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'person': '02c083884c7d45b39cc68e1314fec56c',
      'EVENT': 'transaction',
      'TIME': 0,
      'offer_group': 'amount',
      'offer_id': '0.83'},
     {'person': '9fa9ae8f57894cc9a3b8a9bbe0fc1b2f',
      'EVENT': 'transaction',
      'TIME': 0,
      'offer_group': 'amount',
      'offer_id': '34.56'},
     {'person': '54890f68699049c2a04d415abc25e717',
      'EVENT': 'transaction',
      'TIME': 0,
      'offer_group': 'amount',
      'offer_id': '13.23'},
     {'person': 'b2f1cd155b864803ad8334cdf13c4bd2',
      'EVENT': 'transaction',
      'TIME': 0,
      'offer_group': 'amount',
      'offer_id': '19.51'},
     {'person': 'fe97aa22dd3e48c8b143116a8403dd52',
      'EVENT': 'transaction',
      'TIME': 0,
      'offer_group': 'amount',
      'offer_id': '18.97'}]



### person_id 컬럼명 변경 및 10자리로 축소


```python
sql = "update transcript set person = (select substr(person,1,10))"
cur.execute(sql)
conn.commit()

sql = "alter table transcript change person person_id text"
cur.execute(sql)
conn.commit()
```


```python
sql = "select * from transcript where offer_group = 'amount' limit 5"
cur.execute(sql)

result = cur.fetchall()
result
```




    [{'person_id': '02c083884c',
      'EVENT': 'transaction',
      'TIME': 0,
      'offer_group': 'amount',
      'offer_id': '0.83'},
     {'person_id': '9fa9ae8f57',
      'EVENT': 'transaction',
      'TIME': 0,
      'offer_group': 'amount',
      'offer_id': '34.56'},
     {'person_id': '54890f6869',
      'EVENT': 'transaction',
      'TIME': 0,
      'offer_group': 'amount',
      'offer_id': '13.23'},
     {'person_id': 'b2f1cd155b',
      'EVENT': 'transaction',
      'TIME': 0,
      'offer_group': 'amount',
      'offer_id': '19.51'},
     {'person_id': 'fe97aa22dd',
      'EVENT': 'transaction',
      'TIME': 0,
      'offer_group': 'amount',
      'offer_id': '18.97'}]



### day,week,time_korea 컬럼 생성


```python
sql = "alter table transcript add day int"
cur.execute(sql)
conn.commit()

sql = "alter table transcript add week int"
cur.execute(sql)
conn.commit()

sql = "alter table transcript add time_korea text"
cur.execute(sql)
conn.commit()
```

**day**


```python
sql = "update transcript set day = time/24"
cur.execute(sql)
conn.commit()
```

**week**


```python
sql = "update transcript set week = day/7"
cur.execute(sql)
conn.commit()
```

**time_korea**


```python
sql = "update transcript set time_korea = '자정' where time%24=0"
cur.execute(sql)
conn.commit()

sql = "update transcript set time_korea = '오전6시' where time%24=6"
cur.execute(sql)
conn.commit()

sql = "update transcript set time_korea = '정오' where time%24=12"
cur.execute(sql)
conn.commit()

sql = "update transcript set time_korea = '오후6시' where time%24=18"
cur.execute(sql)
conn.commit()
```

### transcript.csv 전체 조회

## 데이터 병합


```python
sql = "select * from profile as pr join transcript as t on pr.person_id = t.person_id left outer join portfolio po on t.offer_id = po.offer_id limit 5"
cur.execute(sql)
result = cur.fetchone()
result
```




    {'gender': 'F',
     'age': 75,
     'person_id': '78afa99579',
     'became_member_on': datetime.date(2017, 5, 9),
     'income': '100000.0',
     'age_units10': 70,
     'join_year': 2017,
     'join_month': 5,
     'join_day': 9,
     'now': datetime.date(2021, 6, 22),
     'join_period': 1505,
     't.person_id': '78afa99579',
     'EVENT': 'offer received',
     'TIME': 0,
     'offer_group': 'offer id',
     'offer_id': '9b98b8c7a3',
     'day': 0,
     'week': 0,
     'time_korea': '자정',
     'reward': None,
     'channels': None,
     'difficulty': None,
     'duration': None,
     'offer_type': None,
     'po.offer_id': None,
     'email': None,
     'web': None,
     'mobile': None,
     'social': None,
     'channels_num': None,
     'r_minus_d': None}



### final 테이블로 만들기


```python
sql = "create table final as select pr.gender,pr.age,pr.person_id,pr.became_member_on,pr.income,pr.age_units10,pr.join_year,pr.join_month,pr.join_day,pr.now,pr.join_period,t.event,t.time,t.offer_group,t.offer_id,t.day,t.week,t.time_korea,po.channels,po.difficulty,po.duration,po.offer_type,po.email,po.web,po.mobile,po.social,po.channels_num,po.r_minus_d from profile pr join transcript t on (pr.person_id=t.person_id) left outer join portfolio po on(t.offer_id=po.offer_id)"
cur.execute(sql)
conn.commit()
```

### 소득구간 나누기


```python
sql = "alter table final add income_rank text"
cur.execute(sql)
conn.commit()
```


```python
sql = "update final set income_rank = 'income_4th' where income > 29000 and income <= 50000"
cur.execute(sql)
conn.commit()

sql = "update final set income_rank = 'income_3th' where income > 50000 and income <= 75000 "
cur.execute(sql)
conn.commit()

sql = "update final set income_rank = 'income_2th' where income > 75000 and income <=100000"
cur.execute(sql)
conn.commit()

sql = "update final set income_rank = 'income_1th' where income > 100000 and income <=121000"
cur.execute(sql)
conn.commit()
```

### final의 전체 데이터


```python
sql = "select * from final"
cur.execute(sql)

result = cur.fetchone()
result
```




    {'gender': 'F',
     'age': 75,
     'person_id': '78afa99579',
     'became_member_on': datetime.date(2017, 5, 9),
     'income': '100000.0',
     'age_units10': 70,
     'join_year': 2017,
     'join_month': 5,
     'join_day': 9,
     'now': datetime.date(2021, 6, 22),
     'join_period': 1505,
     'event': 'offer received',
     'time': 0,
     'offer_group': 'offer id',
     'offer_id': '9b98b8c7a3',
     'day': 0,
     'week': 0,
     'time_korea': '자정',
     'channels': None,
     'difficulty': None,
     'duration': None,
     'offer_type': None,
     'email': None,
     'web': None,
     'mobile': None,
     'social': None,
     'channels_num': None,
     'r_minus_d': None,
     'income_rank': 'income_2th'}


