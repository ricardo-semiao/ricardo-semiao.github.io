# Validation - Code Objects

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if an input is a R language code object (symbol, language/call, or
syntactic literal), and optionally check if it is valid parsable code or
an empty symbol.

`test_code()` is the predicate test, while `assert_code()` validates its
input, aborting if it fails the test.

## Usage

``` r
test_code(
  x,
  sym = TRUE,
  lang = TRUE,
  literal = TRUE,
  valid = NULL,
  empty = NULL,
  sentinels = NULL,
  custom = NULL
)

assert_code(
  x,
  sym = TRUE,
  lang = TRUE,
  literal = TRUE,
  valid = NULL,
  empty = NULL,
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

- sym, lang, literal:

  \[`TRUE` \| `FALSE` \| `NULL`\] Whether to allow symbols, language
  objects (calls), or syntactic literals.

- valid:

  \[`logical(1)` \| `NULL`\] Whether the code object must be parsable
  code.

- empty:

  \[`logical(1)` \| `NULL`\] Whether empty symbols are permitted.

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

- \[`TRUE` \| `FALSE`\] for `test_code()`.

- \[`=x`\] `invisible(x)` for `assert_code()`, or aborts if the test
  fails.

## Examples

``` r
x <- 42L

args <- list(
  sym = FALSE,            # Disallow symbols (will pass)
  lang = FALSE,           # Disallow language objects/calls (will pass)
  literal = TRUE,         # Allow syntactic literals (will pass)
  valid = TRUE,           # Must be parsable code (will pass)
  empty = FALSE,          # Disallow empty symbols (will pass)
  sentinels = c("null"),  # Allow NULL code object (not the case of x)
  custom = \(x) x > 100   # Literal value must be > 100 (will fail)
)

rlang::exec(test_code, !!!c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(rlang::exec(assert_code, !!!c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `42` failed `assert_code()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must be of 'type' "syntactic literal".
#> ✔ (pass) valid : must be valid code.
#> ✔ (pass) empty :
#> ✖ (fail) custom: must pass a custom test. Did not.
#> 
#> ℹ See `predicater::assert_code()` and this condition's `rs_assert_error`
#>   attribute for details.
```

## On this page

Test if an input is a R language code object (symbol, language/call, or
syntactic literal), and optionally check if it is valid parsable code or
an empty symbol.

`test_code()` is the predicate test, while `assert_code()` validates its
input, aborting if it fails the test.

## Usage

``` r
test_code(
  x,
  sym = TRUE,
  lang = TRUE,
  literal = TRUE,
  valid = NULL,
  empty = NULL,
  sentinels = NULL,
  custom = NULL
)

assert_code(
  x,
  sym = TRUE,
  lang = TRUE,
  literal = TRUE,
  valid = NULL,
  empty = NULL,
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

- sym, lang, literal:

  \[`TRUE` \| `FALSE` \| `NULL`\] Whether to allow symbols, language
  objects (calls), or syntactic literals.

- valid:

  \[`logical(1)` \| `NULL`\] Whether the code object must be parsable
  code.

- empty:

  \[`logical(1)` \| `NULL`\] Whether empty symbols are permitted.

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

- \[`TRUE` \| `FALSE`\] for `test_code()`.

- \[`=x`\] `invisible(x)` for `assert_code()`, or aborts if the test
  fails.

## Examples

``` r
x <- 42L

args <- list(
  sym = FALSE,            # Disallow symbols (will pass)
  lang = FALSE,           # Disallow language objects/calls (will pass)
  literal = TRUE,         # Allow syntactic literals (will pass)
  valid = TRUE,           # Must be parsable code (will pass)
  empty = FALSE,          # Disallow empty symbols (will pass)
  sentinels = c("null"),  # Allow NULL code object (not the case of x)
  custom = \(x) x > 100   # Literal value must be > 100 (will fail)
)

rlang::exec(test_code, !!!c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(rlang::exec(assert_code, !!!c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `42` failed `assert_code()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must be of 'type' "syntactic literal".
#> ✔ (pass) valid : must be valid code.
#> ✔ (pass) empty :
#> ✖ (fail) custom: must pass a custom test. Did not.
#> 
#> ℹ See `predicater::assert_code()` and this condition's `rs_assert_error`
#>   attribute for details.
```
