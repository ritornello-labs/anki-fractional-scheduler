from __future__ import annotations

import json
import os
import sys

from aqt import gui_hooks, mw
from aqt.qt import QApplication, QTimer

RESULT_ENV = "ANKI_ADDON_WORKBENCH_RESULT"
ADDON_MODULE = "fractional_scheduler"
TOOLS_ACTION = "Fractional Scheduler: Open Config"


def _write(payload: dict) -> None:
    with open(os.environ[RESULT_ENV], "w", encoding="utf-8") as handle:
        json.dump(payload, handle)


def _run_checks() -> None:
    try:
        actions = list(mw.form.menuTools.actions())
        tools_actions = [action.text() for action in actions]
        config_action = next(
            (action for action in actions if action.text() == TOOLS_ACTION),
            None,
        )
        dialog_state = {"opened": False, "title": ""}

        def inspect_then_close_dialog() -> None:
            dialog = QApplication.activeModalWidget()
            if dialog is None:
                return
            dialog_state["opened"] = True
            dialog_state["title"] = dialog.windowTitle()
            QTimer.singleShot(3_000, dialog.reject)

        if config_action is not None:
            QTimer.singleShot(500, inspect_then_close_dialog)
            config_action.trigger()

        _write(
            {
                "ok": (
                    ADDON_MODULE in sys.modules
                    and TOOLS_ACTION in tools_actions
                    and dialog_state["opened"]
                ),
                "checks": [
                    {"name": "addon module loaded", "ok": ADDON_MODULE in sys.modules},
                    {"name": "Tools action registered", "ok": TOOLS_ACTION in tools_actions},
                    {
                        "name": "config dialog opens",
                        "ok": dialog_state["opened"],
                        "title": dialog_state["title"],
                    },
                ],
                "tools_actions": tools_actions,
            }
        )
    except Exception as exc:
        _write({"ok": False, "error": repr(exc)})
    finally:
        mw.app.quit()


def _after_profile_open() -> None:
    QTimer.singleShot(0, _run_checks)


gui_hooks.profile_did_open.append(_after_profile_open)
