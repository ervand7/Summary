package main

import (
	"errors"
	"fmt"
	"sort"
	"sync"
	"time"
)

var (
	ErrInvalidAmount         = errors.New("amount should be positive")
	ErrAccountNotFound       = errors.New("account not found")
	ErrNotInitializedAccount = errors.New("account is not initialized")
	ErrInsufficientFunds     = errors.New("insufficient funds")
)

type OperationType string

var (
	DEBIT  OperationType = "DEBIT"
	CREDIT OperationType = "CREDIT"
)

type Wallet interface {
	Credit(accountID, referenceID string, amount int64) error
	Debit(accountID, referenceID string, amount int64) error
	GetBalance(accountID string) (int64, error)
}

type Operation struct {
	Type      OperationType
	ID        string
	CreatedAt time.Time
	Amount    int64
	Err       error
}

type Account struct {
	ID         string
	Operations map[string]*Operation
}

func NewAccount(accountID string) *Account {
	return &Account{
		ID:         accountID,
		Operations: make(map[string]*Operation),
	}
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

func (s *WalletService) Credit(accountID, referenceID string, amount int64) error {
	s.mu.Lock()
	defer s.mu.Unlock()

	if amount <= 0 {
		return ErrInvalidAmount
	}

	acc, ok := s.accounts[accountID]
	if !ok {
		return ErrAccountNotFound
	}

	if acc == nil {
		return ErrNotInitializedAccount
	}

	if _, exists := acc.Operations[referenceID]; exists {
		return nil
	}

	acc.Operations[referenceID] = &Operation{
		ID:        referenceID,
		Type:      CREDIT,
		CreatedAt: time.Now().UTC(),
		Amount:    amount,
		Err:       nil,
	}

	return nil
}

func (s *WalletService) Debit(accountID, referenceID string, amount int64) error {
	s.mu.Lock()
	defer s.mu.Unlock()

	if amount <= 0 {
		return ErrInvalidAmount
	}

	acc, ok := s.accounts[accountID]
	if !ok {
		return ErrAccountNotFound
	}

	if acc == nil {
		return ErrNotInitializedAccount
	}

	if _, exists := acc.Operations[referenceID]; exists {
		return nil
	}

	balance, err := s.getBalanceLocked(accountID)
	if err != nil {
		acc.Operations[referenceID] = &Operation{
			ID:        referenceID,
			Type:      DEBIT,
			CreatedAt: time.Now().UTC(),
			Amount:    amount,
			Err:       err,
		}
		return err
	}

	if balance-amount < 0 {
		acc.Operations[referenceID] = &Operation{
			ID:        referenceID,
			Type:      DEBIT,
			CreatedAt: time.Now().UTC(),
			Amount:    amount,
			Err:       ErrInsufficientFunds,
		}
		return ErrInsufficientFunds
	}

	acc.Operations[referenceID] = &Operation{
		ID:        referenceID,
		Type:      DEBIT,
		CreatedAt: time.Now().UTC(),
		Amount:    amount,
		Err:       nil,
	}

	return nil
}

func (s *WalletService) GetBalance(accountID string) (int64, error) {
	s.mu.Lock()
	defer s.mu.Unlock()

	return s.getBalanceLocked(accountID)
}

func (s *WalletService) getBalanceLocked(accountID string) (int64, error) {
	acc, ok := s.accounts[accountID]
	if !ok {
		return 0, ErrAccountNotFound
	}

	if acc == nil {
		return 0, ErrNotInitializedAccount
	}

	operations, err := s.getSortedOperationsByAccountID(accountID)
	if err != nil {
		return 0, fmt.Errorf("getSortedOperationsByAccountID: %w", err)
	}

	var balance int64
	for _, op := range operations {
		if op.Err != nil {
			continue
		}

		if op.Type == CREDIT {
			balance += op.Amount
		} else if op.Type == DEBIT {
			balance -= op.Amount
		}
	}

	return balance, nil
}

func (s *WalletService) getSortedOperationsByAccountID(accountID string) ([]*Operation, error) {
	acc, ok := s.accounts[accountID]
	if !ok {
		return nil, ErrAccountNotFound
	}

	result := make([]*Operation, 0, len(acc.Operations))
	for _, op := range acc.Operations {
		result = append(result, op)
	}

	sort.Slice(result, func(i, j int) bool {
		return result[i].CreatedAt.Before(result[j].CreatedAt)
	})

	return result, nil
}

func main() {
	walletService := NewWalletService()

	accID := "acc-1"
	walletService.accounts[accID] = NewAccount(accID)

	var wg sync.WaitGroup
	for i := 0; i < 10; i++ {
		wg.Add(1)

		go func() {
			defer wg.Done()

			err := walletService.Credit(accID, "op-1", 100)
			if err != nil {
				fmt.Println(err.Error())
			}
		}()
	}

	wg.Wait()

	balance, err := walletService.GetBalance(accID)
	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(balance)
}
