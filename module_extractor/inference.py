from nltk.tokenize import sent_tokenize


class HierarchyInference:

    def summarize(self, text, max_sent=2):
        sentences = sent_tokenize(text)
        return " ".join(sentences[:max_sent]).strip()

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
