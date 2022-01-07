from typing import List

from starmart.helper import Typed, Validatable, ImageUtils


class Result(Typed):
    def is_success(self) -> bool:
        raise NotImplementedError(f'Method is_success() not implemented in {type(self).__name__}')


class Success(Result, Validatable):
    def __init__(self, value):
        super().__init__()
        if value is None:
            raise ValueError(f'value cannot be None in {type(self).__name__}')
        if not self.validate_data(value):
            # TODO add documentation link
            raise ValueError(f'value for {type(self).__name__} does not match expected input type')
        self.value = value

    def is_success(self) -> bool:
        return True


class Failure(Result):
    def __init__(self, error):
        super().__init__()
        self.error = error

    def is_success(self) -> bool:
        return False


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Labeled(object):
    def __init__(self, label: str):
        self.label = label


class BoundingBox(Labeled):
    def __init__(self, top_left_coordinate: Coordinate, bottom_right_coordinate: Coordinate,
                 confidence: float, label: str):
        super().__init__(label)
        self.top_left_coordinate = top_left_coordinate
        self.bottom_right_coordinate = bottom_right_coordinate
        self.confidence = confidence

    def width(self):
        return self.bottom_right_coordinate.x - self.top_left_coordinate.x

    def height(self):
        return self.bottom_right_coordinate.y - self.top_left_coordinate.y


class ObjectDetectionResult(Success):
    def __init__(self, bounding_boxes: List[BoundingBox]):
        super().__init__(bounding_boxes)

    def type(self) -> str:
        return 'object_detection'

    def validate_data(self, data) -> bool:
        return all([isinstance(x, BoundingBox) for x in self.value])


class SegmentationMask(Labeled):
    def __init__(self, coordinates: List[Coordinate], label: str):
        super().__init__(label)
        self.coordinates = coordinates


class SegmentationResult(Success):
    def __init__(self, segmentation: SegmentationMask):
        super().__init__(segmentation)

    def type(self) -> str:
        return 'segmentation'

    def validate_data(self, data) -> bool:
        return isinstance(self.value, SegmentationMask)


class Classification(Labeled):
    def __init__(self, label: str, confidence: float):
        super().__init__(label)
        self.confidence = confidence


class ClassificationResult(Success):
    def __init__(self, classifications: List[Classification]):
        super().__init__(classifications)

    def type(self) -> str:
        return 'classification'

    def validate_data(self, data) -> bool:
        return all([isinstance(x, Classification) for x in self.value])


class ImageResult(Success, ImageUtils):
    def __init__(self, base64_image: str):
        super().__init__(base64_image)

    def type(self) -> str:
        return 'image'

    def validate_data(self, data) -> bool:
        return self.validate_base64_image(data)

    def base64_image(self) -> str:
        return self.value


class TextResult(Success):
    def __init__(self, text: str):
        super().__init__(text)

    def type(self) -> str:
        return 'text'

    def validate_data(self, data) -> bool:
        return isinstance(self.value, str)


class NamedResult(Result):
    def __init__(self, name: str, result: Result):
        self.name = name
        self.result = result
        super().__init__()

    def type(self) -> str:
        return self.result.type()

    def is_success(self) -> bool:
        return self.result.is_success()


class CompositeResult(Result):
    def __init__(self, results: List[NamedResult]):
        self.results = results
        super().__init__()

    def type(self) -> str:
        return 'composite'

    def is_success(self) -> bool:
        return all(map(lambda x: x.is_success(), self.results))


class GenericResult(Success):
    def __init__(self, value):
        super().__init__(value)

    def type(self) -> str:
        return 'generic'

    def validate_data(self, data) -> bool:
        return True


class GenericArrayResult(GenericResult):
    def __init__(self, value: List):
        super().__init__(value)

    def type(self) -> str:
        return 'generic_array'


results = dict({
    'object_detection': ObjectDetectionResult,
    'segmentation': SegmentationResult,
    'classification': Classification,
    'image': ImageResult,
    'text': TextResult,
    'composite': CompositeResult,
    'generic': GenericResult,
    'generic_array': GenericArrayResult
})


def get_result(name: str) -> Result or None:
    return results[name]
