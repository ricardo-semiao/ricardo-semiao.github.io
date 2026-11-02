# Package index

[predicater](index.md) 0.0.0.9000

- [Reference](reference/index.md)
- [Changelog](news/index.md)

&nbsp;

- 
- [](https://github.com/ricardo-semiao/predicater/)

## Simple predicates

### Atomic vectors

- [`is_logical()`](reference/predicates-atomic.md)
  [`is_integer()`](reference/predicates-atomic.md)
  [`is_double()`](reference/predicates-atomic.md)
  [`is_complex()`](reference/predicates-atomic.md)
  [`is_character()`](reference/predicates-atomic.md)
  [`is_raw()`](reference/predicates-atomic.md)
  [`is_atomic()`](reference/predicates-atomic.md)
  [`is_numeric()`](reference/predicates-atomic.md) : Type checks -
  Atomic vectors
- [`are_integer_like()`](reference/is_integer_like.md)
  [`is_integer_like()`](reference/is_integer_like.md) : Type checks -
  Integer-like values
- [`are_true()`](reference/predicates-true-false.md)
  [`is_true2()`](reference/predicates-true-false.md)
  [`are_false()`](reference/predicates-true-false.md)
  [`is_false2()`](reference/predicates-true-false.md)
  [`is_bool2()`](reference/predicates-true-false.md) : Type checks -
  TRUE and FALSE values
- [`are_na2()`](reference/is_na2.md) [`is_na2()`](reference/is_na2.md) :
  Type checks - NA values
- [`are_finite()`](reference/predicates-infinite.md)
  [`is_finite()`](reference/predicates-infinite.md)
  [`are_nan()`](reference/predicates-infinite.md)
  [`is_nan()`](reference/predicates-infinite.md)
  [`are_inf()`](reference/predicates-infinite.md)
  [`is_inf()`](reference/predicates-infinite.md) : Type checks - Inf and
  NaN

### Other types

- [`is_list()`](reference/predicates-collections.md)
  [`is_pairlist2()`](reference/predicates-collections.md)
  [`is_environment2()`](reference/predicates-collections.md)
  [`is_vector()`](reference/predicates-collections.md)
  [`is_collection()`](reference/predicates-collections.md) : Type
  checks - Collection types
- [`is_syntactic_literal()`](reference/predicates-language.md)
  [`is_symbol2()`](reference/predicates-language.md)
  [`is_language()`](reference/predicates-language.md)
  [`is_call()`](reference/predicates-language.md)
  [`is_expression2()`](reference/predicates-language.md)
  [`is_code()`](reference/predicates-language.md) : Type checks -
  Language objects
- [`is_function()`](reference/is_function.md)
  [`is_closure()`](reference/is_function.md)
  [`is_primitive()`](reference/is_function.md)
  [`is_primitive_eager()`](reference/is_function.md)
  [`is_primitive_lazy()`](reference/is_function.md) : Type checks -
  Functions
- [`is_type()`](reference/predicates-other-types.md)
  [`is_null()`](reference/predicates-other-types.md)
  [`is_promise()`](reference/predicates-other-types.md)
  [`is_dots()`](reference/predicates-other-types.md)
  [`is_weakref()`](reference/predicates-other-types.md)
  [`is_bytecode()`](reference/predicates-other-types.md)
  [`is_externalptr()`](reference/predicates-other-types.md)
  [`is_char()`](reference/predicates-other-types.md)
  [`is_any()`](reference/predicates-other-types.md) : Type checks -
  Other types

### attributes

- [`is_attrs_allowed()`](reference/is_attrs_allowed.md) : Attribute
  checks - Check if object allows attributes
- [`has_names_valid()`](reference/has_names_valid.md)
  [`are_names_valid()`](reference/has_names_valid.md) : Attribute
  checks - Names
- [`n_dims()`](reference/attributes-dimensions.md)
  [`n_dimnames()`](reference/attributes-dimensions.md)
  [`has_dimnames()`](reference/attributes-dimensions.md)
  [`has_rownames()`](reference/attributes-dimensions.md)
  [`has_dim()`](reference/attributes-dimensions.md) : Attribute checks -
  Dimensions existence and sizes
- [`attrs_rmv()`](reference/attributes-filter.md)
  [`attrs_keep()`](reference/attributes-filter.md)
  [`has_attrs_any()`](reference/attributes-filter.md)
  [`has_attrs_all()`](reference/attributes-filter.md)
  [`has_attrs_only()`](reference/attributes-filter.md) : Attribute
  checks - Check for and filter attributes from object

### Object systems

- [`has_object_bit()`](reference/predicates-objects.md)
  [`has_s4_bit()`](reference/predicates-objects.md)
  [`has_class()`](reference/predicates-objects.md)
  [`is_object_like()`](reference/predicates-objects.md)
  [`is_s4()`](reference/predicates-objects.md)
  [`is_object()`](reference/predicates-objects.md) : Type checks -
  Objects
- [`object_system()`](reference/object_system.md)
  [`is_system()`](reference/object_system.md) : Type checks - Determine
  object-oriented system of object

### Data

- [`is_sorted()`](reference/is_sorted.md) : Data checks - Check if
  object is ordered
- [`is_matching_set()`](reference/is_matching_set.md) : Data checks -
  Check if object is in (and/or not in) a set
- [`any_duplicated()`](reference/any_duplicated.md)
  [`are_duplicated()`](reference/any_duplicated.md) : Data checks -
  Check for duplicate values
- [`is_empty2()`](reference/is_empty2.md) : Metadata checks - Check if a
  collection is empty

## Object comparison

### Comparison and prototypes

- [`identical2()`](reference/identical2.md)
  [`identical_flag()`](reference/identical2.md) : Compare - Exact
  equality with more flexibility
- [`is_ptype()`](reference/is_ptype.md)
  [`is_ptype_list()`](reference/is_ptype.md) : Compare - Check if object
  is of prototype

### If-else and pattern matching

- [`match_hash()`](reference/match_hash.md)
  [`match_id()`](reference/match_hash.md)
  [`match_ptype()`](reference/match_hash.md)
  [`match_when()`](reference/match_hash.md) : Compare - Pattern matching
- [`if_else2()`](reference/if_else2.md) : Compare - Vectorized if-else
- [`case_when2()`](reference/case_when2.md) : Compare - Vectorized
  nested if-else

## Complex predicates and validation

### Atomic vectors

- [`test_integer()`](reference/tests-numeric.md)
  [`test_double()`](reference/tests-numeric.md)
  [`test_complex()`](reference/tests-numeric.md)
  [`assert_integer()`](reference/tests-numeric.md)
  [`assert_double()`](reference/tests-numeric.md)
  [`assert_complex()`](reference/tests-numeric.md) : Validation -
  Numeric vectors
- [`test_logical()`](reference/test-logical_raw.md)
  [`test_raw()`](reference/test-logical_raw.md)
  [`assert_logical()`](reference/test-logical_raw.md)
  [`assert_raw()`](reference/test-logical_raw.md) : Validation - Logical
  and Raw vectors
- [`test_character()`](reference/test_character.md)
  [`assert_character()`](reference/test_character.md) : Validation -
  Character vectors

### Language objects

- [`test_expression()`](reference/test_expression.md)
  [`assert_expression()`](reference/test_expression.md) : Validation -
  Expression vectors
- [`test_symbol()`](reference/test_symbol.md)
  [`assert_symbol()`](reference/test_symbol.md) : Validation - Symbol
- [`test_language()`](reference/test_language.md)
  [`assert_language()`](reference/test_language.md) : Validation -
  Language
- [`test_code()`](reference/test_code.md)
  [`assert_code()`](reference/test_code.md) : Validation - Code Objects

### Other types

- [`test_list()`](reference/test_list.md)
  [`assert_list()`](reference/test_list.md) : Validation - List
- [`test_vector()`](reference/test_vector.md)
  [`assert_vector()`](reference/test_vector.md) : Validation - General
  vectors
- [`test_environment()`](reference/test_environment.md)
  [`assert_environment()`](reference/test_environment.md) : Validation -
  Environment
- [`test_function()`](reference/test_function.md)
  [`assert_function()`](reference/test_function.md) : Validation -
  Function
- [`test_promise()`](reference/tests-other_types.md)
  [`test_dots()`](reference/tests-other_types.md)
  [`test_weakref()`](reference/tests-other_types.md)
  [`test_bytecode()`](reference/tests-other_types.md)
  [`test_externalptr()`](reference/tests-other_types.md)
  [`assert_null()`](reference/tests-other_types.md)
  [`assert_promise()`](reference/tests-other_types.md)
  [`assert_dots()`](reference/tests-other_types.md)
  [`assert_weakref()`](reference/tests-other_types.md)
  [`assert_bytecode()`](reference/tests-other_types.md)
  [`assert_externalptr()`](reference/tests-other_types.md) :
  Validation - Other types

### Attributes

- [`test_names()`](reference/test_names.md)
  [`assert_names()`](reference/test_names.md) : Validation - Names
  attribute
- [`test_matrix()`](reference/test_matrix.md)
  [`assert_matrix()`](reference/test_matrix.md) : Validation - Matrix
  and array attributes
- [`test_class()`](reference/test_class.md)
  [`assert_class()`](reference/test_class.md) : Validation - Class
  attribute
- [`test_object()`](reference/test_object.md)
  [`assert_object()`](reference/test_object.md) : Validation -
  Object-related attributes

### Validation via external functions

- [`assert_from_msg()`](reference/assert_from_msg.md)
  [`assert_from_error()`](reference/assert_from_msg.md) : Validation -
  Rethrow errors with more information
- [`assert_ptype()`](reference/assert_ptype.md) : Validation - If object
  is of prototype
- [`assert_predicate()`](reference/assert_predicate.md) : Validation -
  Throw error from custom predicate
- [`test_multiple()`](reference/test_multiple.md) : Validation - Test
  for one of multiple types

## Utilities

### Logical utilities

- [`pany()`](reference/pany.md) [`pall()`](reference/pany.md)
  [`pany_na()`](reference/pany.md) [`pall_na()`](reference/pany.md) :
  Parallel any and all
- [`reduce_predicate()`](reference/reduce_predicate.md)
  [`accumulate_predicate()`](reference/reduce_predicate.md) : Reduce
  binary predicate over a list

### Attributes utilities

- [`attrs_rmv()`](reference/attributes-filter.md)
  [`attrs_keep()`](reference/attributes-filter.md)
  [`has_attrs_any()`](reference/attributes-filter.md)
  [`has_attrs_all()`](reference/attributes-filter.md)
  [`has_attrs_only()`](reference/attributes-filter.md) : Attribute
  checks - Check for and filter attributes from object
- [`names3()`](reference/attributes-getters-setters.md)
  [`` `names3<-`() ``](reference/attributes-getters-setters.md)
  [`dimnames2()`](reference/attributes-getters-setters.md)
  [`` `dimnames2<-`() ``](reference/attributes-getters-setters.md)
  [`rownames2()`](reference/attributes-getters-setters.md)
  [`` `rownames2<-`() ``](reference/attributes-getters-setters.md)
  [`class2()`](reference/attributes-getters-setters.md)
  [`` `class2<-`() ``](reference/attributes-getters-setters.md) :
  Attribute utilities - Getters and setters
- [`attr2()`](reference/attr2.md) : Attribute utilities - Get attribute
  of object

### Others

- [`check_installed2()`](reference/check_installed2.md) : Check if user
  accepted a package installation
- [`c2()`](reference/c2.md) : Combine many vectors into one vector

## On this page

## Simple predicates

### Atomic vectors

- [`is_logical()`](reference/predicates-atomic.md)
  [`is_integer()`](reference/predicates-atomic.md)
  [`is_double()`](reference/predicates-atomic.md)
  [`is_complex()`](reference/predicates-atomic.md)
  [`is_character()`](reference/predicates-atomic.md)
  [`is_raw()`](reference/predicates-atomic.md)
  [`is_atomic()`](reference/predicates-atomic.md)
  [`is_numeric()`](reference/predicates-atomic.md) : Type checks -
  Atomic vectors
- [`are_integer_like()`](reference/is_integer_like.md)
  [`is_integer_like()`](reference/is_integer_like.md) : Type checks -
  Integer-like values
- [`are_true()`](reference/predicates-true-false.md)
  [`is_true2()`](reference/predicates-true-false.md)
  [`are_false()`](reference/predicates-true-false.md)
  [`is_false2()`](reference/predicates-true-false.md)
  [`is_bool2()`](reference/predicates-true-false.md) : Type checks -
  TRUE and FALSE values
- [`are_na2()`](reference/is_na2.md) [`is_na2()`](reference/is_na2.md) :
  Type checks - NA values
- [`are_finite()`](reference/predicates-infinite.md)
  [`is_finite()`](reference/predicates-infinite.md)
  [`are_nan()`](reference/predicates-infinite.md)
  [`is_nan()`](reference/predicates-infinite.md)
  [`are_inf()`](reference/predicates-infinite.md)
  [`is_inf()`](reference/predicates-infinite.md) : Type checks - Inf and
  NaN

### Other types

- [`is_list()`](reference/predicates-collections.md)
  [`is_pairlist2()`](reference/predicates-collections.md)
  [`is_environment2()`](reference/predicates-collections.md)
  [`is_vector()`](reference/predicates-collections.md)
  [`is_collection()`](reference/predicates-collections.md) : Type
  checks - Collection types
- [`is_syntactic_literal()`](reference/predicates-language.md)
  [`is_symbol2()`](reference/predicates-language.md)
  [`is_language()`](reference/predicates-language.md)
  [`is_call()`](reference/predicates-language.md)
  [`is_expression2()`](reference/predicates-language.md)
  [`is_code()`](reference/predicates-language.md) : Type checks -
  Language objects
- [`is_function()`](reference/is_function.md)
  [`is_closure()`](reference/is_function.md)
  [`is_primitive()`](reference/is_function.md)
  [`is_primitive_eager()`](reference/is_function.md)
  [`is_primitive_lazy()`](reference/is_function.md) : Type checks -
  Functions
- [`is_type()`](reference/predicates-other-types.md)
  [`is_null()`](reference/predicates-other-types.md)
  [`is_promise()`](reference/predicates-other-types.md)
  [`is_dots()`](reference/predicates-other-types.md)
  [`is_weakref()`](reference/predicates-other-types.md)
  [`is_bytecode()`](reference/predicates-other-types.md)
  [`is_externalptr()`](reference/predicates-other-types.md)
  [`is_char()`](reference/predicates-other-types.md)
  [`is_any()`](reference/predicates-other-types.md) : Type checks -
  Other types

### attributes

- [`is_attrs_allowed()`](reference/is_attrs_allowed.md) : Attribute
  checks - Check if object allows attributes
- [`has_names_valid()`](reference/has_names_valid.md)
  [`are_names_valid()`](reference/has_names_valid.md) : Attribute
  checks - Names
- [`n_dims()`](reference/attributes-dimensions.md)
  [`n_dimnames()`](reference/attributes-dimensions.md)
  [`has_dimnames()`](reference/attributes-dimensions.md)
  [`has_rownames()`](reference/attributes-dimensions.md)
  [`has_dim()`](reference/attributes-dimensions.md) : Attribute checks -
  Dimensions existence and sizes
- [`attrs_rmv()`](reference/attributes-filter.md)
  [`attrs_keep()`](reference/attributes-filter.md)
  [`has_attrs_any()`](reference/attributes-filter.md)
  [`has_attrs_all()`](reference/attributes-filter.md)
  [`has_attrs_only()`](reference/attributes-filter.md) : Attribute
  checks - Check for and filter attributes from object

### Object systems

- [`has_object_bit()`](reference/predicates-objects.md)
  [`has_s4_bit()`](reference/predicates-objects.md)
  [`has_class()`](reference/predicates-objects.md)
  [`is_object_like()`](reference/predicates-objects.md)
  [`is_s4()`](reference/predicates-objects.md)
  [`is_object()`](reference/predicates-objects.md) : Type checks -
  Objects
- [`object_system()`](reference/object_system.md)
  [`is_system()`](reference/object_system.md) : Type checks - Determine
  object-oriented system of object

### Data

- [`is_sorted()`](reference/is_sorted.md) : Data checks - Check if
  object is ordered
- [`is_matching_set()`](reference/is_matching_set.md) : Data checks -
  Check if object is in (and/or not in) a set
- [`any_duplicated()`](reference/any_duplicated.md)
  [`are_duplicated()`](reference/any_duplicated.md) : Data checks -
  Check for duplicate values
- [`is_empty2()`](reference/is_empty2.md) : Metadata checks - Check if a
  collection is empty

## Object comparison

### Comparison and prototypes

- [`identical2()`](reference/identical2.md)
  [`identical_flag()`](reference/identical2.md) : Compare - Exact
  equality with more flexibility
- [`is_ptype()`](reference/is_ptype.md)
  [`is_ptype_list()`](reference/is_ptype.md) : Compare - Check if object
  is of prototype

### If-else and pattern matching

- [`match_hash()`](reference/match_hash.md)
  [`match_id()`](reference/match_hash.md)
  [`match_ptype()`](reference/match_hash.md)
  [`match_when()`](reference/match_hash.md) : Compare - Pattern matching
- [`if_else2()`](reference/if_else2.md) : Compare - Vectorized if-else
- [`case_when2()`](reference/case_when2.md) : Compare - Vectorized
  nested if-else

## Complex predicates and validation

### Atomic vectors

- [`test_integer()`](reference/tests-numeric.md)
  [`test_double()`](reference/tests-numeric.md)
  [`test_complex()`](reference/tests-numeric.md)
  [`assert_integer()`](reference/tests-numeric.md)
  [`assert_double()`](reference/tests-numeric.md)
  [`assert_complex()`](reference/tests-numeric.md) : Validation -
  Numeric vectors
- [`test_logical()`](reference/test-logical_raw.md)
  [`test_raw()`](reference/test-logical_raw.md)
  [`assert_logical()`](reference/test-logical_raw.md)
  [`assert_raw()`](reference/test-logical_raw.md) : Validation - Logical
  and Raw vectors
- [`test_character()`](reference/test_character.md)
  [`assert_character()`](reference/test_character.md) : Validation -
  Character vectors

### Language objects

- [`test_expression()`](reference/test_expression.md)
  [`assert_expression()`](reference/test_expression.md) : Validation -
  Expression vectors
- [`test_symbol()`](reference/test_symbol.md)
  [`assert_symbol()`](reference/test_symbol.md) : Validation - Symbol
- [`test_language()`](reference/test_language.md)
  [`assert_language()`](reference/test_language.md) : Validation -
  Language
- [`test_code()`](reference/test_code.md)
  [`assert_code()`](reference/test_code.md) : Validation - Code Objects

### Other types

- [`test_list()`](reference/test_list.md)
  [`assert_list()`](reference/test_list.md) : Validation - List
- [`test_vector()`](reference/test_vector.md)
  [`assert_vector()`](reference/test_vector.md) : Validation - General
  vectors
- [`test_environment()`](reference/test_environment.md)
  [`assert_environment()`](reference/test_environment.md) : Validation -
  Environment
- [`test_function()`](reference/test_function.md)
  [`assert_function()`](reference/test_function.md) : Validation -
  Function
- [`test_promise()`](reference/tests-other_types.md)
  [`test_dots()`](reference/tests-other_types.md)
  [`test_weakref()`](reference/tests-other_types.md)
  [`test_bytecode()`](reference/tests-other_types.md)
  [`test_externalptr()`](reference/tests-other_types.md)
  [`assert_null()`](reference/tests-other_types.md)
  [`assert_promise()`](reference/tests-other_types.md)
  [`assert_dots()`](reference/tests-other_types.md)
  [`assert_weakref()`](reference/tests-other_types.md)
  [`assert_bytecode()`](reference/tests-other_types.md)
  [`assert_externalptr()`](reference/tests-other_types.md) :
  Validation - Other types

### Attributes

- [`test_names()`](reference/test_names.md)
  [`assert_names()`](reference/test_names.md) : Validation - Names
  attribute
- [`test_matrix()`](reference/test_matrix.md)
  [`assert_matrix()`](reference/test_matrix.md) : Validation - Matrix
  and array attributes
- [`test_class()`](reference/test_class.md)
  [`assert_class()`](reference/test_class.md) : Validation - Class
  attribute
- [`test_object()`](reference/test_object.md)
  [`assert_object()`](reference/test_object.md) : Validation -
  Object-related attributes

### Validation via external functions

- [`assert_from_msg()`](reference/assert_from_msg.md)
  [`assert_from_error()`](reference/assert_from_msg.md) : Validation -
  Rethrow errors with more information
- [`assert_ptype()`](reference/assert_ptype.md) : Validation - If object
  is of prototype
- [`assert_predicate()`](reference/assert_predicate.md) : Validation -
  Throw error from custom predicate
- [`test_multiple()`](reference/test_multiple.md) : Validation - Test
  for one of multiple types

## Utilities

### Logical utilities

- [`pany()`](reference/pany.md) [`pall()`](reference/pany.md)
  [`pany_na()`](reference/pany.md) [`pall_na()`](reference/pany.md) :
  Parallel any and all
- [`reduce_predicate()`](reference/reduce_predicate.md)
  [`accumulate_predicate()`](reference/reduce_predicate.md) : Reduce
  binary predicate over a list

### Attributes utilities

- [`attrs_rmv()`](reference/attributes-filter.md)
  [`attrs_keep()`](reference/attributes-filter.md)
  [`has_attrs_any()`](reference/attributes-filter.md)
  [`has_attrs_all()`](reference/attributes-filter.md)
  [`has_attrs_only()`](reference/attributes-filter.md) : Attribute
  checks - Check for and filter attributes from object
- [`names3()`](reference/attributes-getters-setters.md)
  [`` `names3<-`() ``](reference/attributes-getters-setters.md)
  [`dimnames2()`](reference/attributes-getters-setters.md)
  [`` `dimnames2<-`() ``](reference/attributes-getters-setters.md)
  [`rownames2()`](reference/attributes-getters-setters.md)
  [`` `rownames2<-`() ``](reference/attributes-getters-setters.md)
  [`class2()`](reference/attributes-getters-setters.md)
  [`` `class2<-`() ``](reference/attributes-getters-setters.md) :
  Attribute utilities - Getters and setters
- [`attr2()`](reference/attr2.md) : Attribute utilities - Get attribute
  of object

### Others

- [`check_installed2()`](reference/check_installed2.md) : Check if user
  accepted a package installation
- [`c2()`](reference/c2.md) : Combine many vectors into one vector
