from pathlib import Path
from typing import Optional, Union

from cryptography.hazmat.primitives.asymmetric.types import PRIVATE_KEY_TYPES
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def load_key_from_disk(
    path: str, secret: Optional[bytes] = None
) -> Union[bytes, PRIVATE_KEY_TYPES]:
    """Load Key from Disk with a given Path

    This Function loads the specified key from disks and returns it as Bytes or Private Key type (if there is a secret specified).

    Args:
        path (str): path to the keyfile
        secret (str, optional): secret for the keyfile. Defaults to None.

    Returns:
        Union[bytes, PRIVATE_KEY_TYPES]: the loaded key
    """

    file = Path(path)
    key_bytes = file.read_bytes()

    # if no secret is specified return the bytes as is
    if secret is None:
        return key_bytes

    return serialization.load_pem_private_key(
        key_bytes, password=secret, backend=default_backend()
    )
