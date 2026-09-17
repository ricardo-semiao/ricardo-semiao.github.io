# Validation - Environment

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if an object is an environment.

`test_environment()` is the predicate test, while `assert_environment()`
validates its input, aborting if it fails the test.

## Usage

``` r
test_environment(
  x,
  len = NULL,
  env_has = NULL,
  env_sees = NULL,
  parents = NULL,
  namespace = NULL,
  sentinels = NULL,
  custom = NULL,
  custom_map = NULL
)

assert_environment(
  x,
  len = NULL,
  env_has = NULL,
  env_sees = NULL,
  parents = NULL,
  namespace = NULL,
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

- env_has, env_sees:

  \[[`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\]
  Symbol names that must exist directly in `x`, or inherited from one of
  its parents, respectively (see
  [`rlang::env_has()`](https://rlang.r-lib.org/reference/env_has.html)).
  Set to `NULL` to not test.

- parents:

  \[[`environment()`](https://rdrr.io/r/base/environment.html) \|
  [`list()`](https://rdrr.io/r/base/list.html) \| `NULL`\] Environment
  or list of environments to test as parents of `x`. If a single
  environment is supplied, tests if `x` inherits from it. If a list is
  supplied, tests if
  [`rlang::env_parents()`](https://rlang.r-lib.org/reference/env_parent.html)
  matches the list identically. Set to `NULL` to not test.

- namespace:

  \[`TRUE` \| `FALSE` \| `NULL`\] Test if `x` is a namespace environment
  via
  [`rlang::is_namespace()`](https://rlang.r-lib.org/reference/is_namespace.html).
  Set to `NULL` to not test.

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

- \[`TRUE` \| `FALSE`\] for `test_environment()`.

- \[`=x`\] `invisible(x)` for `assert_environment()`, or aborts if the
  test fails.

## Examples

``` r
x <- rlang::new_environment(list(a = 1, b = 2), parent = rlang::global_env())

args <- list(
  len = c(1, 5),         # Length (number of bindings) must be between 1 and 5 (will pass)
  env_has = c("a", "b"), # Environment must directly bind "a" and "b" (will pass)
  env_sees = "__x__",    # Environment or its parents must see symbol "__x__" (will fail)
  parents = rlang::global_env(),
  # Must inherit from the global environment (will pass)
  namespace = TRUE,      # Must be a package namespace (will fail)
  sentinels = c("null"), # Allow NULL environment (not the case of x)
  custom = NULL,         # Not test
  custom_map = \(val) is.numeric(val)
  # All binding values must be numeric (will pass)
)

do.call(test_environment, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_environment, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_environment()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must be of type "environment".
#> ✔ (pass) len   : length must be in range 1 to 5.
#> ✖ (fail) namespace:
#> ✔ (pass) parents: must be child of specific parents.
#> ✔ (pass) env_has: must contain "a" and "b".
#> ✖ (fail) env_sees: must contain or inherit "__x__". Is missing "__x__".
#> ✔ (pass) custom_map: all elements must pass a custom test.
#> 
#> ℹ See `predicater::assert_environment()` and this condition's `rs_assert_error`
#>   attribute for details.
```

## On this page

Test if an object is an environment.

`test_environment()` is the predicate test, while `assert_environment()`
validates its input, aborting if it fails the test.

## Usage

``` r
test_environment(
  x,
  len = NULL,
  env_has = NULL,
  env_sees = NULL,
  parents = NULL,
  namespace = NULL,
  sentinels = NULL,
  custom = NULL,
  custom_map = NULL
)

assert_environment(
  x,
  len = NULL,
  env_has = NULL,
  env_sees = NULL,
  parents = NULL,
  namespace = NULL,
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

- env_has, env_sees:

  \[[`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\]
  Symbol names that must exist directly in `x`, or inherited from one of
  its parents, respectively (see
  [`rlang::env_has()`](https://rlang.r-lib.org/reference/env_has.html)).
  Set to `NULL` to not test.

- parents:

  \[[`environment()`](https://rdrr.io/r/base/environment.html) \|
  [`list()`](https://rdrr.io/r/base/list.html) \| `NULL`\] Environment
  or list of environments to test as parents of `x`. If a single
  environment is supplied, tests if `x` inherits from it. If a list is
  supplied, tests if
  [`rlang::env_parents()`](https://rlang.r-lib.org/reference/env_parent.html)
  matches the list identically. Set to `NULL` to not test.

- namespace:

  \[`TRUE` \| `FALSE` \| `NULL`\] Test if `x` is a namespace environment
  via
  [`rlang::is_namespace()`](https://rlang.r-lib.org/reference/is_namespace.html).
  Set to `NULL` to not test.

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

- \[`TRUE` \| `FALSE`\] for `test_environment()`.

- \[`=x`\] `invisible(x)` for `assert_environment()`, or aborts if the
  test fails.

## Examples

``` r
x <- rlang::new_environment(list(a = 1, b = 2), parent = rlang::global_env())

args <- list(
  len = c(1, 5),         # Length (number of bindings) must be between 1 and 5 (will pass)
  env_has = c("a", "b"), # Environment must directly bind "a" and "b" (will pass)
  env_sees = "__x__",    # Environment or its parents must see symbol "__x__" (will fail)
  parents = rlang::global_env(),
  # Must inherit from the global environment (will pass)
  namespace = TRUE,      # Must be a package namespace (will fail)
  sentinels = c("null"), # Allow NULL environment (not the case of x)
  custom = NULL,         # Not test
  custom_map = \(val) is.numeric(val)
  # All binding values must be numeric (will pass)
)

do.call(test_environment, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_environment, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_environment()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must be of type "environment".
#> ✔ (pass) len   : length must be in range 1 to 5.
#> ✖ (fail) namespace:
#> ✔ (pass) parents: must be child of specific parents.
#> ✔ (pass) env_has: must contain "a" and "b".
#> ✖ (fail) env_sees: must contain or inherit "__x__". Is missing "__x__".
#> ✔ (pass) custom_map: all elements must pass a custom test.
#> 
#> ℹ See `predicater::assert_environment()` and this condition's `rs_assert_error`
#>   attribute for details.
```
