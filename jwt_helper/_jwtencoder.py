import jwt
import datetime

from dataclasses import dataclass
from typing import Union
from cryptography.hazmat.primitives.asymmetric.types import PRIVATE_KEY_TYPES

from ._signmethods import SignMethod


@dataclass
class JWTEncoder:
    """This class helps encoding JWTs

    Attributes:
        issuer (str): The Issuer who created the JWT.
        signmethod (SignMethod): The Algorithm used to create the JWT.
        secret (bytes | PRIVATE_KEY_TYPES | str): The secret used to create the JWT signature
    """

    issuer: str
    signmethod: SignMethod
    secret: Union[bytes, PRIVATE_KEY_TYPES, str]

    def __repr__(self):
        return f"JWTEncoder(issuer={self.issuer!r}, signmethod={self.signmethod!r})"

    def create_jwt(self, headers: dict, body: dict, valid_minutes: int) -> str:
        """This Function will create the JWT Token

        Args:
            headers (dict): additional data for the JWT Header.
            body (dict): the JWT Payload.
            valid_minutes (int): the lifetime of the token.

        Returns:
            str: The JWT Token generated
        """

        valid_until = datetime.datetime.now() + datetime.timedelta(
            minutes=valid_minutes
        )

        jwt_headers = {
            "iss": self.issuer,
            "iat": datetime.datetime.now().timestamp(),
            "nbf": datetime.datetime.now().timestamp(),
            "exp": valid_until.timestamp(),
        }

        for key, value in headers.items():
            if key not in ["iss", "iat", "nbf", "exp"]:
                jwt_headers[key] = value

        token = jwt.encode(
            body,
            self.secret,
            headers=jwt_headers,
            algorithm=self.signmethod.value,
        )
        return token
