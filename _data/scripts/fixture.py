"""
Script for generating a Django fixture to for all the papers.

python3 _data/scripts/fixture.py _data/papers.csv ../rss-video/site/submit/fixtures/papers.json
"""

import argparse
import csv
import json
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('papers')
    parser.add_argument('output')
    parser.add_argument('--model', default='submit.Paper')
    args = parser.parse_args()

    with open(args.papers) as f:
        reader = csv.DictReader(f)
        papers = { paper['external_id'] : (paper['talk_id'], paper['title'], paper['authors'])
                   for paper in reader }

    data = []
    for paper_id, (talk_id, title, authors) in papers.items():
        data.append({
            'model': args.model,
            'pk': paper_id,
            'fields': {
                'paper_id': paper_id,
                'session_id': talk_id,
                'title': title,
                'authors': authors,
            }
        })
    data.sort(key=lambda m: m['pk'])

    with open(args.output, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=2, separators=(',', ': '))

if __name__ == '__main__':
    main()
