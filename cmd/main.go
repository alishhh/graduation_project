package main

import (
	"log"

	darigerkz "github.com/alishhh/graduation_project"
	handler "github.com/alishhh/graduation_project/pkg/handlers"
)

func main() {
	handlers := new(handler.Handler)
	srv := new(darigerkz.Server)
	if err := srv.Run("8080", handlers.InitRouters()); err != nil {
		log.Fatalf("error occured while running http server: %s", err.Error())
	}
}
