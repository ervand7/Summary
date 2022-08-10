package myMath

import "testing"

func TestAdd(t *testing.T) {
	// args — описывает аргументы тестируемой функции
	type args struct {
		a int
		b int
	}
	// описывает структуру тестовых данных и сами тесты
	tests := []struct {
		name    string
		args    args
		want    int
		wantErr bool
	}{
		{
			name: "Test Positive",
			args: args{
				a: 1,
				b: 2,
			},
			want:    3,
			wantErr: false,
		},
		{
			name: "Test Negative 1",
			args: args{
				a: -1,
				b: 2,
			},
			want:    0,
			wantErr: true,
		},
		{
			name: "Test Negative 2",
			args: args{
				a: 1,
				b: -2,
			},
			want:    0,
			wantErr: true,
		},

		{
			name: "Test Negative all",
			args: args{
				a: -1,
				b: -2,
			},
			want:    0,
			wantErr: true,
		},
	}
	// вызываем тестируемую функцию для каждого тестового случая
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := Add(tt.args.a, tt.args.b)
			if (err != nil) != tt.wantErr {
				t.Errorf(
					"Add() error = %v, wantErr %v",
					err,
					tt.wantErr,
				)
				return
			}
			if got != tt.want {
				t.Errorf(
					"Add() got = %v, want %v",
					got, tt.want)
			}
		})
	}
}
