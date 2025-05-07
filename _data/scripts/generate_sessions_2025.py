"""
This script generates the sessions .csv and .json files for the session
page and the individual session pages for the RSS 2025 conference.

The list of papers (extracted from google sheet) are parsed to determine
which papers are in which sessions. Then, the session names are replaced
by the names in the program schedule (extracted from separate google sheet).

The output is 2 files:
1) a csv file for the all sessions page
2) a json file for individual session pages

Note: This script isn't general. A lot is hardcoded to work with with the
nuances of the data extracted from google sheets.
"""
import pandas as pd
import re
from datetime import datetime
import os
import json

USE_PROGRAM_SESSION_NAMES = True  #toggle this flag to switch naming source

#load csvs
paper_input_path = "../rss2025PaperSessions_data_v3.csv"
program_input_path = "../rss2025Program_data.csv"
output_path = "../rss2025PaperSessions.csv"

df_papers = pd.read_csv(paper_input_path)
df_program = pd.read_csv(program_input_path)

#######################################
# generate paper sessions .csv files
#
# This generates the .csv needed for
# the "Paper Sessions" page.
#######################################
#extract merged program sessions
#handles empty multi-row blocks from spreadsheet
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

        #collect times as datetime objects
        start_dt_list = []
        end_dt_list = []
        for idx in indices:
            try:
                parts = time_slots[idx].strip().split("-")
                if len(parts) == 2:
                    start_str = parts[0].strip()
                    end_str = parts[1].strip()
                    start_dt = datetime.strptime(start_str, "%I:%M")
                    end_dt = datetime.strptime(end_str, "%I:%M")

                    #assume pm if hour < 8 (e.g., conference is from 9am to 8pm)
                    if start_dt.hour < 8:
                        start_dt = start_dt.replace(hour=start_dt.hour + 12)
                    if end_dt.hour < 8:
                        end_dt = end_dt.replace(hour=end_dt.hour + 12)

                    start_dt_list.append(start_dt)
                    end_dt_list.append(end_dt)
            except Exception:
                continue

        if start_dt_list and end_dt_list:
            min_start = min(start_dt_list)
            max_end = max(end_dt_list)
            program_long.append({
                "SessionDisplayName": title_raw,
                "Number": number,
                "Date": date,
                "Time": f"{min_start.strftime('%-I:%M')} - {max_end.strftime('%-I:%M')}"
            })

df_program_sessions = pd.DataFrame(program_long)
df_program_sessions["Title"] = df_program_sessions["SessionDisplayName"].apply(
    lambda x: re.sub(r"^\d+\s*[.-]\s*", "", x).strip())
df_program_sessions["SessionName"] = df_program_sessions["Number"].astype(str) + ". " + df_program_sessions["Title"]

#debug: program sessions
print("\n=== Extracted df_program_sessions ===")
print(df_program_sessions.to_string(index=False))

def format_date(date_str):
    try:
        parsed = datetime.strptime(date_str, "%A, %B %d, %Y")
        return parsed.strftime("%d-%b")
    except Exception:
        return ""

def format_time_range(time_range):
    try:
        start_raw, end_raw = [t.strip() for t in time_range.split('-')]

        def to_dt(t_str):
            return datetime.strptime(t_str, "%I:%M")

        start = to_dt(start_raw)
        end = to_dt(end_raw)

        #add 12 hours to anything before 8am, to account am/pm 
        #since conferece is between 9am and 8pm
        if start.hour < 8:
            start = start.replace(hour=start.hour + 12)
        if end.hour < 8:
            end = end.replace(hour=end.hour + 12)

        return f"{start.strftime('%-I:%M%p').lower()}–{end.strftime('%-I:%M%p').lower()}"
    except Exception:
        return time_range.strip()

def normalize_title(title):
    title = title.replace("&", "and").lower()
    for n in range(1, 21):
        title = re.sub(rf'\b{n}\b', int_to_roman(n).lower(), title)
    return title.strip()

def int_to_roman(n):
    numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ''
    for value, numeral in numerals:
        while n >= value:
            result += numeral
            n -= value
    return result

#lookup table of normalized session, e.g., (date, time)
session_time_map = {}
title_override_map = {}
for _, row in df_program_sessions.iterrows():
    key = normalize_title(row["Title"])
    session_time_map[key] = (format_date(row["Date"]), format_time_range(row["Time"]))
    title_override_map[key] = f'{row["Number"]}. {row["Title"]}'

#debug: session times
print("\n=== Session Time Map ===")
for k, v in session_time_map.items():
    print(f"{k:40} -> {v}")

#generate rows for sessions
session_rows = []
for original in df_papers["Session Name"].dropna().unique():
    match = re.match(r"(\d+)\s*-\s*(.+)", original)
    if match:
        number = int(match.group(1))
        title = match.group(2).strip()
        norm_title = normalize_title(title)
        if USE_PROGRAM_SESSION_NAMES:
            display_name = title_override_map.get(norm_title)
            if not display_name:
                for key, val in title_override_map.items():
                    if norm_title in key:
                        display_name = val
                        break
                if not display_name:
                    display_name = f"{number}. {title}"
        else:
            display_name = f"{number}. {title}"
    else:
        display_name = original.strip()
        norm_title = normalize_title(original)

    date, time = session_time_map.get(norm_title, ("", ""))
    if not date:
        for key, val in session_time_map.items():
            if norm_title in key:
                date, time = val
                break

    session_link = f"session{number}"

    session_rows.append({
        "Date": date,
        "Time": time,
        "SessionName": display_name,
        "SessionLink": session_link,
        "C1": "",
        "C1A": "",
        "C2": "",
        "C2A": ""
    })

#debug: unsorted session rows
print("\n=== Raw Session Rows ===")
print(pd.DataFrame(session_rows).to_string(index=False))

#save to csv
def extract_sort_key(time_str):
    try:
        start = time_str.split("–")[0].strip()
        return datetime.strptime(start, "%I:%M%p")
    except:
        return datetime.strptime("11:59pm", "%I:%M%p")

df_out = pd.DataFrame(session_rows)
df_out["SortKey"] = df_out["Time"].apply(extract_sort_key)
df_out = df_out.sort_values(by=["Date", "SortKey"]).drop(columns=["SortKey"]).reset_index(drop=True)

#debug: final results
print("\n=== Final Sorted Output ===")
print(df_out.to_string(index=False))

df_out.to_csv(output_path, index=False)
print(f"\nSaved to {output_path}")

########################################
# generate sessions .json files
#
# This generates the .json files needed
# for the individual session pages.
########################################
session_json_dir = "../session_jsons"
os.makedirs(session_json_dir, exist_ok=True)

#mapping of session name to session number
session_num_lookup = {}
for _, row in df_out.iterrows():
    match = re.match(r"(\d+)\.", row["SessionName"])
    if match:
        number = int(match.group(1))
        key = normalize_title(row["SessionName"].split(". ", 1)[1])
        session_num_lookup[key] = number

#quick fix not finding normalized session name
session_num_lookup["vla"] = 2

#normalize the session title for matching
def get_session_key(title):
    match = re.match(r"(\d+)\s*-\s*(.+)", title)
    if match:
        return normalize_title(match.group(2).strip())
    return normalize_title(title)

#generate .json file per session
for session_name, group in df_papers.groupby("Session Name"):
    key = get_session_key(session_name)
    session_number = session_num_lookup.get(key)
    if session_number is None:
        print(f"Could not find session number for: {session_name}")
        continue

    papers = []
    for _, paper in group.iterrows():
        papers.append({
            "title": paper["Title"],
            "authors": ", ".join(str(paper["Authors"]).replace(";", ",").split(",")),
            "keywords": paper.get("Keywords", ""),
            "pdf": paper.get("PDF_Link", ""),
        })

    session_link = df_out[df_out["SessionName"].str.startswith(f"{session_number}.")]["SessionLink"].values[0]
    out_path = os.path.join(session_json_dir, f"{session_link}.json")
    with open(out_path, "w") as f:
        json.dump(papers, f, indent=2)

    print(f"Wrote {out_path}")
