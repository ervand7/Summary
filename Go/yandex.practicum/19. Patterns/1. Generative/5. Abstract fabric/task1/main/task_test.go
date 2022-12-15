package main

import (
	"fmt"
	"testing"
)

/*
Представьте сервис, в котором пользователи могут быть либо продавцами, либо покупателями.
При регистрации они могут использовать OAuth Яндекса или Google, откуда сервис получает
их имена. Есть скелет кода аутентификации через Google. Добавьте код аутентификации
через Яндекс и внесите изменения в функцию AuthFactory.
*/

// Customer — покупатель.
type Customer struct {
	Name string
}

func (c *Customer) SetName(name string) {
	c.Name = name
}

func (c *Customer) String() string {
	return fmt.Sprintf("Customer: %s", c.Name)
}

// Seller — продавец.
type Seller struct {
	Name string
}

func (c *Seller) SetName(name string) {
	c.Name = name
}

func (c *Seller) String() string {
	return fmt.Sprintf("Seller: %s", c.Name)
}

// Provider — интерфейс фабрики.
type Provider interface {
	NewCustomer() *Customer
	NewSeller() *Seller
}

type GoogleAuth struct {
}

func (g *GoogleAuth) NewCustomer() *Customer {
	var customer Customer
	// получаем имя из Google-аккаунта
	name := "Google Customer"
	customer.SetName(name)
	return &customer
}

func (g *GoogleAuth) NewSeller() *Seller {
	var seller Seller
	// получаем имя из Google-аккаунта
	name := "Google Seller"
	seller.SetName(name)
	return &seller
}

type YandexAuth struct {
}

func (y *YandexAuth) NewCustomer() *Customer {
	var customer Customer
	name := "Yandex Customer"
	customer.SetName(name)
	return &customer
}

func (y *YandexAuth) NewSeller() *Seller {
	var seller Seller
	name := "Yandex Seller"
	seller.SetName(name)
	return &seller
}

// AuthFactory — фабричный метод
func AuthFactory(provider string) Provider {
	switch provider {
	case "google":
		return &GoogleAuth{}
	case "yandex":
		return &YandexAuth{}
	default:
		panic(fmt.Sprintf("unknown provider %s", provider))
	}
	return nil
}

func TestAuth(t *testing.T) {
	googleAuth := AuthFactory("google")
	yandexAuth := AuthFactory("yandex")

	if googleAuth.NewCustomer().String() != "Customer: Google Customer" {
		t.Errorf("wrong google customer")
	}
	if googleAuth.NewSeller().String() != "Seller: Google Seller" {
		t.Errorf("wrong google seller")
	}
	if yandexAuth.NewCustomer().String() != "Customer: Yandex Customer" {
		t.Errorf("wrong yandex customer")
	}
	if yandexAuth.NewSeller().String() != "Seller: Yandex Seller" {
		t.Errorf("wrong yandex seller")
	}
}
