# nJGL 2026-10-28
#

## Party abbreviation
parties <- c('m', 'c', 'l',
             'kd', 's', 'v',
             'mp', 'sd', 'local')
parties <- c('v', 's', 'mp', 'c', 'l', 'm', 'kd', 'sd', 'local')


## Plotting colours for parties
party_colours <- c('#92d0fc','#0c6310','#3165de',
                   '#97c98d','#8a6424','#ababab',
                   '#9931de','#d1180f','#82010c')
party_colours <- c('#82010c','#d1180f','#97c98d','#0c6310','#3165de','#92d0fc','#9931de','#8a6424','#ababab')

## Party names (Swedish)
party_names <- c('Moderaterna','Centerpartiet','Liberalerna',
                 'Kristdemokraterna','Socialdemokraterna','Vänsterpartiet',
                 'Miljöpartiet','Sverigedemokraterna','Övriga partier')
party_names <- c('Vänsterpartiet','Socialdemokraterna','Miljöpartiet', 'Centerpartiet',
                 'Liberalerna', 'Moderaterna', 'Kristdemokraterna', 'Sverigedemokraterna',
                 'Övriga partier')

## Party names (Swedish)
party_abrevs <- c('m','c','l', 'Kd','S','V','Mp','Sd','Övr.')
party_abrevs <- c('v','s','mp','c', 'l','m','kd','sd', 'Övr.')

## Party abbreviations in the column order of the cleaned data
## (party_m:party_misc and seats_m:seats_misc). Use these to name anything
## selected from the data, then reorder by `party_abrevs` for plotting.
data_abrevs <- c('m','c','l','kd','s','v','mp','sd','Övr.')
party_abrevs <- c('v','s','mp','c', 'l','m','kd','sd', 'Övr.')
