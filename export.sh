# Script to export all of the required code, graphs, and diagrams for the wiki in one go

# zip up code - careful will only take the lastest commited version on your current branch
git archive --format zip --output export/UNSW-iGEM-mathematical-modelling.zip HEAD

# export flow chart
python3 render.py model.py | neato -T png -o export/model.png
