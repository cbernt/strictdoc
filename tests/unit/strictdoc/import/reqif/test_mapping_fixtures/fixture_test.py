# test_mapping_test.py
import pytest


@pytest.fixture
def fixture_test_type_map():
    # spec_object_type = "test"
    attributes_map = {
        "_BSKKIS2GEeyvlO4vtsM_UA": "requirement_ID",
        "_BSKKJC2GEeyvlO4vtsM_UA": "type",
        "_BSKKJS2GEeyvlO4vtsM_UA": "initial_condition",
        "_BSKKJi2GEeyvlO4vtsM_UA": "test_sequence",
        "_a5wPYC2GEeyvlO4vtsM_UA": "target_value",
        "_DjbacC2MEeyvlO4vtsM_UA": "objective",
        "_IjYFQC2XEeyvlO4vtsM_UA": "traceability",
        "_g_yJwC2XEeyvlO4vtsM_UA": "status",
    }
    type_map = {"_BSKKIC2GEeyvlO4vtsM_UA": ["test", attributes_map]}
    return type_map


@pytest.fixture
def fixture_test_relation_map():
    # spec_object_type = "test"
    relation_map = {
        "LLR001-T001": ["LLR001", "SLR001"],
        "LLR002-T001": ["LLR002", "SLR002"],
    }
    return relation_map


@pytest.fixture
def fixture_test_uid():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_uid_malformed():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="SR1114f'?">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_uid_missing():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_type_malformed():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Soft'ware">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_traceability_malformed():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="malforme'd">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_traceability_missing():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_title_malformed():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Test'Me">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_title_missing():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_initial_condition_malformed():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="malformed'''''">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_initial_condition_missing():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_test_sequence_malformed():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="MALFORME''''DDD">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_test_sequence_missing():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_target_value_malformed():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="mal'formed">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_target_value_missing():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Draft">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string


@pytest.fixture
def fixture_test_status_malformed():
    # 1 create testobject from string
    object_string = r"""<SPEC-OBJECT IDENTIFIER="_21rDgC2NEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-15T11:37:14.335+02:00">
              <VALUES>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="LLR001-T001">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKIS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="true">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_a5wPYC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The test function shall test the mapping of the ReqIF attribute requirement_ID to the SDoC attribute UID.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_DjbacC2MEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="ReqIF requirement_ID is passed into the mapping function.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJS2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="The correct value for the requirement_ID shall be passed to the function and the function returns the same value as result and compares it to the predefined test value.">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_BSKKJi2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="Malforme'd">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_g_yJwC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
                <ATTRIBUTE-VALUE-STRING THE-VALUE="..\..\..\tests\unit\strictdoc\import\reqif">
                  <DEFINITION>
                    <ATTRIBUTE-DEFINITION-STRING-REF>_IjYFQC2XEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
                  </DEFINITION>
                </ATTRIBUTE-VALUE-STRING>
              </VALUES>
              <TYPE>
                <SPEC-OBJECT-TYPE-REF>_BSKKIC2GEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
              </TYPE>
            </SPEC-OBJECT>"""
    return object_string
