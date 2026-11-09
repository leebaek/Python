# 8. Pandas

> Pandas는 표 형태의 데이터를 읽고, 정리하고, 필터링하고, 저장하는 데
> 사용하는 라이브러리다. CSV·엑셀·속성 테이블 처리에 특히 유용하다.

## `pd.read_csv()`

**① 기능**\
CSV 파일을 읽어 DataFrame으로 만든다.

**② 기본 문법**

``` python
pd.read_csv(filepath, encoding=None)
```

**③ 매개변수** - `filepath`: CSV 파일 경로 - `encoding`: 문자 인코딩 -
자주 쓰는 추가 옵션: `dtype`, `usecols`, `na_values`

**④ 사용 예제**

``` python
import pandas as pd

df = pd.read_csv(
    "road_data.csv",
    encoding="utf-8",
    dtype={"road_code": "string"}
)
```

## `pd.read_excel()`

**① 기능**\
엑셀 파일을 읽어 DataFrame으로 만든다.

**② 기본 문법**

``` python
pd.read_excel(io, sheet_name=0)
```

**③ 매개변수** - `io`: 엑셀 파일 경로 - `sheet_name`: 읽을 시트 이름
또는 번호 - 자주 쓰는 추가 옵션: `usecols`, `dtype`, `header`

**④ 사용 예제**

``` python
import pandas as pd

df = pd.read_excel("road_data.xlsx", sheet_name="도로목록")
```

## `DataFrame.head()` / `tail()`

**① 기능**\
DataFrame의 처음 또는 마지막 몇 행을 확인한다.

**② 기본 문법**

``` python
df.head(n=5)
df.tail(n=5)
```

**③ 매개변수** - `n`: 표시할 행 수

**④ 사용 예제**

``` python
df.head()
df.tail(10)
```

## `DataFrame.info()`

**① 기능**\
DataFrame의 행 수, 컬럼명, 자료형, 결측이 아닌 값의 개수 등을 요약해
출력한다.

**② 기본 문법**

``` python
df.info()
```

**③ 매개변수** - 자주 쓰는 옵션: `show_counts`, `memory_usage`

**④ 사용 예제**

``` python
df.info()
```

## `DataFrame.describe()`

**① 기능**\
숫자형 컬럼의 개수, 평균, 표준편차, 최솟값, 사분위수, 최댓값 등을
요약한다.

**② 기본 문법**

``` python
df.describe()
```

**③ 매개변수** - `include`: 포함할 자료형 지정 - `percentiles`: 표시할
사분위수 지정

**④ 사용 예제**

``` python
df.describe()
df.describe(include="all")
```

## `DataFrame.isna()` / `notna()`

**① 기능**\
각 셀의 결측 여부를 True 또는 False로 표시한다.

**② 기본 문법**

``` python
df.isna()
df.notna()
```

**③ 매개변수** - 없음

**④ 사용 예제**

``` python
missing_by_column = df.isna().sum()
```

## `DataFrame.dropna()`

**① 기능**\
결측값이 포함된 행 또는 열을 제거한다.

**② 기본 문법**

``` python
df.dropna(axis=0, how="any")
```

**③ 매개변수** - `axis=0`: 행 기준, `axis=1`: 열 기준 - `how="any"`:
하나라도 결측이면 제거 - `how="all"`: 모두 결측일 때 제거 - `subset`:
특정 컬럼만 검사

**④ 사용 예제**

``` python
clean_df = df.dropna(subset=["road_code", "road_name"])
```

## `DataFrame.fillna()`

**① 기능**\
결측값을 지정한 값이나 방법으로 채운다.

**② 기본 문법**

``` python
df.fillna(value)
```

**③ 매개변수** - `value`: 대체할 값 또는 컬럼별 대체값 딕셔너리 -
`method`: 앞/뒤 값으로 채우는 방식(버전에 따라 사용 방식 확인)

**④ 사용 예제**

``` python
df["remark"] = df["remark"].fillna("")
df["width"] = df["width"].fillna(0)
```

## `DataFrame.loc[]`

**① 기능**\
행·열의 라벨을 기준으로 데이터를 선택하거나 수정한다.

**② 기본 문법**

``` python
df.loc[row_condition, column_labels]
```

**③ 매개변수** - 첫 번째 위치: 행 라벨 또는 조건 - 두 번째 위치: 컬럼명
또는 컬럼 목록

**④ 사용 예제**

``` python
# 도로 폭이 20 이상인 행의 코드와 폭 선택
result = df.loc[df["width"] >= 20, ["road_code", "width"]]

# 조건에 맞는 값 수정
df.loc[df["width"] < 0, "width"] = None
```

## `DataFrame.iloc[]`

**① 기능**\
행·열의 정수 위치를 기준으로 데이터를 선택한다.

**② 기본 문법**

``` python
df.iloc[row_position, column_position]
```

**③ 매개변수** - 행과 열의 정수 위치 또는 슬라이스

**④ 사용 예제**

``` python
first_row = df.iloc[0]
first_three_rows = df.iloc[:3]
```

## `DataFrame.groupby()`

**① 기능**\
특정 컬럼의 값에 따라 데이터를 그룹으로 나누어 집계한다.

**② 기본 문법**

``` python
df.groupby(by)
```

**③ 매개변수** - `by`: 그룹 기준 컬럼명 - 이후 `sum()`, `mean()`,
`count()`, `size()` 등 집계 메서드를 연결한다.

**④ 사용 예제**

``` python
# 행정구역별 도로 건수
count_by_region = df.groupby("region")["road_code"].count()

# 행정구역별 도로 폭 평균
mean_width = df.groupby("region")["width"].mean()
```

## `DataFrame.merge()`

**① 기능**\
공통 컬럼을 기준으로 두 DataFrame을 결합한다.

**② 기본 문법**

``` python
pd.merge(left, right, on="key", how="inner")
```

**③ 매개변수** - `left`, `right`: 결합할 DataFrame - `on`: 공통 키
컬럼 - `how`: 결합 방식(`inner`, `left`, `right`, `outer`)

**④ 사용 예제**

``` python
result = pd.merge(
    roads,
    code_table,
    on="road_code",
    how="left"
)
```

## `pd.concat()`

**① 기능**\
여러 DataFrame을 행 또는 열 방향으로 이어 붙인다.

**② 기본 문법**

``` python
pd.concat(objs, axis=0, ignore_index=False)
```

**③ 매개변수** - `objs`: 결합할 DataFrame 목록 - `axis=0`: 행 방향으로
결합 - `axis=1`: 열 방향으로 결합 - `ignore_index`: 새 인덱스 부여 여부

**④ 사용 예제**

``` python
all_roads = pd.concat(
    [seoul_roads, busan_roads],
    ignore_index=True
)
```

## `DataFrame.drop_duplicates()`

**① 기능**\
지정한 기준으로 중복 행을 제거한다.

**② 기본 문법**

``` python
df.drop_duplicates(subset=None, keep="first")
```

**③ 매개변수** - `subset`: 중복 판단에 사용할 컬럼 - `keep`: 유지할
항목(`first`, `last`, `False`)

**④ 사용 예제**

``` python
unique_roads = df.drop_duplicates(subset=["road_code"])
```

## `DataFrame.astype()`

**① 기능**\
하나 이상의 컬럼 자료형을 변환한다.

**② 기본 문법**

``` python
df.astype(dtype)
```

**③ 매개변수** - `dtype`: 변환할 자료형 또는 컬럼별 자료형 딕셔너리

**④ 사용 예제**

``` python
df["road_code"] = df["road_code"].astype("string")
df["width"] = df["width"].astype("float64")
```

## `DataFrame.value_counts()`

**① 기능**\
컬럼 또는 행 조합별 빈도를 계산한다.

**② 기본 문법**

``` python
series.value_counts(dropna=True)
```

**③ 매개변수** - `dropna`: 결측값을 집계에서 제외할지 여부 -
`normalize`: 비율로 반환할지 여부

**④ 사용 예제**

``` python
df["region"].value_counts()
df["region"].value_counts(normalize=True)
```

## `DataFrame.to_csv()` / `to_excel()`

**① 기능**\
DataFrame을 CSV 또는 엑셀 파일로 저장한다.

**② 기본 문법**

``` python
df.to_csv(path, index=False, encoding="utf-8-sig")
df.to_excel(path, index=False)
```

**③ 매개변수** - `path`: 저장 경로 - `index`: 인덱스 저장 여부 -
`encoding`: CSV 문자 인코딩

**④ 사용 예제**

``` python
df.to_csv("cleaned_roads.csv", index=False, encoding="utf-8-sig")
df.to_excel("cleaned_roads.xlsx", index=False)
```

------------------------------------------------------------------------
