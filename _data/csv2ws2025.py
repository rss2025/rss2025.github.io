import pandas as pd
import json
import click
import re

def normalized_title(title):
    # Removes "Workshop on", "2nd Workshop on", etc., for sorting purposes only
    return re.sub(r"^(?:\d+(?:st|nd|rd|th)?\s+)?Workshop on\s+", "", title, flags=re.IGNORECASE).strip()

@click.command()
@click.argument("input_csv", type=click.Path(exists=True))
@click.argument("output_json", type=click.Path())
@click.option(
    "--skip-lines",
    default="",
    help="Comma-separated list of 1-based CSV data row numbers to skip (excluding header)."
)
@click.option(
    "--start-id",
    default=1,
    type=int,
    help="Starting ID number for the output JSON entries (default: 1)."
)
def convert_workshops(input_csv, output_json, skip_lines, start_id):
    """
    Convert a CSV of workshop data to structured JSON format.

    INPUT_CSV: Path to the CSV file with workshop info.
    OUTPUT_JSON: Path to write the resulting JSON.
    """
    skip_indices = {int(x.strip()) for x in skip_lines.split(",") if x.strip().isdigit()}

    df = pd.read_csv(input_csv, header=None, skip_blank_lines=False).fillna("")
    df.columns = ["title", "website", "contact_name", "contact_email"]

    print(df.columns.tolist())

    workshops = []
    for i, row in enumerate(df.itertuples(index=False), start=1):
        if i in skip_indices:
            click.secho(f"Skipping row {i} (manual skip): {row.title}", fg="yellow")
            continue

        title = row.title.strip()
        website = row.website.strip()
        contact_name = row.contact_name.strip()
        contact_email = row.contact_email.strip()

        if not title and not website and not contact_name and not contact_email:
            click.secho(f"Skipping row {i} (empty row)", fg="yellow")
            continue

        if not title or not website:
            click.secho(f"Skipping row {i} (missing title or website): {title}", fg="yellow")
            continue

        workshops.append({
            "id": 0, #assign this below
            "location": "",
            "title": title,
            "website": website,
            "link": ""
        })

    #sort alphebetically
    workshops.sort(key=lambda x: normalized_title(x["title"]).lower())
    for i, w in enumerate(workshops, start=start_id):
        w["id"] = i

    with open(output_json, "w") as f:
        json.dump(workshops, f, indent=2)

    click.echo(f"Converted {len(workshops)} workshops to {output_json} starting with ID {start_id}")


if __name__ == "__main__":
    convert_workshops()
