# Attribute utilities - Getters and setters

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Functions to get and set names, dimnames, and class of an object, while
requiring values of a specific 'quality'.

## Usage

``` r
names3(x, repair = "unique", how = "names")

names3(x, repair = "unique", how = "names") <- value

dimnames2(x, repair = "unique", how = "dimnames")

dimnames2(x, repair = "unique", how = "dimnames") <- value

rownames2(x, repair = "unique", how = "dimnames")

rownames2(x, repair = "unique", how = "dimnames") <- value

class2(x, how = "class")

class2(x, how = "class") <- value
```

## Arguments

- x:

  \[`any`\] Object to get or set attribute from.

- repair:

  Either a string or a function. If a string, it must be one of
  `"check_unique"`, `"minimal"`, `"unique"`, `"universal"`,
  `"unique_quiet"`, or `"universal_quiet"`. If a function, it is invoked
  with a vector of minimal names and must return minimal names,
  otherwise an error is thrown.

  - Minimal names are never `NULL` or `NA`. When an element doesn't have
    a name, its minimal name is an empty string.

  - Unique names are unique. A suffix is appended to duplicate names to
    make them unique.

  - Universal names are unique and syntactic, meaning that you can
    safely use the names as variables without causing a syntax error.

  The `"check_unique"` option doesn't perform any name repair. Instead,
  an error is raised if the names don't suit the `"unique"` criteria.

  The options `"unique_quiet"` and `"universal_quiet"` are here to help
  the user who calls this function indirectly, via another function
  which exposes `repair` but not `quiet`. Specifying
  `repair = "unique_quiet"` is like specifying
  `repair = "unique", quiet = TRUE`. When the `"*_quiet"` options are
  used, any setting of `quiet` is silently overridden.

- how:

  \[`character(1)`\] How to get or set the attribute:

  - For `names3()`: `"names"` for
    [`names()`](https://rdrr.io/r/base/names.html) and `"attr"` for
    [`attr()`](https://rdrr.io/r/base/attr.html).

  - For `dimnames2()`: `"dimnames"` for
    [`dimnames()`](https://rdrr.io/r/base/dimnames.html) and `"attr"`
    for `attr(x, "dimnames")`.

  - For `rownames2()`: `"dimnames"` for the first element of
    [`dimnames()`](https://rdrr.io/r/base/dimnames.html), `"attr"` for
    `attr(x, "dimnames")[[1]]`, and `"row.names"` for
    `attr(x, "row.names")`.

  - For `class2()`: `"class"` for
    [`class()`](https://rdrr.io/r/base/class.html) and `"attr"` for
    `attr(x, "class")`.

- value:

  \[`any`\] Value to set the attribute to.

## Value

- \[`character(length(x))` \| `NULL`\] For `names3()`.

- \[`list(length(dim(x)))` \| `NULL`\] For `dimnames2()`.

- \[`character(dim(x)[1])` \| `NULL`\] For `rownames2()`.

- \[[`character()`](https://rdrr.io/r/base/character.html)\] For
  `class2()`.

- \[`=value`\] For the setters: The `value` passed, invisibly.

## Examples

``` r
x <- structure(
  1:6, dim = c(2, 3, 1), names = paste0("i", 1:6),
  dimnames = list(c("a", "a"), c("x", "y", "z"), "_bad"),
  class = c("classA", "", NA, "classB", "classA")
)

# Getting repaired names and valid classes:
names3(x) #> c("i1", "i2", "i3", "i4", "i5", "i6") (no repair)
#> [1] "i1" "i2" "i3" "i4" "i5" "i6"

suppressMessages(dimnames2(x))
#> [[1]]
#> [1] "a...1" "a...2"
#> 
#> [[2]]
#> [1] "x" "y" "z"
#> 
#> [[3]]
#> [1] "_bad"
#> 
#> list(c("a...1", "a...2"), c("x", "y", "z"), "_bad")
suppressMessages(dimnames2(x, repair = "universal"))
#> [[1]]
#> [1] "a...1" "a...2"
#> 
#> [[2]]
#> [1] "x" "y" "z"
#> 
#> [[3]]
#> [1] "._bad"
#> 
#> list(c("a...1", "a...2"), c("x", "y", "z"), "._bad")

suppressMessages(rownames2(x)) #> c("a...1", "a...2")
#> [1] "a...1" "a...2"

class2(x) #> c("classA", "classB")
#> [1] "classA" "classB"

# Setting repaired names and valid classes:
class2(x) <- c("again", "duplicates", "again")
class2(x) #> c("again", "duplicates")
#> [1] "again"      "duplicates"

suppressMessages(rownames2(x) <- NULL) # Names are created automatically
rownames(x) #> c("...1", "...2")
#> [1] "...1" "...2"
```

## On this page

Functions to get and set names, dimnames, and class of an object, while
requiring values of a specific 'quality'.

## Usage

``` r
names3(x, repair = "unique", how = "names")

names3(x, repair = "unique", how = "names") <- value

dimnames2(x, repair = "unique", how = "dimnames")

dimnames2(x, repair = "unique", how = "dimnames") <- value

rownames2(x, repair = "unique", how = "dimnames")

rownames2(x, repair = "unique", how = "dimnames") <- value

class2(x, how = "class")

class2(x, how = "class") <- value
```

## Arguments

- x:

  \[`any`\] Object to get or set attribute from.

- repair:

  Either a string or a function. If a string, it must be one of
  `"check_unique"`, `"minimal"`, `"unique"`, `"universal"`,
  `"unique_quiet"`, or `"universal_quiet"`. If a function, it is invoked
  with a vector of minimal names and must return minimal names,
  otherwise an error is thrown.

  - Minimal names are never `NULL` or `NA`. When an element doesn't have
    a name, its minimal name is an empty string.

  - Unique names are unique. A suffix is appended to duplicate names to
    make them unique.

  - Universal names are unique and syntactic, meaning that you can
    safely use the names as variables without causing a syntax error.

  The `"check_unique"` option doesn't perform any name repair. Instead,
  an error is raised if the names don't suit the `"unique"` criteria.

  The options `"unique_quiet"` and `"universal_quiet"` are here to help
  the user who calls this function indirectly, via another function
  which exposes `repair` but not `quiet`. Specifying
  `repair = "unique_quiet"` is like specifying
  `repair = "unique", quiet = TRUE`. When the `"*_quiet"` options are
  used, any setting of `quiet` is silently overridden.

- how:

  \[`character(1)`\] How to get or set the attribute:

  - For `names3()`: `"names"` for
    [`names()`](https://rdrr.io/r/base/names.html) and `"attr"` for
    [`attr()`](https://rdrr.io/r/base/attr.html).

  - For `dimnames2()`: `"dimnames"` for
    [`dimnames()`](https://rdrr.io/r/base/dimnames.html) and `"attr"`
    for `attr(x, "dimnames")`.

  - For `rownames2()`: `"dimnames"` for the first element of
    [`dimnames()`](https://rdrr.io/r/base/dimnames.html), `"attr"` for
    `attr(x, "dimnames")[[1]]`, and `"row.names"` for
    `attr(x, "row.names")`.

  - For `class2()`: `"class"` for
    [`class()`](https://rdrr.io/r/base/class.html) and `"attr"` for
    `attr(x, "class")`.

- value:

  \[`any`\] Value to set the attribute to.

## Value

- \[`character(length(x))` \| `NULL`\] For `names3()`.

- \[`list(length(dim(x)))` \| `NULL`\] For `dimnames2()`.

- \[`character(dim(x)[1])` \| `NULL`\] For `rownames2()`.

- \[[`character()`](https://rdrr.io/r/base/character.html)\] For
  `class2()`.

- \[`=value`\] For the setters: The `value` passed, invisibly.

## Examples

``` r
x <- structure(
  1:6, dim = c(2, 3, 1), names = paste0("i", 1:6),
  dimnames = list(c("a", "a"), c("x", "y", "z"), "_bad"),
  class = c("classA", "", NA, "classB", "classA")
)

# Getting repaired names and valid classes:
names3(x) #> c("i1", "i2", "i3", "i4", "i5", "i6") (no repair)
#> [1] "i1" "i2" "i3" "i4" "i5" "i6"

suppressMessages(dimnames2(x))
#> [[1]]
#> [1] "a...1" "a...2"
#> 
#> [[2]]
#> [1] "x" "y" "z"
#> 
#> [[3]]
#> [1] "_bad"
#> 
#> list(c("a...1", "a...2"), c("x", "y", "z"), "_bad")
suppressMessages(dimnames2(x, repair = "universal"))
#> [[1]]
#> [1] "a...1" "a...2"
#> 
#> [[2]]
#> [1] "x" "y" "z"
#> 
#> [[3]]
#> [1] "._bad"
#> 
#> list(c("a...1", "a...2"), c("x", "y", "z"), "._bad")

suppressMessages(rownames2(x)) #> c("a...1", "a...2")
#> [1] "a...1" "a...2"

class2(x) #> c("classA", "classB")
#> [1] "classA" "classB"

# Setting repaired names and valid classes:
class2(x) <- c("again", "duplicates", "again")
class2(x) #> c("again", "duplicates")
#> [1] "again"      "duplicates"

suppressMessages(rownames2(x) <- NULL) # Names are created automatically
rownames(x) #> c("...1", "...2")
#> [1] "...1" "...2"
```
