package main

import (
	"fmt"
	"net"
	"os"
)

func check_args() {
	if len(os.Args) <= 1 {
		panic(fmt.Sprintf("Debes introducir el argumento: Ej: go run main.go scanme.nmap.org"))
	}
}

func main() {
	check_args()

	for i := 1; i <= 1024; i++ {
		address := fmt.Sprintf(os.Args[1]+":%d", i)
		//fmt.Printf(address)
		conn, err := net.Dial("tcp", address)
		if err != nil {
			// port is closed or filtered
			//fmt.Printf("Port %d is closed \n", i)
			continue
		}
		conn.Close()
		fmt.Printf("Port %d open in %s \n", i, os.Args[1])
	}
}