from typing import List


# Time: O(n * k²)
# Space: O(n * k)
def subdomain_visits(cpdomains: List[str]) -> List[str]:
    h = {}

    for item in cpdomains:
        count, value = item.split()
        count = int(count)
        parts = value.split(".")

        for i in range(len(parts)):
            key = ".".join(parts[i:])
            h[key] = h.get(key, 0) + count

    return [f"{v} {k}" for k, v in h.items()]


print(subdomain_visits(cpdomains=["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
