from xml.etree import ElementTree as etree

import pytest
from strictdoc.imports.reqif.parsers.spec_object_parser import (
    SpecObjectParser,
)

pytest_plugins = [
    "test_mapping_fixtures.fixture_functional",
]

# [HLR001-T001]


def test_mapping_functional_uid_positive(
    fixture_functional_correctreqifobject,
    fixture_functional_type_map,
    fixture_functional_relation_map,
):
    object_string_pos = fixture_functional_correctreqifobject
    xml_object = etree.fromstring(object_string_pos)
    requirement = SpecObjectParser.parse(
        xml_object, fixture_functional_type_map, fixture_functional_relation_map
    )

    # [LLR001-T001]
    assert requirement.uid == "SR001"
    # [/LLR001-T001]


def test_mapping_functional_uid_malformed(
    fixture_functional_malformed_uid,
    fixture_functional_type_map,
    fixture_functional_relation_map,
):
    object_string_pos = fixture_functional_malformed_uid
    xml_object = etree.fromstring(object_string_pos)

    # [LLR001-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_functional_type_map,
            fixture_functional_relation_map,
        )
    # [/LLR001-T002]


def test_mapping_functional_uid_missing(
    fixture_functional_missing_uid,
    fixture_functional_type_map,
    fixture_functional_relation_map,
):
    object_string_pos = fixture_functional_missing_uid
    xml_object = etree.fromstring(object_string_pos)

    # [LLR001-T003]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_functional_type_map,
            fixture_functional_relation_map,
        )
    # [/LLR001-T003]


def test_mapping_functional_allocation_positive(
    fixture_functional_correctreqifobject,
    fixture_functional_type_map,
    fixture_functional_relation_map,
):
    object_string_pos = fixture_functional_correctreqifobject
    xml_object = etree.fromstring(object_string_pos)
    requirement = SpecObjectParser.parse(
        xml_object, fixture_functional_type_map, fixture_functional_relation_map
    )

    # [LLR002-T001]
    assert requirement.special_fields[1].field_value == "Software"
    # [/LLR002-T001]


def test_mapping_functional_allocation_malformed(
    fixture_functional_malformed_allocation,
    fixture_functional_type_map,
    fixture_functional_relation_map,
):
    object_string_pos = fixture_functional_malformed_allocation
    xml_object = etree.fromstring(object_string_pos)

    # [LLR002-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_functional_type_map,
            fixture_functional_relation_map,
        )
    # [/LLR002-T002]


def test_mapping_functional_asil_positive(
    fixture_functional_correctreqifobject,
    fixture_functional_type_map,
    fixture_functional_relation_map,
):
    object_string_pos = fixture_functional_correctreqifobject
    xml_object = etree.fromstring(object_string_pos)
    requirement = SpecObjectParser.parse(
        xml_object, fixture_functional_type_map, fixture_functional_relation_map
    )

    # [LLR003-T001]
    assert requirement.special_fields[0].field_value == "ASIL-A"
    # [/LLR003-T001]


def test_mapping_functional_asil_malformed(
    fixture_functional_malformed_asil,
    fixture_functional_type_map,
    fixture_functional_relation_map,
):
    object_string_pos = fixture_functional_malformed_asil
    xml_object = etree.fromstring(object_string_pos)

    # [LLR003-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_functional_type_map,
            fixture_functional_relation_map,
        )
    # [/LLR003-T002]


def test_mapping_functional_status_positive(
    fixture_functional_correctreqifobject,
    fixture_functional_type_map,
    fixture_functional_relation_map,
):
    object_string_pos = fixture_functional_correctreqifobject
    xml_object = etree.fromstring(object_string_pos)
    requirement = SpecObjectParser.parse(
        xml_object, fixture_functional_type_map, fixture_functional_relation_map
    )

    # [LLR004-T001]
    assert requirement.status == "Draft"
    # [/LLR004-T001]


def test_mapping_functional_status_malformed(
    fixture_functional_malformed_status,
    fixture_functional_type_map,
    fixture_functional_relation_map,
):
    object_string_pos = fixture_functional_malformed_status
    xml_object = etree.fromstring(object_string_pos)

    # [LLR004-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_functional_type_map,
            fixture_functional_relation_map,
        )
    # [/LLR004-T002]


def test_mapping_functional_title_positive(
    fixture_functional_correctreqifobject,
    fixture_functional_type_map,
    fixture_functional_relation_map,
):
    object_string_pos = fixture_functional_correctreqifobject
    xml_object = etree.fromstring(object_string_pos)
    requirement = SpecObjectParser.parse(
        xml_object, fixture_functional_type_map, fixture_functional_relation_map
    )

    # [LLR005-T001]
    assert requirement.status == "Draft"
    # [/LLR005-T001]


def test_mapping_functional_title_malformed(
    fixture_functional_malformed_title,
    fixture_functional_type_map,
    fixture_functional_relation_map,
):
    object_string_pos = fixture_functional_malformed_title
    xml_object = etree.fromstring(object_string_pos)

    # [LLR005-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_functional_type_map,
            fixture_functional_relation_map,
        )
    # [/LLR005-T002]


def test_mapping_functional_title_missing(
    fixture_functional_missing_title,
    fixture_functional_type_map,
    fixture_functional_relation_map,
):
    object_string_pos = fixture_functional_missing_title
    xml_object = etree.fromstring(object_string_pos)

    # [LLR005-T003]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object,
            fixture_functional_type_map,
            fixture_functional_relation_map,
        )
    # [/LLR005-T003]


# [/HLR001-T001]
