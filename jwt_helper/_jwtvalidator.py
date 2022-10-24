import jwt

from dataclasses import dataclass,field
from typing import Union

from ._issuer import Issuer
from ._signmethods import SignMethod

@dataclass
class JWTValidator:
    """A class to help verify JWT Tokens

    Attributes:
        issuers (dict): A dictionary storing our Trusted Issuers and their methods and secrets
    """
    issuers: dict[str, Issuer] = field(default_factory=dict)

    def check_token(self, token: str) -> bool:
        """Function to check if a token is valid

        This Function checks a JWT Token for it's validity. The Tokens 'iss' Header entry gets used to determine
        the Issuer from our Issuers list.

        Args:
            token (str): JWT Token we want to verify

        Raises:
            ValueError: If the Issuer is not known to us throw this

        Returns:
            bool: Validity of the Token
        """

        # get token header
        headers = jwt.get_unverified_header(token)

        # get_issuer
        try:
            issuer = self.issuers[headers["iss"]]
        except KeyError:
            raise ValueError("Tokens Issuer is not Trusted")

        # validate token
        jwt.decode(
            token,
            key=issuer.secret,
            algorithms=[method.value for method in issuer.methods],
            options={"require": ["exp", "iss"]},
        )

        return True

    def remove_issuer(self, issuer: str) -> bool:
        """Remove and issuer (by name) from our dictionary of trusted issuers

        Args:
            issuer (str): Name of the Issuer to remove

        Returns:
            bool: Removal success
        """
        try:
            self.issuers.pop(issuer)
            return True
        except KeyError:
            return False
