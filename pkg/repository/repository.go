package repository

type Authorization interface {
}

type User interface {
}

type Doctor interface {
}

type Repository struct {
	Authorization
	User
	Doctor
}

func NewRepository() *Repository {
	return &Repository{}
}
