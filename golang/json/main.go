package main

import (
	"fmt"
	"math/rand"
	"strings"
)

func gen(s *[]string) func(t interface{}) {
	return func(t interface{}) {
		*s = append(*s, fmt.Sprintf("%v", t))
	}
}
func main() {

	words := strings.Fields("ink runs from the corners of my mouth")
	rand.Shuffle(len(words), func(i, j int) {
		words[i], words[j] = words[j], words[i]
	})
	fmt.Println(words)

}
