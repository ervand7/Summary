package main

import "context"

func (c *cache) _refreshKey(
	ctx context.Context, key CacheKey,
) (interface{}, error) {
	storedValueInterface, err, _ := c.singleFlightGroup.Do(string(key),
		func() (interface{}, error) {
			value, expireAt, err := c.valueProvider.GetValue(ctx, key)
			if err != nil {
				return nil, err
			}

			result := storedValue{
				value:    value,
				expireAt: expireAt,
			}

			c.storage.Store(key, result)

			return result, nil
		})
	if err != nil {
		return nil, err
	}

	return storedValueInterface.(storedValue).value, nil
}
