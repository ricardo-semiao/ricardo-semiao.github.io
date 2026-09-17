# Type checks - Determine object-oriented system of object

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

R has many object-oriented systems, including S3, S4, RC, R6, R.oo, S7,
proto, and ggproto. This function determines to which of these an object
belongs, extending the test done by
[`sloop::otype()`](https://sloop.r-lib.org/reference/otype.html).

If `x` fails [`is.object()`](https://rdrr.io/r/base/is.object.html), the
function returns `"base"`. `x` matches `"S3"` if it is an object but
does not match any other system, so systems not implemented here will
fall into that category.

`is_system()` tests if an object belongs to a specific system.

## Usage

``` r
object_system(x)

is_system(x, system)
```

## Arguments

- x:

  \[`any`\] An object to test.

- system:

  \[`character(1)`\] Object-oriented system to check for.

## Value

- \[`character(1)`\] For `object_system()`: the object-oriented system
  of `x`.

- \[`TRUE` \| `FALSE`\] For `is_system()`: The scalar result of the
  test.

## Details

The implemented check is as below:

1.  If not [`is.object()`](https://rdrr.io/r/base/is.object.html),
    return `"base"`.

2.  Else, if [`isS4()`](https://rdrr.io/r/base/isS4.html), return `"RC"`
    if `is(x, "refClass")`, else return `"S4"`.

3.  Else, if `inherits_any(x, "S7_object")` and `typeof(x) == "object"`
    (as an additional safeguard), return `"S7"`.

4.  Else, if `inherits_any(x, "R6")` and
    [`rlang::is_environment()`](https://rlang.r-lib.org/reference/is_environment.html),
    return `"R6"`.

5.  Else, if `inherits_any(x, "ggproto")` and
    [`rlang::is_environment()`](https://rlang.r-lib.org/reference/is_environment.html),

6.  return `"ggproto"`.

7.  Else, if `inherits_any(x, "proto")` and
    `all(c(".super", ".that") %in% names(x))` and
    [`rlang::is_environment()`](https://rlang.r-lib.org/reference/is_environment.html),
    return `"proto"`.

8.  Else, if `inherits_any(x, "Object")` and
    `all(c(".env", "...modifiers", "...finalize") %in% names(attributes(x)))`
    and `is_logical(x, 1)`, return `"R.oo"`.

## Examples

``` r
object_system(1:10) #> "base"
#> [1] "base"

object_system(factor(letters)) #> "S3"
#> [1] "S3"

xs4 <- methods::setClass("my_s4_int", contains = "integer")(1:10)
object_system(xs4) #> "S4"
#> [1] "S4"

is_system(xs4, "S4") #> TRUE
#> [1] TRUE
```

## On this page

R has many object-oriented systems, including S3, S4, RC, R6, R.oo, S7,
proto, and ggproto. This function determines to which of these an object
belongs, extending the test done by
[`sloop::otype()`](https://sloop.r-lib.org/reference/otype.html).

If `x` fails [`is.object()`](https://rdrr.io/r/base/is.object.html), the
function returns `"base"`. `x` matches `"S3"` if it is an object but
does not match any other system, so systems not implemented here will
fall into that category.

`is_system()` tests if an object belongs to a specific system.

## Usage

``` r
object_system(x)

is_system(x, system)
```

## Arguments

- x:

  \[`any`\] An object to test.

- system:

  \[`character(1)`\] Object-oriented system to check for.

## Value

- \[`character(1)`\] For `object_system()`: the object-oriented system
  of `x`.

- \[`TRUE` \| `FALSE`\] For `is_system()`: The scalar result of the
  test.

## Details

The implemented check is as below:

1.  If not [`is.object()`](https://rdrr.io/r/base/is.object.html),
    return `"base"`.

2.  Else, if [`isS4()`](https://rdrr.io/r/base/isS4.html), return `"RC"`
    if `is(x, "refClass")`, else return `"S4"`.

3.  Else, if `inherits_any(x, "S7_object")` and `typeof(x) == "object"`
    (as an additional safeguard), return `"S7"`.

4.  Else, if `inherits_any(x, "R6")` and
    [`rlang::is_environment()`](https://rlang.r-lib.org/reference/is_environment.html),
    return `"R6"`.

5.  Else, if `inherits_any(x, "ggproto")` and
    [`rlang::is_environment()`](https://rlang.r-lib.org/reference/is_environment.html),

6.  return `"ggproto"`.

7.  Else, if `inherits_any(x, "proto")` and
    `all(c(".super", ".that") %in% names(x))` and
    [`rlang::is_environment()`](https://rlang.r-lib.org/reference/is_environment.html),
    return `"proto"`.

8.  Else, if `inherits_any(x, "Object")` and
    `all(c(".env", "...modifiers", "...finalize") %in% names(attributes(x)))`
    and `is_logical(x, 1)`, return `"R.oo"`.

## Examples

``` r
object_system(1:10) #> "base"
#> [1] "base"

object_system(factor(letters)) #> "S3"
#> [1] "S3"

xs4 <- methods::setClass("my_s4_int", contains = "integer")(1:10)
object_system(xs4) #> "S4"
#> [1] "S4"

is_system(xs4, "S4") #> TRUE
#> [1] TRUE
```
