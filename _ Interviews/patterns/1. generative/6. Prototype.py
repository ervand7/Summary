import copy

# Prototype — create objects by copying
# ❓ The idea
# Instead of creating an object from scratch, clone an existing one.
# Useful when creation is:
# - expensive
# - complex
# - configuration-heavy


class Document:
    def __init__(self, title: str, content: list[str]):
        self.title = title
        self.content = content

    def clone(self):
        return copy.deepcopy(self)


# Usage
doc1 = Document("Report", ["page1", "page2"])
doc2 = doc1.clone()

doc2.title = "Report copy"
doc2.content.append("page3")

print(doc1.content)  # ['page1', 'page2']
print(doc2.content)  # ['page1', 'page2', 'page3']
