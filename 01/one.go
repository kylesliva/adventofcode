package main

import(
	"fmt"
	// "os"
)

func main(){
	// create slice of test masses
	masses := []float32{14, 1969, 100756}

	// fmt.Println(masses)

	var fuel []float32 

	for _, v := range masses {
		// fmt.Println(v)
		var computedFuel float32
		computedFuel = computeFuel(v)
		fuel = append(fuel, computedFuel)
	}

	fmt.Println(fuel)

}

// func readMass(path) {

// }

func computeFuel(mass float32) float32{
	mass = mass / 3
	// fmt.Println(mass)
	mass = float32(int(mass))
	mass = mass - 2

	if mass <= 0 {
		return 0
	}

	return mass + computeFuel(mass)
}