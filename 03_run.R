# nJGL 2026-10-26
#
#

#####################################################################################
# nJGL 2022-06-02 Set the working directory - RStudio, R, Commandline
if (interactive() && requireNamespace("rstudioapi", quietly = TRUE) &&
    rstudioapi::isAvailable()) {
    script_path <- rstudioapi::getSourceEditorContext()$path
} else {
    script_path <- sub("^--file=", "", grep("^--file=", commandArgs(), value = TRUE)[1])
}
setwd(dirname(normalizePath(script_path)))
#####################################################################################


# These libraries
library(ggplot2)
library(tidyr)
library(igraph)

# These paths:
DATA_SCB <- paste('data', 'cleaned', 'election_results.csv', sep="/")
DATA_SKR <- paste('data', 'cleaned', 'municipal_coalitions.csv', sep="/")

# Universal function toolbox
source('rsrc/tools.R')



#####################################################################################
# Data loaders

source('rsrc/load.R')


