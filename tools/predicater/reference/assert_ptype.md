# Validation - If object is of prototype

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

This function wraps [`is_ptype()`](is_ptype.md) and aborts with a custom
message if the check fails. It is useful for testing function arguments.

## Usage

``` r
assert_ptype(
  ptype,
  ...,
  args_ptype = list(),
  msg = NULL,
  x_names = NULL,
  env = caller_env(),
  args_cnd = list()
)
```

## Arguments

- ptype:

  \[`any`\] The prototype to check against. See
  [`is_ptype()`](is_ptype.md) for details on what is a prototype.

- ...:

  \[`any` each\] Objects to check.

- args_ptype:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] Additional arguments
  to pass to [`is_ptype()`](is_ptype.md).

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
  f <- \(x) test_ptype(x, numeric())
  f("a")
})
#> Error in test_ptype(x, numeric()) : could not find function "test_ptype"
#> Error in `f()`:
#> ! Argument `x` is not of prototype `numeric()`.
```

## On this page

This function wraps [`is_ptype()`](is_ptype.md) and aborts with a custom
message if the check fails. It is useful for testing function arguments.

## Usage

``` r
assert_ptype(
  ptype,
  ...,
  args_ptype = list(),
  msg = NULL,
  x_names = NULL,
  env = caller_env(),
  args_cnd = list()
)
```

## Arguments

- ptype:

  \[`any`\] The prototype to check against. See
  [`is_ptype()`](is_ptype.md) for details on what is a prototype.

- ...:

  \[`any` each\] Objects to check.

- args_ptype:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] Additional arguments
  to pass to [`is_ptype()`](is_ptype.md).

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
  f <- \(x) test_ptype(x, numeric())
  f("a")
})
#> Error in test_ptype(x, numeric()) : could not find function "test_ptype"
#> Error in `f()`:
#> ! Argument `x` is not of prototype `numeric()`.
```
