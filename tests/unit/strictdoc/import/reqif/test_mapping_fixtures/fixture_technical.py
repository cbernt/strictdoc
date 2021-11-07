import pytest


@pytest.fixture
def fixture_technical_type_map():
    attributes_map = {
        "_oE860C2FEeyvlO4vtsM_UA": "requirement_ID",
        "_wgHwUC2FEeyvlO4vtsM_UA": "allocation_to_component",
        "_4xnFYC2FEeyvlO4vtsM_UA": "asil",
        "_-_ye4C2FEeyvlO4vtsM_UA": "status",
        "_7Eyo8C2FEeyvlO4vtsM_UA": "target_value",
        "_rWmRwC2FEeyvlO4vtsM_UA": "technical_description",
        "_9J6iYC2FEeyvlO4vtsM_UA": "comment",
    }
    type_map = {"_dSe2wC2FEeyvlO4vtsM_UA": ["technical", attributes_map]}
    return type_map


@pytest.fixture
def fixture_technical_relation_map():
    # spec_object_type = "test"
    relation_map = {
        "LLR204": ["LLR001", "SR001"],
        "LLR002-T001": ["LLR002", "SR002"],
    }
    return relation_map


@pytest.fixture
def fixture_technical_uid():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_uid_malformed():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="!?LLR204?!as''''''df">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_uid_missing():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_allocation_to_component():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_allocation_to_component_malformed():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="''software''">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_asil():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_asil_malformed():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="IL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_status():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_status_malformed():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="M4lf0rm'3d">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_target_value():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_target_value_malformed():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SP3CIaL_F'''''i3LD(initial_c0ndiTi0n)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_target_value_missing():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_technical_description():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_technical_description_malformed():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="!?adsfasdf?!'">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_technical_description_missing():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_comment():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="no comment">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_technical_comment_malformed():
    # 1 create testobject from string
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_twogozC5EeyQ56CSv4ZenA" LAST-CHANGE="2021-10-19T10:52:02.224+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR204">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_oE860C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_-_ye4C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="ASIL-A">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_4xnFYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_wgHwUC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SPECIAL FIELD(initial_condition)">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_7Eyo8C2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The mapping function shall map initial_condition to SPECIAL FIELD(initial_condition).">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_rWmRwC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="'abc'">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_9J6iYC2FEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_dSe2wC2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos
