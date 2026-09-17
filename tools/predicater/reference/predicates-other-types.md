# Type checks - Other types

[predicater](../index.md) 0.0.0.9000

- [Reference](../reference/index.md)
- [Changelog](../news/index.md)

&nbsp;

- 

Test if object is of a specific type
([`typeof()`](https://rdrr.io/r/base/typeof.html)). The test is
invariant to attributes such as class. The general `is_type()` checks
for any user-supplied type.

See the Details section for the full list of types.

Functions from rlang:
[`rlang::is_null()`](https://rlang.r-lib.org/reference/type-predicates.html),
[`rlang::is_weakref()`](https://rlang.r-lib.org/reference/is_weakref.html).

## Usage

``` r
is_type(x, type, n = NULL)

is_null()

is_promise(x)

is_dots(x, n = NULL)

is_weakref(x)

is_bytecode(x)

is_externalptr(x)

is_char(x)

is_any(x)
```

## Arguments

- x:

  \[`any`\] An object to test.

- type:

  \[`character(1)`\] A type to test for, as returned by
  [`typeof()`](https://rdrr.io/r/base/typeof.html).

- n:

  \[`integer(1)` \| `NULL`\] Length of `x`, set to `NULL` to not test.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Details

The full list of R object types
([`typeof()`](https://rdrr.io/r/base/typeof.html)) can be seen in ["R
Internals" section
1.1.3](https://cran.r-project.org/doc/manuals/r-release/R-ints.html#The-_0060data_0027).

The existing types and their corresponding C SEXP types are:

- Atomic vectors: *"logical"/LGLSXP*, *"integer"/INTSXP*,
  *"double"/"numeric"/REALSXP*, *"complex"/CPLXSXP*, *"raw"*/RAWSXP.

- Lists: *"list"/VECSXP*, *"pairlist"/LISTSXP*.

- Objects: *"s4"/S4SXP, "object"/OBJSXP*.

- Language-related: *"symbol"/"name"/SYMSXP*, *"language"/LANGSXP*,
  *"expression"/EXPRSXP*.

- Functions: *"closure"/CLOSXP*, *"builtin"/SPECIALSXP*,
  *"special"/BUILTINSXP*.

- Promises: *"promise"/PROMSXP*, *"..."/DOTSXP*.

- Environments: *"environment"/ENVSXP*.

- Null: *"NULL"/NILSXP*.

- Bytecode: *"bytecode"/BCODESXP*.

- External pointer: *"externalptr"/EXTPTRSXP*.

- Weak reference: *"weakref"/WEAKREFSXP*.

- Internal-only: *"char"/CHARSXP*, *"any"/ANYSXP*.

## Examples

``` r
is_type(1:10, "integer") #> TRUE
#> [1] TRUE
is_type(NULL, "NULL") #> TRUE
#> [1] TRUE
```

## On this page

Test if object is of a specific type
([`typeof()`](https://rdrr.io/r/base/typeof.html)). The test is
invariant to attributes such as class. The general `is_type()` checks
for any user-supplied type.

See the Details section for the full list of types.

Functions from rlang:
[`rlang::is_null()`](https://rlang.r-lib.org/reference/type-predicates.html),
[`rlang::is_weakref()`](https://rlang.r-lib.org/reference/is_weakref.html).

## Usage

``` r
is_type(x, type, n = NULL)

is_null()

is_promise(x)

is_dots(x, n = NULL)

is_weakref(x)

is_bytecode(x)

is_externalptr(x)

is_char(x)

is_any(x)
```

## Arguments

- x:

  \[`any`\] An object to test.

- type:

  \[`character(1)`\] A type to test for, as returned by
  [`typeof()`](https://rdrr.io/r/base/typeof.html).

- n:

  \[`integer(1)` \| `NULL`\] Length of `x`, set to `NULL` to not test.

## Value

\[`TRUE` \| `FALSE`\] The scalar result of the test.

## Details

The full list of R object types
([`typeof()`](https://rdrr.io/r/base/typeof.html)) can be seen in ["R
Internals" section
1.1.3](https://cran.r-project.org/doc/manuals/r-release/R-ints.html#The-_0060data_0027).

The existing types and their corresponding C SEXP types are:

- Atomic vectors: *"logical"/LGLSXP*, *"integer"/INTSXP*,
  *"double"/"numeric"/REALSXP*, *"complex"/CPLXSXP*, *"raw"*/RAWSXP.

- Lists: *"list"/VECSXP*, *"pairlist"/LISTSXP*.

- Objects: *"s4"/S4SXP, "object"/OBJSXP*.

- Language-related: *"symbol"/"name"/SYMSXP*, *"language"/LANGSXP*,
  *"expression"/EXPRSXP*.

- Functions: *"closure"/CLOSXP*, *"builtin"/SPECIALSXP*,
  *"special"/BUILTINSXP*.

- Promises: *"promise"/PROMSXP*, *"..."/DOTSXP*.

- Environments: *"environment"/ENVSXP*.

- Null: *"NULL"/NILSXP*.

- Bytecode: *"bytecode"/BCODESXP*.

- External pointer: *"externalptr"/EXTPTRSXP*.

- Weak reference: *"weakref"/WEAKREFSXP*.

- Internal-only: *"char"/CHARSXP*, *"any"/ANYSXP*.

## Examples

``` r
is_type(1:10, "integer") #> TRUE
#> [1] TRUE
is_type(NULL, "NULL") #> TRUE
#> [1] TRUE
```
