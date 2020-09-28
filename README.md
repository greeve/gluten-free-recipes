# gluten-free-recipes

A repository of gluten free recipes and scripts to turn the recipes into a cookbook. 

# Instructions

1. Prepare recipes using the template file `template_recipe.md`.
2. Store the recipes in the `recipes` folder.
3. Run python script.
    - `python scripts/bookmaker.py recipes/`
4. Run the bash script to generate the pdf from the markdown
    - `bash md2pdf.sh bin/gluten_free_missionary.md bin/gluten_free_missionary.pdf`

# Utils

## Rename all files in a directory with bash

```
for f in *.txt; do
    mv -- "$f" "${f%.txt}.md"
done
```
