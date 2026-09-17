# Attribute checks - Check for and filter attributes from object

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Functions to test for and filter attributes from an object. Attributes
can be selected by abbreviation in `abbr`, by name in `exact` or
`disallow`, or by regex pattern in `match`.

To remove attributes:

- `attrs_rmv()` returns `x` without the attributes selected.

- `attrs_keep()` returns `x` with only the attributes selected.

To test for attributes:

- `has_attrs_any()` returns `TRUE` if any of the selected attributes are
  present.

- `has_attrs_all()` returns `TRUE` if all of the selected attributes are
  present.

- `has_attrs_only()` returns `TRUE` if all and only the selected
  attributes are present.

## Usage

``` r
attrs_rmv(x, abbr = "", exact = character(), match = character(), perl = FALSE)

attrs_keep(
  x,
  abbr = "",
  exact = character(),
  match = character(),
  perl = FALSE
)

has_attrs_any(
  x,
  abbr = "",
  exact = character(),
  match = character(),
  disallow = character()
)

has_attrs_all(x, abbr = "", exact = character(), disallow = character())

has_attrs_only(x, abbr = "", exact = character())
```

## Arguments

- x:

  \[`any`\] Object to test for or remove attributes from.

- abbr:

  \[`character(1)`\] String of characters specifying attributes to keep:
  `"n"` for 'names'; `"d"` for 'dim'; `"c"` for 'class'; `"r"` for both
  rownames and dimnames.

- exact:

  \[[`character()`](https://rdrr.io/r/base/character.html)\] Other
  attributes to keep, specified by name.

- match:

  \[[`character()`](https://rdrr.io/r/base/character.html)\] Other
  attributes to keep, specified by regex pattern. They are combined with
  the or regex 'or' operator `|`.

- perl:

  \[`TRUE` \| `FALSE`\] Whether to use perl-compatible regex.

- disallow:

  \[[`character()`](https://rdrr.io/r/base/character.html)\] Attributes
  that, if present, will fail the test.

## Value

- \[`=x`\] For `attrs_rmv()` and `attrs_keep()`: Same object as `x` but
  with attributes some removed.

- \[`TRUE` \| `FALSE`\] For `has_attrs_any()`, `has_attrs_all()`, and
  `has_attrs_only()`: the scalar result of the test.

## Examples

``` r
x <- structure(
  1:3, a = 1, b = 2, c = 3,
  names = c("X", "Y", "Z"), dim = c(1, 3), class = "myclass",
  levels = c("aa", "bb", "cc")
)

# Default removal:
attrs_keep(x) # Removes all attributes
#> [1] 1 2 3
attrs_rmv(x) # Removes no attributes
#>      [,1] [,2] [,3]
#> [1,]    1    2    3
#> attr(,"a")
#> [1] 1
#> attr(,"b")
#> [1] 2
#> attr(,"c")
#> [1] 3
#> attr(,"names")
#> [1] "X" "Y" "Z"
#> attr(,"class")
#> [1] "myclass"
#> attr(,"levels")
#> [1] "aa" "bb" "cc"

# Abbreviation, exact, and regex filtering:
attrs_keep(x, abbr = "ncd") # Keeps names, dim, and class
#>      [,1] [,2] [,3]
#> [1,]    1    2    3
#> attr(,"names")
#> [1] "X" "Y" "Z"
#> attr(,"class")
#> [1] "myclass"
attrs_rmv(x, exact = c("levels", "b")) # Removes levels and b
#>      [,1] [,2] [,3]
#> [1,]    1    2    3
#> attr(,"a")
#> [1] 1
#> attr(,"c")
#> [1] 3
#> attr(,"names")
#> [1] "X" "Y" "Z"
#> attr(,"class")
#> [1] "myclass"
attrs_keep(x, match = "^[a-c]$") # Keeps only a, b, and c
#> [1] 1 2 3
#> attr(,"a")
#> [1] 1
#> attr(,"b")
#> [1] 2
#> attr(,"c")
#> [1] 3

# Testing for attributes:
has_attrs_any(x, "c", exact = "levels") #> TRUE (has class and levels)
#> [1] TRUE
has_attrs_any(x, "c", exact = "levels", disallow = "dim") #> FALSE (has dim)
#> [1] FALSE
has_attrs_all(x, exact = c("a", "b", "c")) #> TRUE
#> [1] TRUE
has_attrs_all(x, exact = c("a", "b", "c", "d")) #> FALSE (missing d)
#> [1] FALSE

has_attrs_only(x, exact = c("a", "b", "c")) #> FALSE (has other attributes)
#> [1] FALSE
```

## On this page

Functions to test for and filter attributes from an object. Attributes
can be selected by abbreviation in `abbr`, by name in `exact` or
`disallow`, or by regex pattern in `match`.

To remove attributes:

- `attrs_rmv()` returns `x` without the attributes selected.

- `attrs_keep()` returns `x` with only the attributes selected.

To test for attributes:

- `has_attrs_any()` returns `TRUE` if any of the selected attributes are
  present.

- `has_attrs_all()` returns `TRUE` if all of the selected attributes are
  present.

- `has_attrs_only()` returns `TRUE` if all and only the selected
  attributes are present.

## Usage

``` r
attrs_rmv(x, abbr = "", exact = character(), match = character(), perl = FALSE)

attrs_keep(
  x,
  abbr = "",
  exact = character(),
  match = character(),
  perl = FALSE
)

has_attrs_any(
  x,
  abbr = "",
  exact = character(),
  match = character(),
  disallow = character()
)

has_attrs_all(x, abbr = "", exact = character(), disallow = character())

has_attrs_only(x, abbr = "", exact = character())
```

## Arguments

- x:

  \[`any`\] Object to test for or remove attributes from.

- abbr:

  \[`character(1)`\] String of characters specifying attributes to keep:
  `"n"` for 'names'; `"d"` for 'dim'; `"c"` for 'class'; `"r"` for both
  rownames and dimnames.

- exact:

  \[[`character()`](https://rdrr.io/r/base/character.html)\] Other
  attributes to keep, specified by name.

- match:

  \[[`character()`](https://rdrr.io/r/base/character.html)\] Other
  attributes to keep, specified by regex pattern. They are combined with
  the or regex 'or' operator `|`.

- perl:

  \[`TRUE` \| `FALSE`\] Whether to use perl-compatible regex.

- disallow:

  \[[`character()`](https://rdrr.io/r/base/character.html)\] Attributes
  that, if present, will fail the test.

## Value

- \[`=x`\] For `attrs_rmv()` and `attrs_keep()`: Same object as `x` but
  with attributes some removed.

- \[`TRUE` \| `FALSE`\] For `has_attrs_any()`, `has_attrs_all()`, and
  `has_attrs_only()`: the scalar result of the test.

## Examples

``` r
x <- structure(
  1:3, a = 1, b = 2, c = 3,
  names = c("X", "Y", "Z"), dim = c(1, 3), class = "myclass",
  levels = c("aa", "bb", "cc")
)

# Default removal:
attrs_keep(x) # Removes all attributes
#> [1] 1 2 3
attrs_rmv(x) # Removes no attributes
#>      [,1] [,2] [,3]
#> [1,]    1    2    3
#> attr(,"a")
#> [1] 1
#> attr(,"b")
#> [1] 2
#> attr(,"c")
#> [1] 3
#> attr(,"names")
#> [1] "X" "Y" "Z"
#> attr(,"class")
#> [1] "myclass"
#> attr(,"levels")
#> [1] "aa" "bb" "cc"

# Abbreviation, exact, and regex filtering:
attrs_keep(x, abbr = "ncd") # Keeps names, dim, and class
#>      [,1] [,2] [,3]
#> [1,]    1    2    3
#> attr(,"names")
#> [1] "X" "Y" "Z"
#> attr(,"class")
#> [1] "myclass"
attrs_rmv(x, exact = c("levels", "b")) # Removes levels and b
#>      [,1] [,2] [,3]
#> [1,]    1    2    3
#> attr(,"a")
#> [1] 1
#> attr(,"c")
#> [1] 3
#> attr(,"names")
#> [1] "X" "Y" "Z"
#> attr(,"class")
#> [1] "myclass"
attrs_keep(x, match = "^[a-c]$") # Keeps only a, b, and c
#> [1] 1 2 3
#> attr(,"a")
#> [1] 1
#> attr(,"b")
#> [1] 2
#> attr(,"c")
#> [1] 3

# Testing for attributes:
has_attrs_any(x, "c", exact = "levels") #> TRUE (has class and levels)
#> [1] TRUE
has_attrs_any(x, "c", exact = "levels", disallow = "dim") #> FALSE (has dim)
#> [1] FALSE
has_attrs_all(x, exact = c("a", "b", "c")) #> TRUE
#> [1] TRUE
has_attrs_all(x, exact = c("a", "b", "c", "d")) #> FALSE (missing d)
#> [1] FALSE

has_attrs_only(x, exact = c("a", "b", "c")) #> FALSE (has other attributes)
#> [1] FALSE
```
