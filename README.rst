================
jwt_helper
================

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://pypi.org/project/black

.. image:: https://app.codacy.com/project/badge/Grade/bfc97f9667f64c4a9f7d26f937393260
    :target: https://www.codacy.com/gh/bad-microservices/jwt_helper/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=bad-microservices/jwt_helper&amp;utm_campaign=Badge_Grade

.. image:: https://badge.fury.io/py/jwt_helper.svg
    :target: https://badge.fury.io/py/jwt_helper

.. image:: https://github.com/bad-microservices/jwt_helper/actions/workflows/documentation.yaml/badge.svg
   :target: https://github.com/bad-microservices/jwt_helper/actions?query=workflow:Docs

.. image:: https://github.com/bad-microservices/jwt_helper/actions/workflows/pypi_upload.yaml/badge.svg
    :target: https://github.com/bad-microservices/jwt_helper/actions?query=workflow:pypi

Introduction
=============

`jwt_helper`` aims to be a simple to use wrapper around `pyjwt` with some predefined functions to make life easier.

The most important classes of this library are 

* `JWTEncoder` - A simple Helper class to create JWTs 
* `Issuer` - A class which holds Informations about an Entity that signs JWTs
* `JWTValidator` - A simple class containing multiple `Issuer`s which get used to validate JWTs

Examples
=========

Here are some Examples to show different Features of the `jwt_helper` package


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