from strictdoc.backend.dsl.models.reference import Reference
from strictdoc.backend.dsl.models.requirement import (
    Requirement,
    RequirementComment,
)
from strictdoc.backend.dsl.models.special_field import SpecialField


class SpecObjectParser:
    @staticmethod
    def parse(element, object_type_map, relation_map):

        # get type and attribute map

        element_type_identifier = element[1][0].text
        element_type = object_type_map[element_type_identifier][0]
        attribute_map = object_type_map[element_type_identifier][1]

        # check if value contains ' or ";
        # if yes, raise an error; if no, append to list.
        value_list = []
        for elem in element[0]:
            for char in elem.attrib["THE-VALUE"]:
                if char == '"' or char == "'" or char == "/":
                    raise ValueError("Attribute_contains_illegal_character")
            value_list.append(elem.attrib["THE-VALUE"])

        # append all identifiers from the spec object to an empty list
        identifier_list = []
        for identifier in element[0]:
            identifier_list.append(identifier[0][0].text)

        # check if all identifiers from attibute_map(from spec object type)
        # are in identifier_list(from spec object) and reversed
        # if not, raise ValueError;
        identifier_counter = 0
        for identifier in identifier_list:
            for key in attribute_map:
                if identifier == key:
                    identifier_counter += 1

        if (
            len(identifier_list) != identifier_counter
            or len(attribute_map) != identifier_counter
        ):
            raise ValueError("SpecObject: identifiers are not congruent.")

        # dict with attribute names and corresponding identifiers
        value_number = 0
        dict_attribute_value = {}
        for identifier in identifier_list:
            dict_attribute_value[attribute_map[identifier]] = value_list[
                value_number
            ]
            value_number += 1

        # check if ASIL values are correct
        # if element_type == "functional" or element_type == "technical":
        #     SpecObjectParser.checkasilvalues(dict_attribute_value)

        # check for missing attribute values in predefined spectypes
        if element_type == "test":
            for attribute in dict_attribute_value:
                if dict_attribute_value[attribute] == "":
                    if attribute != "type" and attribute != "status":
                        raise ValueError("Required_attribute_missing")
            # initialize special fields
            special_field_type = SpecialField(
                dict_attribute_value["requirement_ID"],
                "TYPE",
                dict_attribute_value["type"],
            )
            special_field_initial_condition = SpecialField(
                dict_attribute_value["requirement_ID"],
                "INITIAL_CONDITION",
                dict_attribute_value["initial_condition"],
            )
            special_field_test_sequence = SpecialField(
                dict_attribute_value["requirement_ID"],
                "TEST_SEQUENCE",
                dict_attribute_value["test_sequence"],
            )
            special_field_target_value = SpecialField(
                dict_attribute_value["requirement_ID"],
                "TARGET_VALUE",
                dict_attribute_value["target_value"],
            )
            special_fields = [
                special_field_type,
                special_field_initial_condition,
                special_field_test_sequence,
                special_field_target_value,
            ]

            list_references = SpecObjectParser.getparents(
                dict_attribute_value, relation_map
            )
            # get traceability element
            list_references.append(
                Reference(
                    dict_attribute_value["requirement_ID"],
                    "FILE",
                    dict_attribute_value["traceability"],
                )
            )

            # return Requirement object
            req = Requirement(
                "DOCUMENT",
                None,
                None,
                dict_attribute_value["requirement_ID"],
                dict_attribute_value["status"],
                None,
                list_references,
                dict_attribute_value["objective"],
                None,
                None,
                None,
                [],
                special_fields,
            )
            req.ng_level = 1
            return req

        if element_type == "technical":
            for attribute in dict_attribute_value:
                if dict_attribute_value[attribute] == "":
                    if (
                        attribute == "requirement_ID"
                        or attribute == "relation"
                        or attribute == "technical_description"
                    ):
                        raise ValueError("Required_attribute_missing")
            # initialize special fields
            special_field_asil = SpecialField(
                dict_attribute_value["requirement_ID"],
                "ASIL",
                dict_attribute_value["asil"],
            )
            special_field_allocation_to_component = SpecialField(
                dict_attribute_value["requirement_ID"],
                "ALLOCATION_TO_COMPONENT",
                dict_attribute_value["allocation_to_component"],
            )
            special_field_target_value = SpecialField(
                dict_attribute_value["requirement_ID"],
                "TARGET_VALUE",
                dict_attribute_value["target_value"],
            )
            special_fields = [
                special_field_asil,
                special_field_allocation_to_component,
                special_field_target_value,
            ]

            list_references = SpecObjectParser.getparents(
                dict_attribute_value, relation_map
            )
            comment = RequirementComment(
                dict_attribute_value["requirement_ID"],
                None,
                dict_attribute_value["comment"],
            )

            # return Requirement object
            req = Requirement(
                "DOCUMENT",
                None,
                None,
                dict_attribute_value["requirement_ID"],
                dict_attribute_value["status"],
                None,
                list_references,
                dict_attribute_value["technical_description"],
                None,
                None,
                None,
                [comment],
                special_fields,
            )
            req.ng_level = 1
            return req

        if element_type == "functional":
            for attribute in dict_attribute_value:
                if dict_attribute_value[attribute] == "":
                    if (
                        attribute == "requirement_ID"
                        or attribute == "functional_description"
                    ):
                        raise ValueError("Required_attribute_missing")
            # initialize special fields
            special_field_asil = SpecialField(
                dict_attribute_value["requirement_ID"],
                "ASIL",
                dict_attribute_value["asil"],
            )
            special_field_allocation = SpecialField(
                dict_attribute_value["requirement_ID"],
                "ALLOCATION",
                dict_attribute_value["allocation"],
            )
            special_fields = [special_field_asil, special_field_allocation]

            list_references = SpecObjectParser.getparents(
                dict_attribute_value, relation_map
            )

            # return Requirement object
            req = Requirement(
                "DOCUMENT",
                None,
                None,
                dict_attribute_value["requirement_ID"],
                dict_attribute_value["status"],
                None,
                list_references,
                dict_attribute_value["functional_description"],
                None,
                None,
                None,
                [],
                special_fields,
            )
            req.ng_level = 1
            return req

    @staticmethod
    def checkasilvalues(attribute_value):
        # check if values in attribute asil are correct asil values
        asil_values = (
            "ASIL A",
            "ASIL B",
            "ASIL C",
            "ASIL D",
            "ASIL-A",
            "ASIL-B",
            "ASIL-C",
            "ASIL-D",
            "A",
            "B",
            "C",
            "D",
            "QM",
            "",
        )
        if attribute_value["asil"] not in asil_values:
            raise ValueError("Attribute_asil_contains_no_asil_value")

    @staticmethod
    def getparents(dict_attribute_value, relation_map):
        # if element has parent elements, add them to list_references
        if dict_attribute_value["requirement_ID"] in relation_map.keys():
            list_references = []
            references = relation_map[dict_attribute_value["requirement_ID"]]
            for reference in references:
                list_references.append(
                    Reference(
                        dict_attribute_value["requirement_ID"],
                        "PARENT",
                        reference,
                    )
                )
            return list_references
        else:
            return []
