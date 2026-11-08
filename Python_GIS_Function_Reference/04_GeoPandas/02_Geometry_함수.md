# 02. Geometry 함수와 속성

Geometry는 점(Point), 선(LineString), 면(Polygon) 등의 공간 형상입니다.

## 1) Geometry 기본 확인

| 속성·메서드 | 기능 |
|---|---|
| `gdf.geometry` | Geometry 컬럼 접근 |
| `gdf.geom_type` | Geometry 유형 확인 |
| `gdf.geometry.area` | 면적 계산 |
| `gdf.geometry.length` | 길이 계산 |
| `gdf.geometry.bounds` | 객체별 경계 상자 |
| `gdf.total_bounds` | 전체 데이터 경계 |
| `gdf.geometry.is_empty` | 빈 Geometry 여부 |
| `gdf.geometry.is_valid` | 유효성 여부 |
| `gdf.geometry.is_valid_reason` | 유효하지 않은 이유(지원 버전 확인) |

## 2) Geometry 수정·변환

| 메서드 | 기능 | 예 |
|---|---|---|
| `buffer(distance)` | 주변 영역 생성 | `gdf.geometry.buffer(10)` |
| `centroid` | 중심점 | `gdf.geometry.centroid` |
| `representative_point()` | 내부에 위치하는 대표점 | `gdf.geometry.representative_point()` |
| `convex_hull` | 볼록껍질 | `gdf.geometry.convex_hull` |
| `simplify(tolerance)` | 형상 단순화 | `gdf.geometry.simplify(1)` |
| `boundary` | 경계 추출 | `gdf.geometry.boundary` |
| `make_valid()` | 유효한 형상으로 보정 | `gdf.geometry.make_valid()` |
| `set_precision()` | 좌표 정밀도 설정 | 버전·데이터 조건 확인 후 사용 |

## 3) 공간 연산
- `intersection()`: 교차 부분
- `union()`: 합집합 형상
- `difference()`: 한 형상에서 다른 형상을 뺀 부분
- `symmetric_difference()`: 서로 겹치지 않는 부분의 합

```python
intersection_geom = geom_a.intersection(geom_b)
```

## 4) 실무 예제: Geometry 검수
```python
invalid = gdf[~gdf.geometry.is_valid]
empty = gdf[gdf.geometry.is_empty]
print("유효하지 않은 형상:", len(invalid))
print("빈 형상:", len(empty))
```

## 5) 중요 주의사항
- `area`, `length`, `buffer()`의 단위는 좌표계 단위에 영향을 받습니다.
- 경위도 좌표계(EPSG:4326)에서 면적·길이를 평면 단위처럼 계산하면 부정확하거나 단위 해석이 잘못될 수 있습니다.
- 거리·면적 계산 전에 적절한 투영좌표계로 `to_crs()` 변환합니다.
- `make_valid()` 결과는 MultiPolygon 또는 GeometryCollection 등이 될 수 있습니다. 결과 유형과 피처 수를 재검사합니다.
- `centroid`는 폴리곤 바깥에 위치할 수도 있습니다. 내부 점이 필요하면 `representative_point()`를 검토합니다.
