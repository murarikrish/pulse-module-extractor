import re


class ContentExtractor:

    def clean_text(self, text):
        text = re.sub(r"\s+", " ", text)
        return text.strip()

    def extract_sections(self, soup):
        content = soup.find(["main", "article"]) or soup.body

        sections = []
        current = {"title": None, "text": "", "subsections": {}}

        for tag in content.find_all(["h1", "h2", "h3", "p", "li"]):
            if tag.name in ["h1", "h2"]:
                if current["title"]:
                    sections.append(current)
                current = {
                    "title": self.clean_text(tag.get_text()),
                    "text": "",
                    "subsections": {},
                }

            elif tag.name == "h3":
                current["subsections"][self.clean_text(tag.get_text())] = ""

            else:
                txt = self.clean_text(tag.get_text())
                if txt:
                    if current["subsections"]:
                        last = list(current["subsections"].keys())[-1]
                        current["subsections"][last] += f" {txt}"
                    else:
                        current["text"] += f" {txt}"

        sections.append(current)
        return sections
