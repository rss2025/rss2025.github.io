import pandas as pd
import re
from datetime import datetime

#filepaths
paper_path = "../rss2025PaperSessions_data.csv"
program_path = "../rss2025Program_data.csv"
output_path = "../rss2025CameraReadyInfo.csv"

#load csvs
df = pd.read_csv(paper_path)
df_program = pd.read_csv(program_path)

#filter papers
df = df[df["Paper type"].str.lower() != "demo"]
df = df.drop_duplicates(subset=["Paper No"])

def extract_session_number(session_str):
    match = re.match(r"(\d+)", str(session_str))
    return int(match.group(1)) if match else None

df["SessionNum"] = df["Session Name"].apply(extract_session_number)
df = df.dropna(subset=["SessionNum", "Order"])
df["SessionNum"] = df["SessionNum"].astype(int)
df["Order"] = df["Order"].astype(int)

#session name from program
program_long = []
time_slots = df_program["Unnamed: 0"].fillna("").tolist()

for date_col in df_program.columns[1:-1]:
    date = date_col.strip()
    seen = {}
    col_vals = df_program[date_col].fillna(method="ffill")

    for i, cell in enumerate(col_vals):
        if isinstance(cell, str) and re.match(r"^\d+\s*[.-]", cell.strip()):
            match = re.match(r"^(\d+)", cell.strip())
            number = int(match.group(1))
            seen.setdefault(number, []).append(i)

    for number, indices in seen.items():
        if not indices:
            continue
        title_raw = df_program.at[indices[0], date_col].strip()
        program_long.append({
            "Number": number,
            "Title": re.sub(r"^\d+\s*[.-]\s*", "", title_raw).strip()
        })

df_program_sessions = pd.DataFrame(program_long).drop_duplicates("Number")
df_program_sessions["SessionName"] = df_program_sessions["Number"].astype(str) + ". " + df_program_sessions["Title"]

#build map from number to canonical title
canonical_session_map = df_program_sessions.set_index("Number")["SessionName"].to_dict()
canonical_session_title_map = df_program_sessions.set_index("Number")["Title"].to_dict()

#assign canonical names to papers
df["PaperID"] = df.apply(lambda row: f"S{row['SessionNum']}.{row['Order']}", axis=1)
df["CleanSessionName"] = df["SessionNum"].map(canonical_session_title_map)

#final dataframe
camera_ready_df = pd.DataFrame({
    "PaperID": df["PaperID"],
    "PaperTitle": df["Title"],
    "AuthorNames": df["Authors"],
    "SessionName": df["CleanSessionName"]
})

#debug print
print("\n=== Canonical Session Mapping ===")
for num, name in sorted(canonical_session_map.items()):
    print(f"S{num}: {name}")

print("\n=== Final Paper Rows ===")
print(camera_ready_df.head())

#save
camera_ready_df.to_csv(output_path, index=False)
print(f"\nSaved to {output_path}")
