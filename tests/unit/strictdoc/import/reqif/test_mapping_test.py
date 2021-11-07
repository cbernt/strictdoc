from xml.etree import ElementTree as etree

import pytest

from strictdoc.backend.dsl.models.reference import Reference
from strictdoc.imports.reqif.parsers.spec_object_parser import (
    SpecObjectParser,
)

pytest_plugins = ["test_mapping_fixtures.fixture_test"]

# [HLR201-T001]


def test_mapping_test_uid_positive(
    fixture_test_uid, fixture_test_type_map, fixture_test_relation_map
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_uid)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_test_type_map, fixture_test_relation_map
    )

    # 3 assert
    # [LLR201-T001]
    assert requirement.uid == "LLR001-T001"
    # [/LLR201-T001]


def test_mapping_test_type_positive(
    fixture_test_uid, fixture_test_type_map, fixture_test_relation_map
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_uid)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_test_type_map, fixture_test_relation_map
    )

    # [LLR203-T001]
    assert requirement.special_fields[0].field_value == "Software"
    # [/LLR203-T001]


def test_mapping_test_initial_condition_positive(
    fixture_test_uid, fixture_test_type_map, fixture_test_relation_map
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_uid)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_test_type_map, fixture_test_relation_map
    )

    # [LLR204-T001]S
    assert (
        requirement.special_fields[1].field_value
        == "ReqIF requirement_ID is passed into the mapping function."
    )
    # [/LLR204-T001]


def test_mapping_test_test_sequence_positive(
    fixture_test_uid, fixture_test_type_map, fixture_test_relation_map
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_uid)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_test_type_map, fixture_test_relation_map
    )

    # 3 assert
    # [LLR208-T001]
    assert (
        requirement.special_fields[2].field_value
        == "The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value."
    )
    # [/LLR208-T001]


def test_mapping_test_target_value_positive(
    fixture_test_uid, fixture_test_type_map, fixture_test_relation_map
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_uid)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_test_type_map, fixture_test_relation_map
    )

    # 3 assert
    # [LLR207-T001]
    assert requirement.special_fields[3].field_value == "true"
    # [/LLR207-T001]


def test_mapping_test_title_positive(
    fixture_test_uid, fixture_test_type_map, fixture_test_relation_map
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_uid)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_test_type_map, fixture_test_relation_map
    )

    # 3 assert
    # [LLR206-T101]
    assert (
        requirement.title
        == "The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID."
    )
    # [/LLR206-T101]


def test_mapping_test_traceability_positive(
    fixture_test_uid, fixture_test_type_map, fixture_test_relation_map
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_uid)

    reference1 = Reference("LLR001-T001", "PARENT", "LLR001")
    reference2 = Reference("LLR001-T001", "PARENT", "SLR001")
    reference3 = Reference(
        "LLR001-T001", "FILE", r"..\..\..\tests\unit\strictdoc\import\reqif"
    )

    list_references = [reference1, reference2, reference3]

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_test_type_map, fixture_test_relation_map
    )

    # 3 assert
    # [LLR202-T001]
    for ref, reference in zip(list_references, requirement.references):
        assert ref.ref_type == reference.ref_type
    # [/LLR202-T001]


def test_mapping_test_status_positive(
    fixture_test_uid, fixture_test_type_map, fixture_test_relation_map
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_uid)

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_test_type_map, fixture_test_relation_map
    )

    # 3 assert
    # [LLR205-T001]
    assert requirement.status == "Draft"
    # [/LLR205-T001]


def test_mapping_test_uid_malformed(
    fixture_test_uid_malformed, fixture_test_type_map, fixture_test_relation_map
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_uid_malformed)
    # [LLR201-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR201-T002]


def test_mapping_test_uid_missing(
    fixture_test_uid_missing, fixture_test_type_map, fixture_test_relation_map
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_uid_missing)
    # [LLR201-T003]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR201-T003]


def test_mapping_test_type_malformed(
    fixture_test_type_malformed,
    fixture_test_type_map,
    fixture_test_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_type_malformed)
    # [LLR203-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR203-T002]


def test_mapping_test_traceability_malformed(
    fixture_test_traceability_malformed,
    fixture_test_type_map,
    fixture_test_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_traceability_malformed)
    # [LLR202-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR202-T002]


def test_mapping_test_traceability_missing(
    fixture_test_traceability_missing,
    fixture_test_type_map,
    fixture_test_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_traceability_missing)
    # [LLR202-T003]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR202-T003]


def test_mapping_test_title_malformed(
    fixture_test_title_malformed,
    fixture_test_type_map,
    fixture_test_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_title_malformed)
    # [LLR206-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR206-T002]


def test_mapping_test_title_missing(
    fixture_test_title_missing, fixture_test_type_map, fixture_test_relation_map
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_title_missing)
    # [LLR206-T003]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR206-T003]


def test_mapping_test_initial_condition_malformed(
    fixture_test_initial_condition_malformed,
    fixture_test_type_map,
    fixture_test_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_initial_condition_malformed)
    # [LLR204-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR204-T002]


def test_mapping_test_initial_condition_missing(
    fixture_test_initial_condition_missing,
    fixture_test_type_map,
    fixture_test_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_initial_condition_missing)
    # [LLR204-T003]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR204-T003]


def test_mapping_test_test_sequence_malformed(
    fixture_test_test_sequence_malformed,
    fixture_test_type_map,
    fixture_test_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_test_sequence_malformed)
    # [LLR208-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR208-T002]


def test_mapping_test_test_sequence_missing(
    fixture_test_test_sequence_missing,
    fixture_test_type_map,
    fixture_test_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_test_sequence_missing)
    # [LLR208-T003]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR208-T003]


def test_mapping_test_target_value_malformed(
    fixture_test_target_value_malformed,
    fixture_test_type_map,
    fixture_test_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_target_value_malformed)
    # [LLR207-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR207-T002]


def test_mapping_test_target_value_missing(
    fixture_test_target_value_missing,
    fixture_test_type_map,
    fixture_test_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_target_value_missing)
    # [LLR207-T003]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR207-T003]


def test_mapping_test_status_malformed(
    fixture_test_status_malformed,
    fixture_test_type_map,
    fixture_test_relation_map,
):
    # parse object here
    xml_object = etree.fromstring(fixture_test_status_malformed)
    # [LLR205-T002]
    with pytest.raises(ValueError):
        SpecObjectParser.parse(
            xml_object, fixture_test_type_map, fixture_test_relation_map
        )
    # [/LLR205-T002]


# [/HLR201-T001]
