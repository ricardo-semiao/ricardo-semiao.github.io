# Type checks - Integer-like values

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Check if an object can be considered integer in two different
interpretations (`mode`s):

- `"unbounded"`: checks if `x` can be represented as a double-precision
  integer, i.e. `x - round(x)` falls within some tolerance value
  (`tol`). Allows `Inf` and `NaN` values. If so, it can be
  [`round()`](https://rdrr.io/r/base/Round.html)-ded without loss of
  information.

- `"range"`: checks if `x` can be represented as an integer, i.e. passes
  'unbounded' and is within R's allowed integer range. Disallows `Inf`
  and `NaN`. If so, it can be coerced `as.integer(round(x))` without
  losing information.

- Note that `tol` can be set to zero, for a strict check of the decimal
  part.

`are_integer_like()` is vectorized, returning a vector of same length as
`x`, and errors for non-numeric objects. `is_integer_like()` returns
`FALSE` for non-numeric objects, or if not all elements pass
`are_integer_like()`, and `TRUE` otherwise.

## Usage

``` r
are_integer_like(x, mode = "bounded", tol = 0, na = TRUE)

is_integer_like(x, n = NULL, mode = "bounded", tol = 0, na = TRUE)
```

## Arguments

- x:

  \[`any`\] An object to test.

- mode:

  \[`"bounded"` \| `"unbounded"`\] The mode of integer interpretation as
  described above.

- tol:

  \[`double(1)`\] The tolerance for the `"trunc_tol"` and `"range_tol"`
  modes, ignored in other modes. A useful value is
  `sqrt(.Machine$double.eps)`.

- na:

  \[`TRUE` \| `NA`\] What to return for `NA` values. Integer vectors
  always return `TRUE` for `NA` values.

- n:

  \[`integer(1)` \| `NULL`\] Length of `x`, set to `NULL` to not test.

## Value

- \[`logical(length(x))`\] For `are_integer_like()`: the vectorized or
  result of the test.

- \[`TRUE` \| `FALSE` \| `NA`\] For `is_integer_like()`: the scalar
  result of the test. If `na != NA`, then will always return `TRUE` or
  `FALSE`.

## Details

R stores integers with 32 bits, allowing to represent values between
about \\\pm 2 \times 10^9\\ (see `.Machine$integer.max` for the exact
value). Doubles and doubles use the 'binary64' format allowing to
represent values between about \\\pm 1.8 \times 10^{308}\\ (see
`.Machine[c("double.xmin", "double.xmax")]` for the exact value). Thus,
not all zero-decimal doubles can be coerced into integers, which is the
distinction between the `"trunc"` and `"range"` modes.

Note that the mathematical `Inf` and `NaN` concepts exist for integers,
but they cannot be coerced into
[`integer()`](https://rdrr.io/r/base/integer.html) in R; that's why they
are allowed in the `"trunc"` modes and not in `"range"` modes.

Philosophically, for ``` NA`` values, consider:  ```na =
TRUE`as "yes,`NA_real\_`can safely be coerced to`NA_integer\_`"; and `na
=
NA`as "this NA value might have a decimal part, so I don't know if I can consider it an integer". Note that with integer vectors, NA values are surely integers, so they always return`TRUE\`.

## Examples

``` r
x <- c(1.0, NA, 1.0 + 1e-15, 1.0 + 1e-6, NaN, -Inf, 1e200)

# Default test:
are_integer_like(x)
#> [1]  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE
#> c(TRUE, TRUE, FALSE, FALSE, FALSE, FALSE, FALSE)
# By default, NA_real_ values are considered integer-like, since can be
# coerced to NA_integer_

# is_integer_like only returns TRUE if are_integer_like() is all TRUE:
is_integer_like(x) #> FALSE
#> [1] FALSE

# Objects that don't pass is_integer_like() will generate NAs or loss of
# precision when coerced:
suppressWarnings(as.integer(round(x))) #> c(1L, NA, 1L, 1L, NA, NA, NA)
#> [1]  1 NA  1  1 NA NA NA

# Changing NA interpretation:
are_integer_like(x, na = NA)
#> [1]  TRUE    NA FALSE FALSE FALSE FALSE FALSE
#> c(TRUE, NA, FALSE, FALSE, FALSE, FALSE, FALSE)

# Adding tolerance:
are_integer_like(x, tol = sqrt(.Machine$double.eps))
#> [1]  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE
#> c(TRUE, TRUE, TRUE, FALSE, FALSE, FALSE, FALSE)

# Decreasing tolerance:
are_integer_like(x, tol = 1e-5)
#> [1]  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE
#> c(TRUE, TRUE, TRUE, TRUE, FALSE, FALSE, FALSE)

# unbounded mode allows Inf, NaN, and out-of-integer-range values:
are_integer_like(x, mode = "unbounded")
#> [1]  TRUE  TRUE FALSE FALSE  TRUE  TRUE  TRUE
#> c(TRUE, TRUE, FALSE, FALSE, TRUE, TRUE, TRUE)

# Adding tolerance, all pass, and finally is_integer_like() retursn TRUE:
are_integer_like(x, mode = "unbounded", tol = 1e-5)
#> [1] TRUE TRUE TRUE TRUE TRUE TRUE TRUE
#> c(TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE)

is_integer_like(x, mode = "unbounded", tol = 1e-5) #> TRUE
#> [1] TRUE


# are_integer_like() fails for non-numeric objects, while is_integer_like()
# returns FALSE:
try(are_integer_like(list(1L, 2L))) #> Error
#> Error in round(x) : non-numeric argument to mathematical function
is_integer_like(list(1L, 2L)) #> FALSE
#> [1] FALSE

# To test for a single integer-like value, use the n argument:
is_integer_like(1L, n = 1) #> TRUE
#> [1] TRUE
is_integer_like(1:2, n = 1) #> FALSE
#> [1] FALSE


# Integer vectors always return TRUE for NA values:
are_integer_like(c(1L, NA_integer_), na = NA) #> c(TRUE, TRUE)
#> [1] TRUE TRUE
```

## On this page

Check if an object can be considered integer in two different
interpretations (`mode`s):

- `"unbounded"`: checks if `x` can be represented as a double-precision
  integer, i.e. `x - round(x)` falls within some tolerance value
  (`tol`). Allows `Inf` and `NaN` values. If so, it can be
  [`round()`](https://rdrr.io/r/base/Round.html)-ded without loss of
  information.

- `"range"`: checks if `x` can be represented as an integer, i.e. passes
  'unbounded' and is within R's allowed integer range. Disallows `Inf`
  and `NaN`. If so, it can be coerced `as.integer(round(x))` without
  losing information.

- Note that `tol` can be set to zero, for a strict check of the decimal
  part.

`are_integer_like()` is vectorized, returning a vector of same length as
`x`, and errors for non-numeric objects. `is_integer_like()` returns
`FALSE` for non-numeric objects, or if not all elements pass
`are_integer_like()`, and `TRUE` otherwise.

## Usage

``` r
are_integer_like(x, mode = "bounded", tol = 0, na = TRUE)

is_integer_like(x, n = NULL, mode = "bounded", tol = 0, na = TRUE)
```

## Arguments

- x:

  \[`any`\] An object to test.

- mode:

  \[`"bounded"` \| `"unbounded"`\] The mode of integer interpretation as
  described above.

- tol:

  \[`double(1)`\] The tolerance for the `"trunc_tol"` and `"range_tol"`
  modes, ignored in other modes. A useful value is
  `sqrt(.Machine$double.eps)`.

- na:

  \[`TRUE` \| `NA`\] What to return for `NA` values. Integer vectors
  always return `TRUE` for `NA` values.

- n:

  \[`integer(1)` \| `NULL`\] Length of `x`, set to `NULL` to not test.

## Value

- \[`logical(length(x))`\] For `are_integer_like()`: the vectorized or
  result of the test.

- \[`TRUE` \| `FALSE` \| `NA`\] For `is_integer_like()`: the scalar
  result of the test. If `na != NA`, then will always return `TRUE` or
  `FALSE`.

## Details

R stores integers with 32 bits, allowing to represent values between
about \\\pm 2 \times 10^9\\ (see `.Machine$integer.max` for the exact
value). Doubles and doubles use the 'binary64' format allowing to
represent values between about \\\pm 1.8 \times 10^{308}\\ (see
`.Machine[c("double.xmin", "double.xmax")]` for the exact value). Thus,
not all zero-decimal doubles can be coerced into integers, which is the
distinction between the `"trunc"` and `"range"` modes.

Note that the mathematical `Inf` and `NaN` concepts exist for integers,
but they cannot be coerced into
[`integer()`](https://rdrr.io/r/base/integer.html) in R; that's why they
are allowed in the `"trunc"` modes and not in `"range"` modes.

Philosophically, for ``` NA`` values, consider:  ```na =
TRUE`as "yes,`NA_real\_`can safely be coerced to`NA_integer\_`"; and `na
=
NA`as "this NA value might have a decimal part, so I don't know if I can consider it an integer". Note that with integer vectors, NA values are surely integers, so they always return`TRUE\`.

## Examples

``` r
x <- c(1.0, NA, 1.0 + 1e-15, 1.0 + 1e-6, NaN, -Inf, 1e200)

# Default test:
are_integer_like(x)
#> [1]  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE
#> c(TRUE, TRUE, FALSE, FALSE, FALSE, FALSE, FALSE)
# By default, NA_real_ values are considered integer-like, since can be
# coerced to NA_integer_

# is_integer_like only returns TRUE if are_integer_like() is all TRUE:
is_integer_like(x) #> FALSE
#> [1] FALSE

# Objects that don't pass is_integer_like() will generate NAs or loss of
# precision when coerced:
suppressWarnings(as.integer(round(x))) #> c(1L, NA, 1L, 1L, NA, NA, NA)
#> [1]  1 NA  1  1 NA NA NA

# Changing NA interpretation:
are_integer_like(x, na = NA)
#> [1]  TRUE    NA FALSE FALSE FALSE FALSE FALSE
#> c(TRUE, NA, FALSE, FALSE, FALSE, FALSE, FALSE)

# Adding tolerance:
are_integer_like(x, tol = sqrt(.Machine$double.eps))
#> [1]  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE
#> c(TRUE, TRUE, TRUE, FALSE, FALSE, FALSE, FALSE)

# Decreasing tolerance:
are_integer_like(x, tol = 1e-5)
#> [1]  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE
#> c(TRUE, TRUE, TRUE, TRUE, FALSE, FALSE, FALSE)

# unbounded mode allows Inf, NaN, and out-of-integer-range values:
are_integer_like(x, mode = "unbounded")
#> [1]  TRUE  TRUE FALSE FALSE  TRUE  TRUE  TRUE
#> c(TRUE, TRUE, FALSE, FALSE, TRUE, TRUE, TRUE)

# Adding tolerance, all pass, and finally is_integer_like() retursn TRUE:
are_integer_like(x, mode = "unbounded", tol = 1e-5)
#> [1] TRUE TRUE TRUE TRUE TRUE TRUE TRUE
#> c(TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE)

is_integer_like(x, mode = "unbounded", tol = 1e-5) #> TRUE
#> [1] TRUE


# are_integer_like() fails for non-numeric objects, while is_integer_like()
# returns FALSE:
try(are_integer_like(list(1L, 2L))) #> Error
#> Error in round(x) : non-numeric argument to mathematical function
is_integer_like(list(1L, 2L)) #> FALSE
#> [1] FALSE

# To test for a single integer-like value, use the n argument:
is_integer_like(1L, n = 1) #> TRUE
#> [1] TRUE
is_integer_like(1:2, n = 1) #> FALSE
#> [1] FALSE


# Integer vectors always return TRUE for NA values:
are_integer_like(c(1L, NA_integer_), na = NA) #> c(TRUE, TRUE)
#> [1] TRUE TRUE
```
