import os
import sys
from jinja2 import Environment, PackageLoader,FileSystemLoader, StrictUndefined

from strictdoc.export.html.document_type import DocumentType


class DocumentTableHTMLGenerator:
    env = Environment(
        loader=PackageLoader("strictdoc", "export/html/templates"),
        undefined=StrictUndefined,
    )
    env.globals.update(isinstance=isinstance)

    @staticmethod
    def export(
        config, document, traceability_index, markup_renderer, link_renderer
    ):
        output = ""

        if getattr(sys, 'frozen', False):
             # we are running in a bundle
            exe_dir = sys._MEIPASS
            
            bundle_dir = os.path.join(exe_dir,"strictdoc","strictdoc","export","html","templates")
            print("bundledir:" + bundle_dir)
            l_loader = FileSystemLoader(searchpath=bundle_dir)
            l_env = Environment(
                loader=l_loader,
                undefined=StrictUndefined,
            )
            template = l_env.get_template(
                "single_document_table/document.jinja.html"
                )
        else:
            template = DocumentTableHTMLGenerator.env.get_template(
                "single_document_table/document.jinja.html"
            )

        root_path = document.meta.get_root_path_prefix()
        static_path = f"{root_path}/_static"
        document_iterator = traceability_index.get_document_iterator(document)

        output += template.render(
            config=config,
            document=document,
            traceability_index=traceability_index,
            renderer=markup_renderer,
            link_renderer=link_renderer,
            document_type=DocumentType.table(),
            standalone=False,
            root_path=root_path,
            static_path=static_path,
            document_iterator=document_iterator,
        )

        return output
