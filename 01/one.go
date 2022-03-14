// run with go run one.go </path/to/input-file>
package main

import(
	"fmt"
	"io/ioutil"
	"bufio"
	"bytes"
	"strconv"
	"os"	
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main(){

	// pull input file path from CLI
	fileloc := os.Args[1]

	dat, err := ioutil.ReadFile(fileloc)
	check(err)

	var masses []float32

	scanner := bufio.NewScanner(bytes.NewReader(dat))
	for scanner.Scan() {
		value, err := strconv.ParseFloat(scanner.Text(), 32)
		check(err)

		masses = append(masses, float32(value))
	}

	var fuel []float32 

	for _, v := range masses {
		var computedFuel float32
		computedFuel = computeFuel(v)
		fuel = append(fuel, computedFuel)
	}

	fmt.Println(int(sum(fuel)))

}

func sum(array []float32) float32 {  
	var result float32
	result = 0  
	for _, v := range array {  
	 result += v  
	}  
	return result  
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