"""Explicitly freeze a new paper release; ordinary builds never call this command."""
import json

from paper.revision100.common import PAPER, ROOT, environment, sha, verify_inputs


def main():
    verify_inputs()
    paths=[PAPER/'input-lock.json',PAPER/'main.tex',PAPER/'references.bib',PAPER/'Makefile',PAPER/'experiment-index.json']
    paths += sorted((PAPER/'revision100').glob('*.py'))+sorted((PAPER/'revision100').glob('*.json'))
    paths += [ROOT/'scripts/publish_paper.py', ROOT/'tests/test_paper.py']
    # Current source dependencies are bound independently of historical analysis IDs.
    paths += sorted((ROOT/'atlas').glob('*.py'))
    content={'release':'100-capital-publication-revision-2026-09-09','note':'Explicit release operation. Build validates these hashes and never rewrites them.','environment':environment(),'files':{str(p.relative_to(ROOT)):sha(p) for p in paths}}
    (PAPER/'release-lock.json').write_text(json.dumps(content,indent=2)+'\n')
    print('Frozen',len(paths),'release inputs')


if __name__=='__main__':main()
