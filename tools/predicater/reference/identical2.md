# Compare - Exact equality with more flexibility

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Similar to [`identical()`](https://rdrr.io/r/base/identical.html) but
with more flexibility on how to handle data and attributes.

- `identical2()` test two objects for exact equality.

- `identical_flag()` runs
  [`identical()`](https://rdrr.io/r/base/identical.html) or
  `identical2()` recursively, returning the comparison results in a list
  with the same structure as `x`. Useful to flag where `x` and `y`
  differ.

To see if multiple objects are identical, wrap them in a list and use
[`reduce_predicate()`](reduce_predicate.md). To vectorize over two
lists, checking that each pair of elements between them are identical,
use `Map(identical2, x, y)` (see
[`Map()`](https://rdrr.io/r/base/funprog.html)).

## Usage

``` r
identical2(
  x,
  y,
  single_NA = TRUE,
  single_zero = TRUE,
  ord_data = TRUE,
  ord_attrs = FALSE,
  tol_type = "none",
  tol = sqrt(.Machine$double.eps),
  ignore_data = character(),
  ignore_attrs = list()
)

identical_flag(x, y, ..., fun = "identical2", .is_attrs = FALSE)
```

## Arguments

- x, y:

  \[`any`\] Any R object.

- single_NA, single_zero:

  \[`TRUE` \| `FALSE` each\] Whether to treat `NA` values as a identical
  to each other, and the same for `+0` vs. `-0`.

- ord_data, ord_attrs:

  \[`TRUE` \| `FALSE` each\] Whether to keep the order of the data and
  attributes in `x` and `y`.

- tol_type:

  \[`"none"` \| `"abs"` \| `"rel"`\] Type of tolerance to use when
  comparing numeric values. One of:

  - `"none"`: no tolerance (default).

  - `"abs"`: absolute tolerance.

  - `"rel"`: relative tolerance.

- tol:

  \[`numeric(1)`\] Tolerance value.

- ignore_data:

  \[[`character()`](https://rdrr.io/r/base/character.html) \|
  [`integer()`](https://rdrr.io/r/base/integer.html)\] indexes or names
  of elements to ignore when comparing `x` and `y`. Names are compared
  against
  [`rlang::names2()`](https://rlang.r-lib.org/reference/names2.html).

- ignore_attrs:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] Arguments to pass to
  [`attrs_rmv()`](attributes-filter.md) to remove attributes from `x`
  and `y`

- ...:

  For `identical_flag()`: arguments passed to `identical2()` or
  [`identical()`](https://rdrr.io/r/base/identical.html).

- fun:

  \[`"identical"` \| `"identical2"`\] For `identical_flag()`: function
  to use for comparison.

- .is_attrs:

  \[`TRUE` \| `FALSE`\] For internal use only.

## Value

- \[`TRUE` \| `FALSE`\] For `identical2()`: the scalar result of the
  test.

- `identical_flag()` returns a object with the same structure as `x` and
  logical elements.

## Examples

``` r
x <- structure(c(1, 2, 3), a = "a", b = "b", c = "c")
y <- structure(c(3, 2, 1), b = "b", a = "a", c = "d")

identical2(x, y) #> FALSE
#> [1] FALSE

# Pre-sort data and ignore "c" attribute:
identical2(
  x, y, ord_data = FALSE,
  ignore_attrs = list(exact = c("c"))
) #> TRUE
#> [1] TRUE

# Consider attribute order:
identical2(
  x, y, ord_data = FALSE,
  ignore_attrs = list(exact = c("c")), ord_attrs = TRUE
) #> FALSE
#> [1] FALSE

# No sorting but accept up to 2.1 numerical absolute tolerance:
identical2(
  x, y, tol_type = "abs", tol = 2.1,
  ignore_attrs = list(exact = c("c"))
) #> TRUE
#> [1] TRUE

# Understading where the differences are:
identical_flag(x, y)
#> $.data
#> [1] FALSE  TRUE FALSE
#> 
#> $.attrs
#> $.attrs$a
#> $.attrs$a$.data
#> [1] TRUE
#> 
#> 
#> $.attrs$b
#> $.attrs$b$.data
#> [1] TRUE
#> 
#> 
#> $.attrs$c
#> $.attrs$c$.data
#> [1] FALSE
#> 
#> 
#> 
#> $.data
#> c(FALSE, TRUE, FALSE) # First (3 & 1) and third (1 & 3) elements are different
#>
#> $.attrs
#> $.attrs$a
#> $.attrs$a$.data
#> TRUE
#>
#> $.attrs$b
#> $.attrs$b$.data
#> TRUE
#>
#> $.attrs$c
#> $.attrs$c$.data
#> FALSE # Attribute "c" ("c" & "d") is different
```

## On this page

Similar to [`identical()`](https://rdrr.io/r/base/identical.html) but
with more flexibility on how to handle data and attributes.

- `identical2()` test two objects for exact equality.

- `identical_flag()` runs
  [`identical()`](https://rdrr.io/r/base/identical.html) or
  `identical2()` recursively, returning the comparison results in a list
  with the same structure as `x`. Useful to flag where `x` and `y`
  differ.

To see if multiple objects are identical, wrap them in a list and use
[`reduce_predicate()`](reduce_predicate.md). To vectorize over two
lists, checking that each pair of elements between them are identical,
use `Map(identical2, x, y)` (see
[`Map()`](https://rdrr.io/r/base/funprog.html)).

## Usage

``` r
identical2(
  x,
  y,
  single_NA = TRUE,
  single_zero = TRUE,
  ord_data = TRUE,
  ord_attrs = FALSE,
  tol_type = "none",
  tol = sqrt(.Machine$double.eps),
  ignore_data = character(),
  ignore_attrs = list()
)

identical_flag(x, y, ..., fun = "identical2", .is_attrs = FALSE)
```

## Arguments

- x, y:

  \[`any`\] Any R object.

- single_NA, single_zero:

  \[`TRUE` \| `FALSE` each\] Whether to treat `NA` values as a identical
  to each other, and the same for `+0` vs. `-0`.

- ord_data, ord_attrs:

  \[`TRUE` \| `FALSE` each\] Whether to keep the order of the data and
  attributes in `x` and `y`.

- tol_type:

  \[`"none"` \| `"abs"` \| `"rel"`\] Type of tolerance to use when
  comparing numeric values. One of:

  - `"none"`: no tolerance (default).

  - `"abs"`: absolute tolerance.

  - `"rel"`: relative tolerance.

- tol:

  \[`numeric(1)`\] Tolerance value.

- ignore_data:

  \[[`character()`](https://rdrr.io/r/base/character.html) \|
  [`integer()`](https://rdrr.io/r/base/integer.html)\] indexes or names
  of elements to ignore when comparing `x` and `y`. Names are compared
  against
  [`rlang::names2()`](https://rlang.r-lib.org/reference/names2.html).

- ignore_attrs:

  \[[`list()`](https://rdrr.io/r/base/list.html)\] Arguments to pass to
  [`attrs_rmv()`](attributes-filter.md) to remove attributes from `x`
  and `y`

- ...:

  For `identical_flag()`: arguments passed to `identical2()` or
  [`identical()`](https://rdrr.io/r/base/identical.html).

- fun:

  \[`"identical"` \| `"identical2"`\] For `identical_flag()`: function
  to use for comparison.

- .is_attrs:

  \[`TRUE` \| `FALSE`\] For internal use only.

## Value

- \[`TRUE` \| `FALSE`\] For `identical2()`: the scalar result of the
  test.

- `identical_flag()` returns a object with the same structure as `x` and
  logical elements.

## Examples

``` r
x <- structure(c(1, 2, 3), a = "a", b = "b", c = "c")
y <- structure(c(3, 2, 1), b = "b", a = "a", c = "d")

identical2(x, y) #> FALSE
#> [1] FALSE

# Pre-sort data and ignore "c" attribute:
identical2(
  x, y, ord_data = FALSE,
  ignore_attrs = list(exact = c("c"))
) #> TRUE
#> [1] TRUE

# Consider attribute order:
identical2(
  x, y, ord_data = FALSE,
  ignore_attrs = list(exact = c("c")), ord_attrs = TRUE
) #> FALSE
#> [1] FALSE

# No sorting but accept up to 2.1 numerical absolute tolerance:
identical2(
  x, y, tol_type = "abs", tol = 2.1,
  ignore_attrs = list(exact = c("c"))
) #> TRUE
#> [1] TRUE

# Understading where the differences are:
identical_flag(x, y)
#> $.data
#> [1] FALSE  TRUE FALSE
#> 
#> $.attrs
#> $.attrs$a
#> $.attrs$a$.data
#> [1] TRUE
#> 
#> 
#> $.attrs$b
#> $.attrs$b$.data
#> [1] TRUE
#> 
#> 
#> $.attrs$c
#> $.attrs$c$.data
#> [1] FALSE
#> 
#> 
#> 
#> $.data
#> c(FALSE, TRUE, FALSE) # First (3 & 1) and third (1 & 3) elements are different
#>
#> $.attrs
#> $.attrs$a
#> $.attrs$a$.data
#> TRUE
#>
#> $.attrs$b
#> $.attrs$b$.data
#> TRUE
#>
#> $.attrs$c
#> $.attrs$c$.data
#> FALSE # Attribute "c" ("c" & "d") is different
```
