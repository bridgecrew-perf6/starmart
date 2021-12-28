<!-- markdownlint-disable -->

<a href="../starmart/result.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `result.py`






---

## <kbd>class</kbd> `BoundingBox`




<a href="../starmart/result.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(
    top_left_coordinate: Coordinate,
    bottom_right_coordinate: Coordinate,
    confidence: float,
    label: str
)
```









---

## <kbd>class</kbd> `Classification`




<a href="../starmart/result.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(label: str, confidence: float)
```









---

## <kbd>class</kbd> `ClassificationResult`




<a href="../starmart/result.py#L89"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(classifications: List[Classification])
```








---

<a href="../starmart/result.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `CompositeResult`




<a href="../starmart/result.py#L126"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(results: List[NamedResult])
```








---

<a href="../starmart/result.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `Coordinate`




<a href="../starmart/result.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(x, y)
```









---

## <kbd>class</kbd> `Failure`




<a href="../starmart/result.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(error)
```








---

<a href="../starmart/result.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `GenericArrayResult`




<a href="../starmart/result.py#L146"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(value: List)
```








---

<a href="../starmart/result.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `GenericResult`




<a href="../starmart/result.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(value)
```








---

<a href="../starmart/result.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `ImageResult`




<a href="../starmart/result.py#L97"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(image: bytes)
```








---

<a href="../starmart/result.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `Labeled`




<a href="../starmart/result.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(label: str)
```









---

## <kbd>class</kbd> `NamedResult`




<a href="../starmart/result.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(name: str, result: Result)
```








---

<a href="../starmart/result.py#L121"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `ObjectDetectionResult`




<a href="../starmart/result.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(bounding_boxes: List[BoundingBox])
```








---

<a href="../starmart/result.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `Result`




<a href="../starmart/result.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__()
```








---

<a href="../starmart/result.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `SegmentationMask`




<a href="../starmart/result.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(coordinates: List[Coordinate], label: str)
```









---

## <kbd>class</kbd> `SegmentationResult`




<a href="../starmart/result.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(segmentation: SegmentationMask)
```








---

<a href="../starmart/result.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `Success`




<a href="../starmart/result.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(value)
```








---

<a href="../starmart/result.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `TextResult`




<a href="../starmart/result.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(text: str)
```








---

<a href="../starmart/result.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
