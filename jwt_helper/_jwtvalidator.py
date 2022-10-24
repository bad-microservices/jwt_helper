import jwt

from dataclasses import dataclass, field

from ._issuer import Issuer


@dataclass
class JWTValidator:
    """A class to help verify JWT Tokens

    Attributes:
        issuers (dict): A dictionary storing our Trusted Issuers and their methods and secrets
    """

    issuers: dict[str, Issuer] = field(default_factory=dict)

    def verify_jwt(self, token: str) -> bool:
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

    @staticmethod
    def get_jwt_as_dict_untrusted(jwt_token:str) -> dict:
        """Returns the content of the JWT without validating its signature.

        Args:
            jwt_token (str): jwt to decode

        TODO:
            * add example code here

        Returns:
            dict: JWT Content as dict
        """

        return {
            "headers":jwt.get_unverified_header(jwt_token),
            "payload":jwt.decode(jwt_token, options={"verify_signature": False})
        }

    def get_jwt_as_dict(self,jwt_token:str) -> dict:
        """Gets JWT Content as dict but verifies the JWT itself

        Args:
            jwt_token (str): JWT Token to get the data from

        Raises:
            ValueError: If jwt could not be validated

        Returns:
            dict: JWT Content as dict
        """

        if not self.verify_jwt(jwt_token):
            raise ValueError("JWT Invalid")

        return JWTValidator.get_jwt_as_dict_untrusted(jwt_token) 


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
