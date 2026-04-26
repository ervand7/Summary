package main

import (
	"errors"
	"fmt"
	"sync"
)

/*
Build a small Go component:
```Debit(accountID, operationID string, amount int64) error```
Requirements:
 - Balance must never become negative.
 - Same operationID must be idempotent.
 - Concurrent calls must be safe.
 - Failed operations must not corrupt state.
 - Retrying the same operation must return the same result.

Example:
```
Initial balance: 100

Debit("user-1", "op-1", 30) -> OK, balance = 70
Debit("user-1", "op-1", 30) -> OK, balance = 70  // idempotent
Debit("user-1", "op-2", 100) -> insufficient funds, balance = 70
Debit("user-1", "op-2", 100) -> insufficient funds, balance = 70
```

What interviewer expects you to say before coding
Important invariants:
 - balance >= 0
 - invalid amount
 - operationID is applied at most once
 - same operationID always returns same result
 - balance update and operation recording must be atomic
 - all shared state must be protected by mutex
*/

type DebitMaker interface {
	Debit(accountID, operationID string, amount int64) error
}

var (
	ErrInvalidAmount     = errors.New("amount must be positive")
	ErrInsufficientFunds = errors.New("insufficient funds")
	ErrAccountNotFound   = errors.New("account not found")
)

type OperationResult struct {
	Err error
}

type Account struct {
	Balance    int64
	Operations map[string]OperationResult
}

type WalletService struct {
	mu       sync.Mutex
	accounts map[string]*Account
}

func NewWalletService() *WalletService {
	return &WalletService{
		accounts: make(map[string]*Account),
	}
}

func (s *WalletService) CreateAccount(accountID string, balance int64) {
	s.mu.Lock()
	defer s.mu.Unlock()

	s.accounts[accountID] = &Account{
		Balance:    balance,
		Operations: make(map[string]OperationResult),
	}
}

func (s *WalletService) Debit(accountID, operationID string, amount int64) error {
	s.mu.Lock()
	defer s.mu.Unlock()

	// first make checks
	if amount <= 0 {
		return ErrInvalidAmount
	}

	acc, ok := s.accounts[accountID]
	if !ok {
		return ErrAccountNotFound
	}

	// Idempotency check.
	if result, exists := acc.Operations[operationID]; exists {
		return result.Err
	}

	// Business validation.
	if acc.Balance < amount {
		acc.Operations[operationID] = OperationResult{
			Err: ErrInsufficientFunds,
		}
		return ErrInsufficientFunds
	}

	// Atomic state transition:
	// 1. update balance
	// 2. save operation result
	acc.Balance -= amount
	acc.Operations[operationID] = OperationResult{
		Err: nil,
	}

	return nil
}

func (s *WalletService) Balance(accountID string) (int64, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	acc, ok := s.accounts[accountID]
	if !ok {
		return 0, ErrAccountNotFound
	}

	return acc.Balance, nil
}

func main() {
	service := NewWalletService()
	service.CreateAccount("user-1", 100)

	var wg sync.WaitGroup

	// check concurrent access and idempotency
	for i := 0; i < 10; i++ {
		wg.Add(1)

		go func() {
			defer wg.Done()

			err := service.Debit("user-1", "op-1", 30)
			fmt.Println("debit result:", err)
		}()
	}

	wg.Wait()

	balance, _ := service.Balance("user-1")
	fmt.Println("final balance:", balance)
}
