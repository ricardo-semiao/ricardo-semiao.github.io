# Validation - Names attribute

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if an object's names (or character vector of names) satisfies some
conditions.

`test_names()` is the predicate test, while `assert_names()` validates
its input, aborting if it fails the test.

Hint: use `sentinels = c("null")` to allow no (`NULL`) names, and
`empty = TRUE` to always pass the test if the underlying vector `x` is
empty.

## Usage

``` r
test_names(
  x,
  n_na = NULL,
  n_empty = NULL,
  n_dup = NULL,
  n_invalid = NULL,
  set = NULL,
  tests_char = NULL,
  how = "names",
  empty = NULL,
  sentinels = NULL,
  custom = NULL
)

assert_names(
  x,
  n_na = NULL,
  n_empty = NULL,
  n_dup = NULL,
  n_invalid = NULL,
  set = NULL,
  tests_char = NULL,
  how = "names",
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

  \[`any`\] An object to get names from, or a character vector of names
  to test.

- n_na, n_dup, n_empty, n_invalid:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `\(){}` \|
  `NULL`\] Possible values for the number of `NA` elements, number of
  duplicate elements, number of elements with zero length, number of
  non-syntactic elements. The options of each argument 'arg' are:

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

- tests_char:

  \[`list`\] A list of additional arguments passed to
  [`test_character()`](test_character.md).

- how:

  \[`"names"` \| `"x"` \| `"attr"` \| `"colnames"` \| `"row.names"` \|
  `integer(1)`\] How to extract names from `x`: `"x"` for `x` directly;
  `"names"` for `names(x)`; `"attr"` for `attr(x, "names")`;
  `"colnames"` for `colnames(x)`; `"row.names"` for
  `attr(x, "row.names")`; or a positive integer for
  `dimnames(x)[[how]]`.

- empty:

  \[`TRUE` \| `NULL`\] Whether to early pass the test if the underlying
  vector `x` is empty.

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

- \[`TRUE` \| `FALSE`\] for `test_names()`.

- \[`=x`\] `invisible(x)` for `assert_names()`, or aborts if the test
  fails.

## Examples

``` r
x <- rlang::set_names(1:6, c("a", "b", "c", NA, "", ""))

args <- list(
  n_na = 0,              # No NA names (will fail)
  n_dup = NULL,          # Don't test for duplicates
  n_empty = c(0, -1),    # Between 0 and length(x) - 1 empty names (will pass)
  n_invalid = c(0, Inf), # Between 0 and Inf invalid names (same as not testing)
  set = list(yes = c("a", "b"), no = c("d", "e")),
  # Names must be only "a" or "b", and not "d" nor "e" (will fail)
  how = "names",         # Use `names(x)` as the names vector to test
  empty = NULL,          # Don't allow empty `x` (will pass)
  sentinels = c("null"), # Allow `NULL` names (not the case of x)
  custom = \(x) isTRUE(all(nchar(x) == 1))
  # All names must be a single character (will fail)
)

do.call(test_names, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_names, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_names()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : names must be of type "character".
#> ✖ (fail) n_na  : #of NA values must be 0. Was 1.
#> ✔ (pass) n_empty: #of empty string names must be in range 0 to -1.
#> ✔ (pass) n_invalid: #of syntactically invalid names must be in range 0 to Inf.
#> ✖ (fail) set   : must be in a custom set. Was not.
#> ✖ (fail) custom: must pass a custom test. Did not.
#> 
#> ℹ See `predicater::assert_names()` and this condition's `rs_assert_error`
#>   attribute for details.
```

## On this page

Test if an object's names (or character vector of names) satisfies some
conditions.

`test_names()` is the predicate test, while `assert_names()` validates
its input, aborting if it fails the test.

Hint: use `sentinels = c("null")` to allow no (`NULL`) names, and
`empty = TRUE` to always pass the test if the underlying vector `x` is
empty.

## Usage

``` r
test_names(
  x,
  n_na = NULL,
  n_empty = NULL,
  n_dup = NULL,
  n_invalid = NULL,
  set = NULL,
  tests_char = NULL,
  how = "names",
  empty = NULL,
  sentinels = NULL,
  custom = NULL
)

assert_names(
  x,
  n_na = NULL,
  n_empty = NULL,
  n_dup = NULL,
  n_invalid = NULL,
  set = NULL,
  tests_char = NULL,
  how = "names",
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

  \[`any`\] An object to get names from, or a character vector of names
  to test.

- n_na, n_dup, n_empty, n_invalid:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html) \| `\(){}` \|
  `NULL`\] Possible values for the number of `NA` elements, number of
  duplicate elements, number of elements with zero length, number of
  non-syntactic elements. The options of each argument 'arg' are:

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

- tests_char:

  \[`list`\] A list of additional arguments passed to
  [`test_character()`](test_character.md).

- how:

  \[`"names"` \| `"x"` \| `"attr"` \| `"colnames"` \| `"row.names"` \|
  `integer(1)`\] How to extract names from `x`: `"x"` for `x` directly;
  `"names"` for `names(x)`; `"attr"` for `attr(x, "names")`;
  `"colnames"` for `colnames(x)`; `"row.names"` for
  `attr(x, "row.names")`; or a positive integer for
  `dimnames(x)[[how]]`.

- empty:

  \[`TRUE` \| `NULL`\] Whether to early pass the test if the underlying
  vector `x` is empty.

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

- \[`TRUE` \| `FALSE`\] for `test_names()`.

- \[`=x`\] `invisible(x)` for `assert_names()`, or aborts if the test
  fails.

## Examples

``` r
x <- rlang::set_names(1:6, c("a", "b", "c", NA, "", ""))

args <- list(
  n_na = 0,              # No NA names (will fail)
  n_dup = NULL,          # Don't test for duplicates
  n_empty = c(0, -1),    # Between 0 and length(x) - 1 empty names (will pass)
  n_invalid = c(0, Inf), # Between 0 and Inf invalid names (same as not testing)
  set = list(yes = c("a", "b"), no = c("d", "e")),
  # Names must be only "a" or "b", and not "d" nor "e" (will fail)
  how = "names",         # Use `names(x)` as the names vector to test
  empty = NULL,          # Don't allow empty `x` (will pass)
  sentinels = c("null"), # Allow `NULL` names (not the case of x)
  custom = \(x) isTRUE(all(nchar(x) == 1))
  # All names must be a single character (will fail)
)

do.call(test_names, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_names, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_names()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : names must be of type "character".
#> ✖ (fail) n_na  : #of NA values must be 0. Was 1.
#> ✔ (pass) n_empty: #of empty string names must be in range 0 to -1.
#> ✔ (pass) n_invalid: #of syntactically invalid names must be in range 0 to Inf.
#> ✖ (fail) set   : must be in a custom set. Was not.
#> ✖ (fail) custom: must pass a custom test. Did not.
#> 
#> ℹ See `predicater::assert_names()` and this condition's `rs_assert_error`
#>   attribute for details.
```
