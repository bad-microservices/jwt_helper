from dataclasses import dataclass
from typing import Union

from jwt_helper._signmethods import SignMethod
from jwt_helper._load_key_from_disk import load_key_from_disk

import base64

SECRET_METHODS = {
    "plain": lambda val: val,
    "base64plain": lambda val: base64.b64decode(val.encode("utf-8")).decode("utf8"),
    "base64key": base64.b64decode,
    "keyfile": load_key_from_disk,
}


@dataclass
class Issuer:
    """This class represents an Issuer

    An Issuer is an auth-server which creates JWT Tokens. We list supported Methods for validating there cookies and the Secret belonging to it here.
    We have a list of supported methods here so Attackers cant swap the signing method around (for example switching from HS to RS Signature and
    using the Public Key as HMAC secret)

    Attributes:
        name (str): The name of the issuer which is also included in the JWT Header
        secret (bytes | string): either the symetric HMAC secret or the Public key used to verify the Signature
        methods (list[SignMethod]): The list of supported Signin Methods for the specified Issuer

    """

    name: str
    secret: Union[bytes, str]
    methods: list[SignMethod]

    def __repr__(self):
        return f"Issuer(name: {self.name}, methods: {self.methods})"

    @staticmethod
    def from_dict(data: dict):
        # translate sign methods
        methods = []
        for method in data["methods"]:
            methods.append(SignMethod[method])
        # load key the specified way
        key_type = data["secret"]["type"]
        secret_value = data["secret"]["value"]

        if not (
            key_type == "keyfile"
            or key_type == "base64plain"
            or key_type == "base64key"
            or key_type == "plain"
        ):
            raise ValueError(f"keytype {key_type} not supported")
        secret = SECRET_METHODS[key_type](secret_value)

        return Issuer(data["name"], secret, methods)
