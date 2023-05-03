from datetime import datetime, timezone

print(datetime.now())
print(datetime.now(timezone.utc))
print(datetime.now(timezone.max))
print(datetime.now(timezone.min))