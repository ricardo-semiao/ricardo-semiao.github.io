# Compare - Vectorized nested if-else

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

This function allows you to vectorise multiple
[`if_else()`](https://dplyr.tidyverse.org/reference/if_else.html)
statements. Each case is evaluated sequentially and the first match for
each element determines the corresponding value in the output vector. If
no cases match, the `.default` is used as a final "else" statment.

`case_when()` is an R equivalent of the SQL "searched" `CASE WHEN`
statement.

## Usage

``` r
case_when2(.default, ..., .ptype = NULL)
```

## Arguments

- .default:

  The value used when all of the LHS inputs return either `FALSE` or
  `NA`.

  `.default` must be size 1 or the same size as the common size computed
  from `...`.

  `.default` participates in the computation of the common type with the
  RHS inputs.

  `NA` values in the LHS conditions are treated like `FALSE`, meaning
  that the result at those locations will be assigned the `.default`
  value. To handle missing values in the conditions differently, you
  must explicitly catch them with another condition before they fall
  through to the `.default`. This typically involves some variation of
  `is.na(x) ~ value` tailored to your usage of `case_when()`.

  If `NULL`, the default, a missing value will be used.

- ...:

  \<[`dynamic-dots`](https://rlang.r-lib.org/reference/dyn-dots.html)\>
  A sequence of two-sided formulas. The left hand side (LHS) determines
  which values match this case. The right hand side (RHS) provides the
  replacement value.

  The LHS inputs must evaluate to logical vectors.

  The RHS inputs will be coerced to their common type.

  All inputs will be recycled to their common size. That said, we
  encourage all LHS inputs to be the same size. Recycling is mainly
  useful for RHS inputs, where you might supply a size 1 input that will
  be recycled to the size of the LHS inputs.

  `NULL` inputs are ignored.

- .ptype:

  An optional prototype declaring the desired output type. If supplied,
  this overrides the common type of the RHS inputs.

## Value

A vector with the same size as the common size computed from the inputs
in `...` and the same type as the common type of the RHS inputs in
`...`.

## See also

[`case_match()`](https://dplyr.tidyverse.org/reference/case_match.html)

## Examples

``` r
x <- 1:10
case_when2(
  x %% 3 == 0 ~ "buzz",
  x %% 2 == 0 ~ "fizz",
  .default = as.character(x)
)
#>  [1] "1"    "fizz" "buzz" "fizz" "5"    "buzz" "7"    "fizz" "buzz" "fizz"
#> c("1", "fizz", "buzz", "fizz", "5", "buzz", "7", "fizz", "buzz", "10")

# See ?dplyr::case_when for more examples
```

## On this page

This function allows you to vectorise multiple
[`if_else()`](https://dplyr.tidyverse.org/reference/if_else.html)
statements. Each case is evaluated sequentially and the first match for
each element determines the corresponding value in the output vector. If
no cases match, the `.default` is used as a final "else" statment.

`case_when()` is an R equivalent of the SQL "searched" `CASE WHEN`
statement.

## Usage

``` r
case_when2(.default, ..., .ptype = NULL)
```

## Arguments

- .default:

  The value used when all of the LHS inputs return either `FALSE` or
  `NA`.

  `.default` must be size 1 or the same size as the common size computed
  from `...`.

  `.default` participates in the computation of the common type with the
  RHS inputs.

  `NA` values in the LHS conditions are treated like `FALSE`, meaning
  that the result at those locations will be assigned the `.default`
  value. To handle missing values in the conditions differently, you
  must explicitly catch them with another condition before they fall
  through to the `.default`. This typically involves some variation of
  `is.na(x) ~ value` tailored to your usage of `case_when()`.

  If `NULL`, the default, a missing value will be used.

- ...:

  \<[`dynamic-dots`](https://rlang.r-lib.org/reference/dyn-dots.html)\>
  A sequence of two-sided formulas. The left hand side (LHS) determines
  which values match this case. The right hand side (RHS) provides the
  replacement value.

  The LHS inputs must evaluate to logical vectors.

  The RHS inputs will be coerced to their common type.

  All inputs will be recycled to their common size. That said, we
  encourage all LHS inputs to be the same size. Recycling is mainly
  useful for RHS inputs, where you might supply a size 1 input that will
  be recycled to the size of the LHS inputs.

  `NULL` inputs are ignored.

- .ptype:

  An optional prototype declaring the desired output type. If supplied,
  this overrides the common type of the RHS inputs.

## Value

A vector with the same size as the common size computed from the inputs
in `...` and the same type as the common type of the RHS inputs in
`...`.

## See also

[`case_match()`](https://dplyr.tidyverse.org/reference/case_match.html)

## Examples

``` r
x <- 1:10
case_when2(
  x %% 3 == 0 ~ "buzz",
  x %% 2 == 0 ~ "fizz",
  .default = as.character(x)
)
#>  [1] "1"    "fizz" "buzz" "fizz" "5"    "buzz" "7"    "fizz" "buzz" "fizz"
#> c("1", "fizz", "buzz", "fizz", "5", "buzz", "7", "fizz", "buzz", "10")

# See ?dplyr::case_when for more examples
```
