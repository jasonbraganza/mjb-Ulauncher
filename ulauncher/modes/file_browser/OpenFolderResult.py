from __future__ import annotations

from ulauncher.internals import actions
from ulauncher.internals.query import Query
from ulauncher.internals.result import Result


class OpenFolderResult(Result):
    compact = True
    icon = "system-file-manager"
    path = ""

    def on_activation(self, _query: Query, _alt: bool = False) -> dict[str, str]:
        return actions.Open(self.path)
