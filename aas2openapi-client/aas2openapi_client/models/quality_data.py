from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.quality_feature import QualityFeature


T = TypeVar("T", bound="QualityData")


@attr.s(auto_attribs=True)
class QualityData:
    """
    Attributes:
        id (str):
        quality_feature (List['QualityFeature']):
        description (Union[Unset, str]):
        id_short (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id: str
    quality_feature: List["QualityFeature"]
    description: Union[Unset, str] = UNSET
    id_short: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        quality_feature = []
        for quality_feature_item_data in self.quality_feature:
            quality_feature_item = quality_feature_item_data.to_dict()

            quality_feature.append(quality_feature_item)

        description = self.description
        id_short = self.id_short
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_": id,
                "quality_feature": quality_feature,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if id_short is not UNSET:
            field_dict["id_short"] = id_short
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.quality_feature import QualityFeature

        d = src_dict.copy()
        id = d.pop("id_")

        quality_feature = []
        _quality_feature = d.pop("quality_feature")
        for quality_feature_item_data in _quality_feature:
            quality_feature_item = QualityFeature.from_dict(quality_feature_item_data)

            quality_feature.append(quality_feature_item)

        description = d.pop("description", UNSET)

        id_short = d.pop("id_short", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        quality_data = cls(
            id=id,
            quality_feature=quality_feature,
            description=description,
            id_short=id_short,
            semantic_id=semantic_id,
        )

        quality_data.additional_properties = d
        return quality_data

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
