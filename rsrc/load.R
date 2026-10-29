# nJGL 2026-10-28
#


# Load election results and municipal coalitions
scb <- read.csv2(DATA_SCB, sep=",") %>% select(-X)
skr <- read.csv2(DATA_SKR, sep=",") %>% select(-c(X, compound_abrev))

# Check if municipal codes are matching sets
if (length(setdiff(scb$mun_code, skr$mun_code)) > 0) {
    stop("Error: Some municipal codes are not matching between datasets.")
}

# Bring the two together
df <- scb %>%
    left_join(skr %>% select(-c('mun_label')), by='mun_code')

# Data formats should be ok
# str(df)


## Municipal voting results for 2018 from:
## https://historik.val.se/val/val2018/slutresultat/K/rike/index.html
res2018 <- c(.2006, .0967, .0681, .0520, .2758, .0769, .0462, .1274, .0095 + .0468)
res2022 <- c(.1910, .0671, .0461, .0534, .3033, .0675, .0508, .2054, .0154)
