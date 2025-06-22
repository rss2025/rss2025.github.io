"""
This script generates the following:

1) the .csv for the "Accepted Papers" page that contains the paper titles,
authors, ids, sessions, etc... based on the google sheets for the list of
papers and the program schedule (as the session names are matched with the
ones listed in the program schedule)
2) the .json for the "Demos" page that contains the demo titles, authors,
ids, etc...
3) the .md files for the individual paper pages.
4) the camera ready integration .csv

Note, the abstracts are modified to fix issues with formatting due to latex 
commands included in the abstracts from the openreview data.

TODO:(jared):
- generate demo pages
- add data for dates/times for poster sessions
"""
import pandas as pd
import re
import csv
import json
import os
import html

################################
#      Paper Overrides
################################
manual_title_overrides = {
    172: "Particle-Grid Neural Dynamics for Learning Deformable Object Models from RGB-D Videos",
    215: "A low-cost and lightweight 6 DoF bimanual arm for dynamic and contact-rich manipulation",
}

################################
#      Handle Latex/Macros
################################
latex_symbol_map = {
    r'\alpha': 'α', r'\beta': 'β', r'\gamma': 'γ', r'\delta': 'δ', r'\epsilon': 'ε',
    r'\zeta': 'ζ', r'\eta': 'η', r'\theta': 'θ', r'\iota': 'ι', r'\kappa': 'κ',
    r'\lambda': 'λ', r'\mu': 'μ', r'\nu': 'ν', r'\xi': 'ξ', r'\omicron': 'ο',
    r'\pi': 'π', r'\rho': 'ρ', r'\sigma': 'σ', r'\tau': 'τ', r'\upsilon': 'υ',
    r'\phi': 'φ', r'\chi': 'χ', r'\psi': 'ψ', r'\omega': 'ω',

    r'\Gamma': 'Γ', r'\Delta': 'Δ', r'\Theta': 'Θ', r'\Lambda': 'Λ', r'\Xi': 'Ξ',
    r'\Pi': 'Π', r'\Sigma': 'Σ', r'\Upsilon': 'Υ', r'\Phi': 'Φ', r'\Psi': 'Ψ',
    r'\Omega': 'Ω', r'\Epsilon': 'Ε',

    r'\leq': '≤', r'\geq': '≥', r'\neq': '≠', r'\approx': '≈',
    r'\times': '×', r'\pm': '±', r'\infty': '∞', r'\circ': '°',
}

def convert_latex_to_html(text):
    if not isinstance(text, str):
        return text

    #replace backticks with single quotes to avoid showing up as code
    text = re.sub(r'`([^`]+)`', r"'\1'", text)

    #math mode
    text = re.sub(r'\$\\textit\{([^{}]+)\}\$', r'<em>\1</em>', text)
    text = re.sub(r'\$\\emph\{([^{}]+)\}\$', r'<em>\1</em>', text)
    text = re.sub(r'\$\\textbf\{([^{}]+)\}\$', r'<strong>\1</strong>', text)
    text = re.sub(r'\$\\underline\{([^{}]+)\}\$', r'<u>\1</u>', text)

    #special case: $-Text\ MoreText-$ changed to —Text MoreText—
    def replace_dash_block(m):
        content = m.group(1).replace(r'\ ', ' ')
        return '—' + content + '—'

    text = re.sub(r'\$-([^\$]+)-\$', replace_dash_block, text)

    #subscripted greek  $\pi_0$ changed to π₀
    text = re.sub(
        r'\$(\\[a-zA-Z]+)_([0-9])\$',
        lambda m: latex_symbol_map.get(m.group(1), m.group(1)) + chr(0x2080 + int(m.group(2))),
        text
    )

    #special case: $11^{\circ}$ changed to 11°
    text = re.sub(r'\$([0-9.]+)\^\{\\circ\}\$', r'\1°', text)

    #replace $... \text{...} ...$ with just the text
    text = re.sub(r'\$([^$]*?)\\text\{([^{}]+)\}([^$]*?)\$', r'\1\2\3', text)

    #strip remaining $...$ math mode (i.e., replace $text$ with text)
    #greek letters and math symbols are already replaced above
    text = re.sub(r'\$(.*?)\$', r'\1', text)

    #handle cmds outside of math mode
    text = re.sub(r'\\textit\{([^{}]+)\}', r'<em>\1</em>', text)
    text = re.sub(r'\{\\it ([^{}]+)\}', r'<em>\1</em>', text)
    text = re.sub(r'\\emph\{([^{}]+)\}', r'<em>\1</em>', text)
    text = re.sub(r'(?<!\w)_(\w[^_]*?)_(?!\w)', r'<em>\1</em>', text)

    text = re.sub(r'\\textbf\{([^{}]+)\}', r'<strong>\1</strong>', text)
    text = re.sub(r'\{\\bf ([^{}]+)\}', r'<strong>\1</strong>', text)

    text = re.sub(r'\\underline\{([^{}]+)\}', r'<u>\1</u>', text)

    #replace escaped characters
    text = text.replace(r'\%', '%')
    text = text.replace(r'\_', '_')
    text = text.replace(r'\&', '&')
    text = text.replace(r'\$', '$')

    #replace shorthand
    text = re.sub(r'\\ie(\{\})?', '<em>i.e.</em>', text)
    text = re.sub(r'\\eg(\{\})?', '<em>e.g.</em>', text)
    text = re.sub(r'\\etal(\{\})?', '<em>et al.</em>', text)
    text = re.sub(r'\\etc(\{\})?', '<em>etc.</em>', text)

    #replace Greek and math symbols
    for latex_cmd, symbol in latex_symbol_map.items():
        text = text.replace(latex_cmd, symbol)

    #replace known custom macros
    special_macro_map = {
        r'\spot': '<span style="font-variant: small-caps;">Spot</span>',
        r'\tutor': '<span style="font-variant: small-caps;">Astrid</span>',
    }
    for macro, replacement in special_macro_map.items():
        text = text.replace(macro, replacement)

    return html.unescape(text)

####################################
#  Handle Formatting Author Names
####################################
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
paper_path = "../rss2025PaperSessions_data_v3.csv"
program_path = "../rss2025Program_data.csv"
output_path = "../rss2025CameraReadyInfo.csv"

################################
#     ACCEPTED PAPERS PAGE
################################
#load csv papers (from google sheet)
df = pd.read_csv(paper_path, encoding="utf-8")
df_program = pd.read_csv(program_path, encoding="utf-8")

#load csv papers (from openreview data), we create a mapping here to use
#titles and abtracts from the openreview data
abstract_df = pd.read_csv("../openreview_data_2025.csv", encoding="utf-8")
title_map = dict(zip(abstract_df["Paper No"], abstract_df["Title"]))
abstract_map = dict(zip(abstract_df["Paper No"], abstract_df["Abstract"]))

df = df.drop_duplicates(subset=["Paper No"])

def extract_session_number(session_str):
    match = re.match(r"(\d+)", str(session_str))
    return int(match.group(1)) if match else None

df["SessionNum"] = df["Session Name"].apply(extract_session_number)
df = df.dropna(subset=["SessionNum", "Order"])
df["SessionNum"] = df["SessionNum"].astype(int)
df["Order"] = df["Order"].astype(int)
df["Title"] = df["Paper No"].map(title_map).fillna(df["Title"])

#apply paper title changes
df["Title"] = df.apply(
    lambda row: manual_title_overrides.get(row["Paper No"], row["Title"]),
    axis=1
)

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
# df["PaperID"] = df.apply(lambda row: f"S{row['SessionNum']}.{row['OrderinSession']}", axis=1)
# df = df.sort_values(by=["SessionNum", "OrderinSession"]).reset_index(drop=True)
df = df.sort_values(by=["SessionNum", "Order"]).reset_index(drop=True)
df["PaperID"] = df.index + 1
df["PaperID"] = df["PaperID"].apply(lambda x: f"{x}")

#assign clean session names
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
    # "OrderinSession": df["OrderinSession"],
    "OrderinSession": df["Order"],
    "SessionNum": df["SessionNum"],
    "OriginalPaperID": df["Paper No"],
})

#debug print
print("\n=== Canonical Session Mapping ===")
for num, name in sorted(canonical_session_map.items()):
    print(f"S{num}: {name}")

print("\n=== Final Paper Rows ===")
print(camera_ready_df.head())

#save
camera_ready_df.to_csv(output_path, index=False, quoting=csv.QUOTE_NONNUMERIC)
print(f"\nSaved to {output_path}")

#######################
#      DEMOS PAGE
#######################
#we can just reuse the accepted papers list (but find the indices
#based on the rows where paper type == "demo")
demo_df = df[df["Paper type"].str.lower().str.strip() == "demo"].copy()

#manually add specific papers by paper id
manual_demo_ids = [93, 129]
manual_demos = df[df["PaperID"].astype(int).isin(manual_demo_ids)]
demo_df = pd.concat([demo_df, manual_demos]).drop_duplicates(subset=["PaperID"])

demo_json = []
# for idx, row in enumerate(demo_df.itertuples(index=False), start=1):
for _, row in demo_df.iterrows():
    paper_id = int(row["PaperID"])
    demo_json.append({
        "papernumber": paper_id,
        "papertitle": row.Title,
        "authors": row.Authors,
        "link": f"/program/papers/{paper_id}/",
        "demoday": "",
        "demolocation": "",
        "time": ""
    })

demo_json = sorted(demo_json, key=lambda x: x["papernumber"])

# with open("../demos.json", "w") as f:
#     import json
#     json.dump(demo_json, f, indent=2, ensure_ascii=False)

# print("Saved to ../demos.json")

print('Warning skipping generating demos.json due to manualy changes in .md files')

############################
#       PAPER PAGES
############################
morning_str = "Poster Session"
afternoon_str = "Poster Session"
poster_session_days = {
    "day1after": f"{afternoon_str} (Day 1): Saturday, June 21, 6:30-8:00 PM",
    "day2morn": f"{morning_str} (Day 2): Sunday, June 22, 12:30-2:00 PM",
    "day2after": f"{afternoon_str} (Day 2): Sunday, June 22, 6:30-8:00 PM",
    "day3morn": f"{morning_str} (Day 3): Monday, June 23, 12:30-2:00 PM",
    "day3after": f"{afternoon_str} (Day 3): Monday, June 23, 6:30-8:00 PM",
    "day4morn": f"{morning_str} (Day 4): Tuesday, June 24, 12:30-2:00 PM",
    "day4after": f"{afternoon_str} (Day 4): Tuesday, June 24, 4:00-5:30 PM",
}

poster_session_info = {
    # Saturday, June 21
    "1": poster_session_days["day1after"], # Perception and Navigation  
    "2": poster_session_days["day1after"], # VLA Models
    "3": poster_session_days["day1after"], # Scaling Robot Learning

    # Sunday, June 22
    "4": poster_session_days["day2morn"],  # Perception
    "5": poster_session_days["day2morn"],  # Planning
    "6": poster_session_days["day2after"], # Manipulation I
    "7": poster_session_days["day2after"], # Humanoids
    "8": poster_session_days["day2after"], # Imitation Learning I

    # Monday, June 23
    "9": poster_session_days["day3morn"],  # HRI
    "10": poster_session_days["day3morn"], # Multi-Robot Systems
    "11": poster_session_days["day3after"],# Manipulation II
    "12": poster_session_days["day3after"],# Control and Dynamics
    "13": poster_session_days["day3after"],# Mobile Manipulation and Locomotion

    # Tuesday, June 24
    "14": poster_session_days["day4morn"], # Robot Design
    "15": poster_session_days["day4morn"], # Navigation
    "16": poster_session_days["day4morn"], # Manipulation III
    "17": poster_session_days["day4after"],# Imitation Learning II
}

#output directory for paper .md files
output_dir = "../../_program/papers"

#clear out old .md files before writing new ones
if os.path.exists(output_dir):
    for filename in os.listdir(output_dir):
        if filename.endswith(".md"):
            os.remove(os.path.join(output_dir, filename))
else:
    os.makedirs(output_dir)

#add original paper number for use in PDF link
#we may change this later
camera_ready_df["OriginalPaperNo"] = df["Paper No"]


camera_ready_sorted = camera_ready_df.sort_values(by=["SessionNum", "OrderinSession"]).reset_index(drop=True)

#generate the .md files
for i, row in camera_ready_sorted.iterrows():
    paper_id = row.PaperID
    paper_number = int(row.OriginalPaperNo)
    paper_number_str = f"{paper_number:03d}"
    filename = f"{paper_id}.md"
    # filename = f"{int(paper_id):03d}.md"
    filepath = os.path.join(output_dir, filename)
    # pdf_url = f"https://www.roboticsproceedings.org/rss21/p{paper_number_str}.pdf"
    pdf_url = f"https://www.roboticsproceedings.org/rss21/p{int(paper_id):03d}.pdf"

    #we replace common latex symbols and macros with html, and we retain the
    #paragraph formatting as provided in the openreview data (e.g., a blank
    #space between lines represents a paragraph break followed by an indent)
    raw_abstract = abstract_map.get(paper_number, "Abstract not available.")
    abstract_text = convert_latex_to_html(raw_abstract).replace("\n\n", "<br>&nbsp;&nbsp;&nbsp;&nbsp;").replace("\n", " ")
    # abstract_text = convert_latex_to_html(raw_abstract).replace("\n", " ").strip()

    #posters session info (hard coded above)
    session_num = str(row.SessionNum)
    poster_line = poster_session_info.get(str(row.SessionNum))

    # Navigation links
    prev_link = ""
    next_link = ""

    if i > 0:
        prev_id = camera_ready_sorted.iloc[i - 1].PaperID
        prev_link = f'''<a href="{{{{ site.baseurl }}}}/program/papers/{prev_id}/" title="Previous Paper">
            <div class="paper-menu-icon">
                <i class="fa fa-chevron-left"></i><br>
                <span class="paper-menu-label">Back</span>
            </div>
        </a>'''
    else:
        prev_link = '''<div class="paper-menu-icon invisible"></div>'''
        prev_id = ""

    if i < len(camera_ready_sorted) - 1:
        next_id = camera_ready_sorted.iloc[i + 1].PaperID
        next_link = f'''<a href="{{{{ site.baseurl }}}}/program/papers/{next_id}/" title="Next Paper">
            <div class="paper-menu-icon">
                <i class="fa fa-chevron-right"></i><br>
                <span class="paper-menu-label">Next</span>
            </div>
        </a>'''
    else:
        next_link = '''<div class="paper-menu-icon invisible"></div>'''
        next_id = ""

    md_content = f"""---
layout: paper
title: "{row.PaperTitle}"
invisible: true
prev_id: "{prev_id}"
next_id: "{next_id}"
---
<div class="paper-authors">
  <div class="paper-author-box">
    <div class="paper-author-name">{row.AuthorNames}</div>
    <div class="paper-author-uni"></div>
  </div>
</div>

<div class="paper-pdf">
  <div>
    <a href="{pdf_url}" title="Download PDF" target="_blank">
      <img src="{{{{ site.baseurl }}}}/images/paper_link_cardinal_red.png" alt="Paper PDF" width="33" height="40" />
    </a>
  </div>
</div>

### Paper ID {paper_id}
{{: style="margin-top: 10px; text-align: center;" }}

### [Session {row.SessionName}]({{{{ site.baseurl }}}}/program/papersession?session={row.SessionName.replace(' ', '%20')})
{{: style="text-align: center;" }}

#### {poster_line}
{{: style="margin-top: 10px; color: #555555; text-align: center;" }}

<b style="color: black;">Abstract: </b>{abstract_text}
{{: style="color:gray; font-size: 120%; text-align: justified;" }}

<div class="paper-menu">
  <div class="paper-menu-inner">
    {prev_link}
    <a href="{{{{ site.baseurl }}}}/program/papers" title="All Papers">
      <div class="paper-menu-icon">
        <i class="fa fa-list"></i><br>
        <span class="paper-menu-label">Papers</span>
      </div>
    </a>
    {next_link}
  </div>
</div>
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(md_content)

print(f"\nWrote {len(camera_ready_df)} markdown files to `{output_dir}/`, with abstracts included.")

############################################
# generate RSS25-CameraReadyIntegration.csv
############################################

# # Convert abstracts from LaTeX to HTML-safe text
# camera_ready_df["Abstract"] = camera_ready_df["OriginalPaperNo"].map(abstract_map).fillna("Abstract not available.")
# # camera_ready_df["Abstract"] = camera_ready_df["Abstract"].apply(convert_latex_to_html)
# camera_ready_df["Abstract"] = camera_ready_df["Abstract"].apply(
#     lambda x: convert_latex_to_html(x).replace("\n", " ").replace("\r", " ").strip()
# )

# # Extract first author's last name
# def get_first_author_lastname(authors_str):
#     first_author = authors_str.split(",")[0].strip()
#     parts = first_author.split()
#     return parts[-1] if parts else "Unknown"

# camera_ready_df["FirstAuthorLastName"] = camera_ready_df["AuthorNames"].apply(get_first_author_lastname)

# # Build the list of strings
# integration_lines = []
# header = "PaperID#PaperTitle#Abstract#AuthorNames#AuthorNames"
# integration_lines.append(header)

# for row in camera_ready_df.itertuples(index=False):
#     line = f'{row.PaperID}#{row.PaperTitle}#{row.Abstract}#{row.AuthorNames}#{row.FirstAuthorLastName}'
#     integration_lines.append(f'"{line}"')

# # Save the file
# with open("../RSS25-CameraReadyIntegration.csv", "w", encoding="utf-8") as f:
#     f.write("\n".join(integration_lines))

# print("Saved to ../RSS25-CameraReadyIntegration.csv")

# TODO(jared): add when poster session available
# #### Poster Session day 1
# {{: style="margin-top: 10px; color: #555555; text-align: center;" }}

#replace ### Paper {int(paper_id):03d} with ### Paper ID {paper_id} if 
#going back to S1.1, S1.2, naming convention