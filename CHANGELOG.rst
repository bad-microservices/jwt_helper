Changelog
===============

0.0.10
-------
* added :code:`not_before_grace_time` as parameter to :code:`JWTValidator.verify_jwt`
  * Defaults to 30 seconds

0.0.9
------
* Fix Deprecation Warning for :code:`PRIVATE_KEY_TYPES`

0.0.8
------
* verifying the token did not properly check it...
* check :code:`exp` claim manualy in :code:`verify_jwt` function
* check :code:`nbf` claim manualy in :code:`verify_jwt` function

0.0.7
------
* Bugfix `for key, value in headers.items():` was missing `.items()`

0.0.6
------
* changed `file.read_bytes` to `file.read_bytes()`

0.0.5
------
* `"require": ["exp","iss"]` did not work as excepted. changed it.

0.0.4
------
* fixed bug in `create_jwt`... i should write some tests

0.0.3
------
* added `add_issuer` function to JWTValidator class

0.0.2
------
* added `get_jwt_as_dict_untrusted`
* added `get_jwt_as_dict`

0.0.1
------
* Initial Version
* Supports the following algorithms
    * Symetric
        * HS256
        * HS384
        * HS512
    * Asymetric
        * RS256
        * RS384
        * RS512