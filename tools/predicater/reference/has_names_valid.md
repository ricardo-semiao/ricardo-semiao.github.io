# Attribute checks - Names

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test whether `x` has names with greater flexibility than
[`rlang::is_named()`](https://rlang.r-lib.org/reference/is_named.html),
handling NA, empty, duplicate, and invalid names, as well as empty
vectors.

## Usage

``` r
has_names_valid(
  x,
  na = FALSE,
  empty = FALSE,
  dups = FALSE,
  invalid = TRUE,
  zero_len = TRUE,
  how = "names"
)

are_names_valid(
  x,
  na = FALSE,
  empty = FALSE,
  dups = FALSE,
  invalid = TRUE,
  how = "names"
)
```

## Arguments

- x:

  \[`collection()`, `any`\] For `are_*()`, any collection to test; for
  `is_*()`, any object to test.

- na, empty, dups, invalid:

  \[`TRUE` \| `FALSE`\] What to return for NA, empty, duplicate, or
  invalid names.

- zero_len:

  \[`TRUE` \| `FALSE`\] What to return for an an empty `x`.

- how:

  \[`"names"` \| `"x"` \| `"attr"` \| `"names2"`\] How to extract names:
  "names" for [`names()`](https://rdrr.io/r/base/names.html); `"x"` to
  use `x` itself; "attr" for `attr(x, "names")`; or `"names2"` for
  [`rlang::names2()`](https://rlang.r-lib.org/reference/names2.html).

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Details

The default argument values guarantee that `x` can be safely iterated by
its names.

A `non_collection` is an object that is not an atomic vector, list,
pairlist, expression, or environment. That is, it returns `FALSE` for
[`is_collection()`](predicates-collections.md).

The `how` methods differ only for environments, with "names" returning
names and "attr" returning NULL.

`invalid = FALSE` checks if the names don't change after being passed to
[`make.names()`](https://rdrr.io/r/base/make.names.html).

## Examples

``` r
has_names_valid(mtcars) #> TRUE
#> [1] TRUE

# NA, empty, and duplicate names return FALSE by default:
has_names_valid(rlang::set_names(1:3, c("a", "b", NA))) #> FALSE
#> [1] FALSE
has_names_valid(rlang::set_names(1:3, c("a", "b", NA)), na = TRUE) #> TRUE
#> [1] TRUE

has_names_valid(rlang::set_names(1:3, c("a", "", "b"))) #> FALSE
#> [1] FALSE
has_names_valid(rlang::set_names(1:3, c("a", "a", "a"))) #> FALSE
#> [1] FALSE

# Invalid names and zero-length x's return TRUE by default:
has_names_valid(rlang::set_names(1:3, c("_bad", "b", "c"))) #> TRUE
#> [1] TRUE
has_names_valid(integer(0)) #> TRUE
#> [1] TRUE

# Use `how` to control how names are extracted:
has_names_valid(rlang::base_env(), how = "attr") #> FALSE
#> [1] FALSE
# (envs have no names attribute)
has_names_valid(c("a", "b", "c"), how = "x") #> TRUE (x itself was tested)
#> [1] TRUE

# Vectorized test:
are_names_valid(c("a", "b", "b", NA, ""), how = "x")
#> [1]  TRUE FALSE FALSE FALSE FALSE
#> c(TRUE, FALSE, FALSE, FALSE, FALSE)
```

## On this page

Test whether `x` has names with greater flexibility than
[`rlang::is_named()`](https://rlang.r-lib.org/reference/is_named.html),
handling NA, empty, duplicate, and invalid names, as well as empty
vectors.

## Usage

``` r
has_names_valid(
  x,
  na = FALSE,
  empty = FALSE,
  dups = FALSE,
  invalid = TRUE,
  zero_len = TRUE,
  how = "names"
)

are_names_valid(
  x,
  na = FALSE,
  empty = FALSE,
  dups = FALSE,
  invalid = TRUE,
  how = "names"
)
```

## Arguments

- x:

  \[`collection()`, `any`\] For `are_*()`, any collection to test; for
  `is_*()`, any object to test.

- na, empty, dups, invalid:

  \[`TRUE` \| `FALSE`\] What to return for NA, empty, duplicate, or
  invalid names.

- zero_len:

  \[`TRUE` \| `FALSE`\] What to return for an an empty `x`.

- how:

  \[`"names"` \| `"x"` \| `"attr"` \| `"names2"`\] How to extract names:
  "names" for [`names()`](https://rdrr.io/r/base/names.html); `"x"` to
  use `x` itself; "attr" for `attr(x, "names")`; or `"names2"` for
  [`rlang::names2()`](https://rlang.r-lib.org/reference/names2.html).

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Details

The default argument values guarantee that `x` can be safely iterated by
its names.

A `non_collection` is an object that is not an atomic vector, list,
pairlist, expression, or environment. That is, it returns `FALSE` for
[`is_collection()`](predicates-collections.md).

The `how` methods differ only for environments, with "names" returning
names and "attr" returning NULL.

`invalid = FALSE` checks if the names don't change after being passed to
[`make.names()`](https://rdrr.io/r/base/make.names.html).

## Examples

``` r
has_names_valid(mtcars) #> TRUE
#> [1] TRUE

# NA, empty, and duplicate names return FALSE by default:
has_names_valid(rlang::set_names(1:3, c("a", "b", NA))) #> FALSE
#> [1] FALSE
has_names_valid(rlang::set_names(1:3, c("a", "b", NA)), na = TRUE) #> TRUE
#> [1] TRUE

has_names_valid(rlang::set_names(1:3, c("a", "", "b"))) #> FALSE
#> [1] FALSE
has_names_valid(rlang::set_names(1:3, c("a", "a", "a"))) #> FALSE
#> [1] FALSE

# Invalid names and zero-length x's return TRUE by default:
has_names_valid(rlang::set_names(1:3, c("_bad", "b", "c"))) #> TRUE
#> [1] TRUE
has_names_valid(integer(0)) #> TRUE
#> [1] TRUE

# Use `how` to control how names are extracted:
has_names_valid(rlang::base_env(), how = "attr") #> FALSE
#> [1] FALSE
# (envs have no names attribute)
has_names_valid(c("a", "b", "c"), how = "x") #> TRUE (x itself was tested)
#> [1] TRUE

# Vectorized test:
are_names_valid(c("a", "b", "b", NA, ""), how = "x")
#> [1]  TRUE FALSE FALSE FALSE FALSE
#> c(TRUE, FALSE, FALSE, FALSE, FALSE)
```
