package main

import "fmt"

// Embedding is just anonymous composition that promotes fields and methods.

type Engine struct {
	Power int
}

/* ---- Composition ---- */
type CarWithComposition struct {
	Engine Engine
}

/* ---- Embedding ---- */
type CarWithEmbedding struct {
	Engine
}

func main() {
	comp := CarWithComposition{
		Engine: Engine{Power: 200},
	}

	emb := CarWithEmbedding{
		Engine: Engine{Power: 300},
	}

	// Composition: must use the field name
	fmt.Println("Composition:", comp.Engine.Power)

	// Embedding: field is promoted
	fmt.Println("Embedding:", emb.Power)

	// Embedding still allows full access too
	fmt.Println("Embedding (explicit):", emb.Engine.Power)
}
