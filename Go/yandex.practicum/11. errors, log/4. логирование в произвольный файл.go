package main

import (
	"log"
	"os"
)

/*
Разберём функцию log.New:
 - В первом параметре указывается переменная интерфейсного типа io.Writer,
в данном случае это открытый для записи файл.
 - Второй параметр содержит префикс, который будет добавляться для каждой записи
в лог, и следом указываются флаги логирования.
log.LstdFlags отвечает за вывод даты и времени.
log.Lshortfile отвечает за вывод имени файла и строки, в которой произошла запись в лог.
Функция log.New возвращает указатель на потокобезопасную переменную
типа log.Logger, которую следует использовать для логирования в указанный файл.
*/

func main() {
	flog, err := os.OpenFile(`server.log`, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		log.Fatal(err)
	}
	defer flog.Close()
	mylog := log.New(flog, `serv `, log.LstdFlags|log.Lshortfile)
	mylog.Println(`Start server`)
	mylog.Println(`Finish server`)
}

/*
Есть ещё одна функция, которая перенаправляет вывод при
логировании, — log.SetOutput(w io.Writer). В этом случае Logger не создаётся.
Пример выше мог быть таким:

log.SetOutput(flog)
log.Println(`Start server`)
log.Println(`Finish server`)
*/
