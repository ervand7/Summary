package main

/*
Чтобы узнать, как именно отменили контекст, можно получить
ошибку методом ctx.Err(). Этот метод отдаёт одно из значений:
  context.Canceled — контекст отменён функцией cancel;
  context.DeadlineExceeded — контекст отменён автоматически по времени.
*/
