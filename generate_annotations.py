from pathlib import Path
from string import Template

domains = sorted(Path("domains.txt").read_text().strip().splitlines())

annotation_template = """
    <Annotation about="*.${domain}/*" score="1.0">
        <Label name="_include_"></Label>
        <AdditionalData attribute="original_url" value="{domain}"></AdditionalData>
    </Annotation>
"""
annotation_template = Template(annotation_template.strip("\n"))
annotations = "\n".join(
    annotation_template.substitute(domain=domain) for domain in domains
)

result = f"""
<?xml version="1.0" encoding="UTF-8"?>
<Annotations>
{annotations}
</Annotations>
""".strip()
Path("annotations.xml").write_text(result)
