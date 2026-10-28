# nJGL 2026-10-28
#


# Load election results and municipal coalitions
scb <- read.csv2(DATA_SCB, sep=",") %>% select(-X)
skr <- read.csv2(DATA_SKR, sep=",") %>% select(-c(X, compound_abrev))

# Check if municipal codes are matching sets
if(setdiff(scb$mun_code, skr$mun_code) != 0){
    stop("Error: Some municipal codes are not matching between datasets.")
}

# Bring the two together
df <- scb %>%
    left_join(skr %>% select(-c('mun_label')), by='mun_code')

# Data formats should be ok
# str(df)