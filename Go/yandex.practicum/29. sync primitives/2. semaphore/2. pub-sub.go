package main

import (
	"context"
	"fmt"
	"time"

	"golang.org/x/sync/errgroup"
	"golang.org/x/sync/semaphore"
)

/*
Разберём ещё один пример классического применения семафора — задачу
producer–consumer. Есть несколько потребителей, поставщиков и «склад»,
буфер. Потребитель не может забрать больше, чем припасено на складе.
А поставщик не может привезти больше, чем склад в состоянии принять,
потому что ёмкость склада ограниченна.

Напишем такой склад, используя два семафора:
*/

// Depository модель ограниченного склада
type Depository struct {
	Capacity int64               // ёмкость склада
	Reserve  *semaphore.Weighted // количество запасов
	Storage  *semaphore.Weighted // свободное место
}

// NewDepository конструктор
func NewDepository(cap int64) Depository {
	var d = Depository{
		Capacity: cap,
		Reserve:  semaphore.NewWeighted(cap),
		Storage:  semaphore.NewWeighted(cap)}
	// сначала склад пустой
	d.Reserve.Acquire(context.Background(), cap)
	return d
}

// Produce пополнение склада
func (d Depository) Produce(ctx context.Context, n int64) error {
	// ожидаем освобождения места и используем его
	if err := d.Storage.Acquire(ctx, n); err != nil {
		return err
	}
	// пополняем запасы
	d.Reserve.Release(n)
	fmt.Println("Produced ", n)
	return nil
}

// Consume потребление запасов
func (d Depository) Consume(ctx context.Context, n int64) error {
	// ожидаем достаточного запаса и забираем его
	if err := d.Reserve.Acquire(ctx, n); err != nil {
		return err
	}
	// возвращаем свободное место
	d.Storage.Release(n)
	fmt.Println("Consumed ", n)
	return nil
}

func main() {
	d := NewDepository(100)
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()
	// используем errgroup для повторения пройденного
	grp, ctx := errgroup.WithContext(ctx)
	grp.Go(func() error { return d.Consume(ctx, 20) })
	grp.Go(func() error { return d.Consume(ctx, 10) })
	grp.Go(func() error { return d.Produce(ctx, 10) })
	grp.Go(func() error { return d.Produce(ctx, 20) })
	grp.Go(func() error { return d.Produce(ctx, 30) })
	grp.Go(func() error { return d.Produce(ctx, 50) })
	grp.Go(func() error { return d.Produce(ctx, 30) })
	grp.Go(func() error { return d.Produce(ctx, 50) })
	grp.Go(func() error { return d.Produce(ctx, 40) })
	grp.Go(func() error { return d.Produce(ctx, 20) })
	grp.Go(func() error { return d.Consume(ctx, 20) })
	grp.Go(func() error { return d.Consume(ctx, 40) })
	grp.Go(func() error { return d.Consume(ctx, 80) })
	grp.Go(func() error { return d.Consume(ctx, 20) })
	grp.Go(func() error { return d.Consume(ctx, 60) })
	grp.Go(func() error { return d.Produce(ctx, 20) })
	grp.Go(func() error { return d.Produce(ctx, 50) })
	if err := grp.Wait(); err != nil {
		fmt.Println(err.Error())
	}
}
