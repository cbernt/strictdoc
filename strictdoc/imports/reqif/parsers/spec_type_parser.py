import re
from xml.etree.ElementTree import Element


# [HLR401]
from strictdoc.imports.reqif.models.reqif_spec_object_type import ReqIFSpecObjectType


class SpecTypeParser:
    @staticmethod
    def parse(element_spec_type):
        if "SPEC-OBJECT-TYPE" in element_spec_type.tag:
            return SpecTypeParser.parse_spec_object_type(element_spec_type)
        if "SPEC-RELATION-TYPE" in element_spec_type.tag:
            # TODO
            pass
        return None

    @staticmethod
    def parse_spec_object_type(spec_type):
        attribute_map = {}

        attributes = spec_type.attrib
        try:
            spec_type_id = attributes["IDENTIFIER"]
        except Exception:
            raise ValueError("id_missing")
        if len(spec_type_id) < 1:
            raise ValueError("id_missing")

        regex_search = re.compile("^[a-zA-Z0-9_ ]+$")
        if not regex_search.match(spec_type_id):
            raise ValueError("id_malformed")

        try:
            spec_type_long_name = attributes["LONG-NAME"]
        except Exception:
            raise ValueError("type_missing")
        if len(spec_type_long_name) < 1:
            raise ValueError("type_missing")
        if not regex_search.match(spec_type_long_name):
            raise ValueError("malformed_type")

        spec_attributes = list(spec_type)[0]
        for attribute_definition in spec_attributes:
            try:
                value = attribute_definition.attrib["LONG-NAME"]
                key = attribute_definition.attrib["IDENTIFIER"]
            except Exception:
                raise ValueError("attribute_malformed")
            attribute_map[key] = value

        return ReqIFSpecObjectType(spec_type_id, spec_type_long_name, attribute_map)

# [/HLR401]
