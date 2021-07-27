---
layout: post
title:  "확률분포의 정의"
---

```python
import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
import seaborn as sns
import sympy as sp
import sympy.stats as stats
from sympy.plotting import plot
from sympy import Symbol
from scipy.integrate import quad
import pandas as pd
```

### 1.카이제곱분포

+ 카이제곱분포의 누적분포함수를 정의하여 확률계산하기


```python
## 누적분포함수

def chi_cdf(df, up_b):
    chi = lambda x:(x**((df/2)-1) * sp.E**(-x/2)) / (2**(df/2) * sp.gamma(df/2))
    prob = quad(chi, 0, up_b)
    return prob[0]


## 정의역 구간을 입력받아 확률을 계산하는 함수

def chi_prob(df, low_b, up_b):
    chi = lambda x:(x**((df/2)-1) * sp.E**(-x/2)) / (2**(df/2) * sp.gamma(df/2))
    prob = quad(chi, low_b, up_b)
    return prob[0]

```

+ 그래프 그리기


```python
## 자유도를 입력받아 그래프 그리기

def chi_plot(df):
    
    # x축을 linspace로 정의
    
    list_x=[]
    list_x=np.linspace(0,4*df,10*df)

    # x축의 범위와 간격은 자유도에 비례하게 설정한다.

    list_y=[]
    for i in range(len(list_x)):
        y = (list_x[i]**((df/2)-1) * sp.E**(-list_x[i]/2)) / 2**(df/2) * sp.gamma(df/2)
        list_y.append(y)

    plt.figure(figsize=(10,5))
    plt.plot(list_x,list_y,label = 'chi-square distribution with df %d' %df)
    plt.legend(loc = 'upper right')
    plt.ylabel('Probability')


```


```python
## 입력받은 상한 up_b의 x축에서 가장 가까운 값을 찾아주는 함수

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]
```


```python
## 누적분포함수를 그리고 그 확률을 표시하기


def chi_cdf_plot(df, up_b):
    up_b = int(up_b)
    list_x=np.linspace(0,5*df,10*df)
    list_x = list(list_x)

    list_y=[]
    for i in range(len(list_x)):
        y = (list_x[i]**((df/2)-1) * sp.E**(-list_x[i]/2)) / 2**(df/2) * sp.gamma(df/2)
        list_y.append(y)

    list_x = list(map(float, list_x))
    list_y = list(map(float, list_y))


    ## list_x 에서 up_b 와 가까운 값을 찾아 그 인덱스 번호를 찾는다.

    plt.figure(figsize=(10,5))
    plt.plot(list_x,list_y, label = 'cumulative probability of chi-square(%d)'% df)
    plt.legend(loc = 'upper right')
    plt.fill_between(list_x[0:list_x.index(find_nearest(list_x, up_b))],
                     list_y[0:list_x.index(find_nearest(list_x, up_b))],
                     )
    plt.ylabel('f(x)')

    plt.text(up_b, 
            max(list_y)/2, 
           'probability : %f' % chi_cdf(df, up_b))


```


```python
## X축 구간을 입력받아 그래프를 그리고 그 확률값을 구하기

def chi_prob_plot(df, low_b, up_b):
    k = df
    up_b = int(up_b)
    low_b = int(low_b)
    list_x=np.linspace(0,4*k,10*k)
    list_x = list(list_x)

    list_y=[]
    for i in range(len(list_x)):
        y = (list_x[i]**((k/2)-1) * sp.E**(-list_x[i]/2)) / 2**(k/2) * sp.gamma(k/2)
        list_y.append(y)

    list_x = list(map(float, list_x))
    list_y = list(map(float, list_y))


    ## list_x 에서 up_b 와 가까운 값을 찾아 그 인덱스 번호를 찾는다.

    plt.figure(figsize=(10,5))
    plt.plot(list_x,list_y, label = 'probability of chi-square(%d)'%k)
    plt.legend(loc = 'upper right')
    plt.fill_between(list_x[list_x.index(find_nearest(list_x, low_b)):list_x.index(find_nearest(list_x, up_b))],
                     list_y[list_x.index(find_nearest(list_x, low_b)):list_x.index(find_nearest(list_x, up_b))],
                     )
    plt.ylabel('f(x)')
    plt.text(up_b, 
             max(list_y)/2, 
             'probability : %f' %chi_prob(df, low_b, up_b))

```

### 2. T 분포

+ T 분포의 확률밀도함수를 정의


```python
def T_cdf(df, up_b):
    student = lambda x:((sp.gamma((df+1)/2))/(((df*sp.pi)**(1/2))*sp.gamma(df/2)))\
    *((1+((x**2)/df))**-((df+1)/2))
    return quad(student, float('-inf'), up_b)[0]

## 정의역 구간을 입력받아 확률을 계산하는 함수

def T_prob(df, low_b, up_b):
    student = lambda x:((sp.gamma((df+1)/2))/(((df*sp.pi)**(1/2))*sp.gamma(df/2)))\
    *((1+((x**2)/df))**-((df+1)/2))
    return quad(student, low_b, up_b)[0]

```

+ T 분포의 그래프 그리기


```python
def T_plot(df):
    list_x = np.linspace(-4, 4, 500)
    list_x = list(list_x)

    list_y = []
    for i in range(len(list_x)):
        student = lambda x: ((sp.gamma((df + 1) / 2)) / (((df * sp.pi) ** (1 / 2)) * sp.gamma(df / 2))) \
                            * ((1 + ((x ** 2) / df)) ** -((df + 1) / 2))
        y = quad(student, list_x[i], list_x[i] + 0.0001)[0]
        list_y.append(y)

    list_x = list(map(float, list_x))
    list_y = list(map(float, list_y))

    plt.figure(figsize=(10, 5))
    plt.plot(list_x, list_y, label='T distribution of df(%d)' % df)
    plt.legend(loc='upper right')
    plt.ylabel('P(x)')

```


```python
## T 분포는 자유도에 따른 그래프의 모양 차이가 없으므로, 생략한다.
## 누적분포함수를 그리고 그 확률을 표시하기
def T_cdf_plot(df, up_b):

    # 확률변수 T의 정의역을 임의로 -4~4로 설정한다. -4~4에서 전체 확률은 1과 근사하다.
    list_x=np.linspace(-4,4,500)
    list_x = list(list_x)

    list_y=[]
    for i in range(len(list_x)):
        student = lambda x:((sp.gamma((df+1)/2))/(((df*sp.pi)**(1/2))*sp.gamma(df/2)))\
        *((1+((x**2)/df))**-((df+1)/2))
        y = quad(student, list_x[i], list_x[i]+0.0001)[0]
        list_y.append(y)

    ## 그래프의 y 값이 함수값이 아닌 확률값이므로, 적분범위를 x, x+0.0001로 설정하여 적분값을 
    ## list_y에 대입한다.

    list_x = list(map(float, list_x))
    list_y = list(map(float, list_y))


    plt.figure(figsize=(10,5))
    plt.plot(list_x,list_y, label = 'cumulative probability of T(%d)'% df)
    plt.legend(loc = 'upper right')
    plt.fill_between(list_x[0:list_x.index(find_nearest(list_x, up_b))],
                     list_y[0:list_x.index(find_nearest(list_x, up_b))],
                     )
    plt.ylabel('P(x)')

    plt.text(up_b, 
            max(list_y)/2, 
           'probability : %f' % T_cdf(df, up_b))

```


```python
## X축 구간을 입력받아 그래프를 그리고 그 확률값을 구하기

def T_prob_plot(df, low_b, up_b):

    # 확률변수 T의 정의역을 임의로 -4~4로 설정한다. -4~4에서 전체 확률은 1과 근사하다.
    list_x=np.linspace(-4,4,500)
    list_x = list(list_x)

    list_y=[]
    for i in range(len(list_x)):
        student = lambda x:((sp.gamma((df+1)/2))/(((df*sp.pi)**(1/2))*sp.gamma(df/2)))\
        *((1+((x**2)/df))**-((df+1)/2))
        y = quad(student, list_x[i], list_x[i]+0.0001)[0]
        list_y.append(y)

    ## 그래프의 y 값이 함수값이 아닌 확률값이므로, 적분범위를 x, x+0.0001로 설정하여 적분값을 
    ## list_y에 대입한다.

    list_x = list(map(float, list_x))
    list_y = list(map(float, list_y))


    plt.figure(figsize=(10,5))
    plt.plot(list_x,list_y, label = 'probability of T(%d)'% df)
    plt.legend(loc = 'upper right')
    plt.fill_between(list_x[list_x.index(find_nearest(list_x, low_b)):list_x.index(find_nearest(list_x, up_b))],
                     list_y[list_x.index(find_nearest(list_x, low_b)):list_x.index(find_nearest(list_x, up_b))],
                     )
    plt.ylabel('P(x)')

    plt.text(up_b, 
            max(list_y)/up_b, 
           'probability : %f' % T_prob(df, low_b ,up_b))

```

### 3. F 분포

+ F분포의 확률밀도함수를 정의


```python
def F_cdf(df1, df2, up_b):
    f = lambda x:(1/sp.beta(df1/2, df2/2))*((df1/df2)**(df1/2))*(x**((df1/2)-1))\
                *((1+(x*df1/df2))**(-(df1+df2)/2))
    return quad(f, 0, up_b)[0]


def F_prob(df1, df2, low_b, up_b):
    return (F_cdf(df1, df2, up_b) - F_cdf(df1, df2, low_b))


```

+ F 분포 그래프 그리기


```python
def F_plot(df1, df2):
    list_x=np.linspace(0,(df1+df2)*1.2,1000)
    list_x = list(list_x)

    list_y=[]
    for i in range(len(list_x)):
        y = (1/sp.beta(df1/2, df2/2))*((df1/df2)**(df1/2))*(list_x[i]**((df1/2)-1))\
                *((1+(list_x[i]*df1/df2))**(-(df1+df2)/2))
        list_y.append(y)

    list_x = list(map(float, list_x))
    list_y = list(map(float, list_y))

    plt.figure(figsize=(10,5))
    plt.plot(list_x,list_y, label = 'F distribution with df (%d, %d)'% (df1, df2))
    plt.legend(loc = 'upper right')

```


```python
def F_cdf_plot(df1, df2, up_b):
    up_b = int(up_b)
    list_x=np.linspace(0,(df1+df2)*1.2,1000)
    list_x = list(list_x)

    list_y=[]
    for i in range(len(list_x)):
        y = (1/sp.beta(df1/2, df2/2))*((df1/df2)**(df1/2))*(list_x[i]**((df1/2)-1))\
                *((1+(list_x[i]*df1/df2))**(-(df1+df2)/2))
        list_y.append(y)

    list_x = list(map(float, list_x))
    list_y = list(map(float, list_y))



    plt.figure(figsize=(10,5))
    plt.plot(list_x,list_y, label = 'cumulative probability of F(%d, %d)'% (df1, df2))
    plt.legend(loc = 'upper right')
    plt.fill_between(list_x[0:list_x.index(find_nearest(list_x, up_b))],
                     list_y[0:list_x.index(find_nearest(list_x, up_b))],
                     )
    plt.ylabel('f(x)')

    plt.text(up_b, 
            max(list_y)/2, 
           'probability : %f' % F_cdf(df1, df2, up_b))


```


```python
def F_prob_plot(df1, df2, low_b, up_b):
    up_b = int(up_b)
    low_b = int(low_b)
    list_x=np.linspace(0,(df1+df2)*1.2,1000)
    list_x = list(list_x)

    list_y=[]
    for i in range(len(list_x)):
        y = (1/sp.beta(df1/2, df2/2))*((df1/df2)**(df1/2))*(list_x[i]**((df1/2)-1))\
                *((1+(list_x[i]*df1/df2))**(-(df1+df2)/2))
        list_y.append(y)

    list_x = list(map(float, list_x))
    list_y = list(map(float, list_y))


    plt.figure(figsize=(10,5))
    plt.plot(list_x,list_y, label = 'cumulative probability of F(%d, %d)'% (df1, df2))
    plt.legend(loc = 'upper right')
    plt.fill_between(list_x[list_x.index(find_nearest(list_x, low_b)):list_x.index(find_nearest(list_x, up_b))],
                     list_y[list_x.index(find_nearest(list_x, low_b)):list_x.index(find_nearest(list_x, up_b))],
                     )
    plt.ylabel('f(x)')
    plt.text(up_b, 
             max(list_y)/2, 
             'probability : %f' %F_prob(df1, df2, low_b, up_b))

```
