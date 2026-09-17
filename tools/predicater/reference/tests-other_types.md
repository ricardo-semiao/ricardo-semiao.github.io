# Validation - Other types

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if an object is of various special base R types, including
promises, dots (`...`), weak references, bytecode, or external pointers.

## Usage

``` r
test_promise(x, sentinels = NULL, custom = NULL)

test_dots(x, len = NULL, sentinels = NULL, custom = NULL)

test_weakref(x, sentinels = NULL, custom = NULL)

test_bytecode(x, sentinels = NULL, custom = NULL)

test_externalptr(x, sentinels = NULL, custom = NULL)

assert_null(
  x,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_promise(
  x,
  sentinels = NULL,
  custom = NULL,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_dots(
  x,
  len = NULL,
  sentinels = NULL,
  custom = NULL,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_weakref(
  x,
  sentinels = NULL,
  custom = NULL,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_bytecode(
  x,
  sentinels = NULL,
  custom = NULL,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_externalptr(
  x,
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

- len:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `\(){}` \|
  `NULL`\] Possible values for the length. The options of each argument
  'arg' are:

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
try(assert_null(integer(0))) #> Error
#> Error in eval(expr, envir) : `integer(0)` failed `assert_null()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✖ (fail) type  : must be "NULL". Had type "integer".
#> 
#> ℹ See `predicater::assert_null()` and this condition's `rs_assert_error`
#>   attribute for details.
```

## On this page

Test if an object is of various special base R types, including
promises, dots (`...`), weak references, bytecode, or external pointers.

## Usage

``` r
test_promise(x, sentinels = NULL, custom = NULL)

test_dots(x, len = NULL, sentinels = NULL, custom = NULL)

test_weakref(x, sentinels = NULL, custom = NULL)

test_bytecode(x, sentinels = NULL, custom = NULL)

test_externalptr(x, sentinels = NULL, custom = NULL)

assert_null(
  x,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_promise(
  x,
  sentinels = NULL,
  custom = NULL,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_dots(
  x,
  len = NULL,
  sentinels = NULL,
  custom = NULL,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_weakref(
  x,
  sentinels = NULL,
  custom = NULL,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_bytecode(
  x,
  sentinels = NULL,
  custom = NULL,
  action = "abort",
  env = caller_env(),
  x_name = NULL,
  short_circuit = TRUE,
  report_untested = TRUE,
  args_cnd = list()
)

assert_externalptr(
  x,
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

- len:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `\(){}` \|
  `NULL`\] Possible values for the length. The options of each argument
  'arg' are:

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
try(assert_null(integer(0))) #> Error
#> Error in eval(expr, envir) : `integer(0)` failed `assert_null()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✖ (fail) type  : must be "NULL". Had type "integer".
#> 
#> ℹ See `predicater::assert_null()` and this condition's `rs_assert_error`
#>   attribute for details.
```
