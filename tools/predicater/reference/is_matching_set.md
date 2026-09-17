# Data checks - Check if object is in (and/or not in) a set

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

This function checks if an object is in a set of values, and optionally
if it is not in another set of values. It can check if all, any, or only
the values are in the set.

## Usage

``` r
is_matching_set(x, yes = NULL, no = NULL, mode = "all")
```

## Arguments

- x:

  \[`atomic` \| [`list()`](https://rdrr.io/r/base/list.html)\] An atomic
  vector or list to test.

- yes, no:

  \[`atomic` \| [`list()`](https://rdrr.io/r/base/list.html) \| `NULL`\]
  A set of values that `x` should be in, and not be in, respectively. If
  `NULL`, this check is ignored.

- mode:

  \[`"all"` \| `"any"` \| `"only"`\] The mode of the check: `"all"` for
  all values in `x` must be in `yes`, `"any"` for at least one value in
  `x` must be in `yes`, and `"only"` for all values in `x` must be in
  `yes` and all values in `yes` must be in `x`.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Examples

``` r
x <- c(5, 7, 5, 9, 9)

# Default mode checks if all values in `x` are in `yes` and not in `no`:
is_matching_set(x, yes = 1:10) #> TRUE
#> [1] TRUE
is_matching_set(x, yes = 1:8) #> FALSE
#> [1] FALSE
is_matching_set(x, yes = 1:10, no = 5) #> FALSE
#> [1] FALSE

# Mode `any` passes even if there are values in `x` that are not in `yes`:
is_matching_set(x, yes = 1:6, mode = "any") #> TRUE
#> [1] TRUE

# For mode `only`, all values in `x` must be in `yes` and vice versa:
is_matching_set(x, yes = 1:10, mode = "only") #> FALSE
#> [1] FALSE
is_matching_set(x, yes = c(5, 7, 9), mode = "only") #> TRUE
#> [1] TRUE

# `yes` can be NULL to test only `no` (independent of mode):
is_matching_set(x, no = 11) #> TRUE
#> [1] TRUE
is_matching_set(x) #> TRUE
#> [1] TRUE
```

## On this page

This function checks if an object is in a set of values, and optionally
if it is not in another set of values. It can check if all, any, or only
the values are in the set.

## Usage

``` r
is_matching_set(x, yes = NULL, no = NULL, mode = "all")
```

## Arguments

- x:

  \[`atomic` \| [`list()`](https://rdrr.io/r/base/list.html)\] An atomic
  vector or list to test.

- yes, no:

  \[`atomic` \| [`list()`](https://rdrr.io/r/base/list.html) \| `NULL`\]
  A set of values that `x` should be in, and not be in, respectively. If
  `NULL`, this check is ignored.

- mode:

  \[`"all"` \| `"any"` \| `"only"`\] The mode of the check: `"all"` for
  all values in `x` must be in `yes`, `"any"` for at least one value in
  `x` must be in `yes`, and `"only"` for all values in `x` must be in
  `yes` and all values in `yes` must be in `x`.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Examples

``` r
x <- c(5, 7, 5, 9, 9)

# Default mode checks if all values in `x` are in `yes` and not in `no`:
is_matching_set(x, yes = 1:10) #> TRUE
#> [1] TRUE
is_matching_set(x, yes = 1:8) #> FALSE
#> [1] FALSE
is_matching_set(x, yes = 1:10, no = 5) #> FALSE
#> [1] FALSE

# Mode `any` passes even if there are values in `x` that are not in `yes`:
is_matching_set(x, yes = 1:6, mode = "any") #> TRUE
#> [1] TRUE

# For mode `only`, all values in `x` must be in `yes` and vice versa:
is_matching_set(x, yes = 1:10, mode = "only") #> FALSE
#> [1] FALSE
is_matching_set(x, yes = c(5, 7, 9), mode = "only") #> TRUE
#> [1] TRUE

# `yes` can be NULL to test only `no` (independent of mode):
is_matching_set(x, no = 11) #> TRUE
#> [1] TRUE
is_matching_set(x) #> TRUE
#> [1] TRUE
```
