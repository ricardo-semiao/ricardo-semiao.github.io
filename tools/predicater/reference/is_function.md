# Type checks - Functions

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

There are three types ([`typeof()`](https://rdrr.io/r/base/typeof.html))
of functions in R: `"closure"` (standard functions), or
`"builtin"`/`"special"` (primitive, special functions). See
[`rlang::is_function()`](https://rlang.r-lib.org/reference/is_function.html)
for more details on their difference.

- [`rlang::is_function()`](https://rlang.r-lib.org/reference/is_function.html)
  tests for any function type.

- [`rlang::is_closure()`](https://rlang.r-lib.org/reference/is_function.html)
  tests for closures.

- [`rlang::is_primitive()`](https://rlang.r-lib.org/reference/is_function.html)
  tests for `"builtin"` or `"special"`.

- [`rlang::is_primitive_eager()`](https://rlang.r-lib.org/reference/is_function.html)
  tests for `"builtin"`.

- [`rlang::is_primitive_lazy()`](https://rlang.r-lib.org/reference/is_function.html)
  tests for `"special"`.

## Usage

``` r
is_function(x)

is_closure(x)

is_primitive(x)

is_primitive_eager(x)

is_primitive_lazy(x)
```

## Arguments

- x:

  \[`any`\] An object to test.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## On this page

There are three types ([`typeof()`](https://rdrr.io/r/base/typeof.html))
of functions in R: `"closure"` (standard functions), or
`"builtin"`/`"special"` (primitive, special functions). See
[`rlang::is_function()`](https://rlang.r-lib.org/reference/is_function.html)
for more details on their difference.

- [`rlang::is_function()`](https://rlang.r-lib.org/reference/is_function.html)
  tests for any function type.

- [`rlang::is_closure()`](https://rlang.r-lib.org/reference/is_function.html)
  tests for closures.

- [`rlang::is_primitive()`](https://rlang.r-lib.org/reference/is_function.html)
  tests for `"builtin"` or `"special"`.

- [`rlang::is_primitive_eager()`](https://rlang.r-lib.org/reference/is_function.html)
  tests for `"builtin"`.

- [`rlang::is_primitive_lazy()`](https://rlang.r-lib.org/reference/is_function.html)
  tests for `"special"`.

## Usage

``` r
is_function(x)

is_closure(x)

is_primitive(x)

is_primitive_eager(x)

is_primitive_lazy(x)
```

## Arguments

- x:

  \[`any`\] An object to test.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.
