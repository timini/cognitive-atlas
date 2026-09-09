"""Frozen inputs for the revised 100-capital manuscript."""
import hashlib
import importlib.metadata
import json
import platform
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / 'paper'
EXPORTS = {
    'en': '3b382690950b9511f5806ebc-114bbc2e2e5a9331',
    'ar': 'b2e583773ba8111b0607ae88-3ef8ee3db9b488b1',
    'zh': '2ee0bcb921b94263ac26e635-bae2d55a858255c4',
}
DISTANCE_AUDIT = ROOT/'public/data/language-audits/5e0afd2e6550db2d77fd0561.json'
MAP_AUDIT = ROOT/'public/data/map-audits/68143748b8b5f8ea4f732ca5.json'
LABELS = {'en': 'English', 'ar': 'Arabic', 'zh': 'Chinese'}
GROUPS = {'ar': ['AE','BH','DJ','DZ','EG','IQ','JO','KW','LB','MA','MR','OM','QA','SA','TN'], 'zh': ['CN','SG']}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def verify_inputs():
    lock = json.loads((PAPER/'input-lock.json').read_text())
    for path, expected in lock['files'].items():
        if sha(ROOT/path) != expected:
            raise ValueError(f'Frozen manuscript input changed: {path}')
    return lock


def load_results():
    verify_inputs()
    results = {lang: json.loads((ROOT/'public/data'/export/'result.json').read_text()) for lang, export in EXPORTS.items()}
    assert all(len(r['places']) == 100 and len(r['pairs']) == 4950 for r in results.values())
    return results


def environment():
    return {'python': platform.python_version(), 'packages': {p:importlib.metadata.version(p) for p in ['numpy','scipy','scikit-learn','geographiclib','matplotlib']}, 'uv_lock_sha256':sha(ROOT/'uv.lock')}


def write_report(path, report, script):
    report.update(script_sha256=sha(script), input_lock_sha256=sha(PAPER/'input-lock.json'), environment=environment())
    Path(path).write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
