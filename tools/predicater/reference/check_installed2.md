# Check if user accepted a package installation

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

This function returns `TRUE` if `pkg` is already installed, and prompt
the user to install it otherwise. If the user accepts, returns `TRUE`,
and `FALSE` if he rejects. This is different from
[`rlang::check_installed()`](https://rlang.r-lib.org/reference/is_installed.html)
which will exit the function if the user rejects installation.

Useful for suggesting the user a more featureful path of the function,
while still allowing a fallback path.

Any installation errors, e.g. packages not found, still bubble up.

## Usage

``` r
check_installed2(
  pkg,
  reason = NULL,
  ...,
  version = NULL,
  compare = NULL,
  action = NULL,
  call = caller_env()
)
```

## Arguments

- pkg:

  The package names. Can include version requirements, e.g.
  `"pkg (>= 1.0.0)"`.

- reason:

  Optional string indicating why is `pkg` needed. Appears in error
  messages (if non-interactive) and user prompts (if interactive).

- ...:

  These dots must be empty.

- version:

  Minimum versions for `pkg`. If supplied, must be the same length as
  `pkg`. `NA` elements stand for any versions.

- compare:

  A character vector of comparison operators to use for `version`. If
  supplied, must be the same length as `version`. If `NULL`, `>=` is
  used as default for all elements. `NA` elements in `compare` are also
  set to `>=` by default.

- action:

  An optional function taking `pkg` and `...` arguments. It is called by
  `check_installed()` when the user chooses to update outdated packages.
  The function is passed the missing and outdated packages as a
  character vector of names.

- call:

  The execution environment of a currently running function, e.g.
  `caller_env()`. The function will be mentioned in error messages as
  the source of the error. See the `call` argument of
  [`abort()`](https://rlang.r-lib.org/reference/abort.html) for more
  information.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Examples

``` r
# Safely use inside functions without exiting if the package is not installed:
f <- function(x) {
  if (check_installed2("crazy_print_package")) {
    # If the package is installed or the user chooses to install it
    # Some code such as `crazy_print_package::crazy_print(x)`
  } else {
    # If the package is not installed and the user refused to install it
    print(x)
  }
}
```

## On this page

This function returns `TRUE` if `pkg` is already installed, and prompt
the user to install it otherwise. If the user accepts, returns `TRUE`,
and `FALSE` if he rejects. This is different from
[`rlang::check_installed()`](https://rlang.r-lib.org/reference/is_installed.html)
which will exit the function if the user rejects installation.

Useful for suggesting the user a more featureful path of the function,
while still allowing a fallback path.

Any installation errors, e.g. packages not found, still bubble up.

## Usage

``` r
check_installed2(
  pkg,
  reason = NULL,
  ...,
  version = NULL,
  compare = NULL,
  action = NULL,
  call = caller_env()
)
```

## Arguments

- pkg:

  The package names. Can include version requirements, e.g.
  `"pkg (>= 1.0.0)"`.

- reason:

  Optional string indicating why is `pkg` needed. Appears in error
  messages (if non-interactive) and user prompts (if interactive).

- ...:

  These dots must be empty.

- version:

  Minimum versions for `pkg`. If supplied, must be the same length as
  `pkg`. `NA` elements stand for any versions.

- compare:

  A character vector of comparison operators to use for `version`. If
  supplied, must be the same length as `version`. If `NULL`, `>=` is
  used as default for all elements. `NA` elements in `compare` are also
  set to `>=` by default.

- action:

  An optional function taking `pkg` and `...` arguments. It is called by
  `check_installed()` when the user chooses to update outdated packages.
  The function is passed the missing and outdated packages as a
  character vector of names.

- call:

  The execution environment of a currently running function, e.g.
  `caller_env()`. The function will be mentioned in error messages as
  the source of the error. See the `call` argument of
  [`abort()`](https://rlang.r-lib.org/reference/abort.html) for more
  information.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Examples

``` r
# Safely use inside functions without exiting if the package is not installed:
f <- function(x) {
  if (check_installed2("crazy_print_package")) {
    # If the package is installed or the user chooses to install it
    # Some code such as `crazy_print_package::crazy_print(x)`
  } else {
    # If the package is not installed and the user refused to install it
    print(x)
  }
}
```
