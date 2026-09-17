# Type checks - Atomic vectors

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Check if an object is of a specific atomic type
([`typeof()`](https://rdrr.io/r/base/typeof.html)). The test is
invariant to attributes such as class.

- [`rlang::is_logical()`](https://rlang.r-lib.org/reference/type-predicates.html),
  [`rlang::is_integer()`](https://rlang.r-lib.org/reference/type-predicates.html),
  [`rlang::is_double()`](https://rlang.r-lib.org/reference/type-predicates.html),
  [`rlang::is_complex()`](https://rlang.r-lib.org/reference/type-predicates.html),
  [`rlang::is_character()`](https://rlang.r-lib.org/reference/type-predicates.html),
  and
  [`rlang::is_raw()`](https://rlang.r-lib.org/reference/type-predicates.html)
  check if an object is of the respective atomic type.

- [`rlang::is_atomic()`](https://rlang.r-lib.org/reference/type-predicates.html)
  checks if an object is any of the above.

- `is_numeric()` checks if an object is either an integer or double
  vector.

## Usage

``` r
is_logical(x, n = NULL)

is_integer(x, n = NULL)

is_double(x, n = NULL, finite = NULL)

is_complex(x, n = NULL, finite = NULL)

is_character(x, n = NULL)

is_raw(x, n = NULL)

is_atomic(x, n = NULL)

is_numeric(x, n = NULL)
```

## Arguments

- x:

  \[`any`\] An object to test.

- n:

  \[`integer(1)` \| `NULL`\] Length of `x`, set to `NULL` to not test.

- finite:

  \[`TRUE` \| `FALSE` \| `NULL`\] Whether all values of the vector are
  not `NA`, `NaN`, `Inf`, or `-Inf`. Set to `NULL` to not test.
  [`is_finite()`](predicates-infinite.md) is designed to allow more
  flexibility to this test.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## On this page

Check if an object is of a specific atomic type
([`typeof()`](https://rdrr.io/r/base/typeof.html)). The test is
invariant to attributes such as class.

- [`rlang::is_logical()`](https://rlang.r-lib.org/reference/type-predicates.html),
  [`rlang::is_integer()`](https://rlang.r-lib.org/reference/type-predicates.html),
  [`rlang::is_double()`](https://rlang.r-lib.org/reference/type-predicates.html),
  [`rlang::is_complex()`](https://rlang.r-lib.org/reference/type-predicates.html),
  [`rlang::is_character()`](https://rlang.r-lib.org/reference/type-predicates.html),
  and
  [`rlang::is_raw()`](https://rlang.r-lib.org/reference/type-predicates.html)
  check if an object is of the respective atomic type.

- [`rlang::is_atomic()`](https://rlang.r-lib.org/reference/type-predicates.html)
  checks if an object is any of the above.

- `is_numeric()` checks if an object is either an integer or double
  vector.

## Usage

``` r
is_logical(x, n = NULL)

is_integer(x, n = NULL)

is_double(x, n = NULL, finite = NULL)

is_complex(x, n = NULL, finite = NULL)

is_character(x, n = NULL)

is_raw(x, n = NULL)

is_atomic(x, n = NULL)

is_numeric(x, n = NULL)
```

## Arguments

- x:

  \[`any`\] An object to test.

- n:

  \[`integer(1)` \| `NULL`\] Length of `x`, set to `NULL` to not test.

- finite:

  \[`TRUE` \| `FALSE` \| `NULL`\] Whether all values of the vector are
  not `NA`, `NaN`, `Inf`, or `-Inf`. Set to `NULL` to not test.
  [`is_finite()`](predicates-infinite.md) is designed to allow more
  flexibility to this test.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.
