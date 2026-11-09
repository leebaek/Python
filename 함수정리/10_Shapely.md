# 10. Shapely

> Shapely는 점·선·면 등 geometry 객체를 만들고 공간 관계 및 기하 연산을
> 수행하는 라이브러리다. GeoPandas의 geometry 연산 기반으로 자주
> 사용된다.

## `Point()`

**① 기능**\
점(Point) geometry를 생성한다.

**② 기본 문법**

``` python
from shapely.geometry import Point

Point(x, y)
```

**③ 매개변수** - `x`: X 좌표 - `y`: Y 좌표 - 필요하면 `z` 좌표도 지정할
수 있다.

**④ 사용 예제**

``` python
from shapely.geometry import Point

point = Point(127.0, 37.5)
```

## `LineString()`

**① 기능**\
두 개 이상의 좌표를 연결한 선(LineString) geometry를 생성한다.

**② 기본 문법**

``` python
from shapely.geometry import LineString

LineString([(x1, y1), (x2, y2), ...])
```

**③ 매개변수** - 좌표 튜플의 반복 가능한 객체

**④ 사용 예제**

``` python
from shapely.geometry import LineString

road = LineString([
    (127.0, 37.5),
    (127.01, 37.51),
    (127.02, 37.52)
])
```

## `Polygon()`

**① 기능**\
외곽 경계와 선택적인 내부 구멍으로 면(Polygon) geometry를 생성한다.

**② 기본 문법**

``` python
from shapely.geometry import Polygon

Polygon(shell, holes=None)
```

**③ 매개변수** - `shell`: 외곽 경계를 이루는 좌표 목록 - `holes`: 내부
구멍 좌표 목록(선택)

**④ 사용 예제**

``` python
from shapely.geometry import Polygon

area = Polygon([
    (127.0, 37.5),
    (127.1, 37.5),
    (127.1, 37.6),
    (127.0, 37.6),
    (127.0, 37.5)
])
```

## `geom.area`

**① 기능**\
Polygon 등 geometry의 면적을 반환한다.

**② 기본 문법**

``` python
geom.area
```

**③ 매개변수** - 없음. geometry 객체의 속성(property)이다.

**④ 사용 예제**

``` python
area_value = polygon.area
```

## `geom.length`

**① 기능**\
선 또는 geometry 경계 등의 길이를 반환한다.

**② 기본 문법**

``` python
geom.length
```

**③ 매개변수** - 없음. geometry 객체의 속성(property)이다.

**④ 사용 예제**

``` python
road_length = line.length
```

## `geom.bounds`

**① 기능**\
geometry를 둘러싸는 최소 경계 사각형의 좌표 범위를 반환한다.

**② 기본 문법**

``` python
geom.bounds
```

**③ 매개변수** - 없음. `(minx, miny, maxx, maxy)` 형태의 튜플을
반환한다.

**④ 사용 예제**

``` python
minx, miny, maxx, maxy = polygon.bounds
```

## `geom.is_valid`

**① 기능**\
geometry가 OGC 기준의 유효한 기하 구조인지 True 또는 False로 확인한다.

**② 기본 문법**

``` python
geom.is_valid
```

**③ 매개변수** - 없음. geometry 객체의 속성(property)이다.

**④ 사용 예제**

``` python
valid = polygon.is_valid
```

## `geom.is_empty`

**① 기능**\
geometry가 비어 있는지 True 또는 False로 확인한다.

**② 기본 문법**

``` python
geom.is_empty
```

**③ 매개변수** - 없음. geometry 객체의 속성(property)이다.

**④ 사용 예제**

``` python
if geom.is_empty:
    print("빈 geometry입니다.")
```

## `geom.intersects()`

**① 기능**\
두 geometry가 공간적으로 한 점이라도 공유하거나 겹치는지 확인한다.

**② 기본 문법**

``` python
geom.intersects(other)
```

**③ 매개변수** - `other`: 비교할 geometry

**④ 사용 예제**

``` python
is_intersect = road.intersects(district)
```

## `geom.contains()`

**① 기능**\
한 geometry가 다른 geometry를 내부에 완전히 포함하는지 확인한다.

**② 기본 문법**

``` python
geom.contains(other)
```

**③ 매개변수** - `other`: 포함 여부를 확인할 geometry

**④ 사용 예제**

``` python
is_inside = district.contains(point)
```

## `geom.within()`

**① 기능**\
한 geometry가 다른 geometry 내부에 있는지 확인한다. `contains()`의 반대
방향 관계다.

**② 기본 문법**

``` python
geom.within(other)
```

**③ 매개변수** - `other`: 포함 여부를 확인할 바깥 geometry

**④ 사용 예제**

``` python
is_inside = point.within(district)
```

## `geom.distance()`

**① 기능**\
두 geometry 사이의 최소 평면 거리를 계산한다.

**② 기본 문법**

``` python
geom.distance(other)
```

**③ 매개변수** - `other`: 거리를 계산할 geometry

**④ 사용 예제**

``` python
distance_value = point1.distance(point2)
```

## `geom.buffer()`

**① 기능**\
geometry로부터 지정한 거리만큼 확장된 영역(버퍼)을 생성한다.

**② 기본 문법**

``` python
geom.buffer(distance)
```

**③ 매개변수** - `distance`: 버퍼 거리. 좌표 단위 기준

**④ 사용 예제**

``` python
# 투영좌표계의 단위가 미터인 경우 100m 버퍼
buffer_area = road.buffer(100)
```

## `geom.intersection()`

**① 기능**\
두 geometry가 겹치는 부분을 반환한다.

**② 기본 문법**

``` python
geom.intersection(other)
```

**③ 매개변수** - `other`: 교차 영역을 계산할 geometry

**④ 사용 예제**

``` python
overlap = road_buffer.intersection(district)
```

## `geom.difference()`

**① 기능**\
한 geometry에서 다른 geometry와 겹치는 부분을 제외한 결과를 반환한다.

**② 기본 문법**

``` python
geom.difference(other)
```

**③ 매개변수** - `other`: 제거할 영역을 가진 geometry

**④ 사용 예제**

``` python
remaining_area = study_area.difference(exclusion_area)
```

## `shapely.make_valid()`

**① 기능**\
유효하지 않은 geometry를 가능한 범위에서 유효한 geometry로 수정한다.

**② 기본 문법**

``` python
shapely.make_valid(geometry)
```

**③ 매개변수** - `geometry`: 수정할 geometry

**④ 사용 예제**

``` python
import shapely

fixed_geometry = shapely.make_valid(polygon)
```

------------------------------------------------------------------------
