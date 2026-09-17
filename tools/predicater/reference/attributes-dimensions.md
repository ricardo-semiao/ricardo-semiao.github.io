# Attribute checks - Dimensions existence and sizes

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Functions for the presence and number of dimensions and dimension names
of an object.

- `n_dims()` and `n_dimnames()` return the number of dimensions and
  dimension names, respectively, controlling for empty dimensions and
  invalid names.

- `has_dim()`, `has_dimnames()`, and `has_rownames()` return whether the
  object has dimensions, dimension names, and rownames, respectively.

## Usage

``` r
n_dims(x, empty = TRUE, how = "dim")

n_dimnames(x, invalid = TRUE, how = "dimnames")

has_dimnames(x, n = NULL, how = "dimnames")

has_rownames(x, how = "dimnames")

has_dim(x, n = NULL, how = "dim")
```

## Arguments

- x:

  \[`any`\] An object to test.

- empty:

  \[`TRUE` \| `FALSE`\] Whether to count empty dimensions and dimension
  names.

- how:

  \[`character(1)`\] How to extract the attribute:

  - For dimensions: `"dim"` for
    [`dim()`](https://rdrr.io/r/base/dim.html) and `"attr"` for
    `attr(x, "dim")`.

  - For dimension names: `"dimnames"` for
    [`dimnames()`](https://rdrr.io/r/base/dimnames.html) and `"attr"`
    for `attr(x, "dimnames")`.

  - For rownames: `"rownames"` for
    [`rownames()`](https://rdrr.io/r/base/colnames.html), `"dimnames"`
    for the first element of
    [`dimnames()`](https://rdrr.io/r/base/dimnames.html), and `"attr"`
    for `attr(x, "row.names")`.

- invalid:

  \[`TRUE` \| `FALSE`\] Whether to count dimensions with NA, empty, or
  duplicate names.

- n:

  \[`integer(1)`\] Number of dimensions to check for. Set to `NULL` to
  not test.

## Value

- \[integer(1)\] For `n_dims()` and `n_dimnames()`.

- \[`TRUE` \| `FALSE`\] For `has_dim()`, `has_dimnames()`, and
  `has_rownames()`: the scalar result of the test.

## Examples

``` r
x <- structure(
  1:6, dim = c(2, 3, 1),
  dimnames = list(c("a", "a"), c("x", "y", "z"), NULL)
)

# Counting dimensions and dimension names:
n_dims(x) #> 3
#> [1] 3
n_dims(x, empty = FALSE) #> 2
#> [1] 2

n_dimnames(x) #> 2
#> [1] 2
n_dimnames(x, invalid = FALSE) #> 1 (rownames have duplicates)
#> [1] 1

# Testing for dimensions and dimension names:
has_dimnames(x) #> TRUE
#> [1] TRUE
has_rownames(mtcars) #> TRUE
#> [1] TRUE
has_dim(mtcars) #> TRUE
#> [1] TRUE

# Data frames often have no actual dimension attribues:
has_dim(mtcars, how = "attr") #> FALSE
#> [1] FALSE
has_dimnames(mtcars, how = "attr") #> FALSE
#> [1] FALSE
has_rownames(mtcars, how = "row.names") #> TRUE (but have row.names one)
#> [1] TRUE
```

## On this page

Functions for the presence and number of dimensions and dimension names
of an object.

- `n_dims()` and `n_dimnames()` return the number of dimensions and
  dimension names, respectively, controlling for empty dimensions and
  invalid names.

- `has_dim()`, `has_dimnames()`, and `has_rownames()` return whether the
  object has dimensions, dimension names, and rownames, respectively.

## Usage

``` r
n_dims(x, empty = TRUE, how = "dim")

n_dimnames(x, invalid = TRUE, how = "dimnames")

has_dimnames(x, n = NULL, how = "dimnames")

has_rownames(x, how = "dimnames")

has_dim(x, n = NULL, how = "dim")
```

## Arguments

- x:

  \[`any`\] An object to test.

- empty:

  \[`TRUE` \| `FALSE`\] Whether to count empty dimensions and dimension
  names.

- how:

  \[`character(1)`\] How to extract the attribute:

  - For dimensions: `"dim"` for
    [`dim()`](https://rdrr.io/r/base/dim.html) and `"attr"` for
    `attr(x, "dim")`.

  - For dimension names: `"dimnames"` for
    [`dimnames()`](https://rdrr.io/r/base/dimnames.html) and `"attr"`
    for `attr(x, "dimnames")`.

  - For rownames: `"rownames"` for
    [`rownames()`](https://rdrr.io/r/base/colnames.html), `"dimnames"`
    for the first element of
    [`dimnames()`](https://rdrr.io/r/base/dimnames.html), and `"attr"`
    for `attr(x, "row.names")`.

- invalid:

  \[`TRUE` \| `FALSE`\] Whether to count dimensions with NA, empty, or
  duplicate names.

- n:

  \[`integer(1)`\] Number of dimensions to check for. Set to `NULL` to
  not test.

## Value

- \[integer(1)\] For `n_dims()` and `n_dimnames()`.

- \[`TRUE` \| `FALSE`\] For `has_dim()`, `has_dimnames()`, and
  `has_rownames()`: the scalar result of the test.

## Examples

``` r
x <- structure(
  1:6, dim = c(2, 3, 1),
  dimnames = list(c("a", "a"), c("x", "y", "z"), NULL)
)

# Counting dimensions and dimension names:
n_dims(x) #> 3
#> [1] 3
n_dims(x, empty = FALSE) #> 2
#> [1] 2

n_dimnames(x) #> 2
#> [1] 2
n_dimnames(x, invalid = FALSE) #> 1 (rownames have duplicates)
#> [1] 1

# Testing for dimensions and dimension names:
has_dimnames(x) #> TRUE
#> [1] TRUE
has_rownames(mtcars) #> TRUE
#> [1] TRUE
has_dim(mtcars) #> TRUE
#> [1] TRUE

# Data frames often have no actual dimension attribues:
has_dim(mtcars, how = "attr") #> FALSE
#> [1] FALSE
has_dimnames(mtcars, how = "attr") #> FALSE
#> [1] FALSE
has_rownames(mtcars, how = "row.names") #> TRUE (but have row.names one)
#> [1] TRUE
```
