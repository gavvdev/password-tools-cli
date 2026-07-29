import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).parent / "password-tools")
)

from password_tools import (
    generate_password,
    check_strength,
    is_common_password,
    generate_passphrase,
)
