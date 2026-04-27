"""Post-install hook for the FIMserve Viewer Tethys app.

`tethys install -d` runs this script after conda + pip finish. We install
FIMserv directly from GitHub with `--no-deps`, because FIMserv's declared
pyproject.toml dependency list pulls in a huge graph (awscli, jupyter,
notebook, nodejs-bin, localtileserver, …) that this viewer app does not
use at runtime, and asking pip to resolve it triggers
`error: resolution-too-deep`.

If you ever need a different FIMserv revision, change FIMSERV_GIT_REF
below.
"""

from __future__ import annotations

import subprocess
import sys

# Pin FIMserv to a specific commit so the install is reproducible.
FIMSERV_GIT_REF = "83b278931cea5a04e437bf5f2fde947b5904c7b6"
FIMSERV_GIT_URL = (
    f"git+https://github.com/sdmlua/FIMserv.git@{FIMSERV_GIT_REF}#egg=fimserve"
)


def main() -> int:
    cmd = [
        sys.executable,
        "-m",
        "pip",
        "install",
        "--no-deps",
        "--upgrade",
        FIMSERV_GIT_URL,
    ]
    print("[post_install] " + " ".join(cmd), flush=True)
    return subprocess.call(cmd)


if __name__ == "__main__":
    sys.exit(main())
