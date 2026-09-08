"""Generate manuscript tables, figures and provenance only from saved measurements."""

import hashlib
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "paper"
LABELS = {"en": "English", "fr": "French", "es": "Spanish", "ar": "Arabic", "zh": "Mandarin Chinese"}
COLORS = {"en": "#243447", "fr": "#238b87", "es": "#bd6728", "ar": "#9e4760", "zh": "#6763a5"}
plt.rcParams.update(
    {
        "font.size": 9,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "pdf.fonttype": 42,
        "savefig.bbox": "tight",
    }
)


def esc(s):
    return (
        str(s).replace("\\", r"\textbackslash{}").replace("&", r"\&").replace("_", r"\_").replace("%", r"\%")
    )


def write_rows(name, rows):
    (PAPER / "generated" / name).write_text("\n".join(" & ".join(row) + r" \\" for row in rows) + "\n")


def main():
    audit = json.loads((PAPER / "results/language-difference-audit.json").read_text())
    local = json.loads((PAPER / "results/local-language-audit.json").read_text())
    runs = {}
    models = []
    provenance = []
    for entry in json.loads((ROOT / "public/data/experiments.json").read_text()):
        path = ROOT / "public" / entry["url"].lstrip("/")
        raw = path.read_bytes()
        r = json.loads(raw)
        e = r["experiment"]
        provenance.append(
            {
                "experiment_id": e["id"],
                "export_id": path.parent.name,
                "result_sha256": hashlib.sha256(raw).hexdigest(),
                "collection_code_revision": e["code_revision"],
                "created_at": e["created_at"],
                "model": e["model"],
                "language": e["language"],
                "capital_count": len(r["places"]),
            }
        )
        if e.get("prompt_family") == "great-circle-formatted-number-v2":
            runs[e["language"]] = r
        elif len(r["places"]) == 50:
            models.append(r)
    (PAPER / "results/provenance.json").write_text(json.dumps(provenance, indent=2) + "\n")
    (PAPER / "results/exact-language-prompts.json").write_text(
        json.dumps(
            {l: r["experiment"]["prompt_template"] for l, r in runs.items()}, indent=2, ensure_ascii=False
        )
        + "\n"
    )
    rows = []
    for l, label in LABELS.items():
        r = runs[l]
        m = r["layers"]["median"]["metrics"]
        s = r["layers"]["median"]["reconstructions"]["spherical"]
        rows.append(
            [
                label,
                f"{r['quality']['valid']:,}",
                f"{m['mae_km']:.1f}",
                f"{m['spearman']:.5f}",
                f"{100 * m['triangle_violation_rate']:.2f}",
                f"{s['stress']:.4f}",
            ]
        )
    write_rows("language-table.tex", rows)
    rows = []
    for r in models:
        m = r["layers"]["median"]["metrics"]
        s = r["layers"]["median"]["reconstructions"]["spherical"]
        rows.append(
            [
                esc(r["experiment"]["model"].replace("gemini-", "")),
                f"{r['quality']['valid']:,}",
                f"{m['mae_km']:.1f}",
                f"{m['spearman']:.5f}",
                f"{s['stress']:.4f}",
            ]
        )
    write_rows("model-table.tex", rows)
    write_rows(
        "pairwise-table.tex",
        [
            [
                LABELS[c["a"]] + " / " + LABELS[c["b"]],
                f"{c['mean_absolute_median_disagreement_km']:.1f}",
                f"{c['mae_difference_b_minus_a_km']:+.1f}",
                f"{c['judgment_p_holm_20']:.4f}",
                f"{c['accuracy_p_holm_20']:.4f}",
            ]
            for c in audit["comparisons"]
        ],
    )
    write_rows(
        "local-table.tex",
        [
            [
                LABELS[c["language"]],
                str(len(c["capital_ids"])),
                str(c["home_pairs"]),
                f"{c['home_english_MAE_km']:.1f}",
                f"{c['home_language_MAE_km']:.1f}",
                f"{c['home']['gain_km']:+.1f}",
                f"{c['home']['p_holm_8']:.4f}",
                f"{c['interaction']['gain_km']:+.1f}",
                f"{c['interaction']['p_holm_8']:.4f}",
            ]
            for c in local["results"]
        ],
    )
    write_rows(
        "leaveout-table.tex",
        [
            [
                LABELS[c["language"]],
                f"{min(v['home_gain_km'] for v in c['leave_one_home_capital_out'].values()):+.1f} to {max(v['home_gain_km'] for v in c['leave_one_home_capital_out'].values()):+.1f}",
                f"{min(v['interaction_km'] for v in c['leave_one_home_capital_out'].values()):+.1f} to {max(v['interaction_km'] for v in c['leave_one_home_capital_out'].values()):+.1f}",
            ]
            for c in local["results"]
        ],
    )
    places = runs["en"]["places"]
    write_rows(
        "capitals-table.tex", [[esc(p["id"]), esc(p["capital_name"]), esc(p["country_name"])] for p in places]
    )
    write_rows(
        "experiments-table.tex",
        [
            [
                esc(p["model"].replace("gemini-", "")),
                p["language"],
                str(p["capital_count"]),
                r"\texttt{" + p["experiment_id"] + "}",
            ]
            for p in provenance
        ],
    )
    # Source and deformed coastlines are already persisted by the research pipeline.
    fig, axes = plt.subplots(2, 1, figsize=(7.05, 6.0), layout="constrained")
    for ax, lang in zip(axes, ["en", "ar"]):
        r = runs[lang]
        layer = r["layers"]["median"]
        for country in layer["countries"]:
            for ring in country["rings"]:
                src = np.array(ring["source"])
                dst = np.array(ring["target"])
                ax.plot(src[:, 0], -src[:, 1], color="#c2c7cc", lw=0.35, zorder=1)
                ax.plot(dst[:, 0], -dst[:, 1], color=COLORS[lang], lw=0.45, alpha=0.8, zorder=2)
        actual = np.array([[p["latitude"], p["longitude"]] for p in r["places"]])
        inferred = np.array(layer["reconstructions"]["spherical"]["inferred_latlon"])
        for a, b in zip(actual, inferred):
            dl = (b[1] - a[1] + 180) % 360 - 180
            ax.plot([a[1], a[1] + dl], [a[0], b[0]], color=COLORS[lang], lw=0.6, alpha=0.6)
        ax.scatter(actual[:, 1], actual[:, 0], s=7, color="#303943", label="Reference capitals", zorder=4)
        ax.scatter(
            inferred[:, 1],
            inferred[:, 0],
            s=12,
            facecolors="none",
            edgecolors=COLORS[lang],
            lw=0.7,
            label="Inferred capitals",
            zorder=5,
        )
        ax.set(
            xlim=(-180, 180),
            ylim=(-62, 85),
            ylabel="Latitude (degrees)",
            title=f"{LABELS[lang]} instructions | actual displacement, no magnification",
        )
        ax.grid(alpha=0.13)
        ax.set_aspect("equal", adjustable="box")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="outside lower center", ncol=2, fontsize=8, frameon=False)
    axes[1].set_xlabel("Longitude (degrees; equirectangular display)")
    fig.savefig(PAPER / "figures/reconstructed-worlds.pdf")
    plt.close(fig)
    fig, axes = plt.subplots(1, 2, figsize=(7.05, 3.1), layout="constrained")
    for lang, r in runs.items():
        dim = r["layers"]["median"]["dimensionality"]
        axes[0].plot(
            [d["dimensions"] for d in dim],
            [d["stress"] for d in dim],
            label=LABELS[lang],
            color=COLORS[lang],
            lw=1.3,
        )
    true = runs["en"]["true_earth_dimensionality"]
    axes[0].plot(
        [d["dimensions"] for d in true],
        [d["stress"] for d in true],
        label="WGS84 distances",
        color="black",
        ls="--",
        lw=1.3,
    )
    axes[0].set(
        xlabel="Euclidean dimensions",
        ylabel="Distance-normalized stress",
        xticks=[1, 2, 3, 5, 10],
        title="Geometry and its Earth baseline",
    )
    axes[0].legend(fontsize=6.7, frameon=False)
    cs = [c for c in audit["comparisons"] if c["a"] == "en"]
    y = np.arange(4)
    axes[1].barh(
        y,
        [c["mean_absolute_median_disagreement_km"] for c in cs],
        height=0.55,
        color=[COLORS[c["b"]] for c in cs],
        label="Observed",
    )
    axes[1].plot(
        [c["null_disagreement_mean_km"] for c in cs], y, "k|", ms=14, label="Mean under shuffled labels"
    )
    axes[1].set(
        yticks=y,
        yticklabels=[LABELS[c["b"]] for c in cs],
        xlabel="Mean absolute disagreement (km)",
        title="Distance medians versus English",
    )
    axes[1].invert_yaxis()
    axes[1].legend(fontsize=6.7, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.23))
    fig.savefig(PAPER / "figures/structure-and-language.pdf")
    plt.close(fig)
    fig, axes = plt.subplots(1, 2, figsize=(7.05, 2.8), layout="constrained")
    for ax, key, title in zip(
        axes,
        ["home", "interaction"],
        ["Accuracy gain on associated pairs", "Additional gain versus other pairs"],
    ):
        for i, c in enumerate(local["results"]):
            val = c[key]["gain_km"]
            lo, hi = c[key]["ci95_km"]
            ax.errorbar(
                val, i, xerr=[[val - lo], [hi - val]], fmt="o", color=COLORS[c["language"]], capsize=3
            )
        ax.axvline(0, color="gray", lw=0.8, ls="--")
        ax.set(
            yticks=range(4),
            yticklabels=[LABELS[c["language"]] for c in local["results"]],
            xlabel="Gain in km (positive = benefit)",
            title=title,
        )
        ax.invert_yaxis()
    fig.savefig(PAPER / "figures/local-language-effects.pdf")
    plt.close(fig)
    spanish = next(c for c in local["results"] if c["language"] == "es")
    summary = {
        "spanish_home_gain_km": spanish["home"]["gain_km"],
        "spanish_home_gain_percent": 100 * spanish["home"]["gain_km"] / spanish["home_english_MAE_km"],
        "total_language_valid": sum(r["quality"]["valid"] for r in runs.values()),
        "total_language_attempts": sum(r["quality"]["attempts"] for r in runs.values()),
    }
    (PAPER / "results/manuscript-checks.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
