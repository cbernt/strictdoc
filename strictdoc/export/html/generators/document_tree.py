import os
import sys
from jinja2 import Environment, PackageLoader,FileSystemLoader, StrictUndefined

from strictdoc.core.document_tree_iterator import DocumentTreeIterator
from strictdoc.core.traceability_index import TraceabilityIndex


class DocumentTreeHTMLGenerator:
       
    env = Environment(
        loader=PackageLoader("strictdoc", "export/html/templates"),
        undefined=StrictUndefined,
    )
    env.globals.update(isinstance=isinstance)

    @staticmethod
    def export(config, document_tree, traceability_index: TraceabilityIndex):
        document_tree_iterator = DocumentTreeIterator(document_tree)

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
            template = l_env.get_template("document_tree/document_tree.jinja.html")
        else:   
            template = DocumentTreeHTMLGenerator.env.get_template(
                "document_tree/document_tree.jinja.html"
            )
        output = template.render(
            config=config,
            document_tree=document_tree,
            artefact_list=document_tree_iterator.iterator(),
            static_path="_static",
            traceability_index=traceability_index,
        )

        return output
