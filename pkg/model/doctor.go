package darigerkz

type Doctor struct {
	Id           string `json:"id"`
	Email        string `json:"email"`
	Password     string `json:"password"`
	Firstname    string `json:"firstname"`
	Lastname     string `json:"lastname"`
	Phone_number string `json:"phone_number"`
	Region       string `json:"region"`
	Posisiton    string `json:"posisiton"`
	Workplace    string `json:"workplace"`
	Experience   string `json:"experience"`
	D_raiting    string `json:"d_raiting"`
	Created_at   string `json:"created_at"`
	Updated_at   string `json:"updated_at"`
	Deleted_at   string `json:"deleted_at"`
}