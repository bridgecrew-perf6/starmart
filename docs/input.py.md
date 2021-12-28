<!-- markdownlint-disable -->

<a href="../starmart/input.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `input.py`






---

## <kbd>class</kbd> `CompositeInput`




<a href="../starmart/input.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(inputs: List[NamedInput])
```









---

## <kbd>class</kbd> `GenericArrayInput`




<a href="../starmart/input.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(data: List)
```









---

## <kbd>class</kbd> `GenericInput`




<a href="../starmart/input.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(data)
```









---

## <kbd>class</kbd> `ImageInput`




<a href="../starmart/input.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(base64_image: str)
```








---

<a href="../starmart/input.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_cv2_image`

```python
from_cv2_image(cv2_image)
```





---

<a href="../starmart/input.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(file_path)
```





---

<a href="../starmart/input.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_pillow_image`

```python
from_pillow_image(pillow_image)
```






---

## <kbd>class</kbd> `Input`




<a href="../starmart/input.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(data)
```









---

## <kbd>class</kbd> `NamedInput`




<a href="../starmart/input.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(name: str, input: Input)
```









---

## <kbd>class</kbd> `TextInput`




<a href="../starmart/input.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(text: str)
```











---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
