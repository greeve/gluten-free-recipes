# gluten-free-recipes

A repository of gluten free recipes and scripts to turn the recipes into a cookbook. 

# Utils

## Rename all files in a directory with bash

```
for f in *.txt; do
    mv -- "$f" "${f%.txt}.md"
done
```
