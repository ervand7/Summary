package some

type Abc interface {
	DD(string) error
}

type User struct {
	param  string
	action Abc
}

func (u User) DoSomething() error {
	return u.action.DD(u.param)
}
