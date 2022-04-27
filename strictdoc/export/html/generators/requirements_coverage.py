import os
import sys
from jinja2 import Environment, PackageLoader,FileSystemLoader, StrictUndefined

from strictdoc.cli.cli_arg_parser import ExportCommandConfig
from strictdoc.core.document_tree_iterator import DocumentTreeIterator
from strictdoc.core.traceability_index import TraceabilityIndex
from strictdoc.export.html.document_type import DocumentType
from strictdoc.export.html.renderers.markup_renderer import MarkupRenderer


class RequirementsCoverageHTMLGenerator:
    env = Environment(
        loader=PackageLoader("strictdoc", "export/html/templates"),
        undefined=StrictUndefined,
    )
    env.globals.update(isinstance=isinstance)

    @staticmethod
    def export(
        config: ExportCommandConfig,
        document_tree,
        traceability_index: TraceabilityIndex,
        link_renderer,
    ):
        document_tree_iterator = DocumentTreeIterator(document_tree)

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
            template = l_env.get_template("requirements_coverage/requirements_coverage.jinja.html")
        else:   
            template = RequirementsCoverageHTMLGenerator.env.get_template(
                "requirements_coverage/requirements_coverage.jinja.html"
            )

        markup_renderer = MarkupRenderer.create(
            "RST",
            traceability_index,
            link_renderer,
            None,
        )
        output += template.render(
            config=config,
            document_tree=document_tree,
            traceability_index=traceability_index,
            documents_iterator=document_tree_iterator.iterator(),
            link_renderer=link_renderer,
            renderer=markup_renderer,
            static_path="_static",
            document_type=DocumentType.deeptrace(),
        )

        return output
