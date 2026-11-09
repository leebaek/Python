# 9. GeoPandas

> GeoPandas는 Pandas DataFrame에 공간정보 기능을 더한 라이브러리다. SHP,
> GeoJSON, GeoPackage 등의 공간 데이터를 읽고, 속성 및 공간 연산을
> 수행할 수 있다.

## `gpd.read_file()`

**① 기능**\
SHP, GeoJSON, GeoPackage 등 공간 파일을 읽어 GeoDataFrame으로 만든다.

**② 기본 문법**

``` python
gpd.read_file(filename, layer=None)
```

**③ 매개변수** - `filename`: 공간 파일 경로 - `layer`: GeoPackage 등에서
읽을 레이어명 - 자주 쓰는 추가 옵션: `columns`, `bbox`, `where` 등(지원
여부는 드라이버 확인)

**④ 사용 예제**

``` python
import geopandas as gpd

gdf = gpd.read_file("roads.shp")
```

## `GeoDataFrame.to_file()`

**① 기능**\
GeoDataFrame을 SHP, GeoJSON, GeoPackage 등의 공간 파일로 저장한다.

**② 기본 문법**

``` python
gdf.to_file(filename, driver=None, layer=None)
```

**③ 매개변수** - `filename`: 저장 경로 - `driver`: 저장 형식 드라이버 -
`layer`: GeoPackage 레이어명

**④ 사용 예제**

``` python
gdf.to_file("roads_out.gpkg", layer="roads", driver="GPKG")
```

## `GeoDataFrame.to_crs()`

**① 기능**\
GeoDataFrame의 좌표를 다른 좌표참조체계(CRS)로 변환한다.

**② 기본 문법**

``` python
gdf.to_crs(crs)
```

**③ 매개변수** - `crs`: 변환할 CRS(EPSG 코드 또는 CRS 정의)

**④ 사용 예제**

``` python
# 예: WGS84 경위도에서 국내 투영좌표계로 변환
projected = gdf.to_crs(epsg=5179)
```

## `GeoDataFrame.set_crs()`

**① 기능**\
현재 좌표값이 어떤 좌표참조체계인지 지정하거나 CRS 메타데이터를
설정한다.

**② 기본 문법**

``` python
gdf.set_crs(crs, allow_override=False)
```

**③ 매개변수** - `crs`: 지정할 CRS - `allow_override`: 기존 CRS 정보를
덮어쓸지 여부

**④ 사용 예제**

``` python
# 좌표값이 실제로 EPSG:4326인 것이 확인된 경우
gdf = gdf.set_crs(epsg=4326)
```

## `GeoDataFrame.plot()`

**① 기능**\
GeoDataFrame의 geometry를 간단히 지도 형태로 시각화한다.

**② 기본 문법**

``` python
gdf.plot(column=None, figsize=(10, 10))
```

**③ 매개변수** - `column`: 색상 구분에 사용할 속성 컬럼 - `figsize`:
그림 크기 - 자주 쓰는 옵션: `legend`, `cmap`, `edgecolor`

**④ 사용 예제**

``` python
ax = gdf.plot(figsize=(8, 8), edgecolor="black")
```

## `GeoDataFrame.sjoin()`

**① 기능**\
두 GeoDataFrame을 공간 관계를 기준으로 결합한다.

**② 기본 문법**

``` python
gpd.sjoin(left_df, right_df, how="inner", predicate="intersects")
```

**③ 매개변수** - `left_df`, `right_df`: 결합할 공간 데이터 - `how`: 결합
방식(`inner`, `left`, `right`) - `predicate`: 공간 관계(`intersects`,
`within`, `contains` 등)

**④ 사용 예제**

``` python
# 도로와 행정구역의 공간 관계를 연결하는 예
joined = gpd.sjoin(
    roads,
    districts,
    how="left",
    predicate="intersects"
)
```

## `gpd.overlay()`

**① 기능**\
두 GeoDataFrame의 공간 중첩 연산 결과를 새로운 GeoDataFrame으로 만든다.

**② 기본 문법**

``` python
gpd.overlay(df1, df2, how="intersection")
```

**③ 매개변수** - `df1`, `df2`: 중첩할 GeoDataFrame - `how`:
`intersection`, `union`, `identity`, `difference`,
`symmetric_difference`

**④ 사용 예제**

``` python
overlap = gpd.overlay(roads_area, admin_areas, how="intersection")
```

## `GeoDataFrame.clip()`

**① 기능**\
한 GeoDataFrame의 geometry를 다른 영역 경계로 잘라낸다.

**② 기본 문법**

``` python
gpd.clip(gdf, mask)
```

**③ 매개변수** - `gdf`: 잘라낼 데이터 - `mask`: 자르기
경계(GeoDataFrame, GeoSeries 또는 geometry)

**④ 사용 예제**

``` python
# 관심 지역 경계 안쪽의 도로만 남기기
roads_in_area = gpd.clip(roads, study_area)
```

## `GeoDataFrame.explode()`

**① 기능**\
Multi-part geometry를 여러 행으로 분리한다.

**② 기본 문법**

``` python
gdf.explode(index_parts=False)
```

**③ 매개변수** - `index_parts`: 분리된 geometry의 인덱스 구성 방식

**④ 사용 예제**

``` python
single_parts = gdf.explode(index_parts=False)
```

## `GeoDataFrame.to_postgis()`

**① 기능**\
GeoDataFrame을 PostGIS 데이터베이스 테이블로 저장한다.

**② 기본 문법**

``` python
gdf.to_postgis(name, con, if_exists="fail")
```

**③ 매개변수** - `name`: 저장할 테이블명 - `con`: SQLAlchemy
데이터베이스 연결 - `if_exists`: 테이블이 있을 때 처리 방식(`fail`,
`replace`, `append`) - 자주 쓰는 추가 옵션: `schema`, `index`,
`chunksize`

**④ 사용 예제**

``` python
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://user:password@localhost:5432/gis"
)

gdf.to_postgis(
    name="roads",
    con=engine,
    if_exists="replace",
    index=False
)
```

## `gpd.read_postgis()`

**① 기능**\
PostGIS SQL 쿼리 결과를 GeoDataFrame으로 읽어온다.

**② 기본 문법**

``` python
gpd.read_postgis(sql, con, geom_col="geom")
```

**③ 매개변수** - `sql`: geometry 컬럼을 포함한 SQL 쿼리 - `con`:
데이터베이스 연결 - `geom_col`: geometry 컬럼명

**④ 사용 예제**

``` python
sql = "SELECT * FROM roads"
roads = gpd.read_postgis(sql, engine, geom_col="geom")
```

------------------------------------------------------------------------
