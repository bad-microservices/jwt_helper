Changelog
===============

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