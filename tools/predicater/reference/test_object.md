# Validation - Object-related attributes

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if an input is an 'object' (see
[predicates-objects](predicates-objects.md)), and fits a specific
Object-Oriented (OO) system (see [`object_system()`](object_system.md)).

`test_object()` is the predicate test, while `assert_object()` validates
its input, aborting if it fails the test.

## Usage

``` r
test_object(
  x,
  oo_system = NULL,
  s4_bit = NULL,
  tests_class = NULL,
  sentinels = NULL,
  custom = NULL
)

assert_object(
  x,
  oo_system = NULL,
  s4_bit = NULL,
  tests_class = NULL,
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

- oo_system:

  \[`character(1)` \| `NULL`\] Expected Object-Oriented system name,
  passed to [`object_system()`](object_system.md). Set to `NULL` to not
  test.

- s4_bit:

  \[`TRUE` \| `FALSE` \| `NULL`\] Whether the underlying S4 object bit
  must (`TRUE`) or mustn't be set. Set to `NULL` to not test.

- tests_class:

  \[`list`\] A list of additional class tests passed directly to
  [`test_class()`](test_class.md).

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

- \[`TRUE` \| `FALSE`\] for `test_object()`.

- \[`=x`\] `invisible(x)` for `assert_object()`, or aborts if the test
  fails.

## Examples

``` r
x <- structure(
  list(a = 1),
  class = c("my_s3_class")
)

args <- list(
  oo_system = "S3",  # Must be an S3 object (will pass)
  s4_bit = FALSE,    # Object S4 bit must not be set (will pass)
  tests_class = list(
    classes = list(all = c("my_s3_class", "another_class"))
  ),
  # Class vector must contain all specified classes (will fail)
  sentinels = c("null"),    # Allow NULL/unclassed objects (not the case of x)
  custom = \(x) is_list(x)  # Underlying object structure must be a list (will pass)
)

do.call(test_object, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_object, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_object()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must have a consistent class (see
#>   `predicater::is_object_like()`).
#> ✔ (pass) oo_system: must belong to the "S3" object system.
#> ✔ (pass) s4_bit: S4 bit must be "FALSE".
#> ✖ (fail) tests_class: must pass the custom `predicater::test_class()` test.
#>   Failed "classes".
#> ✔ (pass) custom: must pass a custom test.
#> 
#> ℹ See `predicater::assert_object()` and this condition's `rs_assert_error`
#>   attribute for details.
```

## On this page

Test if an input is an 'object' (see
[predicates-objects](predicates-objects.md)), and fits a specific
Object-Oriented (OO) system (see [`object_system()`](object_system.md)).

`test_object()` is the predicate test, while `assert_object()` validates
its input, aborting if it fails the test.

## Usage

``` r
test_object(
  x,
  oo_system = NULL,
  s4_bit = NULL,
  tests_class = NULL,
  sentinels = NULL,
  custom = NULL
)

assert_object(
  x,
  oo_system = NULL,
  s4_bit = NULL,
  tests_class = NULL,
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

- oo_system:

  \[`character(1)` \| `NULL`\] Expected Object-Oriented system name,
  passed to [`object_system()`](object_system.md). Set to `NULL` to not
  test.

- s4_bit:

  \[`TRUE` \| `FALSE` \| `NULL`\] Whether the underlying S4 object bit
  must (`TRUE`) or mustn't be set. Set to `NULL` to not test.

- tests_class:

  \[`list`\] A list of additional class tests passed directly to
  [`test_class()`](test_class.md).

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

- \[`TRUE` \| `FALSE`\] for `test_object()`.

- \[`=x`\] `invisible(x)` for `assert_object()`, or aborts if the test
  fails.

## Examples

``` r
x <- structure(
  list(a = 1),
  class = c("my_s3_class")
)

args <- list(
  oo_system = "S3",  # Must be an S3 object (will pass)
  s4_bit = FALSE,    # Object S4 bit must not be set (will pass)
  tests_class = list(
    classes = list(all = c("my_s3_class", "another_class"))
  ),
  # Class vector must contain all specified classes (will fail)
  sentinels = c("null"),    # Allow NULL/unclassed objects (not the case of x)
  custom = \(x) is_list(x)  # Underlying object structure must be a list (will pass)
)

do.call(test_object, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_object, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_object()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must have a consistent class (see
#>   `predicater::is_object_like()`).
#> ✔ (pass) oo_system: must belong to the "S3" object system.
#> ✔ (pass) s4_bit: S4 bit must be "FALSE".
#> ✖ (fail) tests_class: must pass the custom `predicater::test_class()` test.
#>   Failed "classes".
#> ✔ (pass) custom: must pass a custom test.
#> 
#> ℹ See `predicater::assert_object()` and this condition's `rs_assert_error`
#>   attribute for details.
```
