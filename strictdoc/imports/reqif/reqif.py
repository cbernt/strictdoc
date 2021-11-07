import re
import sys
from collections import defaultdict
from io import StringIO
from xml.etree import ElementTree as etree
from xml.etree.ElementTree import Element

from strictdoc.backend.dsl.models.document import Document
from strictdoc.backend.dsl.models.document_config import DocumentConfig
from strictdoc.backend.dsl.writer import SDWriter
from strictdoc.imports.reqif.models.spec_type_parser import SpectypeParser
from strictdoc.imports.reqif.models.spec_relation_parser import (
    SpecRelationParser,
)
from strictdoc.imports.reqif.models.spec_hierarchy_parser import (
    SpecHierarchyParser,
)

from strictdoc.imports.reqif.models.spec_object_parser import (
    SpecObjectParser,
)


class Level:
    @staticmethod
    def parse_uid_as_int(int_str):
        pattern = re.compile("^[0-9]+$")
        if pattern.match(int_str):
            return int(int_str)
        return 0  # int_str TODO

    @staticmethod
    def compare(lhs, rhs):
        if len(lhs) < len(rhs):
            return 1
        elif len(lhs) > len(rhs):
            return -1
        else:
            return 0


class ReqIFImport:
    @staticmethod
    def import_from_file(input_file):
        # TODO things missing:
        # - datatypes
        # - output path
        # - SDoc Sections (currently the multiple specifications are shown
        #   together)
        # - Sections

        # Import file.
        with open(input_file, "r", encoding="UTF-8") as file:
            # Read each line in the file, readlines() returns a list of lines
            content = file.read()
        try:
            parsed_xml = etree.parse(StringIO(content), etree.XMLParser())
        except Exception as exception:
            # TODO: handle
            print(f"error: problem parsing file: {exception}")
            sys.exit(1)

        # ReqIF element naming convention: element_xyz where xyz is the name of
        # the reqif(xml) tag. Dashes are turned into underscores.
        element_req_if = parsed_xml.getroot()

        # need to get the namespace for all finds, etc
        # https://stackoverflow.com/a/12946675/598057
        def get_namespace(element):
            m = re.match(r"\\{.*\\}", element.tag)
            return m.group(0) if m else ""

        namespace = get_namespace(element_req_if)
        # also create a dictionary of namespaces for Element.find() (slice
        # removes curly braces)
        namespace_dict = {"": namespace[1:-1]}

        # getting all structural elements from the reqif tree:

        # TODO: The header, containing metadata about the document.
        # element_the_header = element_req_if.find("THE-HEADER", namespace_dict)

        # Core content, contains req-if-content which contains all the actual
        # content.
        element_core_content = element_req_if.find(
            "CORE-CONTENT", namespace_dict
        )

        # TODO: Tool extensions contains information specific to the tool used
        # to create the ReqIF file.
        # element_tool_extensions = element_req_if.find(
        #     "TOOL-EXTENSIONS", namespace_dict
        # )

        # req-if-content contains the requirements and structure
        element_req_if_content = element_core_content.find(
            "REQ-IF-CONTENT", namespace_dict
        )

        # TODO: datatypes contains the various datatypes used to store
        # information
        # element_datatypes = element_req_if_content.find(
        #     "DATATYPES", namespace_dict
        # )

        # Spec types contains the spectypes, basically blueprints for spec
        # objects. Spec types use datatypes to define the kind of information
        # stored.
        element_spec_types = element_req_if_content.find(
            "SPEC-TYPES", namespace_dict
        )

        # spec-objects contains specobjects, which are the actual requirements.
        # every specobject must have a spectype which defines its structure
        element_spec_objects = element_req_if_content.find(
            "SPEC-OBJECTS", namespace_dict
        )

        # Spec-relations contains arbitrarily defined relations between spec
        # objects. These relations may be grouped into relation groups which
        # have user-defined meaning.
        element_spec_relations = element_req_if_content.find(
            "SPEC-RELATIONS", namespace_dict
        )

        # specifications contains one or more specification elements.
        # Each specification element contains a tree of spec-hierarchy elements
        # that represents the basic structure of the document each
        # spec-hierarchy element contains a spec-object.
        element_specifications = element_req_if_content.find(
            "SPECIFICATIONS", namespace_dict
        )

        # Note: the other objects have to be present in a proper ReqIF file as
        # well, but these two are absolutely required.
        if element_spec_types is None or element_spec_objects is None:
            raise ValueError("invalid ReqIF structure")

        # parse spectypes, create a map storing relevant data for each spectype
        parsed_spectypes = {}
        for spectype in list(element_spec_types):
            type_id, type_name, type_map = SpectypeParser.parse(spectype)
            if type_id is not None:
                type_data = [type_name, type_map]
                parsed_spectypes[type_id] = type_data

        # get links between requirements:
        structure_map = defaultdict(list)

        if element_specifications is not None:
            hierarchy_map = SpecHierarchyParser.parse(element_specifications)
            for k, v in hierarchy_map.items():
                structure_map[k].extend(v)
        if element_spec_relations is not None:
            relation_map = SpecRelationParser.parse(element_spec_relations)
            for k, v in relation_map.items():
                structure_map[k].append(v)

        # TODO: The lists contain reqIF ids, but the SpecObjectParser requires
        #       UIDs to correctly set requirements.
        structure_map = ReqIFImport.replace_ids(
            element_spec_objects, parsed_spectypes, structure_map
        )

        document_config = DocumentConfig(None, "0.0.1", "DOC-N-001", [], None)
        document = Document("Test reqif", "Test reqif", document_config, [], [])

        # with parsed spec types and structure map, parse each spec object into
        # a SDoc requirement.
        requirements = []
        for spec_object in element_spec_objects:
            requirement = SpecObjectParser.parse(
                spec_object, parsed_spectypes, structure_map
            )
            requirement.parent = document
            requirements.append(requirement)

        document.section_contents = requirements

        # TODO fix dummy path
        document_content = SDWriter().write(document)
        with open("../../../output/reqif.sdoc", "w") as output_file:
            output_file.write(document_content)

    @staticmethod
    def replace_ids(spec_objects, spec_types, structure_map):
        # TODO: due to bad planning, this function needs to replace all
        #       reqIF ids in the structure map with UIDs.

        # get attribute-identifiers for requirement_ID
        identifier_list = []
        for type_identifier in spec_types:
            type_attributes = spec_types[type_identifier][1]
            for attribute in type_attributes:
                if type_attributes[attribute] == "requirement_ID":
                    identifier_list.append(attribute)

        # create map of all spec_objects and their UID:
        id_map = {}
        for spec_object in spec_objects:
            spec_object: Element
            spec_object_identifier = spec_object.attrib["IDENTIFIER"]

            for attribute in spec_object[0]:
                if attribute[0][0].text in identifier_list:
                    spec_object_uid = attribute.attrib["THE-VALUE"]

            id_map[spec_object_identifier] = spec_object_uid

        # replace all reqif ids with UIDs
        new_map = {}
        for k, v in structure_map.items():
            new_list = []
            for list_item in v:
                new_list.append(id_map[list_item])
            new_map[id_map[k]] = new_list
        return new_map
