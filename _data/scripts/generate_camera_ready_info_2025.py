import pandas as pd
import re
from datetime import datetime
import csv
import json

def normalize_author_names(authors_str):
    def normalize_name(name):
        parts = name.strip().split()
        normalized_parts = []
        for part in parts:
            #capitalize each subpart of a hyphenated name
            subparts = part.split('-')
            normalized_subparts = []
            for sub in subparts:
                if len(sub) == 1:  #single-letter initial without a dot
                    normalized_subparts.append(sub.upper() + ".")
                elif len(sub) == 2 and sub[1] == '.':  #already an initial like "J."
                    normalized_subparts.append(sub.upper())
                else:
                    normalized_subparts.append(sub.capitalize())
            normalized_parts.append('-'.join(normalized_subparts))
        full_name = ' '.join(normalized_parts)

        #capitalize text inside parentheses
        full_name = re.sub(r'\(([^)]+)\)', lambda m: f"({m.group(1).capitalize()})", full_name)

        return full_name

    authors = [normalize_name(name) for name in re.split(r',\s*', authors_str)]
    return ', '.join(authors)


#filepaths
paper_path = "../rss2025PaperSessions_data.csv"
program_path = "../rss2025Program_data.csv"
output_path = "../rss2025CameraReadyInfo.csv"

#########
# PAPERS
#########
#load csvs
# df = pd.read_csv(paper_path)
# df_program = pd.read_csv(program_path)
df = pd.read_csv(paper_path, encoding="utf-8")
df_program = pd.read_csv(program_path, encoding="utf-8")

#filter papers
# df = df[~df["Paper type"].str.contains("demo", case=False, na=False)]
df = df.drop_duplicates(subset=["Paper No"])

#fix numbers because of demos skipped
df["OrderinSession"] = df.groupby("Session Name").cumcount() + 1

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
df["PaperID"] = df.apply(lambda row: f"S{row['SessionNum']}.{row['OrderinSession']}", axis=1)
df["CleanSessionName"] = df["SessionNum"].map(canonical_session_title_map)

#ensure authors are comma separated with a space, and fix capitalization
df["Authors"] = df["Authors"].str.replace(r',\s*', ', ', regex=True)
df["Authors"] = df["Authors"].str.replace(r';\s*', ', ', regex=True)
df["Authors"] = df["Authors"].apply(normalize_author_names)

#hacks to fix greek letters in specific titles
df["Title"] = df["Title"].str.replace(r'\$\s*\\?pi\s*_0\s*\$', 'π₀', regex=True)

#final dataframe
camera_ready_df = pd.DataFrame({
    "PaperID": df["PaperID"],
    "PaperTitle": df["Title"],
    "AuthorNames": df["Authors"],
    "CleanSessionName": df["CleanSessionName"],
    "SessionName": df["SessionNum"].map(canonical_session_map),
    "OrderinSession": df["OrderinSession"],
})

#debug print
print("\n=== Canonical Session Mapping ===")
for num, name in sorted(canonical_session_map.items()):
    print(f"S{num}: {name}")

print("\n=== Final Paper Rows ===")
print(camera_ready_df.head())

#save
# camera_ready_df.to_csv(output_path, index=False)
camera_ready_df.to_csv(output_path, index=False, quoting=csv.QUOTE_NONNUMERIC)
print(f"\nSaved to {output_path}")

#########
# DEMOS
#########
# demo_df = pd.read_csv(paper_path)
demo_df = pd.read_csv(paper_path, encoding="utf-8")
demo_df = demo_df[demo_df["Paper type"].str.contains("demo", case=False, na=False)]

#fix authors formatting (same as above for sessions)
demo_df["Authors"] = demo_df["Authors"].str.replace(r',\s*', ', ', regex=True)
demo_df["Authors"] = demo_df["Authors"].str.replace(r';\s*', ', ', regex=True)
demo_df["Authors"] = demo_df["Authors"].apply(normalize_author_names)

demo_json = []
for idx, row in enumerate(demo_df.itertuples(index=False), start=1):
    demo_json.append({
        "papernumber": idx,
        "papertitle": row.Title,
        "authors": row.Authors,
        "link": "",
        "demoday": "",
        "demolocation": "",
        "time": ""
    })

with open("../demos.json", "w") as f:
    import json
    # json.dump(demo_json, f, indent=2)
    json.dump(demo_json, f, indent=2, ensure_ascii=False)

print("Saved to ../demos.json")
