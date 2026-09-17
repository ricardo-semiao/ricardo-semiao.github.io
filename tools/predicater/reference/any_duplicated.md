# Data checks - Check for duplicate values

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

- `any_duplicated`: is identical to
  [`vctrs::vec_duplicate_any()`](https://vctrs.r-lib.org/reference/vec_duplicate.html),
  and detects the presence of duplicated values, similar to
  [`anyDuplicated()`](https://rdrr.io/r/base/duplicated.html).

- `are_duplicated()` is identical to
  [`vctrs::vec_duplicate_detect()`](https://vctrs.r-lib.org/reference/vec_duplicate.html),
  and returns a logical vector describing if each element of the vector
  is duplicated elsewhere. Unlike duplicated(), it reports all
  duplicated values, not just the second and subsequent repetitions.

## Usage

``` r
any_duplicated(x)

are_duplicated(x)
```

## Arguments

- x:

  \[`atomic()` \| [`list()`](https://rdrr.io/r/base/list.html)\] An
  object to test.

## Value

- \[`TRUE` \| `FALSE`\] For `any_duplicated()`: the scalar result of the
  test.

- \[`logical(length(x))`\] For `are_duplicated()`: a logical vector of
  the same size as `x`, describing if each element is duplicated
  elsewhere.

## Missing values

In most cases, missing values are not considered to be equal, i.e.
`NA == NA` is not `TRUE`. This behaviour would be unappealing here, so
these functions consider all `NAs` to be equal. (Similarly, all `NaN`
are also considered to be equal.)

## Examples

``` r
any_duplicated(1:10)       #> FALSE
#> [1] FALSE
any_duplicated(c(1, 1:10)) #> TRUE
#> [1] TRUE

x <- c(10, 10, 20, 30, 30, 40)
are_duplicated(x) #> c(TRUE, TRUE, FALSE, TRUE, TRUE, FALSE)
#> [1]  TRUE  TRUE FALSE  TRUE  TRUE FALSE
duplicated(x) #> c(FALSE, TRUE, FALSE, FALSE, TRUE, FALSE)
#> [1] FALSE  TRUE FALSE FALSE  TRUE FALSE
# Note that `duplicated()` ignores the first instance of a duplicated value
```

## On this page

- `any_duplicated`: is identical to
  [`vctrs::vec_duplicate_any()`](https://vctrs.r-lib.org/reference/vec_duplicate.html),
  and detects the presence of duplicated values, similar to
  [`anyDuplicated()`](https://rdrr.io/r/base/duplicated.html).

- `are_duplicated()` is identical to
  [`vctrs::vec_duplicate_detect()`](https://vctrs.r-lib.org/reference/vec_duplicate.html),
  and returns a logical vector describing if each element of the vector
  is duplicated elsewhere. Unlike duplicated(), it reports all
  duplicated values, not just the second and subsequent repetitions.

## Usage

``` r
any_duplicated(x)

are_duplicated(x)
```

## Arguments

- x:

  \[`atomic()` \| [`list()`](https://rdrr.io/r/base/list.html)\] An
  object to test.

## Value

- \[`TRUE` \| `FALSE`\] For `any_duplicated()`: the scalar result of the
  test.

- \[`logical(length(x))`\] For `are_duplicated()`: a logical vector of
  the same size as `x`, describing if each element is duplicated
  elsewhere.

## Missing values

In most cases, missing values are not considered to be equal, i.e.
`NA == NA` is not `TRUE`. This behaviour would be unappealing here, so
these functions consider all `NAs` to be equal. (Similarly, all `NaN`
are also considered to be equal.)

## Examples

``` r
any_duplicated(1:10)       #> FALSE
#> [1] FALSE
any_duplicated(c(1, 1:10)) #> TRUE
#> [1] TRUE

x <- c(10, 10, 20, 30, 30, 40)
are_duplicated(x) #> c(TRUE, TRUE, FALSE, TRUE, TRUE, FALSE)
#> [1]  TRUE  TRUE FALSE  TRUE  TRUE FALSE
duplicated(x) #> c(FALSE, TRUE, FALSE, FALSE, TRUE, FALSE)
#> [1] FALSE  TRUE FALSE FALSE  TRUE FALSE
# Note that `duplicated()` ignores the first instance of a duplicated value
```
