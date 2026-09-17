# Validation - Test for one of multiple types

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

This function checks if `x` passes at least one of a set of tests. `x`
is allowed to be any type
[`typeof()`](https://rdrr.io/r/base/typeof.html) in `types`, and needs
to pass the corresponding test for its type.

For example, if `x` is of type `"integer"`, then it is tested with
[`test_integer()`](tests-numeric.md). Pass a list of arguments to the
test function via `...`, with the same argument name as the type. E.g.
`integer = list(len = 2)`.

## Usage

``` r
test_multiple(x, types, ...)
```

## Arguments

- x:

  \[`any`\] An object to test.

- types:

  \[[`character()`](https://rdrr.io/r/base/character.html)\] A character
  vector of types to check against.

- ...:

  \[[`list()`](https://rdrr.io/r/base/list.html) each\] Lists of
  arguments to pass to the test function for each type. The list names

## Value

- \[`TRUE` \| `FALSE`\] for `test_multi()`.

- \[`=x`\] `invisible(x)` for `assert_multi()`, or aborts if the test
  fails.

## Examples

``` r
x <- list(a = 1:2, b = 3:4)

args <- list(
  types = c("integer", "list"),
  list = list(
    custom_map = \(elt) is_integer(elt, 1)
  )
  # Either a integer vector of a list of integer scalars
)

do.call(test_multiple, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE
```

## On this page

This function checks if `x` passes at least one of a set of tests. `x`
is allowed to be any type
[`typeof()`](https://rdrr.io/r/base/typeof.html) in `types`, and needs
to pass the corresponding test for its type.

For example, if `x` is of type `"integer"`, then it is tested with
[`test_integer()`](tests-numeric.md). Pass a list of arguments to the
test function via `...`, with the same argument name as the type. E.g.
`integer = list(len = 2)`.

## Usage

``` r
test_multiple(x, types, ...)
```

## Arguments

- x:

  \[`any`\] An object to test.

- types:

  \[[`character()`](https://rdrr.io/r/base/character.html)\] A character
  vector of types to check against.

- ...:

  \[[`list()`](https://rdrr.io/r/base/list.html) each\] Lists of
  arguments to pass to the test function for each type. The list names

## Value

- \[`TRUE` \| `FALSE`\] for `test_multi()`.

- \[`=x`\] `invisible(x)` for `assert_multi()`, or aborts if the test
  fails.

## Examples

``` r
x <- list(a = 1:2, b = 3:4)

args <- list(
  types = c("integer", "list"),
  list = list(
    custom_map = \(elt) is_integer(elt, 1)
  )
  # Either a integer vector of a list of integer scalars
)

do.call(test_multiple, c(list(x), args)) #> FALSE (not all tests passed)
#> [1] FALSE
```
