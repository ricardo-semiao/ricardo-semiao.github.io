# Attribute checks - Check if object allows attributes

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

In R, some objects do not allow attributes to be set on them. This
function checks whether `attr(x, which) <- value` runs without errors.
See [`attr()`](https://rdrr.io/r/base/attr.html) for details.

Up to R version 4.6.0, only three object types
([`typeof()`](https://rdrr.io/r/base/typeof.html)) disallow attributes:

- `"primitive"` starting in R 4.6.0.

- `"symbol"` starting in R 3.5.0.

- `"NULL"` starting in R 3.4.0.

Besides these, objects of type `"char"` and `"any"`, which exist only in
the internals of R, always return `FALSE`.

## Usage

``` r
is_attrs_allowed(x, cnd_match = NULL, warn = "tw")
```

## Arguments

- x:

  \[`any`\] An object to test.

- cnd_match:

  \[`character(1)`\] String to match in the condition message. If no
  match, the condition is re-thrown. Defaults to allow any message.

- warn:

  \[`"true"` \| `"false"` \| `"warn"` \| `"error"`\] How to handle
  warnings: `"false"` to return `FALSE`;
  ``` "true"`` for  ```TRUE`; `"warn"`to return`TRUE`but re-throw the warning; and`"error"\`
  to throw the warning as an error.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test. Or, re-throws the
caught condition.

## Examples

``` r
is_attrs_allowed(mtcars) #> TRUE
#> [1] TRUE
is_attrs_allowed(NULL) #> FALSE
#> [1] FALSE
```

## On this page

In R, some objects do not allow attributes to be set on them. This
function checks whether `attr(x, which) <- value` runs without errors.
See [`attr()`](https://rdrr.io/r/base/attr.html) for details.

Up to R version 4.6.0, only three object types
([`typeof()`](https://rdrr.io/r/base/typeof.html)) disallow attributes:

- `"primitive"` starting in R 4.6.0.

- `"symbol"` starting in R 3.5.0.

- `"NULL"` starting in R 3.4.0.

Besides these, objects of type `"char"` and `"any"`, which exist only in
the internals of R, always return `FALSE`.

## Usage

``` r
is_attrs_allowed(x, cnd_match = NULL, warn = "tw")
```

## Arguments

- x:

  \[`any`\] An object to test.

- cnd_match:

  \[`character(1)`\] String to match in the condition message. If no
  match, the condition is re-thrown. Defaults to allow any message.

- warn:

  \[`"true"` \| `"false"` \| `"warn"` \| `"error"`\] How to handle
  warnings: `"false"` to return `FALSE`;
  ``` "true"`` for  ```TRUE`; `"warn"`to return`TRUE`but re-throw the warning; and`"error"\`
  to throw the warning as an error.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test. Or, re-throws the
caught condition.

## Examples

``` r
is_attrs_allowed(mtcars) #> TRUE
#> [1] TRUE
is_attrs_allowed(NULL) #> FALSE
#> [1] FALSE
```
