package some

type Store interface {
	Set(key string, value []byte) error
	Get(key string) ([]byte, error)
	Delete(key string) error
}

func Lookup(s Store) []byte {
	return []byte{}
}
