<!-- markdownlint-disable -->

<a href="../starmart/helper.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `helper.py`






---

## <kbd>class</kbd> `BoundingBox`




<a href="../starmart/helper.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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




<a href="../starmart/helper.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(label: str, confidence: float)
```









---

## <kbd>class</kbd> `ClassificationResult`




<a href="../starmart/helper.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(classifications: List[Classification], metadata=None)
```








---

<a href="../starmart/helper.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `CompositeResult`




<a href="../starmart/helper.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(results: List[NamedResult], metadata=None)
```








---

<a href="../starmart/helper.py#L139"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `Coordinate`




<a href="../starmart/helper.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(x, y)
```









---

## <kbd>class</kbd> `Failure`




<a href="../starmart/helper.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(error)
```








---

<a href="../starmart/helper.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `GenericArrayResult`




<a href="../starmart/helper.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(value: List, metadata=None)
```








---

<a href="../starmart/helper.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `GenericResult`




<a href="../starmart/helper.py#L144"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(value, metadata=None)
```








---

<a href="../starmart/helper.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `ImageResult`




<a href="../starmart/helper.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(image: bytes, metadata=None)
```








---

<a href="../starmart/helper.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `Labeled`




<a href="../starmart/helper.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(label: str)
```









---

## <kbd>class</kbd> `NamedResult`




<a href="../starmart/helper.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(name: str, result: Result)
```








---

<a href="../starmart/helper.py#L122"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `ObjectDetectionResult`




<a href="../starmart/helper.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(bounding_boxes: List[BoundingBox], metadata=None)
```








---

<a href="../starmart/helper.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `Result`




<a href="../starmart/helper.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__()
```








---

<a href="../starmart/helper.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `SegmentationMask`




<a href="../starmart/helper.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(coordinates: List[Coordinate], label: str)
```









---

## <kbd>class</kbd> `SegmentationResult`




<a href="../starmart/helper.py#L76"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(segmentation: SegmentationMask, metadata=None)
```








---

<a href="../starmart/helper.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `Success`




<a href="../starmart/helper.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(value, metadata=None)
```








---

<a href="../starmart/helper.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```






---

## <kbd>class</kbd> `TextResult`




<a href="../starmart/helper.py#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(text: str, metadata=None)
```








---

<a href="../starmart/helper.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `is_success`

```python
is_success() → bool
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
