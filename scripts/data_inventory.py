"""
data_inventory.py

Olist veri envanteri: her tablo icin satir/kolon sayisi, eksik veri ve
aday anahtar (primary key) kontrolu.

Kullanim:
    python scripts/data_inventory.py --data-dir data/raw

Not: Bu betik sadece olcer, yorumlamaz. Yorum junior'in isi.
"""
from pathlib import Path
import argparse

import pandas as pd

# Her tablo icin "bu kolon(lar) satiri tekil olarak tanimlar" varsayimimiz.
# Senior aliskanligi: varsayimi koda yaz, sonra veriyle test et.
CANDIDATE_KEYS = {
    "customers": ["customer_id"],
    "geolocation": ["geolocation_zip_code_prefix"],
    "order_items": ["order_id", "order_item_id"],
    "order_payments": ["order_id", "payment_sequential"],
    "order_reviews": ["review_id"],
    "orders": ["order_id"],
    "products": ["product_id"],
    "sellers": ["seller_id"],
    "product_category_name_translation": ["product_category_name"],
}


def table_name(path: Path) -> str:
    """'olist_order_items_dataset.csv' -> 'order_items'"""
    return path.stem.replace("olist_", "").replace("_dataset", "")


def load_tables(data_dir: Path) -> dict[str, pd.DataFrame]:
    files = sorted(data_dir.glob("*.csv"))
    if not files:
        raise SystemExit(f"'{data_dir}' klasorunde CSV bulunamadi.")
    return {table_name(f): pd.read_csv(f) for f in files}


def inventory(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    for name, df in tables.items():
        key = CANDIDATE_KEYS.get(name)
        n_dup = int(df.duplicated(subset=key).sum()) if key else None
        missing_pct = df.isna().mean() * 100
        rows.append(
            {
                "tablo": name,
                "satir": len(df),
                "kolon": df.shape[1],
                "aday_anahtar": ", ".join(key) if key else "-",
                "tekrar_eden_anahtar": n_dup,
                "eksik_kolon_sayisi": int((missing_pct > 0).sum()),
                "max_eksik_%": round(missing_pct.max(), 2),
            }
        )
    return pd.DataFrame(rows)


def missing_report(tables: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    for name, df in tables.items():
        counts = df.isna().sum()
        for col, n in counts[counts > 0].items():
            rows.append(
                {
                    "tablo": name,
                    "kolon": col,
                    "eksik": int(n),
                    "eksik_%": round(n / len(df) * 100, 2),
                }
            )
    return pd.DataFrame(rows).sort_values("eksik_%", ascending=False)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, default=Path("data/raw"))
    args = parser.parse_args()

    tables = load_tables(args.data_dir)

    print("\n=== TABLO ENVANTERI ===")
    print(inventory(tables).to_string(index=False))

    print("\n=== EKSIK VERI (kolon bazinda) ===")
    print(missing_report(tables).to_string(index=False))


if __name__ == "__main__":
    main()
