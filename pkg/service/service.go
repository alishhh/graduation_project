package service

import "github.com/alishhh/graduation_project/pkg/repository"

type Authorization interface {
}

type User interface {
}

type Doctor interface {
}

type Service struct {
	Authorization
	User
	Doctor
}

func NewService(repos *repository.Repository) *Service {
	return &Service{}
}
