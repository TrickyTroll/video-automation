package main

import (
	"flag"
	"fmt"
	"log"
	"regexp"
	"time"

	expect "github.com/google/goexpect"
	"github.com/google/goterm/term"
)

const (
	timeout = 10 * time.Minute
)

var (
	/*
		addr = flag.String("address", "", "address of telnet server")
		user = flag.String("user", "", "username to use")
		pass = flag.String("pass", "", "password to use")
		cmd  = flag.String("cmd", "", "command to run")
	*/

	promptRE = regexp.MustCompile("$")
)

func main() {
	flag.Parse()
	fmt.Println(term.Bluef("echo example"))

	e, _, err := expect.Spawn("/bin/bash", -1)
	if err != nil {
		log.Fatal(err)
	}
	defer e.Close()
	time.Sleep(time.Second)
	e.Expect(promptRE, timeout)
	e.Send("echo 'hello world'\n")
	e.Expect(promptRE, timeout)
	e.Send("exit\n")

	fmt.Println(term.Greenf("%s: result: %s\n", "echo", "Done"))
}
