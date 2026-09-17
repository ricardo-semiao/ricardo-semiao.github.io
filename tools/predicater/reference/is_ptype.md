# Compare - Check if object is of prototype

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Check if `.x` has the same attributes as `.ptype`, with more flexibility
than
[`vctrs::vec_is()`](https://vctrs.r-lib.org/reference/vec_assert.html).
A prototype is a template object that defines metadata:
[`typeof()`](https://rdrr.io/r/base/typeof.html),
[`length()`](https://rdrr.io/r/base/length.html), names of the
attributes, and their values, everything besides data. With
`is_ptype()`, the user can specify which metadata to check and how.

`is_ptype_list()` recursively checks if a list object has the correct
elements given a list prototype, useful when dealing with complex
objects like
`list(a = integer(), b = list(c = character(), d = double()))`.

## Usage

``` r
is_ptype(
  .x,
  .ptype,
  .length = "0|==",
  .attrs = "no",
  class = "0|==",
  dim = "0|==",
  names = "0|==",
  row.names = "0|==",
  dimnames = "0|id",
  ...
)

is_ptype_list(.x, .ptype, .named = TRUE, .depth = 1, ...)
```

## Arguments

- .x:

  \[`any`\] An object to test.

- .ptype:

  \[`any`\] A prototype object that defines metadata to check against
  `.x`.

- .length, .attrs:

  \[`character(1)` \| `\(vx, vp) {}`\] How to check the non-attribute
  metadata – [`length()`](https://rdrr.io/r/base/length.html), and
  attributes names – of `.x` against `ptype`. Can be either: a function
  that takes the metadata's value of `.x` (`vx`) and `.ptype` (`vp`) as
  arguments and returns a boolean; or a string that specifies a
  predefined function (see [Details](#details)).

- class, dim, names, row.names, dimnames, ...:

  \[`character(1)` \| `\(vx, vp) {}`\] How to check the attributes –
  each argument is an attribute name – of `.x` against `.ptype`. With a
  function or string (same as above).

- .named:

  \[`TRUE` \| `FALSE`\] For `is_ptype_list()`, whether to use the names
  of `.x` and `.ptype` for matching them (`TRUE`), or the order
  (`FALSE`).

- .depth:

  \[`integer(1)`\] For `is_ptype_list()`, how many levels of recursion
  to check. `1` means check the first level elements only.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Details

Predefined check functions:

- `"no"`: don't check, always return `TRUE`.

- `"id"`: check if `identical(vp, vx)`.

- `"=="`: check if `all(vp == vx)`.

- `"0|id"` and `"0|=="` ('zero or equal'): same as above, but return
  `TRUE` if `vp` has zero length or is `0`.

- `"id_ord"` and `"==_ord"`: same as above, but ignore the order of
  values.

- `"id_sub"` and `"==_sub"`: same as above, but allow `vx` to be a
  subset of `vp`.

Attributes of attributes of `.x` or `.ptype` are ignored.

## Examples

``` r
# By default, length is checked when the prototype's is not 0:
is_ptype(1:10, integer())  #> TRUE
#> [1] TRUE
is_ptype(1:10, integer(9)) #> FALSE
#> [1] FALSE

# Same is true for class, dim, names, row.names, and dimnames attributes:
is_ptype(matrix(1:9, 3, 3), integer()) #> TRUE
#> [1] TRUE
is_ptype(matrix(1:9, 3, 3), integer(), dim = "==") #> FALSE
#> [1] FALSE

# For less common attributes, checks need to be specified in `...`:
is_ptype(
  factor(c("a", "b")), factor(levels = c("a", "b", "c"))
)
#> [1] TRUE
#> TRUE

is_ptype(
  factor(c("a", "b")), factor(levels = c("a", "b", "c")),
  levels = "=="
)
#> [1] FALSE
#> FALSE

# Complex objects can be checked with `is_ptype_list()`:
schema <- list(a = integer(1), b = data.frame(), c = double())
is_ptype_list(list(a = 1L, b = mtcars, c = rnorm(sample(1:10))), schema)
#> [1] TRUE
#> TRUE
```

## On this page

Check if `.x` has the same attributes as `.ptype`, with more flexibility
than
[`vctrs::vec_is()`](https://vctrs.r-lib.org/reference/vec_assert.html).
A prototype is a template object that defines metadata:
[`typeof()`](https://rdrr.io/r/base/typeof.html),
[`length()`](https://rdrr.io/r/base/length.html), names of the
attributes, and their values, everything besides data. With
`is_ptype()`, the user can specify which metadata to check and how.

`is_ptype_list()` recursively checks if a list object has the correct
elements given a list prototype, useful when dealing with complex
objects like
`list(a = integer(), b = list(c = character(), d = double()))`.

## Usage

``` r
is_ptype(
  .x,
  .ptype,
  .length = "0|==",
  .attrs = "no",
  class = "0|==",
  dim = "0|==",
  names = "0|==",
  row.names = "0|==",
  dimnames = "0|id",
  ...
)

is_ptype_list(.x, .ptype, .named = TRUE, .depth = 1, ...)
```

## Arguments

- .x:

  \[`any`\] An object to test.

- .ptype:

  \[`any`\] A prototype object that defines metadata to check against
  `.x`.

- .length, .attrs:

  \[`character(1)` \| `\(vx, vp) {}`\] How to check the non-attribute
  metadata – [`length()`](https://rdrr.io/r/base/length.html), and
  attributes names – of `.x` against `ptype`. Can be either: a function
  that takes the metadata's value of `.x` (`vx`) and `.ptype` (`vp`) as
  arguments and returns a boolean; or a string that specifies a
  predefined function (see [Details](#details)).

- class, dim, names, row.names, dimnames, ...:

  \[`character(1)` \| `\(vx, vp) {}`\] How to check the attributes –
  each argument is an attribute name – of `.x` against `.ptype`. With a
  function or string (same as above).

- .named:

  \[`TRUE` \| `FALSE`\] For `is_ptype_list()`, whether to use the names
  of `.x` and `.ptype` for matching them (`TRUE`), or the order
  (`FALSE`).

- .depth:

  \[`integer(1)`\] For `is_ptype_list()`, how many levels of recursion
  to check. `1` means check the first level elements only.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Details

Predefined check functions:

- `"no"`: don't check, always return `TRUE`.

- `"id"`: check if `identical(vp, vx)`.

- `"=="`: check if `all(vp == vx)`.

- `"0|id"` and `"0|=="` ('zero or equal'): same as above, but return
  `TRUE` if `vp` has zero length or is `0`.

- `"id_ord"` and `"==_ord"`: same as above, but ignore the order of
  values.

- `"id_sub"` and `"==_sub"`: same as above, but allow `vx` to be a
  subset of `vp`.

Attributes of attributes of `.x` or `.ptype` are ignored.

## Examples

``` r
# By default, length is checked when the prototype's is not 0:
is_ptype(1:10, integer())  #> TRUE
#> [1] TRUE
is_ptype(1:10, integer(9)) #> FALSE
#> [1] FALSE

# Same is true for class, dim, names, row.names, and dimnames attributes:
is_ptype(matrix(1:9, 3, 3), integer()) #> TRUE
#> [1] TRUE
is_ptype(matrix(1:9, 3, 3), integer(), dim = "==") #> FALSE
#> [1] FALSE

# For less common attributes, checks need to be specified in `...`:
is_ptype(
  factor(c("a", "b")), factor(levels = c("a", "b", "c"))
)
#> [1] TRUE
#> TRUE

is_ptype(
  factor(c("a", "b")), factor(levels = c("a", "b", "c")),
  levels = "=="
)
#> [1] FALSE
#> FALSE

# Complex objects can be checked with `is_ptype_list()`:
schema <- list(a = integer(1), b = data.frame(), c = double())
is_ptype_list(list(a = 1L, b = mtcars, c = rnorm(sample(1:10))), schema)
#> [1] TRUE
#> TRUE
```
