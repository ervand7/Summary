package main

/*
 - теги разделяют пробелом;
 - имя тега и его значения разделяют двоеточием без пробелов;
 - значения тега разделяют запятой и заключают в кавычки;
 - имя и значения тега пишут в формате snake_case или camelCase.
*/

type MyUser struct {
	ID        string `json:"id" format:"uuid"`
	Name      string `json:"name"`
	CreatedAt int64  `json:"created_at" format:"unixtime,seconds"`
}
