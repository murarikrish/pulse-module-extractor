class HierarchyInference:

    def summarize(self, text, max_chars=300):
        text = text.strip()
        return text[:max_chars] + ("..." if len(text) > max_chars else "")

    def build_structure(self, pages):
        modules = []

        for url, soup in pages:
            sections = soup["_parsed"]
            for s in sections:
                module = {
                    "module": s["title"],
                    "Description": self.summarize(s["text"]),
                    "Submodules": {},
                }

                for sm, txt in s["subsections"].items():
                    module["Submodules"][sm] = self.summarize(txt)

                modules.append(module)

        return modules
