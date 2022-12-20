package main

import "testing"

const connsN = 100
const triesN = 1000

var (
	chanBalancer   = NewLoadBalancerChan(make([]*Connection, connsN))
	atomicBalancer = NewLoadBalancerAtomic(make([]*Connection, connsN))
	mutexBalancer  = NewLoadBalancerMutex(make([]*Connection, connsN))
)

func BenchmarkNextConn(b *testing.B) {
	chanBalancer.Init()
	defer chanBalancer.Close()

	b.ResetTimer()

	b.Run("chan", func(b *testing.B) {
		for i := 0; i < triesN; i++ {
			chanBalancer.NextConn()
		}
	})
	b.Run("atomic", func(b *testing.B) {
		for i := 0; i < triesN; i++ {
			atomicBalancer.NextConn()
		}
	})
	b.Run("mutex", func(b *testing.B) {
		for i := 0; i < triesN; i++ {
			mutexBalancer.NextConn()
		}
	})
}
