```python
import distribution as distr
import testing as test
import numpy as np
import pandas as pd
```

1. 독립성 검정


```python
score = pd.DataFrame({'1학군':[23, 18, 19],
             '2학군':[33, 35, 37],
             '3학군':[50, 45, 45],
             '4학군':[20, 39, 21],
             '5학군':[24, 63, 28]},
             index = ['1등급', '2등급', '3등급'])
score
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
      <th>1학군</th>
      <th>2학군</th>
      <th>3학군</th>
      <th>4학군</th>
      <th>5학군</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1등급</th>
      <td>23</td>
      <td>33</td>
      <td>50</td>
      <td>20</td>
      <td>24</td>
    </tr>
    <tr>
      <th>2등급</th>
      <td>18</td>
      <td>35</td>
      <td>45</td>
      <td>39</td>
      <td>63</td>
    </tr>
    <tr>
      <th>3등급</th>
      <td>19</td>
      <td>37</td>
      <td>45</td>
      <td>21</td>
      <td>28</td>
    </tr>
  </tbody>
</table>
</div>




```python
test.chisq_indep_test(score)
print('학군과 성적은 상관이 있습니다.')
```

    유의수준을 입력하세요 : 0.05
    -----검정 결과-----
    검정통계량 : 22.317482
    p 값은 0.004360 입니다.
    귀무가설을 기각합니다.
    학군과 성적은 상관이 있습니다.
    


    
![png](output_3_1.png)
    


2. 등분산 데이터 T 검정


```python
data1 = np.random.randint(20,size = 30)
data2 = np.random.randint(20,size = 30)
print(np.mean(data1))
print(np.mean(data2))
```

    8.333333333333334
    9.066666666666666
    


```python
test.F_test(data1, data2)
```

    유의수준을 입력하세요 : 0.05
    -----검정 결과-----
    검정통계량 : 0.965867
    p 값은 0.463069 입니다.
    귀무가설을 채택합니다. 분산은 같습니다.
    


    
![png](output_6_1.png)
    



```python
test.two_sample_T(data1, data2)
```

    유의수준을 입력하세요 : 0.05
    1.정규성? 2.비정규성?
    None1
    1.독립표본? 2.대응표본?
    None1
    1. 등분산? 2.이분산?
    None1
    합동분산 독립표본 T 검정을 실행합니다.
    -----검정 결과-----
    검정통계량 : -0.001369
    신뢰구간 : -2.092184 < mu < 1.931864
    p 값은 0.499365 입니다.
    귀무가설을 채택합니다. 두 표본의 평균은 같습니다.
    


    
![png](output_7_1.png)
    



```python
test.one_sample_T(data1)
```

    유의수준을 입력하세요 : 0.05
    귀무가설로 설정할 평균값을 입력하세요 : 
    None10
    1.단측검정? 2.양측검정?
    None1
    1. mu > 10.000000 2. mu < 10.000000
    None1
    1표본 단측 T 검정을 실행합니다.
    -----검정 결과-----
    p 값은 0.759068 입니다.
    검정통계량 : -0.712476
    신뢰구간 : mu < 1.707415
    귀무가설을 채택합니다. 평균은 10.000000 입니다.
    


    
![png](output_8_1.png)
    


3. 이분산 데이터 T검정


```python
data1 = np.random.randint(20,size = 30)
data2 = np.random.randint(50,size = 30)
print(np.var(data1))
print(np.var(data2))
```

    29.115555555555556
    237.69000000000003
    


```python
test.F_test(data1, data2)
```

    유의수준을 입력하세요 : 0.05
    -----검정 결과-----
    검정통계량 : 0.118786
    p 값은 0.000000 입니다.
    귀무가설을 기각합니다. 분산은 다릅니다.
    


    
![png](output_11_1.png)
    



```python
test.two_sample_T(data1, data2)
```

    유의수준을 입력하세요 : 0.05
    1.정규성? 2.비정규성?
    None1
    1.독립표본? 2.대응표본?
    None1
    1. 등분산? 2.이분산?
    None2
    Welch T 검정을 실행합니다.
    p 값은 0.000807 입니다.
    -----검정 결과-----
    검정통계량 : -3.393405
    신뢰구간 : -2.140281 < mu < 1.963928
    귀무가설을 기각합니다. 두 표본의 평균은 다릅니다.
    


    
![png](output_12_1.png)
    

