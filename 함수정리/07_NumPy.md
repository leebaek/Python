# 7. NumPy

> NumPy는 숫자 배열을 빠르게 처리하는 라이브러리다. 일반 Python
> 리스트보다 대규모 수치 연산에 효율적이며 Pandas와 GeoPandas의 기반이
> 된다.

## `np.array()`

**① 기능**\
리스트 등의 데이터를 NumPy 배열(ndarray)로 만든다.

**② 기본 문법**

``` python
np.array(object, dtype=None)
```

**③ 매개변수** - `object`: 배열로 만들 데이터 - `dtype`: 배열의 자료형

**④ 사용 예제**

``` python
import numpy as np

coordinates = np.array([[127.0, 37.5], [129.0, 35.2]])
```

## `np.arange()`

**① 기능**\
지정한 간격으로 숫자 배열을 생성한다.

**② 기본 문법**

``` python
np.arange(start, stop, step)
```

**③ 매개변수** - `start`: 시작값 - `stop`: 끝값(포함하지 않음) - `step`:
증가 간격

**④ 사용 예제**

``` python
import numpy as np

ids = np.arange(1, 6)
# array([1, 2, 3, 4, 5])
```

## `np.zeros()` / `np.ones()`

**① 기능**\
지정한 크기의 배열을 0 또는 1로 채워 생성한다.

**② 기본 문법**

``` python
np.zeros(shape, dtype=float)
np.ones(shape, dtype=float)
```

**③ 매개변수** - `shape`: 배열의 크기 또는 차원 - `dtype`: 자료형

**④ 사용 예제**

``` python
import numpy as np

empty_values = np.zeros(5)
one_values = np.ones((2, 3))
```

## `reshape()`

**① 기능**\
배열의 요소 수를 유지하면서 배열의 모양(차원)을 변경한다.

**② 기본 문법**

``` python
array.reshape(newshape)
```

**③ 매개변수** - `newshape`: 변경할 배열 모양

**④ 사용 예제**

``` python
import numpy as np

values = np.array([1, 2, 3, 4, 5, 6])
matrix = values.reshape(2, 3)
```

## `np.where()`

**① 기능**\
조건에 맞는 위치를 찾거나 조건에 따라 값을 선택한다.

**② 기본 문법**

``` python
np.where(condition, x, y)
```

**③ 매개변수** - `condition`: 참·거짓 조건 - `x`: 조건이 True일 때
선택할 값 - `y`: 조건이 False일 때 선택할 값

**④ 사용 예제**

``` python
import numpy as np

values = np.array([10, 20, 30, 40])
result = np.where(values >= 30, "대상", "제외")
```

## `np.isnan()`

**① 기능**\
배열 요소가 NaN(숫자가 아님/결측을 나타내는 부동소수점 값)인지 검사한다.

**② 기본 문법**

``` python
np.isnan(array)
```

**③ 매개변수** - `array`: 검사할 숫자 배열 또는 숫자형 값

**④ 사용 예제**

``` python
import numpy as np

values = np.array([1.0, np.nan, 3.0])
missing = np.isnan(values)
```

## `np.unique()`

**① 기능**\
배열에서 중복을 제거한 고유값을 반환한다.

**② 기본 문법**

``` python
np.unique(array, return_counts=False)
```

**③ 매개변수** - `array`: 검사할 배열 - `return_counts`: 각 고유값의
개수도 반환할지 여부

**④ 사용 예제**

``` python
import numpy as np

regions = np.array(["서울", "부산", "서울", "인천"])
unique_regions, counts = np.unique(regions, return_counts=True)
```

## `np.nanmean()` / `np.nanmax()` / `np.nanmin()`

**① 기능**\
NaN 값을 제외하고 평균·최댓값·최솟값을 계산한다.

**② 기본 문법**

``` python
np.nanmean(array)
np.nanmax(array)
np.nanmin(array)
```

**③ 매개변수** - `array`: 계산할 배열

**④ 사용 예제**

``` python
import numpy as np

values = np.array([10.0, np.nan, 30.0])
average = np.nanmean(values)
```

------------------------------------------------------------------------
