# Type checks - Inf and NaN

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Check if an object is `Inf`, `-Inf`, `NaN`, or none of them, flexibly
dealing with `NA` values.

The `are_*()` functions are vectorized, returning a vector of the same
length as `x`, and errors for non-numeric objects. The `is_*()`
functions return `FALSE` for non-numeric objects, or if not all elements
pass the corresponding `are_*()` function, and `TRUE` otherwise.

## Usage

``` r
are_finite(x, na = NA)

is_finite(x, na = NA)

are_nan(x, na = NA)

is_nan(x, na = NA)

are_inf(x, na = NA, signs = "+-")

is_inf(x, na = NA, signs = "+-")
```

## Arguments

- x:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html), `any`\] For
  `are_*()`, a numeric vector to test; for `is_*()`, any object to test.

- na:

  \[`TRUE` \| `FALSE` \| `NA`\] What to return for `NA` values.

- signs:

  \[`character(1)`\] For `are_inf()` and `is_inf()` – which signs of
  infinity to allow: `"+"` for positive infinity, `"-"` for negative
  infinity, or `"+-"`/`"-+"` for both.

## Value

- \[`logical(length(x))`\] For `are_*`: the vectorized or result of the
  test.

- \[`TRUE` \| `FALSE` \| `NA`\] For `is_*`: the scalar result of the
  test. If `na != NA`, then will always return `TRUE` or `FALSE`.

## Details

Currently, `NaN` values can never arise from operations with `NA`
(`NA + NaN #> NA`), so treating `NaN` as `NA` via `nan = NA` is not
recommended.

## Examples

``` r
x <- c(1, Inf, -Inf, NaN, NA)

# The default tests:
are_finite(x)
#> [1]  TRUE FALSE FALSE FALSE    NA
#> c(TRUE, FALSE, FALSE, FALSE, NA)

are_inf(x)
#> [1] FALSE  TRUE  TRUE FALSE    NA
#> c(FALSE, TRUE, TRUE, FALSE, NA)

are_nan(x)
#> [1] FALSE FALSE FALSE  TRUE    NA
#> c(FALSE, FALSE, FALSE, TRUE, NA)

# For all, the NA value's result can be controlled:
are_finite(x, na = FALSE)
#> [1]  TRUE FALSE FALSE FALSE FALSE
#> c(TRUE, FALSE, FALSE, FALSE, FALSE)

are_nan(x, na = TRUE)
#> [1] FALSE FALSE FALSE  TRUE  TRUE
#> c(FALSE, FALSE, FALSE, TRUE, TRUE)

# We can consider only +Inf or -Inf:
are_inf(x, signs = "+")
#> [1] FALSE  TRUE FALSE FALSE    NA
#> c(FALSE, TRUE, FALSE, FALSE, NA)

# Errors for non-numeric objects:
try(are_finite(list(1, 2))) #> Error
#> Error in is.nan(x) : default method not implemented for type 'list'

# The is_* predicates test scalars:
is_finite(1) #> TRUE
#> [1] TRUE
is_finite(1:10) #> FALSE
#> [1] FALSE

# To get a single TRUE/FALSE result, use all(are_*(...)):
all(are_finite(1:10)) #> TRUE
#> [1] TRUE
```

## On this page

Check if an object is `Inf`, `-Inf`, `NaN`, or none of them, flexibly
dealing with `NA` values.

The `are_*()` functions are vectorized, returning a vector of the same
length as `x`, and errors for non-numeric objects. The `is_*()`
functions return `FALSE` for non-numeric objects, or if not all elements
pass the corresponding `are_*()` function, and `TRUE` otherwise.

## Usage

``` r
are_finite(x, na = NA)

is_finite(x, na = NA)

are_nan(x, na = NA)

is_nan(x, na = NA)

are_inf(x, na = NA, signs = "+-")

is_inf(x, na = NA, signs = "+-")
```

## Arguments

- x:

  \[[`numeric()`](https://rdrr.io/r/base/numeric.html), `any`\] For
  `are_*()`, a numeric vector to test; for `is_*()`, any object to test.

- na:

  \[`TRUE` \| `FALSE` \| `NA`\] What to return for `NA` values.

- signs:

  \[`character(1)`\] For `are_inf()` and `is_inf()` – which signs of
  infinity to allow: `"+"` for positive infinity, `"-"` for negative
  infinity, or `"+-"`/`"-+"` for both.

## Value

- \[`logical(length(x))`\] For `are_*`: the vectorized or result of the
  test.

- \[`TRUE` \| `FALSE` \| `NA`\] For `is_*`: the scalar result of the
  test. If `na != NA`, then will always return `TRUE` or `FALSE`.

## Details

Currently, `NaN` values can never arise from operations with `NA`
(`NA + NaN #> NA`), so treating `NaN` as `NA` via `nan = NA` is not
recommended.

## Examples

``` r
x <- c(1, Inf, -Inf, NaN, NA)

# The default tests:
are_finite(x)
#> [1]  TRUE FALSE FALSE FALSE    NA
#> c(TRUE, FALSE, FALSE, FALSE, NA)

are_inf(x)
#> [1] FALSE  TRUE  TRUE FALSE    NA
#> c(FALSE, TRUE, TRUE, FALSE, NA)

are_nan(x)
#> [1] FALSE FALSE FALSE  TRUE    NA
#> c(FALSE, FALSE, FALSE, TRUE, NA)

# For all, the NA value's result can be controlled:
are_finite(x, na = FALSE)
#> [1]  TRUE FALSE FALSE FALSE FALSE
#> c(TRUE, FALSE, FALSE, FALSE, FALSE)

are_nan(x, na = TRUE)
#> [1] FALSE FALSE FALSE  TRUE  TRUE
#> c(FALSE, FALSE, FALSE, TRUE, TRUE)

# We can consider only +Inf or -Inf:
are_inf(x, signs = "+")
#> [1] FALSE  TRUE FALSE FALSE    NA
#> c(FALSE, TRUE, FALSE, FALSE, NA)

# Errors for non-numeric objects:
try(are_finite(list(1, 2))) #> Error
#> Error in is.nan(x) : default method not implemented for type 'list'

# The is_* predicates test scalars:
is_finite(1) #> TRUE
#> [1] TRUE
is_finite(1:10) #> FALSE
#> [1] FALSE

# To get a single TRUE/FALSE result, use all(are_*(...)):
all(are_finite(1:10)) #> TRUE
#> [1] TRUE
```
