package main

import "golang.org/x/exp/constraints"

// все эти определения эквивалентны
type VectorInt1[T constraints.Signed] []T
type VectorInt2[T ~int | ~int8 | ~int16 | ~int32 | ~int64] []T
type VectorInt3[T interface{~int | ~int8 | ~int16 | ~int32 | ~int64}] []T