# Validation - Language

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if an object is a call (language object).

`test_language()` is the predicate test, while `assert_language()`
validates its input, aborting if it fails the test.

## Usage

``` r
test_language(
  x,
  name = NULL,
  ns = NULL,
  n_args = NULL,
  arg_names = NULL,
  simple = NULL,
  valid = NULL,
  sentinels = NULL,
  custom = NULL
)

assert_language(
  x,
  name = NULL,
  ns = NULL,
  n_args = NULL,
  arg_names = NULL,
  simple = NULL,
  valid = NULL,
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

- name, ns:

  \[`character(1)` \| `NULL`\] Expected function name and namespace of
  the call, via
  [`rlang::call_name()`](https://rlang.r-lib.org/reference/call_name.html)
  and
  [`rlang::call_ns()`](https://rlang.r-lib.org/reference/call_name.html).
  Set to `NULL` to not test.

- n_args:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `\(){}` \|
  `NULL`\] Possible values for the NA. The options of each argument
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

- arg_names:

  \[[`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\]
  Expected exact names of the call arguments. Set to `NULL` to not test.

- simple:

  \[`TRUE` \| `FALSE` \| `NULL`\] Test if the call is simple via
  [`rlang::is_call_simple()`](https://rlang.r-lib.org/reference/call_name.html).
  Set to `NULL` to not test.

- valid:

  \[`TRUE` \| `FALSE` \| `NULL`\] Test if the call is parsable. Set to
  `NULL` to not test.

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

- \[`TRUE` \| `FALSE`\] for `test_language()`.

- \[`=x`\] `invisible(x)` for `assert_language()`, or aborts if the test
  fails.

## Examples

``` r
x <- quote(rlang::env(a = 1, b = 2))

args <- list(
  name = "fn",             # Function name must be "fn" (will pass)
  ns = "otherpkg",         # Namespace must be "otherpkg" (will fail)
  n_args = c(1, 5),        # Number of arguments must be between 1 and 5 (will pass)
  arg_names = c("a", "b"), # Argument names must match exact character vector (will pass)
  simple = FALSE,          # Must not be a simple call without names/namespace (will pass)
  valid = TRUE,            # Must be a parsable, valid call (will pass)
  sentinels = c("null"),   # Allow NULL call (not the case of x)
  custom = NULL            # No custom test predicate
)

rlang::exec(test_language, !!!c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(rlang::exec(assert_language, !!!c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : 
#>   `.Primitive("quote")(rlang::env(a = 1, b = 2))` failed
#> `assert_language()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must be of type "language".
#> ✖ (fail) name  : must have call name "fn". Was "env".
#> ✖ (fail) ns    : must have call namespace "otherpkg". Was "rlang".
#> ✔ (pass) n_args: #of arguments must be in range 1 to 5.
#> ✔ (pass) arg_names: must have argument names: "a" and "b".
#> ✖ (fail) simple: must be not a simple call. Was simple.
#> ✔ (pass) valid : must be a valid call.
#> 
#> ℹ See `predicater::assert_language()` and this condition's `rs_assert_error`
#>   attribute for details.
```

## On this page

Test if an object is a call (language object).

`test_language()` is the predicate test, while `assert_language()`
validates its input, aborting if it fails the test.

## Usage

``` r
test_language(
  x,
  name = NULL,
  ns = NULL,
  n_args = NULL,
  arg_names = NULL,
  simple = NULL,
  valid = NULL,
  sentinels = NULL,
  custom = NULL
)

assert_language(
  x,
  name = NULL,
  ns = NULL,
  n_args = NULL,
  arg_names = NULL,
  simple = NULL,
  valid = NULL,
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

- name, ns:

  \[`character(1)` \| `NULL`\] Expected function name and namespace of
  the call, via
  [`rlang::call_name()`](https://rlang.r-lib.org/reference/call_name.html)
  and
  [`rlang::call_ns()`](https://rlang.r-lib.org/reference/call_name.html).
  Set to `NULL` to not test.

- n_args:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `\(){}` \|
  `NULL`\] Possible values for the NA. The options of each argument
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

- arg_names:

  \[[`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\]
  Expected exact names of the call arguments. Set to `NULL` to not test.

- simple:

  \[`TRUE` \| `FALSE` \| `NULL`\] Test if the call is simple via
  [`rlang::is_call_simple()`](https://rlang.r-lib.org/reference/call_name.html).
  Set to `NULL` to not test.

- valid:

  \[`TRUE` \| `FALSE` \| `NULL`\] Test if the call is parsable. Set to
  `NULL` to not test.

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

- \[`TRUE` \| `FALSE`\] for `test_language()`.

- \[`=x`\] `invisible(x)` for `assert_language()`, or aborts if the test
  fails.

## Examples

``` r
x <- quote(rlang::env(a = 1, b = 2))

args <- list(
  name = "fn",             # Function name must be "fn" (will pass)
  ns = "otherpkg",         # Namespace must be "otherpkg" (will fail)
  n_args = c(1, 5),        # Number of arguments must be between 1 and 5 (will pass)
  arg_names = c("a", "b"), # Argument names must match exact character vector (will pass)
  simple = FALSE,          # Must not be a simple call without names/namespace (will pass)
  valid = TRUE,            # Must be a parsable, valid call (will pass)
  sentinels = c("null"),   # Allow NULL call (not the case of x)
  custom = NULL            # No custom test predicate
)

rlang::exec(test_language, !!!c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(rlang::exec(assert_language, !!!c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : 
#>   `.Primitive("quote")(rlang::env(a = 1, b = 2))` failed
#> `assert_language()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must be of type "language".
#> ✖ (fail) name  : must have call name "fn". Was "env".
#> ✖ (fail) ns    : must have call namespace "otherpkg". Was "rlang".
#> ✔ (pass) n_args: #of arguments must be in range 1 to 5.
#> ✔ (pass) arg_names: must have argument names: "a" and "b".
#> ✖ (fail) simple: must be not a simple call. Was simple.
#> ✔ (pass) valid : must be a valid call.
#> 
#> ℹ See `predicater::assert_language()` and this condition's `rs_assert_error`
#>   attribute for details.
```
