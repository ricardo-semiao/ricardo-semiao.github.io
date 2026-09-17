# Validation - Matrix and array attributes

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if an object has matrix/array-related attributes that pass some
conditions.

`test_matrix()` is a predicate test, while `assert_matrix()` validates
their input, aborting if it fails the test.

## Usage

``` r
test_matrix(
  x,
  n_dims = NULL,
  dims_shape = NULL,
  names_apply = NULL,
  how = "dim",
  sentinels = NULL,
  custom = NULL,
  custom_apply = NULL
)

assert_matrix(
  x,
  n_dims = NULL,
  dims_shape = NULL,
  names_apply = NULL,
  how = "dim",
  sentinels = NULL,
  custom = NULL,
  custom_apply = NULL,
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

- n_dims:

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

- dims_shape:

  \[[`list()`](https://rdrr.io/r/base/list.html) \|
  [`integer()`](https://rdrr.io/r/base/integer.html) \| `NULL`\]
  Expected size constraints for each dimension. Can be a vector of
  dimension sizes or a list of range specs (as for `n_dims`). Set to
  `NULL` to not test.

- names_apply:

  \[[`list()`](https://rdrr.io/r/base/list.html) \| `NULL`\] A list of
  arguments passed to [`test_names()`](test_names.md) to test each
  dimension's names. For separate tests for each dimension, use a list
  of formulas, with the LHS being the dimension integer index, and the
  RHS being the list of arguments to [`test_names()`](test_names.md). An
  empty list() test for the presence of names.

- how:

  \[`"dim"` \| `"x"` \| `"attr"`\] How to extract dimensions from `x`:
  `"dim"` for [`dim()`](https://rdrr.io/r/base/dim.html); `"x"` or `x`
  directly `"attr"` for `attr(x, "dim")`.

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

- custom_apply:

  \[[`list()`](https://rdrr.io/r/base/list.html) \| `NULL`\] A list of
  formulas. For each margin in the LHS (as in `MARGIN` in
  [`apply()`](https://rdrr.io/r/base/apply.html)), test the function in
  the RHS across that margin.

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

- \[`TRUE` \| `FALSE`\] for `test_*()`.

- \[`=x`\] `invisible(x)` for `assert_*()`, or aborts if the test fails.

## Examples

``` r
x <- matrix(
  1:6, nrow = 2, ncol = 3,
  dimnames = list(c("r1", "r2"), c("c1", "c2", "c3"))
)

args <- list(
  n_dims = 2, # Must be exactly 2-dimensional (will pass)
  dims_shape = list(2, c(1, Inf)),
  # 2 rows, and cols between 1 and Inf (will pass)
  names_apply = list(
    1 ~ list(n_na = 0, n_dup = 0),
    # Row names must have no NAs or duplicates (will pass)
    2 ~ list(set = list(no = c("c4")))
    # Column names must not contain "c4" (will pass)
  ),
  how = "dim",                # Use `dim(x)` to extract dimensions (will pass)
  sentinels = c("null"),      # Allow NULL x (not the case of x)
  custom = \(x) is.matrix(x), # Must be a standard matrix (will pass)
  custom_apply = list(1 ~ \(row) sum(row) > 10)
  # Sum of elements across each row must exceed 10 (will fail)
)

do.call(test_matrix, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_matrix, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_matrix()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : dim must be of type "integer".
#> ✔ (pass) n_dims: #of dimensions must be 2.
#> ✔ (pass) dims_shape: each dimension size must be in custom range.
#> ✖ (fail) names_apply: each dimension names must pass custom
#>   `predicater::test_names()` test. Failed for dimensions 1 and 2.
#> ✔ (pass) custom: must pass a custom test.
#> ✖ (fail) custom_apply: must pass custom tests along some margins. Failed for
#>   margin 1.
#> 
#> ℹ See `predicater::assert_matrix()` and this condition's `rs_assert_error`
#>   attribute for details.
```

## On this page

Test if an object has matrix/array-related attributes that pass some
conditions.

`test_matrix()` is a predicate test, while `assert_matrix()` validates
their input, aborting if it fails the test.

## Usage

``` r
test_matrix(
  x,
  n_dims = NULL,
  dims_shape = NULL,
  names_apply = NULL,
  how = "dim",
  sentinels = NULL,
  custom = NULL,
  custom_apply = NULL
)

assert_matrix(
  x,
  n_dims = NULL,
  dims_shape = NULL,
  names_apply = NULL,
  how = "dim",
  sentinels = NULL,
  custom = NULL,
  custom_apply = NULL,
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

- n_dims:

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

- dims_shape:

  \[[`list()`](https://rdrr.io/r/base/list.html) \|
  [`integer()`](https://rdrr.io/r/base/integer.html) \| `NULL`\]
  Expected size constraints for each dimension. Can be a vector of
  dimension sizes or a list of range specs (as for `n_dims`). Set to
  `NULL` to not test.

- names_apply:

  \[[`list()`](https://rdrr.io/r/base/list.html) \| `NULL`\] A list of
  arguments passed to [`test_names()`](test_names.md) to test each
  dimension's names. For separate tests for each dimension, use a list
  of formulas, with the LHS being the dimension integer index, and the
  RHS being the list of arguments to [`test_names()`](test_names.md). An
  empty list() test for the presence of names.

- how:

  \[`"dim"` \| `"x"` \| `"attr"`\] How to extract dimensions from `x`:
  `"dim"` for [`dim()`](https://rdrr.io/r/base/dim.html); `"x"` or `x`
  directly `"attr"` for `attr(x, "dim")`.

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

- custom_apply:

  \[[`list()`](https://rdrr.io/r/base/list.html) \| `NULL`\] A list of
  formulas. For each margin in the LHS (as in `MARGIN` in
  [`apply()`](https://rdrr.io/r/base/apply.html)), test the function in
  the RHS across that margin.

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

- \[`TRUE` \| `FALSE`\] for `test_*()`.

- \[`=x`\] `invisible(x)` for `assert_*()`, or aborts if the test fails.

## Examples

``` r
x <- matrix(
  1:6, nrow = 2, ncol = 3,
  dimnames = list(c("r1", "r2"), c("c1", "c2", "c3"))
)

args <- list(
  n_dims = 2, # Must be exactly 2-dimensional (will pass)
  dims_shape = list(2, c(1, Inf)),
  # 2 rows, and cols between 1 and Inf (will pass)
  names_apply = list(
    1 ~ list(n_na = 0, n_dup = 0),
    # Row names must have no NAs or duplicates (will pass)
    2 ~ list(set = list(no = c("c4")))
    # Column names must not contain "c4" (will pass)
  ),
  how = "dim",                # Use `dim(x)` to extract dimensions (will pass)
  sentinels = c("null"),      # Allow NULL x (not the case of x)
  custom = \(x) is.matrix(x), # Must be a standard matrix (will pass)
  custom_apply = list(1 ~ \(row) sum(row) > 10)
  # Sum of elements across each row must exceed 10 (will fail)
)

do.call(test_matrix, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_matrix, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_matrix()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : dim must be of type "integer".
#> ✔ (pass) n_dims: #of dimensions must be 2.
#> ✔ (pass) dims_shape: each dimension size must be in custom range.
#> ✖ (fail) names_apply: each dimension names must pass custom
#>   `predicater::test_names()` test. Failed for dimensions 1 and 2.
#> ✔ (pass) custom: must pass a custom test.
#> ✖ (fail) custom_apply: must pass custom tests along some margins. Failed for
#>   margin 1.
#> 
#> ℹ See `predicater::assert_matrix()` and this condition's `rs_assert_error`
#>   attribute for details.
```
