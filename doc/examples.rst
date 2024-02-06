Examples
=================

Creating a `JWTEncoder` to create JWTs
---------------------------------------

.. code-block:: python

    from jwt_helper import JWTEncoder, SignMethod

    jwt_encoder = JWTEncoder(
        issuer="test_issuer", signmethod=SignMethod.HS512, secret="super_secret_hmac_key"
    )


Creating a JWT with that `JWTEncoder`
--------------------------------------

.. code-block:: python

    jwt = jwt_encoder.create_jwt(
        headers={"generic_jwt_header_item": "test123"},
        body={"username": "test123"},
        valid_minutes=10,
    )


Creating a `JWTValidator` with multiple known JWT Issuers
----------------------------------------------------------


.. code-block:: python

    from jwt_helper import JWTValidator, Issuer, SignMethod

    validator = JWTValidator()
    validator.add_issuer(
        Issuer(
            name="test_issuer",
            secret="super_secret_hmac_key",
            methods=[SignMethod.HS256, SignMethod.HS384, SignMethod.HS512],
        )
    )

    validator.add_issuer(
        Issuer(
            name="another_jwt_issuer",
            secret="another secret hmac key",
            methods=[SignMethod.HS256],
        )
    )


Verifying the generated JWT with the validator
------------------------------------------------

.. code-block:: python

    if not validator.verify_jwt(jwt):
        print("JWT is invalid")

    jwt_content = validator.get_jwt_as_dict(jwt)