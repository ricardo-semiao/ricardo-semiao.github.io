# Type checks - TRUE and FALSE values

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Check if an object is literally `TRUE` or `FALSE`, controlling for `NA`
values.
[`rlang::is_bool()`](https://rlang.r-lib.org/reference/scalar-type-predicates.html)
checks for either `TRUE` or `FALSE`.

## Usage

``` r
are_true(x, na = FALSE)

is_true2(x, na = FALSE)

are_false(x, na = FALSE)

is_false2(x, na = FALSE)

is_bool2(x, na = FALSE)
```

## Arguments

- x:

  \[[`logical()`](https://rdrr.io/r/base/logical.html), `any`\] For
  `are_*()`, a logical vector; for `is_*()`, an object to test.

- na:

  \[`FALSE` \| `NA`\] What to return for `NA` values.

## Value

- \[`logical(length(x))`\] For `are_*`: the vectorized or result of the
  test.

- \[`TRUE` \| `FALSE` \| `NA`\] For `is_*`: the scalar result of the
  test. If `na != NA`, the result is always `TRUE` or `FALSE`.

## Examples

``` r
x <- c(TRUE, FALSE, NA)

# Vectorized tests:
are_true(x)           #> c(TRUE, FALSE, FALSE)
#> [1]  TRUE FALSE FALSE
are_true(x, na = NA)  #> c(TRUE, FALSE, NA)
#> [1]  TRUE FALSE    NA
are_false(x)          #> c(FALSE, TRUE, FALSE)
#> [1] FALSE  TRUE FALSE
are_false(x, na = NA) #> c(FALSE, TRUE, NA)
#> [1] FALSE  TRUE    NA

are_true(logical(0))  #> logical(0)
#> logical(0)
try(are_true(1:3)) #> Error (only works for logical vectors)
#> Error in are_true(1:3) : `x` must be a logical vector.

# Scalar tests:
is_true2(c(TRUE, TRUE)) #> FALSE
#> [1] FALSE
is_true2(TRUE) #> TRUE
#> [1] TRUE
is_true2(NA) #> FALSE
#> [1] FALSE
is_true2(NA, na = NA) #> NA
#> [1] NA
# And similar for is_false2()

is_bool2(TRUE) #> TRUE
#> [1] TRUE
is_bool2(FALSE) #> TRUE
#> [1] TRUE
is_bool2(NA) #> FALSE
#> [1] FALSE
is_bool2(NA, na = NA) #> NA
#> [1] NA
```

## On this page

Check if an object is literally `TRUE` or `FALSE`, controlling for `NA`
values.
[`rlang::is_bool()`](https://rlang.r-lib.org/reference/scalar-type-predicates.html)
checks for either `TRUE` or `FALSE`.

## Usage

``` r
are_true(x, na = FALSE)

is_true2(x, na = FALSE)

are_false(x, na = FALSE)

is_false2(x, na = FALSE)

is_bool2(x, na = FALSE)
```

## Arguments

- x:

  \[[`logical()`](https://rdrr.io/r/base/logical.html), `any`\] For
  `are_*()`, a logical vector; for `is_*()`, an object to test.

- na:

  \[`FALSE` \| `NA`\] What to return for `NA` values.

## Value

- \[`logical(length(x))`\] For `are_*`: the vectorized or result of the
  test.

- \[`TRUE` \| `FALSE` \| `NA`\] For `is_*`: the scalar result of the
  test. If `na != NA`, the result is always `TRUE` or `FALSE`.

## Examples

``` r
x <- c(TRUE, FALSE, NA)

# Vectorized tests:
are_true(x)           #> c(TRUE, FALSE, FALSE)
#> [1]  TRUE FALSE FALSE
are_true(x, na = NA)  #> c(TRUE, FALSE, NA)
#> [1]  TRUE FALSE    NA
are_false(x)          #> c(FALSE, TRUE, FALSE)
#> [1] FALSE  TRUE FALSE
are_false(x, na = NA) #> c(FALSE, TRUE, NA)
#> [1] FALSE  TRUE    NA

are_true(logical(0))  #> logical(0)
#> logical(0)
try(are_true(1:3)) #> Error (only works for logical vectors)
#> Error in are_true(1:3) : `x` must be a logical vector.

# Scalar tests:
is_true2(c(TRUE, TRUE)) #> FALSE
#> [1] FALSE
is_true2(TRUE) #> TRUE
#> [1] TRUE
is_true2(NA) #> FALSE
#> [1] FALSE
is_true2(NA, na = NA) #> NA
#> [1] NA
# And similar for is_false2()

is_bool2(TRUE) #> TRUE
#> [1] TRUE
is_bool2(FALSE) #> TRUE
#> [1] TRUE
is_bool2(NA) #> FALSE
#> [1] FALSE
is_bool2(NA, na = NA) #> NA
#> [1] NA
```
