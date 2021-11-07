from xml.etree import ElementTree as etree

import pytest

from strictdoc.imports.reqif.models.spec_type_parser import SpectypeParser

spectype_string = """<SPEC-OBJECT-TYPE IDENTIFIER="_gFhrWmojEeuExICsU7Acmg" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="FUNCTIONAL">
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
spectype = etree.fromstring(spectype_string)

spectype_string_no_id = """<SPEC-OBJECT-TYPE LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="FUNCTIONAL">
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
spectype_no_id = etree.fromstring(spectype_string_no_id)

spectype_string_id_malformed = """<SPEC-OBJECT-TYPE IDENTIFIER="\n\\nnnn\\???!" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="FUNCTIONAL">
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
spectype_id_malformed = etree.fromstring(spectype_string_id_malformed)

spectype_string_no_type = """<SPEC-OBJECT-TYPE IDENTIFIER="_gFhrWmojEeuExICsU7Acmg" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="">
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
spectype_no_type = etree.fromstring(spectype_string_no_type)

spectype_string_unknown_type = """<SPEC-OBJECT-TYPE IDENTIFIER="_gFhrWmojEeuExICsU7Acmg" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="Requirement TypeEEEEE">
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
spectype_unknown_type = etree.fromstring(spectype_string_unknown_type)

spectype_string_attribute_malformed = """<SPEC-OBJECT-TYPE IDENTIFIER="_gFhrWmojEeuExICsU7Acmg" LAST-CHANGE="2021-02-08T16:37:07.454+01:00" LONG-NAME="FUNCTIONAL">
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
    spectype_string_attribute_malformed
)


# [HLR401-T001]
def test_spectypeparser():
    spectype_id, spectype_type, attribute_map = SpectypeParser.parse(spectype)
    assert spectype_id == "_gFhrWmojEeuExICsU7Acmg"
    assert spectype_type == "FUNCTIONAL"
    assert len(attribute_map) == 2
    assert attribute_map.get("_gFhrW2ojEeuExICsU7Acmg") == "ReqIF.ForeignID"
    assert attribute_map.get("_aqZG4GxpEeuaU7fHySy8Bw") == "NOTES"


# [/HLR401-T001]

# [LLR401-T001]
def test_get_id():
    spectype_id, spectype_type, attribute_map = SpectypeParser.parse(spectype)
    assert spectype_id == "_gFhrWmojEeuExICsU7Acmg"


# [/LLR401-T001]

# [LLR402-T001]
def test_get_type():
    spectype_id, spectype_type, attribute_map = SpectypeParser.parse(spectype)
    assert spectype_type == "FUNCTIONAL"


# [/LLR402-T001]

# [LLR403-T001]
def test_get_attribute_map():
    spectype_id, spectype_type, attribute_map = SpectypeParser.parse(spectype)
    assert attribute_map.get("_gFhrW2ojEeuExICsU7Acmg") == "ReqIF.ForeignID"
    assert attribute_map.get("_aqZG4GxpEeuaU7fHySy8Bw") == "NOTES"


# [/LLR403-T001]

# [LLR401-T002]
def test_get_id_no_id():
    with pytest.raises(ValueError, match="id_missing"):
        spectype_id, spectype_type, attribute_map = SpectypeParser.parse(
            spectype_no_id
        )


# [/LLR401-T002]

# [LLR401-T003]
def test_get_id_malformed_id():
    with pytest.raises(ValueError, match="id_malformed"):
        spectype_id, spectype_type, attribute_map = SpectypeParser.parse(
            spectype_id_malformed
        )


# [/LLR401-T003]

# [LLR402-T002]
def test_get_type_no_type():
    with pytest.raises(ValueError, match="type_missing"):
        spectype_id, spectype_type, attribute_map = SpectypeParser.parse(
            spectype_no_type
        )


# [/LLR402-T002]

# [LLR402-T003]
def test_get_type_unknown_type():
    with pytest.raises(ValueError, match="unknown_type"):
        spectype_id, spectype_type, attribute_map = SpectypeParser.parse(
            spectype_unknown_type
        )


# [/LLR402-T003]

# [LLR403-T002]
def test_get_attribute_map_malformed_attribute():
    with pytest.raises(ValueError, match="attribute_malformed"):
        spectype_id, spectype_type, attribute_map = SpectypeParser.parse(
            spectype_attribute_malformed
        )


# [/LLR403-T002]
