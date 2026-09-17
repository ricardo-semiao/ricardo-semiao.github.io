# Validation - General vectors

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if an input is a vector of a given mode (atomic, list, expression,
or pairlist) and optionally validate length, missing values, duplicate
counts, set inclusion, and ordering constraints.

`test_vector()` is the predicate test, while `assert_vector()` validates
its input, aborting if it fails the test.

## Usage

``` r
test_vector(
  x,
  mode = "atomic",
  len = NULL,
  n_na = NULL,
  n_null = NULL,
  n_empty = NULL,
  n_dup = NULL,
  sentinels = NULL,
  custom = NULL,
  custom_map = NULL
)

assert_vector(
  x,
  mode = "atomic",
  len = NULL,
  n_na = NULL,
  n_null = NULL,
  n_empty = NULL,
  n_dup = NULL,
  sentinels = NULL,
  custom = NULL,
  custom_map = NULL,
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

  \[`"atomic"` \| `"list"` \| `"expression"` \| `"pairlist"`\] Allowed
  vector types. They are additive: `"atomic"` allows atomic vectors,
  `list` allows atomic and lists, `expression` allows atomic, lists, and
  expression objects, and `pairlist` allows all.

- len, n_na, n_null, n_empty, n_dup:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `\(){}` \|
  `NULL`\] Possible values for the length, number of `NA` elements,
  number of `NULL` elements, number of elements with zero length, number
  of duplicate elements. The options of each argument 'arg' are:

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

- custom:

  \[`function(x)` \| `NULL`\] A custom function that takes `x` as first
  argument and returns a single `TRUE` or `FALSE`. Set to `NULL` to not
  test.

- custom_map:

  \[`function(x)` \| `NULL`\] A custom function that is applied to each
  element of `x`. Must return a single `TRUE` or `FALSE` for each
  element. Set to `NULL` to not test.

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

- \[`TRUE` \| `FALSE`\] for `test_vector()`.

- \[`=x`\] `invisible(x)` for `assert_vector()`, or aborts if the test
  fails.

## Examples

``` r
x <- list(1, 2, NA, 2, NULL)

args <- list(
  mode = "list",          # Allow atomic vectors and lists (will pass)
  len = c(1, 10),         # Length must be between 1 and 10 (will pass)
  n_na = 0,               # No NA values allowed (will fail)
  n_null = c(0, 1),       # At most 1 NULL element allowed (will pass)
  n_empty = 0,            # No empty elements allowed (will pass)
  n_dup = 0,              # No duplicate elements allowed (will fail)
  sentinels = c("null"),  # Allow NULL x (not the case of x)
  custom = NULL,          # Not tested
  custom_map = \(elt) length(elt) <= 1
  # All list elements must have length <= 1 (will pass)
)

do.call(test_vector, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_vector, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_vector()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must be of 'type' "list".
#> ✔ (pass) len   : length must be in range 1 to 10.
#> ✔ (pass) n_na  : #of NA values must be 0.
#> ✔ (pass) n_null: #of NULL values must be in range 0 to 1.
#> ✖ (fail) n_empty: #of empty values must be 0. Was 1.
#> ✖ (fail) n_dup : #of duplicate values must be 0. Was 1.
#> ✔ (pass) custom_map: all elements must pass a custom test.
#> 
#> ℹ See `predicater::assert_vector()` and this condition's `rs_assert_error`
#>   attribute for details.
```

## On this page

Test if an input is a vector of a given mode (atomic, list, expression,
or pairlist) and optionally validate length, missing values, duplicate
counts, set inclusion, and ordering constraints.

`test_vector()` is the predicate test, while `assert_vector()` validates
its input, aborting if it fails the test.

## Usage

``` r
test_vector(
  x,
  mode = "atomic",
  len = NULL,
  n_na = NULL,
  n_null = NULL,
  n_empty = NULL,
  n_dup = NULL,
  sentinels = NULL,
  custom = NULL,
  custom_map = NULL
)

assert_vector(
  x,
  mode = "atomic",
  len = NULL,
  n_na = NULL,
  n_null = NULL,
  n_empty = NULL,
  n_dup = NULL,
  sentinels = NULL,
  custom = NULL,
  custom_map = NULL,
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

  \[`"atomic"` \| `"list"` \| `"expression"` \| `"pairlist"`\] Allowed
  vector types. They are additive: `"atomic"` allows atomic vectors,
  `list` allows atomic and lists, `expression` allows atomic, lists, and
  expression objects, and `pairlist` allows all.

- len, n_na, n_null, n_empty, n_dup:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `\(){}` \|
  `NULL`\] Possible values for the length, number of `NA` elements,
  number of `NULL` elements, number of elements with zero length, number
  of duplicate elements. The options of each argument 'arg' are:

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

- custom:

  \[`function(x)` \| `NULL`\] A custom function that takes `x` as first
  argument and returns a single `TRUE` or `FALSE`. Set to `NULL` to not
  test.

- custom_map:

  \[`function(x)` \| `NULL`\] A custom function that is applied to each
  element of `x`. Must return a single `TRUE` or `FALSE` for each
  element. Set to `NULL` to not test.

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

- \[`TRUE` \| `FALSE`\] for `test_vector()`.

- \[`=x`\] `invisible(x)` for `assert_vector()`, or aborts if the test
  fails.

## Examples

``` r
x <- list(1, 2, NA, 2, NULL)

args <- list(
  mode = "list",          # Allow atomic vectors and lists (will pass)
  len = c(1, 10),         # Length must be between 1 and 10 (will pass)
  n_na = 0,               # No NA values allowed (will fail)
  n_null = c(0, 1),       # At most 1 NULL element allowed (will pass)
  n_empty = 0,            # No empty elements allowed (will pass)
  n_dup = 0,              # No duplicate elements allowed (will fail)
  sentinels = c("null"),  # Allow NULL x (not the case of x)
  custom = NULL,          # Not tested
  custom_map = \(elt) length(elt) <= 1
  # All list elements must have length <= 1 (will pass)
)

do.call(test_vector, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_vector, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_vector()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must be of 'type' "list".
#> ✔ (pass) len   : length must be in range 1 to 10.
#> ✔ (pass) n_na  : #of NA values must be 0.
#> ✔ (pass) n_null: #of NULL values must be in range 0 to 1.
#> ✖ (fail) n_empty: #of empty values must be 0. Was 1.
#> ✖ (fail) n_dup : #of duplicate values must be 0. Was 1.
#> ✔ (pass) custom_map: all elements must pass a custom test.
#> 
#> ℹ See `predicater::assert_vector()` and this condition's `rs_assert_error`
#>   attribute for details.
```
