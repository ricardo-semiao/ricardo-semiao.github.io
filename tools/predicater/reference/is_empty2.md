# Metadata checks - Check if a collection is empty

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Is a collection object (see
[`is_collection()`](predicates-collections.md)) empty, i.e. has zero
length? Similar to
[`rlang::is_empty()`](https://rlang.r-lib.org/reference/is_empty.html),
but yields an error for non-collections, including `NULL` by default.

Note that objects of type 'S4' and 'object' are not considered
collections, even if they are 'filled' with slots/attributes.

## Usage

``` r
is_empty2(x, null = FALSE)
```

## Arguments

- x:

  \[`any`\] An object to test.

- null:

  \[`TRUE` \| `FALSE`\] Should `NULL` be considered a collection? If
  false will error for `NULL`, else, will return `TRUE`.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Examples

``` r
is_empty2(list()) #> TRUE
#> [1] TRUE
is_empty2(list(1)) #> FALSE
#> [1] FALSE
is_empty2(list(NULL)) #> FALSE
#> [1] FALSE

is_empty2(character(0)) #> TRUE
#> [1] TRUE
is_empty2(letters) #> FALSE
#> [1] FALSE

# Only works for collections (see ?is_collection()):
try(is_empty2(sum))
#> Error in is_empty2(sum) : `x` is not a collection.
#> Error in is_empty2(sum) : `x` is not a collection.

# But can be made to work with NULL:
is_empty2(NULL, null = TRUE) #> TRUE
#> [1] TRUE
```

## On this page

Is a collection object (see
[`is_collection()`](predicates-collections.md)) empty, i.e. has zero
length? Similar to
[`rlang::is_empty()`](https://rlang.r-lib.org/reference/is_empty.html),
but yields an error for non-collections, including `NULL` by default.

Note that objects of type 'S4' and 'object' are not considered
collections, even if they are 'filled' with slots/attributes.

## Usage

``` r
is_empty2(x, null = FALSE)
```

## Arguments

- x:

  \[`any`\] An object to test.

- null:

  \[`TRUE` \| `FALSE`\] Should `NULL` be considered a collection? If
  false will error for `NULL`, else, will return `TRUE`.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Examples

``` r
is_empty2(list()) #> TRUE
#> [1] TRUE
is_empty2(list(1)) #> FALSE
#> [1] FALSE
is_empty2(list(NULL)) #> FALSE
#> [1] FALSE

is_empty2(character(0)) #> TRUE
#> [1] TRUE
is_empty2(letters) #> FALSE
#> [1] FALSE

# Only works for collections (see ?is_collection()):
try(is_empty2(sum))
#> Error in is_empty2(sum) : `x` is not a collection.
#> Error in is_empty2(sum) : `x` is not a collection.

# But can be made to work with NULL:
is_empty2(NULL, null = TRUE) #> TRUE
#> [1] TRUE
```
