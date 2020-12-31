#!/usr/bin/env python
import argparse
import collections
import json
import logging
import pathlib


logger = logging.getLogger(__name__)

MAIN_CATEGORIES = collections.OrderedDict([
    ('Flour', None),
    ('Breads', None),
    ('Breakfast', None),
    ('Lunch', None),
    ('Snacks', None),
    ('Sides', None),
    ('Dinner', [
        'American',
        'Asian',
        'Indian',
        'Italian',
        'Mexican',
        'Soups-Crockpot',
    ]),
    ('Dessert', None),
])

HEADER = """---
title: For My Gluten Free Missionary
author: Adriana Reeve
keywords: [gluten free, recipe, cookbook]
rights: ©2020
language: en-US
---
"""


def get_argument_parser():
    parser = argparse.ArgumentParser(
        prog='bookmaker',
        description='A Python script for making a gluten-free cookbook',
    )
    parser.add_argument(
        'source',
        help='Filepath to source files',
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        default=False,
    )

    return parser


def main():
    # Setup command line arguments
    parser = get_argument_parser()

    # Parse command line arguments and config file
    args = parser.parse_args()

    # Setup logging
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    recipes = collections.defaultdict(lambda: collections.defaultdict(dict))

    p = pathlib.Path(args.source)
    for filepath in p.glob('**/*.md'):
        with open(filepath) as fin:
            lines = fin.readlines()
            categories, _, title = lines[:3]
            body = lines[2:]
            categories = categories.strip()
            title = title.replace('#', '').strip()
            if '/' in categories:
                category, sub_category = categories.split('/')
            else:
                category = categories
                sub_category = 'recipes'

            recipes[category][sub_category][title] = ''.join(body).strip()

    contents = HEADER
    contents += '\\newpage\n\n'

    for category, sub_categories in MAIN_CATEGORIES.items():
        print(category)
        contents += '# {}\n\n'.format(category)

        if not sub_categories:
            titles = recipes[category]['recipes']
            titles = dict(sorted(titles.items()))
            for title, title_content in titles.items():
                contents += title_content
                contents += '\n\n\\newpage\n\n'
        else:
            for sub_category in sub_categories:
                print('  ', sub_category)
                contents += '# {}\n\n'.format(sub_category)
                titles = recipes[category][sub_category]
                titles = dict(sorted(titles.items()))
                for title, title_content in titles.items():
                    contents += title_content
                    contents += '\n\n\\newpage\n\n'

    with open('bin/gluten_free_missionary.md', 'w') as fout:
        fout.write(contents)


if __name__ == '__main__':
    main()
