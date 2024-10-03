"""
Script for adding Jekyll front matter and organizers to workshop pages.

python3 _data/scripts/workshops.py _data/workshops.csv _data/workshops_raw_html/ _program/workshops/
"""

import argparse
import csv
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file')
    parser.add_argument('indir')
    parser.add_argument('outdir')
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    with open(args.csv_file) as f:
        reader = csv.DictReader(f)
        workshop_data = { workshop['internal_id'] : workshop for workshop in reader }

    for fname in os.listdir(args.indir):
        internal_id = os.path.splitext(fname)[0]
        if internal_id not in workshop_data:
            continue

        workshop = workshop_data[internal_id]

        inpath = os.path.join(args.indir, fname)
        outpath = os.path.join(args.outdir,
                               workshop['external_id'].replace('-', '').lower() + '.md')

        front_matter = [
            '-' * 3,
            'layout: page',
            'title: "{}"'.format(workshop['title']),
            'comments: true',
            'invisible: true',
            '-' * 3,
        ]

        data = [
            'Organizers: {organizers}'.format(organizers=workshop['organizers'].replace(',', ', ')),
            'Website: <a href="{url}">{url}</a>'.format(url=workshop['url'])
        ]
        formatted_data = ['<p class="text-left"><i>{}</i></p>'.format(d) for d in data]

        with open(inpath) as fin:
            page_data = [
                '\n'.join(front_matter),
                '\n'.join(formatted_data),
                fin.read(),
                '{% include disqus.html %}'
            ]

        with open(outpath, 'w') as fout:
            outtext = '\n\n'.join(page_data)
            fout.write(outtext)

if __name__ == '__main__':
    main()
