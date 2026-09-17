# Validation - Throw error from custom predicate

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

This function evaluates a custom predicate function on an object and
aborts with a custom message if the check fails. It is useful for
testing function arguments.

## Usage

``` r
assert_predicate(
  fun,
  ...,
  args_fun = list(),
  msg = NULL,
  x_names = NULL,
  env = caller_env(),
  args_cnd = list()
)
```

## Arguments

- fun:

  \[`\(){}`\] The predicate function to run. Must receive the object to
  test as its first argument.

- ...:

  \[`any` each\] Objects to check.

- args_fun:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] Additional arguments
  to pass to `fun`.

- msg:

  \[`character(1)` \| `NULL`\] The message to use if the check fails. If
  `NULL`, a default message is generated.

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
try({
  f <- \(x) test_when(x, all(.x > 0))
  f(c(-1, 0, 1))
})
#> Error in test_when(x, all(.x > 0)) : could not find function "test_when"
#> Error in `f()`:
#> ! Argument `x` fails `all(.x > 0)`.
```

## On this page

This function evaluates a custom predicate function on an object and
aborts with a custom message if the check fails. It is useful for
testing function arguments.

## Usage

``` r
assert_predicate(
  fun,
  ...,
  args_fun = list(),
  msg = NULL,
  x_names = NULL,
  env = caller_env(),
  args_cnd = list()
)
```

## Arguments

- fun:

  \[`\(){}`\] The predicate function to run. Must receive the object to
  test as its first argument.

- ...:

  \[`any` each\] Objects to check.

- args_fun:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] Additional arguments
  to pass to `fun`.

- msg:

  \[`character(1)` \| `NULL`\] The message to use if the check fails. If
  `NULL`, a default message is generated.

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
try({
  f <- \(x) test_when(x, all(.x > 0))
  f(c(-1, 0, 1))
})
#> Error in test_when(x, all(.x > 0)) : could not find function "test_when"
#> Error in `f()`:
#> ! Argument `x` fails `all(.x > 0)`.
```
