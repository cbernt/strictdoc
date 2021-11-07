import pytest


@pytest.fixture
def fixture_functional_type_map():
    attributes_map = {
        "_FEHY0C2GEeyvlO4vtsM_UA": "requirement_ID",
        "_KMVP0C2GEeyvlO4vtsM_UA": "allocation",
        "_MZGCUC2GEeyvlO4vtsM_UA": "asil",
        "_OlZh0C2GEeyvlO4vtsM_UA": "status",
        "_Hx6b0C2GEeyvlO4vtsM_UA": "functional_description",
    }
    type_map = {"_gV9O0C2FEeyvlO4vtsM_UA": ["functional", attributes_map]}
    return type_map


@pytest.fixture
def fixture_functional_relation_map():
    relation_map = {
        "SR001": ["LLR001", "SR002"],
        "LLR002-T001": ["LLR002", "SR003"],
    }
    return relation_map


@pytest.fixture
def fixture_functional_correctreqifobject():
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_eDO24C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-19T11:35:12.673+02:00">
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
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The import function shall import a .reqif file and convert it to an .sdoc file.">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_Hx6b0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_gV9O0C2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_functional_missing_uid():
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_eDO24C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-19T11:35:12.673+02:00">
          <VALUES>
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
            <ATTRIBUTE-VALUE-STRING THE-VALUE="none">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_MZGCUC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The import function shall import a .reqif file and convert it to an .sdoc file.">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_Hx6b0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_gV9O0C2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_functional_malformed_uid():
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_eDO24C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-19T11:35:12.673+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="\\n\n\n\n">
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
            <ATTRIBUTE-VALUE-STRING THE-VALUE="none">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_MZGCUC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The import function shall import a .reqif file and convert it to an .sdoc file.">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_Hx6b0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_gV9O0C2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_functional_malformed_allocation():
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_eDO24C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-19T11:35:12.673+02:00">
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
            <ATTRIBUTE-VALUE-STRING THE-VALUE="?\n\\n\n">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_KMVP0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="none">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_MZGCUC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The import function shall import a .reqif file and convert it to an .sdoc file.">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_Hx6b0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_gV9O0C2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_functional_malformed_asil():
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_eDO24C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-19T11:35:12.673+02:00">
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
            <ATTRIBUTE-VALUE-STRING THE-VALUE="abc">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_MZGCUC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The import function shall import a .reqif file and convert it to an .sdoc file.">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_Hx6b0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_gV9O0C2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_functional_malformed_status():
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_eDO24C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-19T11:35:12.673+02:00">
          <VALUES>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="SR001">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_FEHY0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="?\n\n\\n">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_OlZh0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="Software">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_KMVP0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="none">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_MZGCUC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="The import function shall import a .reqif file and convert it to an .sdoc file.">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_Hx6b0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_gV9O0C2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_functional_malformed_title():
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_eDO24C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-19T11:35:12.673+02:00">
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
            <ATTRIBUTE-VALUE-STRING THE-VALUE="none">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_MZGCUC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
            <ATTRIBUTE-VALUE-STRING THE-VALUE="?\n\n\\n">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_Hx6b0C2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_gV9O0C2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos


@pytest.fixture
def fixture_functional_missing_title():
    object_string_pos = r"""<SPEC-OBJECT IDENTIFIER="_eDO24C2IEeyvlO4vtsM_UA" LAST-CHANGE="2021-10-19T11:35:12.673+02:00">
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
            <ATTRIBUTE-VALUE-STRING THE-VALUE="none">
              <DEFINITION>
                <ATTRIBUTE-DEFINITION-STRING-REF>_MZGCUC2GEeyvlO4vtsM_UA</ATTRIBUTE-DEFINITION-STRING-REF>
              </DEFINITION>
            </ATTRIBUTE-VALUE-STRING>
          </VALUES>
          <TYPE>
            <SPEC-OBJECT-TYPE-REF>_gV9O0C2FEeyvlO4vtsM_UA</SPEC-OBJECT-TYPE-REF>
          </TYPE>
        </SPEC-OBJECT>"""
    return object_string_pos
