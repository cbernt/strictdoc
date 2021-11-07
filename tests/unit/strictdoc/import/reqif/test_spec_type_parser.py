from xml.etree import ElementTree as etree

import pytest

from strictdoc.imports.reqif.models.reqif_spec_object_type import ReqIFSpecObjectType
from strictdoc.imports.reqif.parsers.spec_type_parser import SpecTypeParser


# [HLR401-T001, LLR401-T001, LLR402-T001, LLR403-T001]
def test_01_nominal_case():
    spec_type_string = """
<SPEC-OBJECT-TYPE IDENTIFIER="_gFhrWmojEeuExICsU7Acmg" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="FUNCTIONAL">
  <SPEC-ATTRIBUTES>
    <ATTRIBUTE-DEFINITION-STRING IDENTIFIER="_gFhrW2ojEeuExICsU7Acmg" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="ReqIF.ForeignID">
      <TYPE>
        <DATATYPE-DEFINITION-STRING-REF>_gFhrVGojEeuExICsU7Acmg</DATATYPE-DEFINITION-STRING-REF>
      </TYPE>
    </ATTRIBUTE-DEFINITION-STRING>
    <ATTRIBUTE-DEFINITION-STRING DESC="Testattribute" IDENTIFIER="_aqZG4GxpEeuaU7fHySy8Bw" LAST-CHANGE="2021-02-11T14:02:05.129+01:00" LONG-NAME="NOTES" IS-EDITABLE="true">
      <TYPE>
        <DATATYPE-DEFINITION-STRING-REF>_gFhrU2ojEeuExICsU7Acmg</DATATYPE-DEFINITION-STRING-REF>
      </TYPE>
      <DEFAULT-VALUE/>
    </ATTRIBUTE-DEFINITION-STRING>
  </SPEC-ATTRIBUTES>
</SPEC-OBJECT-TYPE>
    """
    spec_type_xml = etree.fromstring(spec_type_string)

    reqif_spec_object_type = SpecTypeParser.parse(spec_type_xml)
    assert isinstance(reqif_spec_object_type, ReqIFSpecObjectType)
    assert reqif_spec_object_type.identifier == "_gFhrWmojEeuExICsU7Acmg"
    assert reqif_spec_object_type.long_name == "FUNCTIONAL"
    attribute_map = reqif_spec_object_type.attribute_map
    assert len(attribute_map) == 2
    assert attribute_map.get("_gFhrW2ojEeuExICsU7Acmg") == "ReqIF.ForeignID"
    assert attribute_map.get("_aqZG4GxpEeuaU7fHySy8Bw") == "NOTES"
# [/HLR401-T001, LLR401-T001, LLR402-T001, LLR403-T001]


# [LLR401-T002]
def test_02_get_id_no_id():
    spec_type_string_no_id = """
<SPEC-OBJECT-TYPE LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="FUNCTIONAL">
  <SPEC-ATTRIBUTES>
    <ATTRIBUTE-DEFINITION-STRING IDENTIFIER="" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="ReqIF.ForeignID">
      <TYPE>
        <DATATYPE-DEFINITION-STRING-REF>_gFhrVGojEeuExICsU7Acmg</DATATYPE-DEFINITION-STRING-REF>
      </TYPE>
    </ATTRIBUTE-DEFINITION-STRING>
    <ATTRIBUTE-DEFINITION-STRING DESC="Testattribute" IDENTIFIER="_aqZG4GxpEeuaU7fHySy8Bw" LAST-CHANGE="2021-02-11T14:02:05.129+01:00" LONG-NAME="NOTES" IS-EDITABLE="true">
      <TYPE>
        <DATATYPE-DEFINITION-STRING-REF>_gFhrU2ojEeuExICsU7Acmg</DATATYPE-DEFINITION-STRING-REF>
      </TYPE>
      <DEFAULT-VALUE/>
    </ATTRIBUTE-DEFINITION-STRING>
  </SPEC-ATTRIBUTES>
</SPEC-OBJECT-TYPE>
    """
    spectype_no_id = etree.fromstring(spec_type_string_no_id)
    with pytest.raises(ValueError, match="id_missing"):
        SpecTypeParser.parse(
            spectype_no_id
        )
# [/LLR401-T002]


# [LLR401-T003]
def test_03_get_id_malformed_id():
    spec_type_string_id_malformed = """
<SPEC-OBJECT-TYPE IDENTIFIER="\n\\nnnn\\???!" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="FUNCTIONAL">
  <SPEC-ATTRIBUTES>
    <ATTRIBUTE-DEFINITION-STRING IDENTIFIER="_gFhrW2ojEeuExICsU7Acmg" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="ReqIF.ForeignID">
      <TYPE>
        <DATATYPE-DEFINITION-STRING-REF>_gFhrVGojEeuExICsU7Acmg</DATATYPE-DEFINITION-STRING-REF>
      </TYPE>
    </ATTRIBUTE-DEFINITION-STRING>
    <ATTRIBUTE-DEFINITION-STRING DESC="Testattribute" IDENTIFIER="_aqZG4GxpEeuaU7fHySy8Bw" LAST-CHANGE="2021-02-11T14:02:05.129+01:00" LONG-NAME="NOTES" IS-EDITABLE="true">
      <TYPE>
        <DATATYPE-DEFINITION-STRING-REF>_gFhrU2ojEeuExICsU7Acmg</DATATYPE-DEFINITION-STRING-REF>
      </TYPE>
      <DEFAULT-VALUE/>
    </ATTRIBUTE-DEFINITION-STRING>
  </SPEC-ATTRIBUTES>
</SPEC-OBJECT-TYPE>
    """
    spectype_id_malformed = etree.fromstring(spec_type_string_id_malformed)
    with pytest.raises(ValueError, match="id_malformed"):
        SpecTypeParser.parse(
            spectype_id_malformed
        )
# [/LLR401-T003]


# [LLR402-T002]
def test_04_get_type_no_type():
    spec_type_string_no_type = """
<SPEC-OBJECT-TYPE IDENTIFIER="_gFhrWmojEeuExICsU7Acmg" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="">
  <SPEC-ATTRIBUTES>
    <ATTRIBUTE-DEFINITION-STRING IDENTIFIER="_gFhrW2ojEeuExICsU7Acmg" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="ReqIF.ForeignID">
      <TYPE>
        <DATATYPE-DEFINITION-STRING-REF>_gFhrVGojEeuExICsU7Acmg</DATATYPE-DEFINITION-STRING-REF>
      </TYPE>
    </ATTRIBUTE-DEFINITION-STRING>
    <ATTRIBUTE-DEFINITION-STRING DESC="Testattribute" IDENTIFIER="_aqZG4GxpEeuaU7fHySy8Bw" LAST-CHANGE="2021-02-11T14:02:05.129+01:00" LONG-NAME="NOTES" IS-EDITABLE="true">
      <TYPE>
        <DATATYPE-DEFINITION-STRING-REF>_gFhrU2ojEeuExICsU7Acmg</DATATYPE-DEFINITION-STRING-REF>
      </TYPE>
      <DEFAULT-VALUE/>
    </ATTRIBUTE-DEFINITION-STRING>
  </SPEC-ATTRIBUTES>
</SPEC-OBJECT-TYPE>
    """
    spectype_no_type = etree.fromstring(spec_type_string_no_type)
    with pytest.raises(ValueError, match="type_missing"):
        SpecTypeParser.parse(spectype_no_type)
# [/LLR402-T002]


# [LLR403-T002]
def test_05_get_attribute_map_malformed_attribute():
    spec_type_string_attribute_malformed = """
<SPEC-OBJECT-TYPE IDENTIFIER="_gFhrWmojEeuExICsU7Acmg" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="FUNCTIONAL">
  <SPEC-ATTRIBUTES>
      <TYPE>
        <DATATYPE-DEFINITION-STRING-REF>_gFhrVGojEeuExICsU7Acmg</DATATYPE-DEFINITION-STRING-REF>
      </TYPE>

    <ATTRIBUTE-DEFINITION-STRING DESC="Testattribute" IDENTIFIER="_aqZG4GxpEeuaU7fHySy8Bw" LAST-CHANGE="2021-02-11T14:02:05.129+01:00" LONG-NAME="NOTES" IS-EDITABLE="true">
      <TYPE>
        <DATATYPE-DEFINITION-STRING-REF>_gFhrU2ojEeuExICsU7Acmg</DATATYPE-DEFINITION-STRING-REF>
      </TYPE>
      <DEFAULT-VALUE/>
    </ATTRIBUTE-DEFINITION-STRING>
  </SPEC-ATTRIBUTES>
</SPEC-OBJECT-TYPE>
    """
    spectype_attribute_malformed = etree.fromstring(
        spec_type_string_attribute_malformed
    )
    with pytest.raises(ValueError, match="attribute_malformed"):
        SpecTypeParser.parse(
            spectype_attribute_malformed
        )
# [/LLR403-T002]
