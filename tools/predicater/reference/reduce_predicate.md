# Reduce binary predicate over a list

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

This function applies a binary predicate function `.f` over a list `.l`,
checking if the result is `TRUE` for any or all ordered pairs within
`.l`.

`accumulate_predicate()` is similar, but returns a logical vector of the
accumulated results of the tests.

## Usage

``` r
reduce_predicate(.l, .f, ..., .op = "or")

accumulate_predicate(.l, .f, ..., .op = "or")
```

## Arguments

- .l:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] A list of objects to
  compare.

- .f:

  \[`function()`\] A binary predicate function, that uses their first
  two arguments for the operation, and returns a single `TRUE` or
  `FALSE`.

- ...:

  Additional arguments passed to `.f`.

- .op:

  \[`"or"` \| `"and"`\] Whether to check if the predicate is `TRUE` for
  any or any or all ordered pairs within `.l`.

## Value

- \[`TRUE` \| `FALSE` \| `NA`\] For `reduce_predicate()`: the scalar
  reduced result.

- \[`logical(length(.l) - 1)`\] For `accumulate_predicate()`: the
  accumulated results.

## Examples

``` r
reduce_predicate(list(1L, 1.0, 3), `==`, .op = "or") #> TRUE
#> [1] TRUE
reduce_predicate(list(1L, 1.0, 3), `==`, .op = "and") #> FALSE
#> [1] FALSE

accumulate_predicate(list(1L, 1.0, 3), `==`, .op = "and") #> c(TRUE, FALSE)
#> [1]  TRUE FALSE
accumulate_predicate(list(1L, 1.0, 3), identical, .op = "and") #> c(FALSE, FALSE)
#> [1] FALSE FALSE
```

## On this page

This function applies a binary predicate function `.f` over a list `.l`,
checking if the result is `TRUE` for any or all ordered pairs within
`.l`.

`accumulate_predicate()` is similar, but returns a logical vector of the
accumulated results of the tests.

## Usage

``` r
reduce_predicate(.l, .f, ..., .op = "or")

accumulate_predicate(.l, .f, ..., .op = "or")
```

## Arguments

- .l:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] A list of objects to
  compare.

- .f:

  \[`function()`\] A binary predicate function, that uses their first
  two arguments for the operation, and returns a single `TRUE` or
  `FALSE`.

- ...:

  Additional arguments passed to `.f`.

- .op:

  \[`"or"` \| `"and"`\] Whether to check if the predicate is `TRUE` for
  any or any or all ordered pairs within `.l`.

## Value

- \[`TRUE` \| `FALSE` \| `NA`\] For `reduce_predicate()`: the scalar
  reduced result.

- \[`logical(length(.l) - 1)`\] For `accumulate_predicate()`: the
  accumulated results.

## Examples

``` r
reduce_predicate(list(1L, 1.0, 3), `==`, .op = "or") #> TRUE
#> [1] TRUE
reduce_predicate(list(1L, 1.0, 3), `==`, .op = "and") #> FALSE
#> [1] FALSE

accumulate_predicate(list(1L, 1.0, 3), `==`, .op = "and") #> c(TRUE, FALSE)
#> [1]  TRUE FALSE
accumulate_predicate(list(1L, 1.0, 3), identical, .op = "and") #> c(FALSE, FALSE)
#> [1] FALSE FALSE
```
