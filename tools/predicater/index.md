# predicater

[predicater](index.md) 0.0.0.9000

- [Reference](reference/index.md)
- [Changelog](news/index.md)

&nbsp;

- 

Validation of R objects with more consistency and flexibility than base
‘is’ functions, having predictable and well documented behavior.
Provides simple ‘is’/‘are’/‘has’ predicates, and complex assertions for
common input validation needs. Includes improved object comparison,
prototypes, if-else chains, and pattern matching.

predicater has three main parts:

- **Simple predicates:** functions to test the type/data (`is_*()`) or
  attributes (`has_*()`) of an object. Always returning a logical
  scalar, but with vectorized versions (`are_*()`). They are better
  named and more consistent than base R `is.*()` functions, while at the
  same time allowing the user more flexibility.
- **Complex predicates and assertions:** functions to test multiple
  properties of an object (`test_*()`) and raise informative errors when
  any of the tests fails (`assert_*()`). They are useful for input
  validation, and allow lots of control, meeting most of the needs a
  developer can have.
- **Objects comparison:** a more flexible
  [`base::identical()`](https://rdrr.io/r/base/identical.html); a notion
  of *prototype* (see [vctrs
  prototypes](https://vctrs.r-lib.org/articles/type-size.html)) expanded
  for any metadata/attributes; pattern matching, similar to
  [`base::switch()`](https://rdrr.io/r/base/switch.html) but for any
  object, not just strings; and self-contained re-exports of
  [`funs::if_else()`](https://rdrr.io/pkg/funs/man/if_else.html) and
  [`dplyr::case_when()`](https://dplyr.tidyverse.org/reference/case_when.html).

## Main contributions to the ecosystem

This package extends the consistency that
[rlang](https://rlang.r-lib.org/) brings to the R ecosystem, by
introducing predicates for types, attributes, and other properties
missing in rlang.

The validation functions are an alternative to several other packages,
currently two of the most prominent being
[checkmate](https://mllg.github.io/checkmate/) and
[chk](https://github.com/poissonconsulting/chk). This package offers
more control over the tests, a more modern error reporting, and a
clearer separation between testing the type/data of an object and its
attributes – e.g. [`test_integer()`](reference/tests-numeric.md) for the
type and values v.s. [`test_matrix()`](reference/test_matrix.md) for the
‘dim’ and ‘dimnames’ attributes. At the same time, these packages are
much more established and have a bigger commitment to performance than
this one currently has.

Finally, the ‘comparison’ functions present useful additions to R logic:
the pattern matching in `match_*()` functions seems like a long needed
addition to the R language; the [`is_ptype()`](reference/is_ptype.md)
function generalizes testing the metadata of an object; and
[`identical2()`](reference/identical2.md),
[`if_else2()`](reference/if_else2.md), and
[`case_when2()`](reference/case_when2.md) are modern versions of very
popular functions.

## Main functions

predicater standardizes the naming and API of many
`is_*()`/`has_*()`/`are_*()` functions, but the most novel ones include:

- Testing for attributes with `has_attrs_any`/`all`/`only` and filtering
  with `attrs_rmv`/`keep`.
- More consistent tests for `NA`, `NaN`, `Inf`, and finite values, with
  `is`/[`are_na2()`](reference/is_na2.md),
  `is`/[`are_finite()`](reference/predicates-infinite.md), and
  [`is_nan()`](reference/predicates-infinite.md)/[`is_inf()`](reference/predicates-infinite.md),
  e.g. solving `is.na(NaN) #> TRUE`.
- Expanding the test for ‘any vector type’ to ‘any collection type’ with
  [`is_collection()`](reference/predicates-collections.md), possibly
  including environments, pairlists, expression vectors, and NULL.
- [`is_integer_like()`](reference/is_integer_like.md), that organizes
  the common test for ‘integer-ish’ into two modes: `"unbounded"` -
  difference from `round(x)` within a given tolerance; and `"bounded"` -
  unbounded + within the R integer range. Correctly dealing with `NaN`
  and `Inf` values, while allowing control over `NA` values.
- Testing for names with
  `has`/[`are_names_valid()`](reference/has_names_valid.md), having more
  control over empty, NA, duplicate and invalid names.
- A more organized notion of ‘object’, merging S4/object bits, S4/object
  typeof’s and class attribute in
  [`is_object_like()`](reference/predicates-objects.md) and
  [`object_system()`](reference/object_system.md).
- The compare functions cited in the previous section.

The `test_*()` and `assert_*()` suite introduces a ‘menu’ of sub-tests
shared across functions, with a focus on flexibility, and a modern
reporting of errors. Below is an example for validating an integer-like
object.

[`library`](https://rdrr.io/r/base/library.html)`(``predicater``)`` `` ``# Object to be validated:`` ``x`` ``<-`` `[`c`](https://rdrr.io/r/base/c.html)`(``1.0``, ``2.0``, ``3.0`` ``+`` ``1e-100``, ``4.0``, ``Inf``)`` `` ``# Defining the sub tests:`` ``args`` ``<-`` `[`list`](https://rdrr.io/r/base/list.html)`(`` `` mode ``=`` ``"unbounded"``, ``# Equal to round(x), within a tolerance (will pass)`` `` mode_tol ``=`` `[`sqrt`](https://rdrr.io/r/base/MathFun.html)`(``.Machine``$``double.eps``)``,`` `` len ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``1``, ``10``)``, ``# Length must be between 1 and 10 (will pass)`` `` n_dup ``=`` ``0``, ``# No duplicate values allowed (will pass)`` `` n_nan ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``0``, ``-``2``)``, ``# At most length(x) - 2 NaN values (will pass)`` `` n_na ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``0``, ``2``, ``3``)``, ``# 0, 2, or 3 NA values (will pass)`` `` n_inf ``=`` \``(``n``, ``l``)`` ``n``/``l`` ``<=`` ``0.5``, ``# n of Inf <= 50% of total (will pass)`` `` range ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``-``5``, ``+``5``)``, ``# Values between -5 and 5 (will fail)`` `` set ``=`` `[`list`](https://rdrr.io/r/base/list.html)`(``yes ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``1``)``, no ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``0``)``)``, ``# Must contain 1, and not 0 (will pass)`` `` sentinels ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``"null"``)``, ``# If not a numeric vector, x can be a NULL sentinel`` `` sorted ``=`` ``"desc"``, ``# Must be sorted in descending order (will fail)`` `` custom ``=`` ``NULL`` ``# Any user-given custom function`` ``)`` `` ``rlang``::`[`exec`](https://rlang.r-lib.org/reference/exec.html)`(``test_integer``, ``x``, ``!``!``!``args``)`` ``#> FALSE (not all tests passed)`

Normally one would call `test_integer(x, ...)`, but I defined the
arguments first for visualization purposes.

Note that all sub-tests about ‘the number/size of something’ (len, n_na,
etc.) can have different specifications (a single value, a range, a set
of values, or a custom function). They appear in many other `test_*()`
functions, as well as `set`, `sentinels`, `custom`, etc.

For the validation, often one will call `assert_integer(x, ...)` to
validate user input to his function. Note that `assert_*()` functions
allow control over the conditions’ environment, argument name, and
others.

`my_fun`` ``<-`` ``function``(``x``)`` ``{`` `` ``rlang``::`[`exec`](https://rlang.r-lib.org/reference/exec.html)`(`` `` ``assert_integer``, ``x``, ``!``!``!``args``,`` `` env ``=`` ``rlang``::`[`current_env`](https://rlang.r-lib.org/reference/stack.html)`(``)``, ``` # Shows the error coming from `my_fun()` ``` `` short_circuit ``=`` ``FALSE``, ``# Reports all sub-tests, beyond the first fail`` `` args_cnd ``=`` `[`list`](https://rdrr.io/r/base/list.html)`(``class ``=`` ``"my_fun_error"``)`` `` ``)`` `` `` ``# ... code depending on x's integer properties`` ``}`` `` `[`try`](https://rdrr.io/r/base/try.html)`(``my_fun``(``x``)``)`

``` R
## Error in my_fun(x) : `x` failed `assert_integer()`:
## ✔ (pass) sentinels: no sentinel values allowed.
## ✔ (pass) type  : must pass `predicater::is_integer_like()`() in "unbounded"
##   mode.
## ✔ (pass) len   : length must be in range 1 to 10.
## ✔ (pass) n_na  : #of NA values must be in set 0, 2, and 3.
## ✔ (pass) n_dup : #of duplicate values must be 0.
## ✔ (pass) n_nan : #of NaN values must be in range 0 to -2.
## ✔ (pass) n_inf : #of Inf values must satisfy a custom function.
## ✖ (fail) range : must be in range -5 to 5. Found Inf.
## ✖ (fail) set   : must be in a custom set. Was not.
## ✖ (fail) sorted: must be in descending order. Did not.
## 
## ℹ See `predicater::assert_integer()` and this condition's `rs_assert_error`
##   attribute for details.
```

The error describes each sub-test and the reason (if possible) for the
failure. Tests not defined (e.g. `custom = NULL`) are not reported.

The `assert_*()` functions return `x` on success, so they can be used in
pipelines:

`mtcars``$``mpg`` ``|>`` ``# Some external data`` `` `[`tan`](https://rdrr.io/r/base/Trig.html)`(``)`` ``|>`` ``# Some transformation`` `` `[`assert_double`](reference/tests-numeric.md)`(`` `` range ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``-``10``, ``10``)``, sorted ``=`` ``"asc"``,`` `` x_name ``=`` ``"tan(mpg)"`` `` ``)`` ``|>`` ``# Validation`` `` `[`cos`](https://rdrr.io/r/base/Trig.html)`(``)`` ``|>`` ``# If passes, continue the pipeline`` `` `[`try`](https://rdrr.io/r/base/try.html)`(``)`

``` R
## Error in (function (...)  : `tan(mpg)` failed `assert_double()`:
## ✔ (pass) sentinels: no sentinel values allowed.
## ✖ (fail) range : must be in range -10 to 10. Found -47.0730006551673.
## • (skip) sorted: skiped given failure.
## ✔ (pass) type  : must pass `predicater::is_double()`.
## 
## ℹ See `predicater::assert_double()` and this condition's `rs_assert_error`
##   attribute for details.
```

Note that with `short_circuit = TRUE` (the default), the first failing
sub-test will raise an error, and the rest will be left as ‘(skip)’.

## Installation

You can install the development version of predicater from
[GitHub](https://github.com/predicater) with any of the following
commands:

`# install.packages(c("pak", "renv", "remotes"))`` ``pak``::`[`pak`](https://pak.r-lib.org/reference/pak.html)`(``"ricardo-semiao/predicater"``)`` ``renv``::`[`install`](https://rstudio.github.io/renv/reference/install.html)`(``"ricardo-semiao/predicater"``)`` ``remotes``::`[`install_github`](https://remotes.r-lib.org/reference/install_github.html)`(``"ricardo-semiao/predicater"``)`

## Development status

Currently, predicater is in an **experimental** stage. The API is not
stable yet and will go through breaking changes.

All functions have examples, and they are validated in the test suite.
Still, the tests are not extensive and the functions have not been
battle-tested yet.

Currently, the functions do not verify their inputs, although they are
well documented in the help pages.

In the future, I plan to substitute the underlying engines of many
functions with C code to improve performance and have cleaner access to
the underlying C representation of the R objects.

Some future additions are planned: - `is_*_scalar()` for all types of
objects, that also allow for excluding the `NA` value. - Predicates for
all items in the C data header of R objects, as is the case of
[`has_object_bit()`](reference/predicates-objects.md). - A reporting
framework that allows the user to store the results of `test_*()`
functions and branch from and report them in a more flexible way than
directly raising an error.

## License

- [Full license](LICENSE.md)
- [MIT](https://opensource.org/licenses/mit-license.php) + file
  [LICENSE](LICENSE-text.md)

## Citation

- [Citing predicater](authors.html#citation)

## Developers

- Ricardo Semião\
  Author, maintainer

## Dev status

- [![Lifecycle:
  experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://lifecycle.r-lib.org/articles/stages.html#experimental)
- [![R-CMD-check](https://github.com/ricardo-semiao/predicater/actions/workflows/R-CMD-check.yaml/badge.svg)](https://github.com/ricardo-semiao/predicater/actions/workflows/R-CMD-check.yaml)
- [![Codecov test
  coverage](https://codecov.io/gh/ricardo-semiao/predicater/graph/badge.svg)](https://app.codecov.io/gh/ricardo-semiao/predicater)

Validation of R objects with more consistency and flexibility than base
‘is’ functions, having predictable and well documented behavior.
Provides simple ‘is’/‘are’/‘has’ predicates, and complex assertions for
common input validation needs. Includes improved object comparison,
prototypes, if-else chains, and pattern matching.

predicater has three main parts:

- **Simple predicates:** functions to test the type/data (`is_*()`) or
  attributes (`has_*()`) of an object. Always returning a logical
  scalar, but with vectorized versions (`are_*()`). They are better
  named and more consistent than base R `is.*()` functions, while at the
  same time allowing the user more flexibility.
- **Complex predicates and assertions:** functions to test multiple
  properties of an object (`test_*()`) and raise informative errors when
  any of the tests fails (`assert_*()`). They are useful for input
  validation, and allow lots of control, meeting most of the needs a
  developer can have.
- **Objects comparison:** a more flexible
  [`base::identical()`](https://rdrr.io/r/base/identical.html); a notion
  of *prototype* (see [vctrs
  prototypes](https://vctrs.r-lib.org/articles/type-size.html)) expanded
  for any metadata/attributes; pattern matching, similar to
  [`base::switch()`](https://rdrr.io/r/base/switch.html) but for any
  object, not just strings; and self-contained re-exports of
  [`funs::if_else()`](https://rdrr.io/pkg/funs/man/if_else.html) and
  [`dplyr::case_when()`](https://dplyr.tidyverse.org/reference/case_when.html).

## Main contributions to the ecosystem

This package extends the consistency that
[rlang](https://rlang.r-lib.org/) brings to the R ecosystem, by
introducing predicates for types, attributes, and other properties
missing in rlang.

The validation functions are an alternative to several other packages,
currently two of the most prominent being
[checkmate](https://mllg.github.io/checkmate/) and
[chk](https://github.com/poissonconsulting/chk). This package offers
more control over the tests, a more modern error reporting, and a
clearer separation between testing the type/data of an object and its
attributes – e.g. [`test_integer()`](reference/tests-numeric.md) for the
type and values v.s. [`test_matrix()`](reference/test_matrix.md) for the
‘dim’ and ‘dimnames’ attributes. At the same time, these packages are
much more established and have a bigger commitment to performance than
this one currently has.

Finally, the ‘comparison’ functions present useful additions to R logic:
the pattern matching in `match_*()` functions seems like a long needed
addition to the R language; the [`is_ptype()`](reference/is_ptype.md)
function generalizes testing the metadata of an object; and
[`identical2()`](reference/identical2.md),
[`if_else2()`](reference/if_else2.md), and
[`case_when2()`](reference/case_when2.md) are modern versions of very
popular functions.

## Main functions

predicater standardizes the naming and API of many
`is_*()`/`has_*()`/`are_*()` functions, but the most novel ones include:

- Testing for attributes with `has_attrs_any`/`all`/`only` and filtering
  with `attrs_rmv`/`keep`.
- More consistent tests for `NA`, `NaN`, `Inf`, and finite values, with
  `is`/[`are_na2()`](reference/is_na2.md),
  `is`/[`are_finite()`](reference/predicates-infinite.md), and
  [`is_nan()`](reference/predicates-infinite.md)/[`is_inf()`](reference/predicates-infinite.md),
  e.g. solving `is.na(NaN) #> TRUE`.
- Expanding the test for ‘any vector type’ to ‘any collection type’ with
  [`is_collection()`](reference/predicates-collections.md), possibly
  including environments, pairlists, expression vectors, and NULL.
- [`is_integer_like()`](reference/is_integer_like.md), that organizes
  the common test for ‘integer-ish’ into two modes: `"unbounded"` -
  difference from `round(x)` within a given tolerance; and `"bounded"` -
  unbounded + within the R integer range. Correctly dealing with `NaN`
  and `Inf` values, while allowing control over `NA` values.
- Testing for names with
  `has`/[`are_names_valid()`](reference/has_names_valid.md), having more
  control over empty, NA, duplicate and invalid names.
- A more organized notion of ‘object’, merging S4/object bits, S4/object
  typeof’s and class attribute in
  [`is_object_like()`](reference/predicates-objects.md) and
  [`object_system()`](reference/object_system.md).
- The compare functions cited in the previous section.

The `test_*()` and `assert_*()` suite introduces a ‘menu’ of sub-tests
shared across functions, with a focus on flexibility, and a modern
reporting of errors. Below is an example for validating an integer-like
object.

[`library`](https://rdrr.io/r/base/library.html)`(``predicater``)`` `` ``# Object to be validated:`` ``x`` ``<-`` `[`c`](https://rdrr.io/r/base/c.html)`(``1.0``, ``2.0``, ``3.0`` ``+`` ``1e-100``, ``4.0``, ``Inf``)`` `` ``# Defining the sub tests:`` ``args`` ``<-`` `[`list`](https://rdrr.io/r/base/list.html)`(`` `` mode ``=`` ``"unbounded"``, ``# Equal to round(x), within a tolerance (will pass)`` `` mode_tol ``=`` `[`sqrt`](https://rdrr.io/r/base/MathFun.html)`(``.Machine``$``double.eps``)``,`` `` len ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``1``, ``10``)``, ``# Length must be between 1 and 10 (will pass)`` `` n_dup ``=`` ``0``, ``# No duplicate values allowed (will pass)`` `` n_nan ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``0``, ``-``2``)``, ``# At most length(x) - 2 NaN values (will pass)`` `` n_na ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``0``, ``2``, ``3``)``, ``# 0, 2, or 3 NA values (will pass)`` `` n_inf ``=`` \``(``n``, ``l``)`` ``n``/``l`` ``<=`` ``0.5``, ``# n of Inf <= 50% of total (will pass)`` `` range ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``-``5``, ``+``5``)``, ``# Values between -5 and 5 (will fail)`` `` set ``=`` `[`list`](https://rdrr.io/r/base/list.html)`(``yes ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``1``)``, no ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``0``)``)``, ``# Must contain 1, and not 0 (will pass)`` `` sentinels ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``"null"``)``, ``# If not a numeric vector, x can be a NULL sentinel`` `` sorted ``=`` ``"desc"``, ``# Must be sorted in descending order (will fail)`` `` custom ``=`` ``NULL`` ``# Any user-given custom function`` ``)`` `` ``rlang``::`[`exec`](https://rlang.r-lib.org/reference/exec.html)`(``test_integer``, ``x``, ``!``!``!``args``)`` ``#> FALSE (not all tests passed)`

Normally one would call `test_integer(x, ...)`, but I defined the
arguments first for visualization purposes.

Note that all sub-tests about ‘the number/size of something’ (len, n_na,
etc.) can have different specifications (a single value, a range, a set
of values, or a custom function). They appear in many other `test_*()`
functions, as well as `set`, `sentinels`, `custom`, etc.

For the validation, often one will call `assert_integer(x, ...)` to
validate user input to his function. Note that `assert_*()` functions
allow control over the conditions’ environment, argument name, and
others.

`my_fun`` ``<-`` ``function``(``x``)`` ``{`` `` ``rlang``::`[`exec`](https://rlang.r-lib.org/reference/exec.html)`(`` `` ``assert_integer``, ``x``, ``!``!``!``args``,`` `` env ``=`` ``rlang``::`[`current_env`](https://rlang.r-lib.org/reference/stack.html)`(``)``, ``` # Shows the error coming from `my_fun()` ``` `` short_circuit ``=`` ``FALSE``, ``# Reports all sub-tests, beyond the first fail`` `` args_cnd ``=`` `[`list`](https://rdrr.io/r/base/list.html)`(``class ``=`` ``"my_fun_error"``)`` `` ``)`` `` `` ``# ... code depending on x's integer properties`` ``}`` `` `[`try`](https://rdrr.io/r/base/try.html)`(``my_fun``(``x``)``)`

``` R
## Error in my_fun(x) : `x` failed `assert_integer()`:
## ✔ (pass) sentinels: no sentinel values allowed.
## ✔ (pass) type  : must pass `predicater::is_integer_like()`() in "unbounded"
##   mode.
## ✔ (pass) len   : length must be in range 1 to 10.
## ✔ (pass) n_na  : #of NA values must be in set 0, 2, and 3.
## ✔ (pass) n_dup : #of duplicate values must be 0.
## ✔ (pass) n_nan : #of NaN values must be in range 0 to -2.
## ✔ (pass) n_inf : #of Inf values must satisfy a custom function.
## ✖ (fail) range : must be in range -5 to 5. Found Inf.
## ✖ (fail) set   : must be in a custom set. Was not.
## ✖ (fail) sorted: must be in descending order. Did not.
## 
## ℹ See `predicater::assert_integer()` and this condition's `rs_assert_error`
##   attribute for details.
```

The error describes each sub-test and the reason (if possible) for the
failure. Tests not defined (e.g. `custom = NULL`) are not reported.

The `assert_*()` functions return `x` on success, so they can be used in
pipelines:

`mtcars``$``mpg`` ``|>`` ``# Some external data`` `` `[`tan`](https://rdrr.io/r/base/Trig.html)`(``)`` ``|>`` ``# Some transformation`` `` `[`assert_double`](reference/tests-numeric.md)`(`` `` range ``=`` `[`c`](https://rdrr.io/r/base/c.html)`(``-``10``, ``10``)``, sorted ``=`` ``"asc"``,`` `` x_name ``=`` ``"tan(mpg)"`` `` ``)`` ``|>`` ``# Validation`` `` `[`cos`](https://rdrr.io/r/base/Trig.html)`(``)`` ``|>`` ``# If passes, continue the pipeline`` `` `[`try`](https://rdrr.io/r/base/try.html)`(``)`

``` R
## Error in (function (...)  : `tan(mpg)` failed `assert_double()`:
## ✔ (pass) sentinels: no sentinel values allowed.
## ✖ (fail) range : must be in range -10 to 10. Found -47.0730006551673.
## • (skip) sorted: skiped given failure.
## ✔ (pass) type  : must pass `predicater::is_double()`.
## 
## ℹ See `predicater::assert_double()` and this condition's `rs_assert_error`
##   attribute for details.
```

Note that with `short_circuit = TRUE` (the default), the first failing
sub-test will raise an error, and the rest will be left as ‘(skip)’.

## Installation

You can install the development version of predicater from
[GitHub](https://github.com/predicater) with any of the following
commands:

`# install.packages(c("pak", "renv", "remotes"))`` ``pak``::`[`pak`](https://pak.r-lib.org/reference/pak.html)`(``"ricardo-semiao/predicater"``)`` ``renv``::`[`install`](https://rstudio.github.io/renv/reference/install.html)`(``"ricardo-semiao/predicater"``)`` ``remotes``::`[`install_github`](https://remotes.r-lib.org/reference/install_github.html)`(``"ricardo-semiao/predicater"``)`

## Development status

Currently, predicater is in an **experimental** stage. The API is not
stable yet and will go through breaking changes.

All functions have examples, and they are validated in the test suite.
Still, the tests are not extensive and the functions have not been
battle-tested yet.

Currently, the functions do not verify their inputs, although they are
well documented in the help pages.

In the future, I plan to substitute the underlying engines of many
functions with C code to improve performance and have cleaner access to
the underlying C representation of the R objects.

Some future additions are planned: - `is_*_scalar()` for all types of
objects, that also allow for excluding the `NA` value. - Predicates for
all items in the C data header of R objects, as is the case of
[`has_object_bit()`](reference/predicates-objects.md). - A reporting
framework that allows the user to store the results of `test_*()`
functions and branch from and report them in a more flexible way than
directly raising an error.
