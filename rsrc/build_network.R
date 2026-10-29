# nJGL 2026-10-28
#



get_adjm <- function(ldf, rel=F){
    # Generate an adjacency matrix for ONE municipality
    ldf <- ldf %>% select(party_m:party_misc)
    n_coalition_parties <- sum(t(ldf[1,] %>% select(party_m:party_misc)))
    
    # Push x onto y to build adjacency matrix
    r <- matrix(rep(unlist(ldf[1,]), ncol(ldf)), nrow=ncol(ldf), byrow=T)
    r[ which(r[1,] != 1), ] <- c(rep(0,ncol(r)))
    colnames(r) <- rownames(r) <- party_abrevs
    
    # Make relative the coalition size
    if(rel == T){r <- r / n_coalition_parties}
    
    # Adjacency matrix is now 0-1 between each party of a governing relation
    # If `rel`==T, the non-0 value of a relationship is <1, (normalized by size)
    r
}




# Two aggregate adjacency matrecies, one absolute and one weighted by coalition
# size:
# In a coalission between only two parties, each party would have more influence
# than if the coalision consisted of six parties. In the weighted adjacency
# matrix, each unit of weight represents something like the power to govern
# one municipality as if being in two coalissions of two parties in two 
# municipalities reflects the same party influence as governing alone in one
# municipality.
am_abs <- Reduce("+", lapply(1:nrow(df), function(x) get_adjm(df[x,])))
am <- Reduce("+", lapply(1:nrow(df), function(x) get_adjm(df[x,], rel=T)))


# 
rule <- data.frame(party = party_names,
                   party_abrev = party_abrevs,
                   muns = sapply(1:ncol(am_abs), function(x) am[x,x]),
                   muns_abs = sapply(1:ncol(am), function(x) am_abs[x,x]),
                   colour = party_colours
)
# Bring in election results.
# National overall election result for each party
rule$nat_elect <- sapply(rule$party, function(x) res2022[which(party_names == x)])
# Sum of municipal mandate seats scored in 2022
rule$mun_seats <- df %>% summarise(across(seats_m:seats_misc, ~ sum(.x, na.rm = TRUE))) %>% t()
rule$mun_elect <- rule$mun_seats / sum(rule$mun_seats)

# Make contrafactual calculations:
# If
rule$contrafactual <- rule$mun_elect * sum(rule$muns)
rule$diff <- rule$contrafactual - rule$muns




# Build network from adjacency matrix
g <- simplify(graph_from_adjacency_matrix(am,
                                          mode="undirected",
                                          weighted=T))

# Establish vertex and edge attributes
V(g)$label <- party_names
V(g)$size <- sapply(V(g)$name, function(x) rule$muns[rule$party_abrev == x] / 2)
V(g)$color <- sapply(V(g)$name, function(x) rule$colour[rule$party_abrev == x])
E(g)$size <- E(g)$weight / 2

# Plot network (igraphs don't store nicely like ggplot does)
layout <- layout.circle(g)
plot(g,
     edge.curved = .3,
     vertex.label.color="black",
     edge.color =  rgb(.7,.7,.7,.7),
     edge.width=E(g)$size,
     layout = layout)

plot(g)
