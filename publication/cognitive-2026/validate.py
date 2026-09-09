"""Check frozen manuscript/guide inputs and complete cognitive publication reviews."""
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    lock = json.loads((BASE / 'review-inputs.json').read_text())
    for relative, expected in lock['files'].items():
        if relative.startswith(('paper/', 'public/')):
            raw = subprocess.check_output(
                ['git', 'show', f"{lock['manuscript_commit']}:{relative}"], cwd=ROOT)
            actual = hashlib.sha256(raw).hexdigest()
        else:
            actual = digest(ROOT / relative)
        require(actual == expected, f'Changed review input: {relative}')
    criteria = json.loads((BASE / 'criteria.json').read_text())
    require({c['id'] for c in criteria} == {f'K{i:02}' for i in range(1, 16)}, 'Criteria incomplete')
    journals = {}
    for path in sorted((BASE / 'journals').glob('*.json')):
        data = json.loads(path.read_text())
        jid = data['journal_id']
        require(jid not in journals, f'Duplicate guide: {jid}')
        guide = BASE / data['guide']
        require(guide.is_file(), f'Missing guide: {guide}')
        require(data['official_sources'], f'No official sources: {jid}')
        require(all(s['url'].startswith('https://') for s in data['official_sources']), jid)
        require(jid in guide.read_text(), f'Missing journal identity: {jid}')
        journals[jid] = data
    require(set(journals) == {f'C{i:02}' for i in range(1, 13)}, 'Need 12 journals')
    expected_cells = {(j, c['id']) for j in journals for c in criteria}
    reports = sorted((BASE / 'reviews').glob('review-*.json'))
    require(len(reports) == 5, 'Need five reviews')
    reviewers = set()
    output = []
    for path in reports:
        data = json.loads(path.read_text())
        rid = data['reviewer_id']
        require(rid not in reviewers, f'Duplicate reviewer: {rid}')
        reviewers.add(rid)
        require(data['manuscript_commit'] == lock['manuscript_commit'], f'Wrong manuscript: {rid}')
        cells = data['assessments']
        require(len(cells) == 180, f'Need 180 cells: {rid}')
        require({(c['journal_id'], c['criterion_id']) for c in cells} == expected_cells, f'Incomplete cells: {rid}')
        narrative = path.with_suffix('.md').read_text()
        require(len(narrative) < 60000, f'GitHub body too long: {rid}')
        for cell in cells:
            require(cell['status'] in {'Pass', 'Partial', 'Fail', 'Unknown', 'N/A'}, f'Bad status: {rid}')
            require(len(cell['reason'].strip()) >= 20, f'Empty reason: {rid}')
            require(cell['reason'] in narrative, f'Markdown reason missing: {rid}/{cell["journal_id"]}/{cell["criterion_id"]}')
            require(cell['evidence'] and all(isinstance(e, str) and e.strip() for e in cell['evidence']), f'No evidence: {rid}')
        require(all(j in narrative for j in journals), f'Missing journal: {rid}')
        require(all(c['id'] in narrative for c in criteria), f'Missing criterion: {rid}')
        output.append({'reviewer_id':rid, 'role':data['role'], 'assessments':len(cells),
                       'statuses':dict(Counter(c['status'] for c in cells)),
                       'report':str(path.with_suffix('.md').relative_to(BASE)),
                       'markdown_sha256':digest(path.with_suffix('.md')), 'json_sha256':digest(path)})
    require(reviewers == {f'R{i:02}' for i in range(1, 6)}, 'Reviewer identity mismatch')
    result = {'manuscript_commit':lock['manuscript_commit'],'journals':12,'criteria':15,'reviewers':5,
              'total_assessments':900,'input_lock_sha256':digest(BASE/'review-inputs.json'),
              'note':'Checks completeness and frozen inputs, not policy truth, acceptance likelihood or independent human agreement.',
              'reviews':output}
    (BASE / 'coverage.json').write_text(json.dumps(result, indent=2)+'\n')
    print('Verified 12 guides, frozen manuscript and guide inputs, five reviews and all 900 criterion assessments.')


if __name__ == '__main__':
    main()
