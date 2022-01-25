import os
from pathlib import Path

from reqif.unparser import ReqIFUnparser

from strictdoc.cli.cli_arg_parser import ExportCommandConfig
from strictdoc.core.document_tree import DocumentTree
from strictdoc.backend.reqif.export.sdoc_to_reqif_converter import (
    SDocToReqIFObjectConverter,
)


class ReqIFExport:
    @staticmethod
    def export(
        config: ExportCommandConfig,
        document_tree: DocumentTree,
        output_reqif_root: str,
    ):
        Path(output_reqif_root).mkdir(parents=True, exist_ok=True)
        output_file = os.path.join(output_reqif_root, "output.reqif")

        reqif_bundle = SDocToReqIFObjectConverter.convert_document_tree(
            config=config, document_tree=document_tree
        )
        reqif_content = ReqIFUnparser.unparse(reqif_bundle)

        with open(output_file, "w", encoding="utf8") as output_file:
            output_file.write(reqif_content)
