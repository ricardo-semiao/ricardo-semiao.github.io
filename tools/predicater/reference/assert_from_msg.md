# Validation - Rethrow errors with more information

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Packages like this one, `checkmate`, and `chk` provide functions to
check objects and return a message or abort if the check fails. This
function allows the user to catch that message/error and generate a
condition with higher flexibility than the original package.

## Usage

``` r
assert_from_msg(
  fun,
  ...,
  args_fun = list(),
  x_names = NULL,
  env = caller_env(),
  args_cnd = list()
)

assert_from_error(
  fun,
  ...,
  args_fun = list(),
  x_names = NULL,
  env = caller_env(),
  args_cnd = list()
)
```

## Arguments

- fun:

  \[`\(){}`\]

  - For `assert_from_msg()`: a function that checks an object and
    returns `TRUE` if the check passes, or a message (`character(1)`) if
    it fails.

  - For `assert_from_error()`: a function that checks an object and
    raises an error if the check fails.

- ...:

  \[`any` each\] Objects to check.

- args_fun:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] Additional arguments
  to pass to `fun`.

- x_names:

  \[[`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\]
  The names of `...` to print in messages. If `NULL`, the name is
  inferred from `...`'s expressions.

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

- args_cnd:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] Additional arguments
  passed to
  [`cli::cli_abort()`](https://cli.r-lib.org/reference/cli_abort.html).

## Value

\[`list(...)`\] `invisible(list(...))`, or aborts if the check fails.

## Examples

``` r
# Using checkmate::check_* functions:
# try({
#   f <- \(x) test_msg(checkmate::check_numeric, x, any.missing = FALSE)
#   f(c(1, NA))
# })
#> Error in `f()`:
#> ! Argument `x` contains missing values (element 2)

# Multiple arguments with the same test:
# try({
#   g <- \(x, y) test_msgs(checkmate::check_logical, x, y, args = list(len = 1))
#   g(TRUE, c(FALSE, TRUE))
# })
#> Error in `g()`:
#> ! Argument `y` must have length 1, but has length 2
```

## On this page

Packages like this one, `checkmate`, and `chk` provide functions to
check objects and return a message or abort if the check fails. This
function allows the user to catch that message/error and generate a
condition with higher flexibility than the original package.

## Usage

``` r
assert_from_msg(
  fun,
  ...,
  args_fun = list(),
  x_names = NULL,
  env = caller_env(),
  args_cnd = list()
)

assert_from_error(
  fun,
  ...,
  args_fun = list(),
  x_names = NULL,
  env = caller_env(),
  args_cnd = list()
)
```

## Arguments

- fun:

  \[`\(){}`\]

  - For `assert_from_msg()`: a function that checks an object and
    returns `TRUE` if the check passes, or a message (`character(1)`) if
    it fails.

  - For `assert_from_error()`: a function that checks an object and
    raises an error if the check fails.

- ...:

  \[`any` each\] Objects to check.

- args_fun:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] Additional arguments
  to pass to `fun`.

- x_names:

  \[[`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\]
  The names of `...` to print in messages. If `NULL`, the name is
  inferred from `...`'s expressions.

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

- args_cnd:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] Additional arguments
  passed to
  [`cli::cli_abort()`](https://cli.r-lib.org/reference/cli_abort.html).

## Value

\[`list(...)`\] `invisible(list(...))`, or aborts if the check fails.

## Examples

``` r
# Using checkmate::check_* functions:
# try({
#   f <- \(x) test_msg(checkmate::check_numeric, x, any.missing = FALSE)
#   f(c(1, NA))
# })
#> Error in `f()`:
#> ! Argument `x` contains missing values (element 2)

# Multiple arguments with the same test:
# try({
#   g <- \(x, y) test_msgs(checkmate::check_logical, x, y, args = list(len = 1))
#   g(TRUE, c(FALSE, TRUE))
# })
#> Error in `g()`:
#> ! Argument `y` must have length 1, but has length 2
```
