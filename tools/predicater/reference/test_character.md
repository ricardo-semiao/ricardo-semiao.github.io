# Validation - Character vectors

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if an object is a character vector.

`test_character()` is the predicate test, while `assert_character()`
validates its input, aborting if it fails the test.

## Usage

``` r
test_character(
  x,
  len = NULL,
  n_na = NULL,
  n_dup = NULL,
  n_char = NULL,
  set = NULL,
  match = NULL,
  sorted = NULL,
  sentinels = NULL,
  custom = NULL,
  perl = FALSE
)

assert_character(
  x,
  len = NULL,
  n_na = NULL,
  n_dup = NULL,
  n_char = NULL,
  set = NULL,
  match = NULL,
  sorted = NULL,
  sentinels = NULL,
  custom = NULL,
  perl = FALSE,
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

- len, n_na, n_dup, n_char:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `\(){}` \|
  `NULL`\] Possible values for the length, number of `NA` elements,
  number of duplicate elements, number of characters (vectorized). The
  options of each argument 'arg' are:

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

- set:

  \[[`character()`](https://rdrr.io/r/base/character.html) \|
  `list(yes = , no = , mode = )` \| `NULL`\] Test if all values of `x`
  are in a set of allowed values. Use a list with `yes` and/or `no`
  elements to defined allowed and disallowed values, with `mode`s
  `"all"` (all `x` in `yes`, the default), `"only"` (all and only `x` in
  `yes`), or `"any"` (any `x` in `yes`). Set to `NULL` to not test.

- match:

  \[[`character()`](https://rdrr.io/r/base/character.html) \|
  `list(yes = , no = )` \| `NULL`\] Test if all elements of `x` match
  regular expression patterns. Pass a character vector of patterns
  (implicitly OR'd together), or a list with `yes` and `no` character
  vectors of patterns. Set to `NULL` to not test.

- sorted:

  \[`"asc"` \| `"desc"` \| `NULL`\] Test if `x` is sorted in ascending
  (`"asc"`) or descending (`"desc"`) order. Set to `NULL` to not test.
  Pair with `n_dup` to test for strictly sorted values.

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

- perl:

  \[`TRUE` \| `FALSE`\] Should Perl-compatible regexps be used in
  `match`?

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

- \[`TRUE` \| `FALSE`\] for `test_character()`.

- \[`=x`\] `invisible(x)` for `assert_character()`, or aborts if the
  test fails.

## Examples

``` r
x <- c("apple", "banana", "cherry", "banana")

args <- list(
  len = c(1, 10),              # Length must be between 1 and 10 (will pass)
  n_na = 0,                    # No NA values allowed (will pass)
  n_dup = 0,                   # No duplicate strings allowed (will fail)
  n_char = c(1, 10),           # Character length of each string between 1 and 10 (will pass)
  set = list(no = c("date")),  # Strings must not contain "date" (will pass)
  match = list(
    yes = "^[a-z]+$",          # All elements must be lowercase letters (will pass)
    no = "x"                   # No element can contain "x" (will pass)
  ),
  sorted = FALSE,              # Don't require vector to be sorted in alphabetical order (will pass)
  sentinels = c("null"),       # Allow NULL x (not the case of x)
  custom = NULL                # No custom predicate
)

do.call(test_character, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_character, c(list(x), args))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_character()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must be of type "character".
#> ✔ (pass) len   : length must be in range 1 to 10.
#> ✔ (pass) n_na  : #of NA values must be 0.
#> ✖ (fail) n_dup : #of duplicate values must be 0. Was 1.
#> • (skip) n_char: skiped given failure.
#> • (skip) set   : skiped given failure.
#> • (skip) match : skiped given failure.
#> • (skip) sorted: skiped given failure.
#> 
#> ℹ See `predicater::assert_character()` and this condition's `rs_assert_error`
#>   attribute for details.
```

## On this page

Test if an object is a character vector.

`test_character()` is the predicate test, while `assert_character()`
validates its input, aborting if it fails the test.

## Usage

``` r
test_character(
  x,
  len = NULL,
  n_na = NULL,
  n_dup = NULL,
  n_char = NULL,
  set = NULL,
  match = NULL,
  sorted = NULL,
  sentinels = NULL,
  custom = NULL,
  perl = FALSE
)

assert_character(
  x,
  len = NULL,
  n_na = NULL,
  n_dup = NULL,
  n_char = NULL,
  set = NULL,
  match = NULL,
  sorted = NULL,
  sentinels = NULL,
  custom = NULL,
  perl = FALSE,
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

- len, n_na, n_dup, n_char:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `\(){}` \|
  `NULL`\] Possible values for the length, number of `NA` elements,
  number of duplicate elements, number of characters (vectorized). The
  options of each argument 'arg' are:

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

- set:

  \[[`character()`](https://rdrr.io/r/base/character.html) \|
  `list(yes = , no = , mode = )` \| `NULL`\] Test if all values of `x`
  are in a set of allowed values. Use a list with `yes` and/or `no`
  elements to defined allowed and disallowed values, with `mode`s
  `"all"` (all `x` in `yes`, the default), `"only"` (all and only `x` in
  `yes`), or `"any"` (any `x` in `yes`). Set to `NULL` to not test.

- match:

  \[[`character()`](https://rdrr.io/r/base/character.html) \|
  `list(yes = , no = )` \| `NULL`\] Test if all elements of `x` match
  regular expression patterns. Pass a character vector of patterns
  (implicitly OR'd together), or a list with `yes` and `no` character
  vectors of patterns. Set to `NULL` to not test.

- sorted:

  \[`"asc"` \| `"desc"` \| `NULL`\] Test if `x` is sorted in ascending
  (`"asc"`) or descending (`"desc"`) order. Set to `NULL` to not test.
  Pair with `n_dup` to test for strictly sorted values.

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

- perl:

  \[`TRUE` \| `FALSE`\] Should Perl-compatible regexps be used in
  `match`?

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

- \[`TRUE` \| `FALSE`\] for `test_character()`.

- \[`=x`\] `invisible(x)` for `assert_character()`, or aborts if the
  test fails.

## Examples

``` r
x <- c("apple", "banana", "cherry", "banana")

args <- list(
  len = c(1, 10),              # Length must be between 1 and 10 (will pass)
  n_na = 0,                    # No NA values allowed (will pass)
  n_dup = 0,                   # No duplicate strings allowed (will fail)
  n_char = c(1, 10),           # Character length of each string between 1 and 10 (will pass)
  set = list(no = c("date")),  # Strings must not contain "date" (will pass)
  match = list(
    yes = "^[a-z]+$",          # All elements must be lowercase letters (will pass)
    no = "x"                   # No element can contain "x" (will pass)
  ),
  sorted = FALSE,              # Don't require vector to be sorted in alphabetical order (will pass)
  sentinels = c("null"),       # Allow NULL x (not the case of x)
  custom = NULL                # No custom predicate
)

do.call(test_character, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_character, c(list(x), args))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_character()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : must be of type "character".
#> ✔ (pass) len   : length must be in range 1 to 10.
#> ✔ (pass) n_na  : #of NA values must be 0.
#> ✖ (fail) n_dup : #of duplicate values must be 0. Was 1.
#> • (skip) n_char: skiped given failure.
#> • (skip) set   : skiped given failure.
#> • (skip) match : skiped given failure.
#> • (skip) sorted: skiped given failure.
#> 
#> ℹ See `predicater::assert_character()` and this condition's `rs_assert_error`
#>   attribute for details.
```
