"""Prepare a public paper and self-contained reproduction bundle from verified inputs."""
import json
import shutil
import zipfile

from paper.revision100.common import PAPER, ROOT, sha, verify_inputs
from paper.revision100.verify import main as verify_paper


def main():
    verify_paper()
    output=ROOT/'public/paper';output.mkdir(exist_ok=True)
    shutil.copy2(PAPER/'cognitive-atlas-paper.pdf',output/'cognitive-atlas-paper.pdf')
    inputs=verify_inputs()
    paths={ROOT/p for p in inputs['files']}
    paths.update(ROOT/p for p in json.loads((PAPER/'release-lock.json').read_text())['files'])
    paths.update(p for p in PAPER.rglob('*') if p.is_file() and p.suffix in {'.py','.json','.md','.tex','.bib','.pdf'} and p.name!='main.pdf' and '__pycache__' not in p.parts)
    paths.update([ROOT/'pyproject.toml',ROOT/'uv.lock',PAPER/'Makefile',ROOT/'tests/test_paper.py',
                  ROOT/'public/data/experiments.json',ROOT/'scripts/audit_language_group.py',
                  ROOT/'scripts/audit_map_group.py'])
    paths.update((ROOT/'reviews').glob('*.md'))
    # Reproduction package contains only explicit inputs, research source and documentation.
    archive=output/'reproduction.zip'
    with zipfile.ZipFile(archive,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(paths):z.write(p,p.relative_to(ROOT))
    manifest={'study':'100 capitals; English, Arabic, written Chinese; Gemini 3.5 Flash','completed_answers':148500,'valid_answers':148491,'pdf_sha256':sha(output/'cognitive-atlas-paper.pdf'),'reproduction_zip_sha256':sha(archive),'files':len(paths),'input_lock_sha256':sha(PAPER/'input-lock.json'),'release_lock_sha256':sha(PAPER/'release-lock.json')}
    (output/'publication.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (output/'index.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cognitive Atlas — paper and data</title><style>body{max-width:720px;margin:70px auto;padding:0 24px;font:18px/1.6 system-ui;color:#243447}a{color:#295d84}h1{line-height:1.2}</style><h1>Geographic geometry across 100 capitals</h1><p>148,500 distance judgments from Gemini 3.5 Flash under English, Arabic, and written Chinese instructions.</p><p><a href="cognitive-atlas-paper.pdf">Read the paper (PDF)</a></p><p><a href="reproduction.zip">Download the complete reproduction package</a> — LaTeX, figures, analysis code, observed data, statistical audits, and source locks. See paper/README.md inside the package for commands.</p><p><a href="publication.json">Publication checksums</a> · <a href="../">Explore the atlas</a></p><p>The study describes observed judgments from fixed prompts and capitals. It has not received independent human peer review.</p></html>''')
    print(json.dumps({**manifest,'bundle_megabytes':archive.stat().st_size/1e6}))


if __name__=='__main__':main()
