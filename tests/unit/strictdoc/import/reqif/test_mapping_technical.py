from xml.etree import ElementTree as etree
from strictdoc.imports.reqif.models.spec_object_parser import (
    SpecObjectParser,
)
import pytest

pytest_plugins = ["test_mapping_fixtures.fixture_technical"]

# [HLR101-T001]


def test_mapping_technical_uid_positive(
    fixture_technical_uid,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_uid)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_technical_type_map, fixture_technical_relation_map
    )
    # 3 assert
    # [LLR101-T001]
    assert requirement.uid == "LLR204"
    # [/LLR101-T001]


def test_mapping_technical_uid_malformed(
    fixture_technical_uid_malformed,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_uid_malformed)
    # [LLR101-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_technical_type_map,
            fixture_technical_relation_map,
        )
    # [/LLR101-T002]


def test_mapping_technical_uid_missing(
    fixture_technical_uid_missing,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_uid_missing)
    # [LLR101-T003]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_technical_type_map,
            fixture_technical_relation_map,
        )
    # [/LLR101-T003]


def test_mapping_technical_allocation_to_component_positive(
    fixture_technical_allocation_to_component,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_allocation_to_component)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_technical_type_map, fixture_technical_relation_map
    )
    # 3 assert
    # [LLR103-T001]
    assert requirement.special_fields[1].field_value == "Software"
    # [/LLR103-T001]


def test_mapping_technical_allocation_to_component_malformed(
    fixture_technical_allocation_to_component_malformed,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(
        fixture_technical_allocation_to_component_malformed
    )
    # [LLR103-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_technical_type_map,
            fixture_technical_relation_map,
        )
    # [/LLR103-T002]


def test_mapping_technical_asil_positive(
    fixture_technical_asil,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_asil)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_technical_type_map, fixture_technical_relation_map
    )
    # 3 assert
    # [LLR104-T001]
    assert requirement.special_fields[0].field_value == "ASIL-A"
    # [/LLR104-T001]


def test_mapping_technical_asil_malformed(
    fixture_technical_asil_malformed,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_asil_malformed)
    # [LLR104-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_technical_type_map,
            fixture_technical_relation_map,
        )
    # [/LLR104-T002]


def test_mapping_technical_status_positive(
    fixture_technical_status,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_status)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_technical_type_map, fixture_technical_relation_map
    )
    # 3 assert
    # [LLR105-T001]
    assert requirement.status == "Draft"
    # [/LLR105-T001]


def test_mapping_technical_status_malformed(
    fixture_technical_status_malformed,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_status_malformed)
    # [LLR105-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_technical_type_map,
            fixture_technical_relation_map,
        )
    # [/LLR105-T002]


def test_mapping_technical_target_value_positive(
    fixture_technical_target_value,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_target_value)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_technical_type_map, fixture_technical_relation_map
    )
    # 3 assert
    # [LLR106-T001]
    assert (
        requirement.special_fields[2].field_value
        == "SPECIAL FIELD(initial_condition)"
    )
    # [/LLR106-T001]


def test_mapping_technical_target_value_malformed(
    fixture_technical_target_value_malformed,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_target_value_malformed)
    # [LLR106-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_technical_type_map,
            fixture_technical_relation_map,
        )
    # [/LLR106-T002]


def test_mapping_technical_technical_description_positive(
    fixture_technical_technical_description,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_technical_description)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_technical_type_map, fixture_technical_relation_map
    )
    # 3 assert
    # [LLR102-T001]
    assert (
        requirement.title
        == "The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition)."
    )
    # [/LLR102-T001]


def test_mapping_technical_technical_description_malformed(
    fixture_technical_technical_description_malformed,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(
        fixture_technical_technical_description_malformed
    )
    # [LLR102-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_technical_type_map,
            fixture_technical_relation_map,
        )
    # [/LLR102-T002]


def test_mapping_technical_technical_description_missing(
    fixture_technical_technical_description_missing,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(
        fixture_technical_technical_description_missing
    )
    # [LLR102-T003]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_technical_type_map,
            fixture_technical_relation_map,
        )
    # [/LLR102-T003]


def test_mapping_technical_comment_positive(
    fixture_technical_comment,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_comment)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_technical_type_map, fixture_technical_relation_map
    )
    # 3 assert
    # [LLR107-T001]
    assert requirement.comments == "no comment"
    # [/LLR107-T001]


def test_mapping_technical_comment_malformed(
    fixture_technical_comment_malformed,
    fixture_technical_type_map,
    fixture_technical_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_technical_comment_malformed)
    # [LLR107-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_technical_type_map,
            fixture_technical_relation_map,
        )
    # [/LLR107-T002]


# [/HLR101-T001]
