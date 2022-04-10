package main

import (
	"log"

	darigerkz "github.com/alishhh/graduation_project"
	"github.com/alishhh/graduation_project/pkg/handler"
	"github.com/alishhh/graduation_project/pkg/repository"
	"github.com/alishhh/graduation_project/pkg/service"
)

func main() {
	repos := repository.NewRepository()
	services := service.NewService(repos)
	handlers := handler.NewHandler(services)

	srv := new(darigerkz.Server)
	if err := srv.Run("8080", handlers.InitRouters()); err != nil {
		log.Fatalf("error occured while running http server: %s", err.Error())
	}
}
