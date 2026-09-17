# Validation - Numeric vectors

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if an object is a numeric vector:

- `test_integer(x, mode = "strict")` tests for integer vectors.

- `test_integer(x, mode = *)` tests for integer-like vectors via
  [`is_integer_like()`](is_integer_like.md), with "bounded" or
  "unbounded" mode.

- `test_double(x, mode = "double")` tests for double vectors.

- `test_double(x, mode = "numeric")` tests for double or integer
  vectors.

- `test_complex()` tests for complex vectors, delegating tests on its
  real, imaginary, modulus, and argument parts, to `test_double()`.

They all are predicate tests, while the `assert_*()` functions validate
their input, aborting if it fails the test.

## Usage

``` r
test_integer(
  x,
  mode = "strict",
  len = NULL,
  n_na = NULL,
  n_dup = NULL,
  n_nan = NULL,
  n_inf = NULL,
  range = NULL,
  set = NULL,
  sorted = NULL,
  custom = NULL,
  sentinels = NULL,
  mode_tol = 0
)

test_double(
  x,
  mode = "double",
  len = NULL,
  n_na = NULL,
  n_dup = NULL,
  n_nan = NULL,
  n_inf = NULL,
  range = NULL,
  set = NULL,
  sorted = NULL,
  sentinels = NULL,
  custom = NULL
)

test_complex(
  x,
  tests_re = NULL,
  tests_im = NULL,
  tests_mod = NULL,
  tests_arg = NULL,
  sentinels = NULL,
  custom = NULL
)

assert_integer(
  x,
  mode = "strict",
  len = NULL,
  n_na = NULL,
  n_dup = NULL,
  n_nan = NULL,
  n_inf = NULL,
  range = NULL,
  set = NULL,
  sorted = NULL,
  custom = NULL,
  sentinels = NULL,
  mode_tol = 0,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_double(
  x,
  mode = "double",
  len = NULL,
  n_na = NULL,
  n_dup = NULL,
  n_nan = NULL,
  n_inf = NULL,
  range = NULL,
  set = NULL,
  sorted = NULL,
  sentinels = NULL,
  custom = NULL,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_complex(
  x,
  tests_re = NULL,
  tests_im = NULL,
  tests_mod = NULL,
  tests_arg = NULL,
  sentinels = NULL,
  custom = NULL,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)
```

## Arguments

- x:

  \[`any`\] An object to test.

- mode:

  - \[`"strict"` \| `"bounded"` \| `"unbounded"`\] For `*_integer()`:
    the `mode` argument to pass to
    [`is_integer_like()`](is_integer_like.md).

  - \[`"double"` \| `"numeric"`\] For `*_double()`: `"double"` to accept
    only [`double()`](https://rdrr.io/r/base/double.html) vectors, or
    `"numeric"` to accept both
    [`double()`](https://rdrr.io/r/base/double.html) and
    [`integer()`](https://rdrr.io/r/base/integer.html) vectors.

- len, n_na, n_dup, n_nan, n_inf:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `\(){}` \|
  `NULL`\] Possible values for the length, number of `NA` elements,
  number of duplicate elements, number of `NaN` elements, number of
  `Inf` elements. The options of each argument 'arg' are:

  - `NULL` to not test.

  - A single non-negative number to test for `. == arg`. If `Inf`,
    `. == length(x)`.

  - A single negative number to test for `. == length(x) + arg`.

  - A vector of two non-negative numbers to test for
    `arg[1] <= . <= arg[2]` (`Inf` is allowed).

  - A vector of three or more non-negative numbers to test for
    `. %in% arg`.

  - A function that receives the value to test and the length of `x`,
    and returns a single `TRUE` or `FALSE`.

- range:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `NULL`\] A
  vector with the upper and lower bound for `x` values. Or a vector with
  three or more values to test for `all(x %in% range)`. Set to `NULL` to
  not test.

- set:

  \[[`integer()`](https://rdrr.io/r/base/integer.html) \|
  `list(yes = , no = , mode = )` \| `NULL`\] Test if all values of `x`
  are in a set of allowed values. Use a list with `yes` and/or `no`
  elements to defined allowed and disallowed values, with `mode`s
  `"all"` (all `x` in `yes`, the default), `"only"` (all and only `x` in
  `yes`), or `"any"` (any `x` in `yes`). Set to `NULL` to not test.

- sorted:

  \[`"asc"` \| `"desc"` \| `NULL`\] Test if `x` is sorted in ascending
  (`"asc"`) or descending (`"desc"`) order. Set to `NULL` to not test.
  Pair with `n_dup` to test for strictly sorted values.

- custom:

  \[`function(x)` \| `NULL`\] A custom function that takes `x` as first
  argument and returns a single `TRUE` or `FALSE`. Set to `NULL` to not
  test.

- sentinels:

  \[[`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\]
  Each entry in this character vector allows `x` to also be some scalar
  sentinel below. Set to `NULL` to disconsider sentinels.

  - `"null"` for `NULL`.

  - `"empty"` for any zero-length object.

  - `"na"` for any `NA` type, or `"na_logical"` for `NA`, `"na_integer"`
    for `NA_integer_`, `"na_real"` for `NA_real_`, `"na_complex"` for
    `NA_complex_`, and `"na_character"` for `NA_character_`.

  - `"nan"` for `NaN`.

  - `"+inf"` for `+Inf`, `"-inf"` for `-Inf`, and `"inf"` for both.

  - `"true"`/`"t"` for `TRUE`, and `"false"`/`"f"` for `FALSE`.

- mode_tol:

  \[`double(1)`\] The `tol` argument to pass to
  [`is_integer_like()`](is_integer_like.md).

- tests_re, tests_im, tests_mod, tests_arg:

  \[[`list()`](https://rdrr.io/r/base/list.html) \| `NULL`\] For
  `*_complex()`: a list with the same named arguments as
  `test_double()`, to test the real, imaginary, modulus and argument
  values of `x`.

- action:

  \[`"abort"` \| `"warn"` \| `"inform"`\] Action to take when the test
  fails:

  - `"abort"` to stop execution and throw an error.

  - `"warning"` to issue a warning and return `invisible(x)`.

  - `"message"` to issue a message and return `invisible(x)`.

- env:

  \[[`environment()`](https://rdrr.io/r/base/environment.html) \|
  [`call()`](https://rdrr.io/r/base/call.html) \| `NULL` \|
  `missing_arg()`\] The call to inform as the origin of the error,
  passed to
  [`rlang::abort()`](https://rlang.r-lib.org/reference/abort.html):

  - An environment in the call stack or a hard-coded defused call.

  - `NULL` for no information.

  - `missing_arg()` to use the assert function itself.

  - The default is `caller_env()`, to display the function where the
    assertion was called.

- x_name:

  \[`character(1)` \| `NULL`\] The name of the object to use in the
  error message. If `NULL`, the name is inferred from the expression
  passed to `x`.

- short_circuit:

  \[`TRUE` \| `FALSE`\] If `TRUE`, the tests results will be reported up
  to the first failure. Else, all tests results are reported. The former
  is more efficient, while the latter is more informative.

- report_untested:

  \[`TRUE` \| `FALSE`\] If `TRUE`, the tests that were not run due to
  short- circuiting will be reported as untested, else, ignored.

- args_cnd:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] Additional arguments
  passed to
  [`cli::cli_abort()`](https://cli.r-lib.org/reference/cli_abort.html),
  [`cli::cli_warn()`](https://cli.r-lib.org/reference/cli_abort.html),
  or
  [`cli::cli_inform()`](https://cli.r-lib.org/reference/cli_abort.html),
  based on the chosen `action`.

## Value

- \[`TRUE` \| `FALSE`\] for `test_*()`.

- \[`=x`\] `invisible(x)` for `assert_*()`, or aborts if the test fails.

## Examples

``` r
# Example 1: Integer-like vector with a floating-point tolerance error
x <- c(1.0, 2.0, 3.0 + 1e-100, 4.0, Inf)

args <- list(
  mode = "unbounded",  # Allow double-precision whole numbers and Inf (will fail on 3.00001)
  mode_tol = sqrt(.Machine$double.eps),
  # Standard tolerance for decimal check
  len = c(1, 10),          # Length must be between 1 and 10 (will pass)
  n_na = 0,                # No NA values allowed (will pass)
  n_dup = 0,               # No duplicate values allowed (will pass)
  n_nan = 0,               # No NaN values allowed (will pass)
  n_inf = 0,               # At most 1 Inf value allowed (will pass)
  range = c(0, 10 ),       # Bounds between 0 and Inf (will fail)
  set = list(no = c(0)),   # Values must not contain 0 (will pass)
  sentinels = c("null"),   # Allow NULL x (not the case of x)
  sorted = "desc",         # Must be sorted in decreasing order (will pass)
  custom = NULL            # No custom predicate
)

do.call(test_integer, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_integer, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_integer()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must pass `predicater::is_integer_like()`() in "unbounded"
#>   mode.
#> ✔ (pass) len   : length must be in range 1 to 10.
#> ✔ (pass) n_na  : #of NA values must be 0.
#> ✔ (pass) n_dup : #of duplicate values must be 0.
#> ✔ (pass) n_nan : #of NaN values must be 0.
#> ✖ (fail) n_inf : #of Inf values must be 0. Was 1.
#> ✖ (fail) range : must be in range 0 to 10. Found Inf.
#> ✔ (pass) set   : must be in a custom set.
#> ✖ (fail) sorted: must be in descending order. Did not.
#> 
#> ℹ See `predicater::assert_integer()` and this condition's `rs_assert_error`
#>   attribute for details.


# Example 2: Testing an integer vector under "numeric" mode
x <- c(1L, 2L, 5L, 10L)

args <- list(
  mode = "numeric",                 # Accepts both double and integer vectors (will pass)
  len = c(1, 10),                   # Length must be between 1 and 10 (will pass)
  n_na = 0,                         # No NA values allowed (will pass)
  n_dup = 0,                        # No duplicate values allowed (will pass)
  n_nan = 0,                        # No NaN values allowed (will pass)
  n_inf = 0,                        # No Inf values allowed (will pass)
  range = c(1, 100),                # Values between 1 and 100 (will pass)
  set = list(yes = c(1L, 2L, 3L)),  # Elements must belong to specified set (will fail)
  sentinels = c("null"),            # Allow NULL x (not the case of x)
  sorted = "asc",                   # Must be sorted in ascending order (will pass)
  custom = NULL                     # No custom predicate
)

do.call(test_double, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_double, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_double()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must pass `predicater::is_numeric()`.
#> ✔ (pass) len   : length must be in range 1 to 10.
#> ✔ (pass) n_na  : #of NA values must be 0.
#> ✔ (pass) n_dup : #of duplicate values must be 0.
#> ✔ (pass) n_nan : #of NaN values must be 0.
#> ✔ (pass) n_inf : #of Inf values must be 0.
#> ✔ (pass) range : must be in range 1 to 100.
#> ✖ (fail) set   : must be in a custom set. Was not.
#> ✔ (pass) sorted: must be in ascending order.
#> 
#> ℹ See `predicater::assert_double()` and this condition's `rs_assert_error`
#>   attribute for details.
```

## On this page

Test if an object is a numeric vector:

- `test_integer(x, mode = "strict")` tests for integer vectors.

- `test_integer(x, mode = *)` tests for integer-like vectors via
  [`is_integer_like()`](is_integer_like.md), with "bounded" or
  "unbounded" mode.

- `test_double(x, mode = "double")` tests for double vectors.

- `test_double(x, mode = "numeric")` tests for double or integer
  vectors.

- `test_complex()` tests for complex vectors, delegating tests on its
  real, imaginary, modulus, and argument parts, to `test_double()`.

They all are predicate tests, while the `assert_*()` functions validate
their input, aborting if it fails the test.

## Usage

``` r
test_integer(
  x,
  mode = "strict",
  len = NULL,
  n_na = NULL,
  n_dup = NULL,
  n_nan = NULL,
  n_inf = NULL,
  range = NULL,
  set = NULL,
  sorted = NULL,
  custom = NULL,
  sentinels = NULL,
  mode_tol = 0
)

test_double(
  x,
  mode = "double",
  len = NULL,
  n_na = NULL,
  n_dup = NULL,
  n_nan = NULL,
  n_inf = NULL,
  range = NULL,
  set = NULL,
  sorted = NULL,
  sentinels = NULL,
  custom = NULL
)

test_complex(
  x,
  tests_re = NULL,
  tests_im = NULL,
  tests_mod = NULL,
  tests_arg = NULL,
  sentinels = NULL,
  custom = NULL
)

assert_integer(
  x,
  mode = "strict",
  len = NULL,
  n_na = NULL,
  n_dup = NULL,
  n_nan = NULL,
  n_inf = NULL,
  range = NULL,
  set = NULL,
  sorted = NULL,
  custom = NULL,
  sentinels = NULL,
  mode_tol = 0,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_double(
  x,
  mode = "double",
  len = NULL,
  n_na = NULL,
  n_dup = NULL,
  n_nan = NULL,
  n_inf = NULL,
  range = NULL,
  set = NULL,
  sorted = NULL,
  sentinels = NULL,
  custom = NULL,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_complex(
  x,
  tests_re = NULL,
  tests_im = NULL,
  tests_mod = NULL,
  tests_arg = NULL,
  sentinels = NULL,
  custom = NULL,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)
```

## Arguments

- x:

  \[`any`\] An object to test.

- mode:

  - \[`"strict"` \| `"bounded"` \| `"unbounded"`\] For `*_integer()`:
    the `mode` argument to pass to
    [`is_integer_like()`](is_integer_like.md).

  - \[`"double"` \| `"numeric"`\] For `*_double()`: `"double"` to accept
    only [`double()`](https://rdrr.io/r/base/double.html) vectors, or
    `"numeric"` to accept both
    [`double()`](https://rdrr.io/r/base/double.html) and
    [`integer()`](https://rdrr.io/r/base/integer.html) vectors.

- len, n_na, n_dup, n_nan, n_inf:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `\(){}` \|
  `NULL`\] Possible values for the length, number of `NA` elements,
  number of duplicate elements, number of `NaN` elements, number of
  `Inf` elements. The options of each argument 'arg' are:

  - `NULL` to not test.

  - A single non-negative number to test for `. == arg`. If `Inf`,
    `. == length(x)`.

  - A single negative number to test for `. == length(x) + arg`.

  - A vector of two non-negative numbers to test for
    `arg[1] <= . <= arg[2]` (`Inf` is allowed).

  - A vector of three or more non-negative numbers to test for
    `. %in% arg`.

  - A function that receives the value to test and the length of `x`,
    and returns a single `TRUE` or `FALSE`.

- range:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `NULL`\] A
  vector with the upper and lower bound for `x` values. Or a vector with
  three or more values to test for `all(x %in% range)`. Set to `NULL` to
  not test.

- set:

  \[[`integer()`](https://rdrr.io/r/base/integer.html) \|
  `list(yes = , no = , mode = )` \| `NULL`\] Test if all values of `x`
  are in a set of allowed values. Use a list with `yes` and/or `no`
  elements to defined allowed and disallowed values, with `mode`s
  `"all"` (all `x` in `yes`, the default), `"only"` (all and only `x` in
  `yes`), or `"any"` (any `x` in `yes`). Set to `NULL` to not test.

- sorted:

  \[`"asc"` \| `"desc"` \| `NULL`\] Test if `x` is sorted in ascending
  (`"asc"`) or descending (`"desc"`) order. Set to `NULL` to not test.
  Pair with `n_dup` to test for strictly sorted values.

- custom:

  \[`function(x)` \| `NULL`\] A custom function that takes `x` as first
  argument and returns a single `TRUE` or `FALSE`. Set to `NULL` to not
  test.

- sentinels:

  \[[`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\]
  Each entry in this character vector allows `x` to also be some scalar
  sentinel below. Set to `NULL` to disconsider sentinels.

  - `"null"` for `NULL`.

  - `"empty"` for any zero-length object.

  - `"na"` for any `NA` type, or `"na_logical"` for `NA`, `"na_integer"`
    for `NA_integer_`, `"na_real"` for `NA_real_`, `"na_complex"` for
    `NA_complex_`, and `"na_character"` for `NA_character_`.

  - `"nan"` for `NaN`.

  - `"+inf"` for `+Inf`, `"-inf"` for `-Inf`, and `"inf"` for both.

  - `"true"`/`"t"` for `TRUE`, and `"false"`/`"f"` for `FALSE`.

- mode_tol:

  \[`double(1)`\] The `tol` argument to pass to
  [`is_integer_like()`](is_integer_like.md).

- tests_re, tests_im, tests_mod, tests_arg:

  \[[`list()`](https://rdrr.io/r/base/list.html) \| `NULL`\] For
  `*_complex()`: a list with the same named arguments as
  `test_double()`, to test the real, imaginary, modulus and argument
  values of `x`.

- action:

  \[`"abort"` \| `"warn"` \| `"inform"`\] Action to take when the test
  fails:

  - `"abort"` to stop execution and throw an error.

  - `"warning"` to issue a warning and return `invisible(x)`.

  - `"message"` to issue a message and return `invisible(x)`.

- env:

  \[[`environment()`](https://rdrr.io/r/base/environment.html) \|
  [`call()`](https://rdrr.io/r/base/call.html) \| `NULL` \|
  `missing_arg()`\] The call to inform as the origin of the error,
  passed to
  [`rlang::abort()`](https://rlang.r-lib.org/reference/abort.html):

  - An environment in the call stack or a hard-coded defused call.

  - `NULL` for no information.

  - `missing_arg()` to use the assert function itself.

  - The default is `caller_env()`, to display the function where the
    assertion was called.

- x_name:

  \[`character(1)` \| `NULL`\] The name of the object to use in the
  error message. If `NULL`, the name is inferred from the expression
  passed to `x`.

- short_circuit:

  \[`TRUE` \| `FALSE`\] If `TRUE`, the tests results will be reported up
  to the first failure. Else, all tests results are reported. The former
  is more efficient, while the latter is more informative.

- report_untested:

  \[`TRUE` \| `FALSE`\] If `TRUE`, the tests that were not run due to
  short- circuiting will be reported as untested, else, ignored.

- args_cnd:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] Additional arguments
  passed to
  [`cli::cli_abort()`](https://cli.r-lib.org/reference/cli_abort.html),
  [`cli::cli_warn()`](https://cli.r-lib.org/reference/cli_abort.html),
  or
  [`cli::cli_inform()`](https://cli.r-lib.org/reference/cli_abort.html),
  based on the chosen `action`.

## Value

- \[`TRUE` \| `FALSE`\] for `test_*()`.

- \[`=x`\] `invisible(x)` for `assert_*()`, or aborts if the test fails.

## Examples

``` r
# Example 1: Integer-like vector with a floating-point tolerance error
x <- c(1.0, 2.0, 3.0 + 1e-100, 4.0, Inf)

args <- list(
  mode = "unbounded",  # Allow double-precision whole numbers and Inf (will fail on 3.00001)
  mode_tol = sqrt(.Machine$double.eps),
  # Standard tolerance for decimal check
  len = c(1, 10),          # Length must be between 1 and 10 (will pass)
  n_na = 0,                # No NA values allowed (will pass)
  n_dup = 0,               # No duplicate values allowed (will pass)
  n_nan = 0,               # No NaN values allowed (will pass)
  n_inf = 0,               # At most 1 Inf value allowed (will pass)
  range = c(0, 10 ),       # Bounds between 0 and Inf (will fail)
  set = list(no = c(0)),   # Values must not contain 0 (will pass)
  sentinels = c("null"),   # Allow NULL x (not the case of x)
  sorted = "desc",         # Must be sorted in decreasing order (will pass)
  custom = NULL            # No custom predicate
)

do.call(test_integer, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_integer, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_integer()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must pass `predicater::is_integer_like()`() in "unbounded"
#>   mode.
#> ✔ (pass) len   : length must be in range 1 to 10.
#> ✔ (pass) n_na  : #of NA values must be 0.
#> ✔ (pass) n_dup : #of duplicate values must be 0.
#> ✔ (pass) n_nan : #of NaN values must be 0.
#> ✖ (fail) n_inf : #of Inf values must be 0. Was 1.
#> ✖ (fail) range : must be in range 0 to 10. Found Inf.
#> ✔ (pass) set   : must be in a custom set.
#> ✖ (fail) sorted: must be in descending order. Did not.
#> 
#> ℹ See `predicater::assert_integer()` and this condition's `rs_assert_error`
#>   attribute for details.


# Example 2: Testing an integer vector under "numeric" mode
x <- c(1L, 2L, 5L, 10L)

args <- list(
  mode = "numeric",                 # Accepts both double and integer vectors (will pass)
  len = c(1, 10),                   # Length must be between 1 and 10 (will pass)
  n_na = 0,                         # No NA values allowed (will pass)
  n_dup = 0,                        # No duplicate values allowed (will pass)
  n_nan = 0,                        # No NaN values allowed (will pass)
  n_inf = 0,                        # No Inf values allowed (will pass)
  range = c(1, 100),                # Values between 1 and 100 (will pass)
  set = list(yes = c(1L, 2L, 3L)),  # Elements must belong to specified set (will fail)
  sentinels = c("null"),            # Allow NULL x (not the case of x)
  sorted = "asc",                   # Must be sorted in ascending order (will pass)
  custom = NULL                     # No custom predicate
)

do.call(test_double, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_double, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_double()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must pass `predicater::is_numeric()`.
#> ✔ (pass) len   : length must be in range 1 to 10.
#> ✔ (pass) n_na  : #of NA values must be 0.
#> ✔ (pass) n_dup : #of duplicate values must be 0.
#> ✔ (pass) n_nan : #of NaN values must be 0.
#> ✔ (pass) n_inf : #of Inf values must be 0.
#> ✔ (pass) range : must be in range 1 to 100.
#> ✖ (fail) set   : must be in a custom set. Was not.
#> ✔ (pass) sorted: must be in ascending order.
#> 
#> ℹ See `predicater::assert_double()` and this condition's `rs_assert_error`
#>   attribute for details.
```
