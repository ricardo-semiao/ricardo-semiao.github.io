# Parallel any and all

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

These functions are wrappers around
[`vctrs::vec_pany()`](https://vctrs.r-lib.org/reference/parallel-operators.html)
and
[`vctrs::vec_pall()`](https://vctrs.r-lib.org/reference/parallel-operators.html),
variants of [`any()`](https://rdrr.io/r/base/any.html) and
[`all()`](https://rdrr.io/r/base/all.html) that work in parallel on
multiple inputs at once. They work similarly to how
[`pmin()`](https://rdrr.io/r/base/Extremes.html) and
[`pmax()`](https://rdrr.io/r/base/Extremes.html) are parallel variants
of [`min()`](https://rdrr.io/r/base/Extremes.html) and
[`max()`](https://rdrr.io/r/base/Extremes.html).

`pany_na()` and `pall_na()` are variants that check for `NA` values in
parallel.

## Usage

``` r
pany(..., .na = NA)

pall(..., .na = NA)

pany_na(..., .nan = FALSE)

pall_na(..., .nan = FALSE)
```

## Arguments

- ...:

  \[[`logical()`](https://rdrr.io/r/base/logical.html) each\] Logical
  vectors with the same size.

- .na:

  \[`TRUE` \| `FALSE` \| `NA`\] What to return for `NA` values.

- .nan:

  \[`TRUE` \| `FALSE`\] Should `NaN` values be treated as `NA`?

## Value

\[[`logical()`](https://rdrr.io/r/base/logical.html)\] A logical vector
of the same size as the inputs.

## Examples

``` r
a <- c(TRUE, TRUE, TRUE, FALSE, FALSE, FALSE, NA, NA, NA)
b <- c(TRUE, FALSE, NA, TRUE, FALSE, NA, TRUE, FALSE, NA)

# Default behavior treats missings like `|` does:
pany(a, b)
#> [1]  TRUE  TRUE  TRUE  TRUE FALSE    NA  TRUE    NA    NA
a | b
#> [1]  TRUE  TRUE  TRUE  TRUE FALSE    NA  TRUE    NA    NA

# Default behavior treats missings like `&` does:
pall(a, b)
#> [1]  TRUE FALSE    NA FALSE FALSE FALSE    NA FALSE    NA
a & b
#> [1]  TRUE FALSE    NA FALSE FALSE FALSE    NA FALSE    NA

# Remove missings from the computation, like `na_rm = TRUE`:
pany(a, b, .na = FALSE)
#> [1]  TRUE  TRUE  TRUE  TRUE FALSE FALSE  TRUE FALSE FALSE
(a & !is.na(a)) | (b & !is.na(b))
#> [1]  TRUE  TRUE  TRUE  TRUE FALSE FALSE  TRUE FALSE FALSE

pall(a, b, .na = TRUE)
#> [1]  TRUE FALSE  TRUE FALSE FALSE FALSE  TRUE FALSE  TRUE
(a | is.na(a)) & (b | is.na(b))
#> [1]  TRUE FALSE  TRUE FALSE FALSE FALSE  TRUE FALSE  TRUE

# Check for missings in parallel:
pany_na(a, b) #> c(FALSE, FALSE, TRUE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE)
#> [1] FALSE FALSE  TRUE FALSE FALSE  TRUE  TRUE  TRUE  TRUE
pall_na(a, b) #> c(FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE)
#> [1] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE
```

## On this page

These functions are wrappers around
[`vctrs::vec_pany()`](https://vctrs.r-lib.org/reference/parallel-operators.html)
and
[`vctrs::vec_pall()`](https://vctrs.r-lib.org/reference/parallel-operators.html),
variants of [`any()`](https://rdrr.io/r/base/any.html) and
[`all()`](https://rdrr.io/r/base/all.html) that work in parallel on
multiple inputs at once. They work similarly to how
[`pmin()`](https://rdrr.io/r/base/Extremes.html) and
[`pmax()`](https://rdrr.io/r/base/Extremes.html) are parallel variants
of [`min()`](https://rdrr.io/r/base/Extremes.html) and
[`max()`](https://rdrr.io/r/base/Extremes.html).

`pany_na()` and `pall_na()` are variants that check for `NA` values in
parallel.

## Usage

``` r
pany(..., .na = NA)

pall(..., .na = NA)

pany_na(..., .nan = FALSE)

pall_na(..., .nan = FALSE)
```

## Arguments

- ...:

  \[[`logical()`](https://rdrr.io/r/base/logical.html) each\] Logical
  vectors with the same size.

- .na:

  \[`TRUE` \| `FALSE` \| `NA`\] What to return for `NA` values.

- .nan:

  \[`TRUE` \| `FALSE`\] Should `NaN` values be treated as `NA`?

## Value

\[[`logical()`](https://rdrr.io/r/base/logical.html)\] A logical vector
of the same size as the inputs.

## Examples

``` r
a <- c(TRUE, TRUE, TRUE, FALSE, FALSE, FALSE, NA, NA, NA)
b <- c(TRUE, FALSE, NA, TRUE, FALSE, NA, TRUE, FALSE, NA)

# Default behavior treats missings like `|` does:
pany(a, b)
#> [1]  TRUE  TRUE  TRUE  TRUE FALSE    NA  TRUE    NA    NA
a | b
#> [1]  TRUE  TRUE  TRUE  TRUE FALSE    NA  TRUE    NA    NA

# Default behavior treats missings like `&` does:
pall(a, b)
#> [1]  TRUE FALSE    NA FALSE FALSE FALSE    NA FALSE    NA
a & b
#> [1]  TRUE FALSE    NA FALSE FALSE FALSE    NA FALSE    NA

# Remove missings from the computation, like `na_rm = TRUE`:
pany(a, b, .na = FALSE)
#> [1]  TRUE  TRUE  TRUE  TRUE FALSE FALSE  TRUE FALSE FALSE
(a & !is.na(a)) | (b & !is.na(b))
#> [1]  TRUE  TRUE  TRUE  TRUE FALSE FALSE  TRUE FALSE FALSE

pall(a, b, .na = TRUE)
#> [1]  TRUE FALSE  TRUE FALSE FALSE FALSE  TRUE FALSE  TRUE
(a | is.na(a)) & (b | is.na(b))
#> [1]  TRUE FALSE  TRUE FALSE FALSE FALSE  TRUE FALSE  TRUE

# Check for missings in parallel:
pany_na(a, b) #> c(FALSE, FALSE, TRUE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE)
#> [1] FALSE FALSE  TRUE FALSE FALSE  TRUE  TRUE  TRUE  TRUE
pall_na(a, b) #> c(FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE)
#> [1] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE
```
