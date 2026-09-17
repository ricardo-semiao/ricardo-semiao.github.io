# Attribute utilities - Get attribute of object

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Identical to [`attr()`](https://rdrr.io/r/base/attr.html) but with
`exact = TRUE` by default.

## Usage

``` r
attr2(x, which, exact = TRUE)
```

## Arguments

- x:

  \[`any`\] Object to get attribute from.

- which:

  \[`character(1)`\] Name of attribute to get.

- exact:

  \[`TRUE` \| `FALSE`\] Whether to match attribute name exactly, or
  allow partial matching.

## Value

\[`any`\] The value of the attribute matched, or NULL if no match was
found.

## Examples

``` r
x <- structure(1, long_name = 2)

# Exact matches by default:
attr(x, "long") #> 2
#> [1] 2
attr2(x, "long") #> NULL
#> NULL
```

## On this page

Identical to [`attr()`](https://rdrr.io/r/base/attr.html) but with
`exact = TRUE` by default.

## Usage

``` r
attr2(x, which, exact = TRUE)
```

## Arguments

- x:

  \[`any`\] Object to get attribute from.

- which:

  \[`character(1)`\] Name of attribute to get.

- exact:

  \[`TRUE` \| `FALSE`\] Whether to match attribute name exactly, or
  allow partial matching.

## Value

\[`any`\] The value of the attribute matched, or NULL if no match was
found.

## Examples

``` r
x <- structure(1, long_name = 2)

# Exact matches by default:
attr(x, "long") #> 2
#> [1] 2
attr2(x, "long") #> NULL
#> NULL
```
