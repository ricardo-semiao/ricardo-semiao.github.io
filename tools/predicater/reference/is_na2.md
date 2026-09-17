# Type checks - NA values

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Checks if an object is `NA`, `NA_integer_`, `NA_real_`, `NA_complex_`,
or `NA_character_`. Differently from
[`is.na()`](https://rdrr.io/r/base/NA.html) and
[`rlang::is_na()`](https://rlang.r-lib.org/reference/are_na.html)/[`rlang::are_na()`](https://rlang.r-lib.org/reference/are_na.html),
it allows to control the behavior for `NaN` objects.

- `are_na2()` is vectorized, returning a vector of same length as `x`,
  and errors for non-atomic objects.

- `is_na2()` returns `FALSE` for non-atomic objects, or if not all
  elements pass `are_na2()`, and `TRUE` otherwise.

## Usage

``` r
are_na2(x, nan = FALSE)

is_na2(x, nan = FALSE, types = NULL)
```

## Arguments

- x:

  \[`any`\] An object to test.

- nan:

  \[`TRUE` \| `FALSE`\] What to return for `NaN` values.

- types:

  \[[`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\] A
  character vector of allowed `NA` types (see
  [`NA`](https://rdrr.io/r/base/NA.html)). Set to `NULL` to allow all
  types.

## Value

- \[`logical(length(x))`\] For `are_*`: the vectorized or result of the
  test.

- \[`TRUE` \| `FALSE`\] For `is_*`: the scalar result of the test.

## Examples

``` r
x <- c(1, Inf, -Inf, NaN, NA)

# are_na() is vectorized:
are_na2(x)
#> [1] FALSE FALSE FALSE FALSE  TRUE
#> c(FALSE, FALSE, FALSE, FALSE, TRUE)

are_na2(x, nan = TRUE)
#> [1] FALSE FALSE FALSE  TRUE  TRUE
#> c(FALSE, FALSE, FALSE, TRUE, TRUE)

are_na2(x, nan = NA)
#> [1] FALSE FALSE FALSE    NA  TRUE
#> c(FALSE, FALSE, FALSE, NA, TRUE)

# Errors for non-atomic objects:
try(are_na2(list(NA, NA))) #> Error
#> Error in is.nan(x) : default method not implemented for type 'list'

# is_na() test for a scalar NA value:
is_na2(c(NA, NA)) #> FALSE
#> [1] FALSE
is_na2(NA) #> TRUE
#> [1] TRUE
is_na2(NaN, nan = TRUE) #> TRUE
#> [1] TRUE

# Use all(are_na2(x)) to test if all elements are NA:
all(are_na2(c(NA, NA))) #> TRUE
#> [1] TRUE

# Accept only NAs of specific types:
is_na2(NA_integer_, types = c("logical", "character")) #> FALSE 
#> [1] FALSE

# To test for a single NA value, use the n argument:
is_na2(NA, n = 1) #> TRUE
#> [1] TRUE
```

## On this page

Checks if an object is `NA`, `NA_integer_`, `NA_real_`, `NA_complex_`,
or `NA_character_`. Differently from
[`is.na()`](https://rdrr.io/r/base/NA.html) and
[`rlang::is_na()`](https://rlang.r-lib.org/reference/are_na.html)/[`rlang::are_na()`](https://rlang.r-lib.org/reference/are_na.html),
it allows to control the behavior for `NaN` objects.

- `are_na2()` is vectorized, returning a vector of same length as `x`,
  and errors for non-atomic objects.

- `is_na2()` returns `FALSE` for non-atomic objects, or if not all
  elements pass `are_na2()`, and `TRUE` otherwise.

## Usage

``` r
are_na2(x, nan = FALSE)

is_na2(x, nan = FALSE, types = NULL)
```

## Arguments

- x:

  \[`any`\] An object to test.

- nan:

  \[`TRUE` \| `FALSE`\] What to return for `NaN` values.

- types:

  \[[`character()`](https://rdrr.io/r/base/character.html) \| `NULL`\] A
  character vector of allowed `NA` types (see
  [`NA`](https://rdrr.io/r/base/NA.html)). Set to `NULL` to allow all
  types.

## Value

- \[`logical(length(x))`\] For `are_*`: the vectorized or result of the
  test.

- \[`TRUE` \| `FALSE`\] For `is_*`: the scalar result of the test.

## Examples

``` r
x <- c(1, Inf, -Inf, NaN, NA)

# are_na() is vectorized:
are_na2(x)
#> [1] FALSE FALSE FALSE FALSE  TRUE
#> c(FALSE, FALSE, FALSE, FALSE, TRUE)

are_na2(x, nan = TRUE)
#> [1] FALSE FALSE FALSE  TRUE  TRUE
#> c(FALSE, FALSE, FALSE, TRUE, TRUE)

are_na2(x, nan = NA)
#> [1] FALSE FALSE FALSE    NA  TRUE
#> c(FALSE, FALSE, FALSE, NA, TRUE)

# Errors for non-atomic objects:
try(are_na2(list(NA, NA))) #> Error
#> Error in is.nan(x) : default method not implemented for type 'list'

# is_na() test for a scalar NA value:
is_na2(c(NA, NA)) #> FALSE
#> [1] FALSE
is_na2(NA) #> TRUE
#> [1] TRUE
is_na2(NaN, nan = TRUE) #> TRUE
#> [1] TRUE

# Use all(are_na2(x)) to test if all elements are NA:
all(are_na2(c(NA, NA))) #> TRUE
#> [1] TRUE

# Accept only NAs of specific types:
is_na2(NA_integer_, types = c("logical", "character")) #> FALSE 
#> [1] FALSE

# To test for a single NA value, use the n argument:
is_na2(NA, n = 1) #> TRUE
#> [1] TRUE
```
