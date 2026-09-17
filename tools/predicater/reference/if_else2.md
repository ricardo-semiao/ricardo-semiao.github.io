# Compare - Vectorized if-else

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

`if_else()` returns a vector filled with elements selected from `true`,
`false`, and (optionally) `na` based on the value of `condition`. It is
a type- and size-stable version of
[`ifelse()`](https://rdrr.io/r/base/ifelse.html).

## Usage

``` r
if_else2(condition, true, false, na = NULL)
```

## Arguments

- condition:

  A logical vector.

- true, false:

  Values to use for `TRUE` and `FALSE` values of `condition`.

- na:

  Values to use for `NA`.

## Value

A vector with the common type of `true`, `false`, and `na`; and the size
of `condition`. Where `condition` is `TRUE`, the result comes from
`true`, where `FALSE` it comes from `false`.

## Examples

``` r
x <- c(NA, 1:4)
if_else2(x > 2, 1, 2) #> c(NA, 2, 1, 1, 1)
#> [1] NA  2  2  1  1
if_else2(x > 2, "small", "big") #> c(NA, "big", "big", "small", "small")
#> [1] NA      "big"   "big"   "small" "small"
if_else2(x > 2, factor("small"), factor("big")) # As above but as a factor
#> [1] <NA>  big   big   small small
#> Levels: small big

y <- as.Date("2020-01-01")
if_else2(x > 2, NA, y + x) #> c(NA, "2020-01-02", "2020-01-03", NA, NA)
#> [1] NA           "2020-01-02" "2020-01-03" NA           NA          
```

## On this page

`if_else()` returns a vector filled with elements selected from `true`,
`false`, and (optionally) `na` based on the value of `condition`. It is
a type- and size-stable version of
[`ifelse()`](https://rdrr.io/r/base/ifelse.html).

## Usage

``` r
if_else2(condition, true, false, na = NULL)
```

## Arguments

- condition:

  A logical vector.

- true, false:

  Values to use for `TRUE` and `FALSE` values of `condition`.

- na:

  Values to use for `NA`.

## Value

A vector with the common type of `true`, `false`, and `na`; and the size
of `condition`. Where `condition` is `TRUE`, the result comes from
`true`, where `FALSE` it comes from `false`.

## Examples

``` r
x <- c(NA, 1:4)
if_else2(x > 2, 1, 2) #> c(NA, 2, 1, 1, 1)
#> [1] NA  2  2  1  1
if_else2(x > 2, "small", "big") #> c(NA, "big", "big", "small", "small")
#> [1] NA      "big"   "big"   "small" "small"
if_else2(x > 2, factor("small"), factor("big")) # As above but as a factor
#> [1] <NA>  big   big   small small
#> Levels: small big

y <- as.Date("2020-01-01")
if_else2(x > 2, NA, y + x) #> c(NA, "2020-01-02", "2020-01-03", NA, NA)
#> [1] NA           "2020-01-02" "2020-01-03" NA           NA          
```
