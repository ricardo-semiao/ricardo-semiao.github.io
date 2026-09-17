# Data checks - Check if object is ordered

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

This function is a wrapper around
[`is.unsorted()`](https://rdrr.io/r/base/is.unsorted.html) to check if a
vector is sorted in ascending or descending order.

## Usage

``` r
is_sorted(x, order = "asc", na.rm = FALSE, strictly = FALSE)
```

## Arguments

- x:

  \[`atomic`\] An atomic vector to test.

- order:

  \[`"asc"` \| `"desc"`\] The order to check for: `"asc"` for ascending,
  `"desc"` for descending.

- na.rm:

  \[`TRUE` \| `FALSE`\] If `TRUE`, `NA` values are removed before
  checking for order. If `FALSE`, `NA` values propagate and imply in an
  `NA` result.

- strictly:

  \[`TRUE` \| `FALSE`\] If `TRUE`, the function checks for strict order,
  meaning that no two elements can be equal.

## Value

\[`TRUE` \| `FALSE` \| `NA`\] The scalar result of the test.. If
`na.rm = TRUE`, the result is always `TRUE` or `FALSE`.

## Examples

``` r
# Control the order of the check with `order` argument
is_sorted(1:5) #> TRUE
#> [1] TRUE
is_sorted(1:5, order = "desc") #> FALSE
#> [1] FALSE

# Control the handling of NA values with `na.rm` argument:
is_sorted(c(1, 2, NA, 4), na.rm = TRUE) #> TRUE
#> [1] TRUE

# Control the strictness of the order with `strictly` argument:
is_sorted(c(1, 2, 2, 4), strictly = TRUE) #> FALSE
#> [1] FALSE
```

## On this page

This function is a wrapper around
[`is.unsorted()`](https://rdrr.io/r/base/is.unsorted.html) to check if a
vector is sorted in ascending or descending order.

## Usage

``` r
is_sorted(x, order = "asc", na.rm = FALSE, strictly = FALSE)
```

## Arguments

- x:

  \[`atomic`\] An atomic vector to test.

- order:

  \[`"asc"` \| `"desc"`\] The order to check for: `"asc"` for ascending,
  `"desc"` for descending.

- na.rm:

  \[`TRUE` \| `FALSE`\] If `TRUE`, `NA` values are removed before
  checking for order. If `FALSE`, `NA` values propagate and imply in an
  `NA` result.

- strictly:

  \[`TRUE` \| `FALSE`\] If `TRUE`, the function checks for strict order,
  meaning that no two elements can be equal.

## Value

\[`TRUE` \| `FALSE` \| `NA`\] The scalar result of the test.. If
`na.rm = TRUE`, the result is always `TRUE` or `FALSE`.

## Examples

``` r
# Control the order of the check with `order` argument
is_sorted(1:5) #> TRUE
#> [1] TRUE
is_sorted(1:5, order = "desc") #> FALSE
#> [1] FALSE

# Control the handling of NA values with `na.rm` argument:
is_sorted(c(1, 2, NA, 4), na.rm = TRUE) #> TRUE
#> [1] TRUE

# Control the strictness of the order with `strictly` argument:
is_sorted(c(1, 2, 2, 4), strictly = TRUE) #> FALSE
#> [1] FALSE
```
