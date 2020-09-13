import collections
import os

from jinja2 import Template, Environment, PackageLoader, select_autoescape

from strictdoc.backend.dsl.models import Requirement
from strictdoc.core.document_tree import FileTree, File
from strictdoc.helpers.hyperlinks import string_to_anchor_id


def get_path_components(folder_path):
    path = os.path.normpath(folder_path)
    return path.split(os.sep)


def get_traceability_link(document_name):
    return "{} - Traceability.html".format(document_name)


def get_traceability_deep_link(document_name):
    return "{} - Traceability Deep.html".format(document_name)


class DocumentTreeHTMLExport:
    OFFSET = 8

    env = Environment(
        loader=PackageLoader('strictdoc', 'export/html/templates'),
        # autoescape=select_autoescape(['html', 'xml'])
    )
    env.globals.update(isinstance=isinstance)

    @staticmethod
    def export(document_tree):
        task_list = collections.deque([document_tree.file_tree])
        artefact_list = []

        while task_list:
            file_tree_or_file = task_list.popleft()
            artefact_list.append(file_tree_or_file)
            if isinstance(file_tree_or_file, FileTree):
                task_list.extendleft(reversed(file_tree_or_file.files))
                task_list.extendleft(reversed(file_tree_or_file.subfolder_trees))


        template = SingleDocumentHTMLExport.env.get_template('document_tree/document_tree.jinja.html')
        output = template.render(document_tree=document_tree,
                                 artefact_list=artefact_list,
                                 get_traceability_link=get_traceability_link,
                                 get_traceability_deep_link=get_traceability_deep_link)

        return output

        output += "<h1>Document tree</h1>"

        output += "<div>"
        for folder_or_file in artefact_list:
            print(folder_or_file)
            if isinstance(folder_or_file, FileTree):
                folder_name = folder_or_file.get_folder_name()
                output += "<div>"
                output += "&nbsp;" * folder_or_file.level * DocumentTreeHTMLExport.OFFSET
                output += "{}/".format(folder_name)
                output += "</div>"
            elif isinstance(folder_or_file, File):
                doc_full_path = folder_or_file.get_full_path()
                document = document_tree.document_map[doc_full_path]
                document_path = '{}.html'.format(document.name)
                output += "<div>"
                output += "&nbsp;" * (folder_or_file.get_level()) * DocumentTreeHTMLExport.OFFSET
                output += '{} (<a href="{}">{}</a>, <a href="{}">{} - Traceability</a>, <a href="{}">{}</a>)'.format(
                    folder_or_file.get_file_name(),
                    document_path, document.name,
                    get_traceability_link(document), document.name,
                    get_traceability_deep_link(document), 'Traceability Deep'
                )
                output += "</div>"

        output += "</div>"
        output += '</body>'

        return output


class SingleDocumentHTMLExport:
    env = Environment(
        loader=PackageLoader('strictdoc', 'export/html/templates'),
        # autoescape=select_autoescape(['html', 'xml'])
    )
    env.globals.update(isinstance=isinstance)

    @staticmethod
    def export(document):
        print("doc: {}, number of sections: {}".format(document.name, len(document.section_contents)))
        output = ""

        template = SingleDocumentHTMLExport.env.get_template('single_document/document.jinja.html')

        output += template.render(document=document)

        return output


class SingleDocumentTraceabilityHTMLExport:
    env = Environment(
        loader=PackageLoader('strictdoc', 'export/html/templates'),
        # autoescape=select_autoescape(['html', 'xml'])
    )
    env.globals.update(isinstance=isinstance)

    @staticmethod
    def export(document_tree, document, traceability_index):
        print("doc: {}, number of sections: {}".format(document.name, len(document.section_contents)))
        output = ""

        template = SingleDocumentHTMLExport.env.get_template('single_document_traceability/document.jinja.html')

        output += template.render(document=document,
                                  traceability_index=traceability_index,
                                  string_to_anchor_id=string_to_anchor_id)

        return output

    @staticmethod
    def export_deep(document_tree, document, traceability_index):
        print("doc: {}, number of sections: {}".format(document.name, len(document.section_contents)))
        output = ""

        template = SingleDocumentHTMLExport.env.get_template('single_document_traceability_deep/document.jinja.html')

        output += template.render(document=document,
                                  traceability_index=traceability_index,
                                  string_to_anchor_id=string_to_anchor_id)

        return output
