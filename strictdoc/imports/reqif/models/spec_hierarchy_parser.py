import re
from collections import defaultdict
from xml.etree.ElementTree import Element


class SpecHierarchyParser:
    @staticmethod
    def parse(specifications):
        """Creates a Map of Child/Parent Links from an eTree Element,
        containing an SpecHierarchy ReqIF"""

        specifications_list = list(specifications)
        relation_map = defaultdict(list)
        for specification in specifications_list:
            specification: Element
            # finds all Children from:
            # (REQ-IF >
            #   CORE-Content >
            #     REQ-IF-CONTENT) >
            #       SPECIFICATIONS >
            #         SPECIFICATION
            children_list = list(specification)[2]
            for spechierarchy in children_list:
                SpecHierarchyParser._recursive(
                    spechierarchy, None, relation_map
                )

        return relation_map

    @staticmethod
    def _recursive(spechierarchy_element, parent_id, relation_map):
        if spechierarchy_element is not None:
            object_element = list(spechierarchy_element)[0]
            spec_object_ref = list(object_element)[0]
            child_id = spec_object_ref.text
            if parent_id is not None:
                regex_search = re.compile("^[a-zA-Z0-9_\\-.]+$")
                if not regex_search.match(parent_id):
                    raise ValueError("spechierarchy_invalidID")
                if not regex_search.match(child_id):
                    raise ValueError("spechierarchy_invalidID")

                parent_list = relation_map[child_id]
                parent_list.append(parent_id)

            spechierarchy_element_list = list(spechierarchy_element)
            if len(spechierarchy_element_list) >= 2:
                children_element = spechierarchy_element_list[1]
                for spec_hierarchy_element in children_element:
                    SpecHierarchyParser._recursive(
                        spec_hierarchy_element, child_id, relation_map
                    )
