# Validation - Class attribute

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if an object inherits from specific classes or has a valid class
vector.

Invalid classes fail the test: non-character vectors, empty character
vectors, or a vector with `NA` values.

`test_class()` is the predicate test, while `assert_class()` validates
its input, aborting if it fails the test.

## Usage

``` r
test_class(
  x,
  classes = NULL,
  tests_char = NULL,
  how = "class",
  sentinels = NULL,
  custom = NULL
)

assert_class(
  x,
  classes = NULL,
  tests_char = NULL,
  how = "class",
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

- classes:

  \[[`list()`](https://rdrr.io/r/base/list.html) \|
  [`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\] A
  named list specifying possible class inheritance criteria. The
  elements are the classes to test against, and the names are which test
  to do: `"any"` for
  [`rlang::inherits_any()`](https://rlang.r-lib.org/reference/inherits_any.html),
  `"all"` for
  [`rlang::inherits_all()`](https://rlang.r-lib.org/reference/inherits_any.html),
  `"only"` for
  [`rlang::inherits_only()`](https://rlang.r-lib.org/reference/inherits_any.html),
  and `"none"` for `!inherits_any()`. If any of the test passes, the
  overall test passes. If a single character, it is tested with
  `inherits_any()`. Set to `NULL` to not test.

- tests_char:

  \[`list`\] A list of additional character tests passed to
  [`test_character()`](test_character.md).

- how:

  \[`"class"` \| `"x"` \| `"attr"`\] How to extract class names for
  `tests_char`: `"x"` for `x` directly; `"class"` for
  [`class()`](https://rdrr.io/r/base/class.html); and `"attr"` for
  `attr(x, "class")`.

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

- \[`TRUE` \| `FALSE`\] for `test_class()`.

- \[`=x`\] `invisible(x)` for `assert_class()`, or aborts if the test
  fails.

## Examples

``` r
x <- structure(
  list(a = 1),
  class = c("another_class", "custom_df", "data.frame")
)

args <- list(
  classes = list(
    all = c("custom_df", "data.frame"),
    none = "matrix"
  ),
  # Must inherit from both custom_df and data.frame, and not matrix (will pass)
  tests_char = list(n_na = 0, n_dup = 0),
  # Class names vector must contain no NAs or duplicates (will pass)
  how = "class",         # Extract class vector via `class(x)` (will pass)
  sentinels = c("null"), # Allow NULL class attribute (not the case of x)
  custom = \(x) has_dim(x)
  # Object must have a dim() value (will fail)
)

do.call(test_class, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_class, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_class()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : class must be a non-empty no-na character vector.
#> ✔ (pass) classes: class must satisfy class inheritance constraints.
#> ✔ (pass) tests_char: class must pass the specified character tests.
#> ✖ (fail) custom: must pass a custom test. Did not.
#> 
#> ℹ See `predicater::assert_class()` and this condition's `rs_assert_error`
#>   attribute for details.
```

## On this page

Test if an object inherits from specific classes or has a valid class
vector.

Invalid classes fail the test: non-character vectors, empty character
vectors, or a vector with `NA` values.

`test_class()` is the predicate test, while `assert_class()` validates
its input, aborting if it fails the test.

## Usage

``` r
test_class(
  x,
  classes = NULL,
  tests_char = NULL,
  how = "class",
  sentinels = NULL,
  custom = NULL
)

assert_class(
  x,
  classes = NULL,
  tests_char = NULL,
  how = "class",
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

- classes:

  \[[`list()`](https://rdrr.io/r/base/list.html) \|
  [`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\] A
  named list specifying possible class inheritance criteria. The
  elements are the classes to test against, and the names are which test
  to do: `"any"` for
  [`rlang::inherits_any()`](https://rlang.r-lib.org/reference/inherits_any.html),
  `"all"` for
  [`rlang::inherits_all()`](https://rlang.r-lib.org/reference/inherits_any.html),
  `"only"` for
  [`rlang::inherits_only()`](https://rlang.r-lib.org/reference/inherits_any.html),
  and `"none"` for `!inherits_any()`. If any of the test passes, the
  overall test passes. If a single character, it is tested with
  `inherits_any()`. Set to `NULL` to not test.

- tests_char:

  \[`list`\] A list of additional character tests passed to
  [`test_character()`](test_character.md).

- how:

  \[`"class"` \| `"x"` \| `"attr"`\] How to extract class names for
  `tests_char`: `"x"` for `x` directly; `"class"` for
  [`class()`](https://rdrr.io/r/base/class.html); and `"attr"` for
  `attr(x, "class")`.

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

- \[`TRUE` \| `FALSE`\] for `test_class()`.

- \[`=x`\] `invisible(x)` for `assert_class()`, or aborts if the test
  fails.

## Examples

``` r
x <- structure(
  list(a = 1),
  class = c("another_class", "custom_df", "data.frame")
)

args <- list(
  classes = list(
    all = c("custom_df", "data.frame"),
    none = "matrix"
  ),
  # Must inherit from both custom_df and data.frame, and not matrix (will pass)
  tests_char = list(n_na = 0, n_dup = 0),
  # Class names vector must contain no NAs or duplicates (will pass)
  how = "class",         # Extract class vector via `class(x)` (will pass)
  sentinels = c("null"), # Allow NULL class attribute (not the case of x)
  custom = \(x) has_dim(x)
  # Object must have a dim() value (will fail)
)

do.call(test_class, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE

try(do.call(assert_class, c(list(x), args, short_circuit = FALSE))) #> Error
#> Error in eval(expr, envir) : `x` failed `assert_class()`:
#> ✔ (pass) sentinels: no sentinel values allowed.
#> ✔ (pass) type  : class must be a non-empty no-na character vector.
#> ✔ (pass) classes: class must satisfy class inheritance constraints.
#> ✔ (pass) tests_char: class must pass the specified character tests.
#> ✖ (fail) custom: must pass a custom test. Did not.
#> 
#> ℹ See `predicater::assert_class()` and this condition's `rs_assert_error`
#>   attribute for details.
```
