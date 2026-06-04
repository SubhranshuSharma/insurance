from difflib import SequenceMatcher
import pandas as pd

THRESHOLD = 0.85

df = pd.read_csv("combined.csv")

def normalize_text(text):
    text = str(text).lower().strip()
    return " ".join(text.split())

seen = []
keep_indices = []
duplicates = []

for idx, text in enumerate(df["original_text"]):
    norm = normalize_text(text)

    duplicate_of = None

    for seen_idx, existing in seen:
        similarity = SequenceMatcher(None, norm, existing).ratio()

        if similarity > THRESHOLD:
            duplicate_of = seen_idx
            duplicates.append(
                (
                    idx,               # duplicate row
                    seen_idx,          # original row
                    similarity,
                    text[:100].replace("\n", " ")
                )
            )
            break

    if duplicate_of is None:
        seen.append((idx, norm))
        keep_indices.append(idx)

print(f"Before: {len(df)}")
print(f"After:  {len(keep_indices)}")
print(f"Removed: {len(df) - len(keep_indices)}")

print("\nDuplicates found:")
for dup_idx, orig_idx, sim, preview in duplicates:
    print(
        f"Row {dup_idx} -> duplicate of Row {orig_idx} "
        f"(similarity={sim:.3f})"
    )
    print(f"  {preview}")
    print()

deduped_df = df.iloc[keep_indices]

deduped_df.to_csv("combined1.csv", index=False)
