from xml.etree import ElementTree as etree
from strictdoc.imports.reqif.models.spec_relation_parser import (
    SpecRelationParser,
)
import pytest

specrelations_Object_string = r"""<SPEC-RELATIONS>
        <SPEC-RELATION IDENTIFIER="_rFhEcDJJEeyeXuftE5Q6Cw" LAST-CHANGE="2021-10-21T10:34:11.458+02:00">
          <TARGET>
            <SPEC-OBJECT-REF>_lLoc8C2-IEeyvlO4.vtsM_UA</SPEC-OBJECT-REF>
          </TARGET>
          <SOURCE>
            <SPEC-OBJECT-REF>_eDO24C2IEeyvlO4vtsM_UA</SPEC-OBJECT-REF>
          </SOURCE>
          <TYPE>
            <SPEC-RELATION-TYPE-REF>_hD4AYDJJEeyeXuftE5Q6Cw</SPEC-RELATION-TYPE-REF>
          </TYPE>
        </SPEC-RELATION>
      </SPEC-RELATIONS>"""
specrelations_Object = etree.fromstring(specrelations_Object_string)

specrelation_string_invalidID = r"""<SPEC-RELATIONS>
        <SPEC-RELATION IDENTIFIER="_rFhEcDJJEeyeXuftE5Q6Cw" LAST-CHANGE="2021-10-21T10:34:11.458+02:00">
          <TARGET>
            <SPEC-OBJECT-REF>_l%Loc8C2IE?e:vlO4!vtsM_UA</SPEC-OBJECT-REF>
          </TARGET>
          <SOURCE>
            <SPEC-OBJECT-REF>_eD/O24C2IEe#yvlO4vtsäM_UA</SPEC-OBJECT-REF>
          </SOURCE>
          <TYPE>
            <SPEC-RELATION-TYPE-REF>_hD4AYDJJEeyeXuftE5Q6Cw</SPEC-RELATION-TYPE-REF>
          </TYPE>
        </SPEC-RELATION>
      </SPEC-RELATIONS>"""
specrelations_invalidID = etree.fromstring(specrelation_string_invalidID)

specrelation_string_missingID = r"""<SPEC-RELATIONS>
        <SPEC-RELATION IDENTIFIER="_rFhEcDJJEeyeXuftE5Q6Cw" LAST-CHANGE="2021-10-21T10:34:11.458+02:00">
          <TARGET>
            <SPEC-OBJECT-REF></SPEC-OBJECT-REF>
          </TARGET>
          <SOURCE>
            <SPEC-OBJECT-REF></SPEC-OBJECT-REF>
          </SOURCE>
          <TYPE>
            <SPEC-RELATION-TYPE-REF>_hD4AYDJJEeyeXuftE5Q6Cw</SPEC-RELATION-TYPE-REF>
          </TYPE>
        </SPEC-RELATION>
      </SPEC-RELATIONS>"""
specrelations_missingID = etree.fromstring(specrelation_string_missingID)


# [LLR301-T001]
def test_specrelationparser_positive():
    relation_map = SpecRelationParser.parse(specrelations_Object)

    assert (
        relation_map["_lLoc8C2-IEeyvlO4.vtsM_UA"] == "_eDO24C2IEeyvlO4vtsM_UA"
    )


# [/LLR301-T001]


# [LLR301-T002]
def test_specrelationparser_malformed_invalidID():
    with pytest.raises(ValueError, match="specrelations_invalidID"):
        relation_map = SpecRelationParser.parse(specrelations_invalidID)


# [/LLR301-T002]

# [LLR301-T003]
def test_specrelationparser_malformed_missingID():
    with pytest.raises(ValueError, match="specrelations_missingID"):
        relation_map = SpecRelationParser.parse(specrelations_missingID)


# [/LLR301-T003]
