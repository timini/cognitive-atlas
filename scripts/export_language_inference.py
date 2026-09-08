"""Publish auditable inference summaries without mixing different city cohorts."""
import hashlib
import json
from pathlib import Path


def export_inference(public='public/data'):
    public = Path(public)
    original = Path('paper/results/language-difference-audit.json')
    raw = original.read_bytes()
    historical = json.loads(raw)
    for source in historical['sources'].values():
        assert hashlib.sha256(Path(source['path']).read_bytes()).hexdigest() == source['sha256']
    audit_root = public/'language-audits'
    audit_root.mkdir(exist_ok=True)
    archive = audit_root/f"paper-50-{hashlib.sha256(raw).hexdigest()[:24]}.json"
    archive.write_bytes(raw)
    reports = [(archive, historical)]
    reports.extend((p, json.loads(p.read_text())) for p in sorted(audit_root.glob('*.json'))
                   if not p.name.startswith('paper-50-'))
    cohorts = []
    for path, report in reports:
        sources = report['sources']
        export_ids = [s.get('export_id', Path(s['path']).parent.name) for s in sources.values()]
        comparisons = [{**c, 'judgment_p_holm': c.get('judgment_p_holm', c.get('judgment_p_holm_20')),
                         'accuracy_p_holm': c.get('accuracy_p_holm', c.get('accuracy_p_holm_20'))}
                       for c in report['comparisons']]
        cohorts.append({'export_ids': export_ids, 'capital_count': report.get('capital_count', 50),
                            'complete_pairs': report['complete_pairs'], 'total_pairs': report['total_pairs'],
                            'permutations': report['permutations'], 'holm_family_size': report.get('holm_family_size', 20),
                            'comparisons': comparisons, 'complete_pair_median_MAE_km': report['complete_pair_median_MAE_km'],
                            'report_url': '/data/language-audits/'+path.name})
    target = public/'language-inference.json'
    target.write_text(json.dumps({'schema_version': 1, 'cohorts': cohorts}, indent=2) + '\n')
    return target


if __name__ == '__main__':
    print(export_inference())
