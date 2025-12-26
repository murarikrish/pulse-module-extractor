from .crawler import DocumentationCrawler
from .extractor import ContentExtractor
from .inference import HierarchyInference


class ModuleExtractionPipeline:

    def run(self, urls):
        crawler = DocumentationCrawler()
        extractor = ContentExtractor()
        infer = HierarchyInference()

        pages = crawler.crawl(urls)

        enriched = []
        for url, soup in pages:
            soup["_parsed"] = extractor.extract_sections(soup)
            enriched.append((url, soup))

        return infer.build_structure(enriched)
