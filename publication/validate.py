"""Verify source locks and full coverage of the five publication-readiness reviews."""
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / 'publication'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    lock = json.loads((PUBLICATION / 'review-inputs.json').read_text())
    for name, expected in lock['files'].items():
        # Reviews refer to the submitted snapshot, even after the live paper is revised.
        if name.startswith('paper/'):
            archived = subprocess.run(
                ['git', 'show', f"{lock['manuscript_commit']}:{name}"],
                cwd=ROOT, check=True, capture_output=True,
            ).stdout
            actual = hashlib.sha256(archived).hexdigest()
        else:
            actual = digest(ROOT / name)
        if actual != expected:
            raise ValueError(f'Review input changed: {name}')
    guides = sorted((PUBLICATION / 'journals').glob('*.md'))
    assert len(guides) == 18, 'Expected 18 journal guides'
    journals = set()
    for guide in guides:
        source = guide.read_text()
        journal = re.search(r'^# (J\d{2})\b', source).group(1)
        journals.add(journal)
        rows = [line for line in source.splitlines() if line.startswith('|')]
        criteria = [match.group(1) for line in rows if (match := re.search(r'\b(C\d{2})\b', line))]
        assert sorted(criteria) == [f'C{i:02}' for i in range(1, 15)], guide
    assert journals == {f'J{i:02}' for i in range(1, 19)}
    expected = {(j, f'C{i:02}') for j in journals for i in range(1, 15)}
    reports = sorted((PUBLICATION / 'reviews').glob('review-*.json'))
    assert len(reports) == 5, 'Expected five completed review JSON companions'
    summaries = []
    reviewers = set()
    original_assessments = {}
    for report in reports:
        data = json.loads(report.read_text())
        reviewer = str(data['reviewer']).zfill(2)
        assert reviewer not in reviewers, 'Repeated reviewer identity'
        reviewers.add(reviewer)
        assert data['manuscript_commit'] == lock['manuscript_commit'], report
        cells = data['assessments']
        original_assessments.update({(reviewer, c['journal'], c['criterion']): c for c in cells})
        assert len(cells) == 252, report
        assert {(c['journal'], c['criterion']) for c in cells} == expected, report
        assert all(c['status'] in {'Pass', 'Partial', 'Fail', 'Unknown', 'N/A'} for c in cells), report
        assert all(isinstance(c['reason'], str) and len(c['reason'].strip()) >= 15 for c in cells), report
        narrative = report.with_suffix('.md')
        text = narrative.read_text()
        assert len(text) < 60000, f'Issue body too long: {narrative}'
        assert all(j in text for j in journals), f'Journal absent from narrative: {narrative}'
        assert all(f'C{i:02}' in text for i in range(1, 15)), narrative
        assert all(c['reason'] in text for c in cells if c['status'] != 'Pass'), (
            f'Non-pass explanation missing or inconsistent in narrative: {narrative}'
        )
        summaries.append({'reviewer': reviewer, 'assessments': len(cells),
                          'statuses': dict(Counter(c['status'] for c in cells)),
                          'report': str(narrative.relative_to(ROOT)),
                          'report_sha256': digest(narrative),
                          'assessment_sha256': digest(report)})
    assert reviewers == {f'{i:02}' for i in range(1, 6)}
    response_path = ROOT / 'paper/publication-dispositions.json'
    if response_path.exists():
        response = json.loads(response_path.read_text())
        for name, expected_hash in response['review_sha256'].items():
            assert digest(ROOT / name) == expected_hash, name
        dispositions = response['assessments']
        assert len(dispositions) == len(original_assessments) == 1260
        assert {(c['reviewer'], c['journal'], c['criterion']) for c in dispositions} == set(original_assessments)
        explanation = (ROOT / response['response_document']).read_text()
        for cell in dispositions:
            original = original_assessments[(cell['reviewer'], cell['journal'], cell['criterion'])]
            assert cell['original_reason'] == original['reason']
            assert cell['original_status'] == original['status']
            assert cell['disposition'] and cell['action'] and cell['response_ids']
            assert all(ref in explanation for ref in cell['response_ids'])
        print('Verified explicit revision dispositions for all 1,260 original assessments')
    result = {'manuscript_commit': lock['manuscript_commit'], 'journals': 18,
              'criteria_per_journal': 14, 'reviewers': 5, 'total_assessments': 1260,
              'input_lock_sha256': digest(PUBLICATION / 'review-inputs.json'),
              'note': 'Coverage is a completeness check, not an acceptance score or scientific validation.',
              'reviews': summaries}
    (PUBLICATION / 'coverage.json').write_text(json.dumps(result, indent=2) + '\n')
    print('Verified 18 guides, archived manuscript inputs, five reviewers and 1,260 assessments')


if __name__ == '__main__':
    main()
