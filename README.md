# Swedish Municipal Coalition data

Swedish municipalities are often governed in multi-party local coalitions. Following the parlaimentary dificulties in forming a national gouvernement in Sweden following the 2026 general elections, this data directory maps the history of municipal coalitions to inspire the process of finding a national governance constallation that can pass through the Riksdag.

Based on methods and visualisation schemas from a similar project based on 2018-data, the goal is to produce visualisations of the municipal coalissions that describe Swedish municipal co-governance.

 1. What parties are able to governe municipalities together?
 2. Which are the most common / uncommon governance constallations?
 3. Where in the country were what constallations practiced in mandate of 2022-2026?
 4. How does actual municipal coalissions differ from the popular mandate given by the elctorate?
 5. Can we see that the exclusion of the left and far-write proposed on the national level is effective in the governance constallation across the Swedish municipalities?

 ## Project tech:

Data manipulation in Python and analysis in R. This project runs in a conda environment `swe_elect` in python and uses the following R-packages:
 - `ggplot2`
 - `tidyr`
 - `igraph`
 - `dplyr`
 - `stringr`

## Workflow:

A sequential workflow triggered by individual python scripts (prefixed with `NN_`-numerals) execute all steps of this data project in the steps described below.

In order to run the entire workflow on your machine:

```
# Establish the same conda environment (and make sure that your R-environment has the appropriate packages)
conda activate swe_elect
# Run the sequential steps
python 01_pull_data.py    # Pull raw data from the web
python 02_wrangle.py      # Pull raw data from the web
Rscript 03_run.R          # Run the entire analysis in R (nicer in RStudio)
```

Manual visualisations can be drawn from data processed by this codebase.