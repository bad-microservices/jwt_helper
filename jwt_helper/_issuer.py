from dataclasses import dataclass
from typing import Union

from ._signmethods import SignMethod


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
    name:str
    secret: Union[bytes, str]
    methods: list[SignMethod]

