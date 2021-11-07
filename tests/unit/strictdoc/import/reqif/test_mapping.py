from xml.etree import ElementTree as etree

from strictdoc.backend.dsl.models.requirement import Requirement
from strictdoc.backend.dsl.models.special_field import SpecialField
from strictdoc.imports.reqif.models.spec_object_parser import (
    SpecObjectParser,
)

pytest_plugins = [
    "test_mapping_fixtures.fixture_functional",
]


def test_mapping_positive(
    fixture_functional_type_map, fixture_functional_relation_map
):
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_eDO24C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:32:40.205+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SR001">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_FEHY0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_OlZh0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_KMVP0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_MZGCUC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The import function shall import a .reqif file and convert it to an .sdoc file">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_Hx6b0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_gV9O0C2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""

    special_field_asil = SpecialField("SR001", "asil", "ASIL-A")
    special_field_allocation = SpecialField("SR001", "allocation", "Software")
    special_fields = [special_field_asil, special_field_allocation]
    # create test object
    test_object = Requirement(
        "DOCUMENT",
        None,
        None,
        "SR001",
        "Draft",
        None,
        None,
        "The import function shall import a .reqif file and convert it to an .sdoc file",
        None,
        None,
        None,
        None,
        special_fields,
    )
    # parse object here
    xml_object = etree.fromstring(object_string_pos, etree.XMLParser())

    # 2 test mapping
    requirement = SpecObjectParser.parse(
        xml_object, fixture_functional_type_map, fixture_functional_relation_map
    )

    # 3 assert
    assert requirement.uid == test_object.uid
    assert requirement.status == test_object.status
    assert (
        requirement.special_fields[0].field_value
        == test_object.special_fields[0].field_value
    )
    assert (
        requirement.special_fields[1].field_value
        == test_object.special_fields[1].field_value
    )
    assert requirement.title == test_object.title
