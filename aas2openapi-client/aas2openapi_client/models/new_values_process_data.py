from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewValuesProcessData")


@attr.s(auto_attribs=True)
class NewValuesProcessData:
    """
    Attributes:
        id_short (str):
        timestamp (str):
        values (List[float]):
        description (Union[Unset, str]):
        semantic_id (Union[Unset, str]):
    """

    id_short: str
    timestamp: str
    values: List[float]
    description: Union[Unset, str] = UNSET
    semantic_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id_short = self.id_short
        timestamp = self.timestamp
        values = self.values

        description = self.description
        semantic_id = self.semantic_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id_short": id_short,
                "timestamp": timestamp,
                "values": values,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if semantic_id is not UNSET:
            field_dict["semantic_id"] = semantic_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id_short = d.pop("id_short")

        timestamp = d.pop("timestamp")

        values = cast(List[float], d.pop("values"))

        description = d.pop("description", UNSET)

        semantic_id = d.pop("semantic_id", UNSET)

        new_values_process_data = cls(
            id_short=id_short,
            timestamp=timestamp,
            values=values,
            description=description,
            semantic_id=semantic_id,
        )

        new_values_process_data.additional_properties = d
        return new_values_process_data

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
