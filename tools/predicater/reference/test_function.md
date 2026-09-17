# Validation - Function

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if an object is a function, with options to inspect function type,
argument names, environments, S3 generics, and methods.

## Usage

``` r
test_function(
  x,
  mode = "function",
  args_names = NULL,
  fn_env = NULL,
  dots = NULL,
  sentinels = NULL,
  custom = NULL
)

assert_function(
  x,
  mode = "function",
  args_names = NULL,
  fn_env = NULL,
  dots = NULL,
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

  \[`"function"` \| `"closure"` \| `"builtin"` \| `"special"` \|
  `"primitive"` \| `NULL`\] Expected function type(s) out of
  `"function"` (any function), `"closure"`, `"builtin"`, `"special"`, or
  `"primitive"` (any of the former two). Set to `NULL` to not test.

- args_names:

  \[[`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\]
  Expected exact argument names of the function. Set to `NULL` to not
  test.

- fn_env:

  \[`environment` \| `NULL`\] Expected environment of the function.
  Checks if `fn_env(x)` is identical to `env` or inherits from it via
  [`rlang::env_inherits()`](https://rlang.r-lib.org/reference/env_inherits.html).
  Set to `NULL` to not test.

- dots:

  \[`TRUE` \| `FALSE` \| `NULL`\] Test if the function has `...` in its
  arguments. Set to `NULL` to not test.

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

- \[`TRUE` \| `FALSE`\] for `test_function()`.

- \[`=x`\] `invisible(x)` for `assert_function()`, or aborts if the test
  fails.

## Examples

``` r
x <- function(a, b = 1, ...) {
  a + b
}

args <- list(
  mode = "closure",            # Must be a standard closure function (will pass)
  args_names = c("a", "b"),    # Exact argument names must match (will fail)
  fn_env = rlang::global_env(),
  # Function environment must equal or inherit from global env (will pass)
  dots = TRUE,                 # Function must accept `...` in arguments (will pass)
  sentinels = c("null"),       # Allow NULL function (not the case of x)
  custom = NULL                # No custom predicate
)

do.call(test_function, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_function, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_function()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must be of type "closure".
#> ✖ (fail) args_names: must have argument names "a" and "b". Had "a", "b", and
#>   "...".
#> ✔ (pass) fn_env: must have the expected environment.
#> ✔ (pass) dots  : must accept `...`.
#> 
#> ℹ See `predicater::assert_function()` and this condition's `rs_assert_error`
#>   attribute for details.
```

## On this page

Test if an object is a function, with options to inspect function type,
argument names, environments, S3 generics, and methods.

## Usage

``` r
test_function(
  x,
  mode = "function",
  args_names = NULL,
  fn_env = NULL,
  dots = NULL,
  sentinels = NULL,
  custom = NULL
)

assert_function(
  x,
  mode = "function",
  args_names = NULL,
  fn_env = NULL,
  dots = NULL,
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

  \[`"function"` \| `"closure"` \| `"builtin"` \| `"special"` \|
  `"primitive"` \| `NULL`\] Expected function type(s) out of
  `"function"` (any function), `"closure"`, `"builtin"`, `"special"`, or
  `"primitive"` (any of the former two). Set to `NULL` to not test.

- args_names:

  \[[`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\]
  Expected exact argument names of the function. Set to `NULL` to not
  test.

- fn_env:

  \[`environment` \| `NULL`\] Expected environment of the function.
  Checks if `fn_env(x)` is identical to `env` or inherits from it via
  [`rlang::env_inherits()`](https://rlang.r-lib.org/reference/env_inherits.html).
  Set to `NULL` to not test.

- dots:

  \[`TRUE` \| `FALSE` \| `NULL`\] Test if the function has `...` in its
  arguments. Set to `NULL` to not test.

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

- \[`TRUE` \| `FALSE`\] for `test_function()`.

- \[`=x`\] `invisible(x)` for `assert_function()`, or aborts if the test
  fails.

## Examples

``` r
x <- function(a, b = 1, ...) {
  a + b
}

args <- list(
  mode = "closure",            # Must be a standard closure function (will pass)
  args_names = c("a", "b"),    # Exact argument names must match (will fail)
  fn_env = rlang::global_env(),
  # Function environment must equal or inherit from global env (will pass)
  dots = TRUE,                 # Function must accept `...` in arguments (will pass)
  sentinels = c("null"),       # Allow NULL function (not the case of x)
  custom = NULL                # No custom predicate
)

do.call(test_function, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_function, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_function()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must be of type "closure".
#> ✖ (fail) args_names: must have argument names "a" and "b". Had "a", "b", and
#>   "...".
#> ✔ (pass) fn_env: must have the expected environment.
#> ✔ (pass) dots  : must accept `...`.
#> 
#> ℹ See `predicater::assert_function()` and this condition's `rs_assert_error`
#>   attribute for details.
```
