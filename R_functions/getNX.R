getNX <- function(cl, Xs = 50, genomeSize = F, order = F){
  cl <- as.numeric(cl)
  cl <- sort(cl, decreasing = T, na.last = T)
  cum_cl <- cumsum(cl)
  
  if(order == F){
    NXs <- c()
    if(genomeSize == F){
      for(X in Xs){
        NXs <- c(NXs, cl[max(c(0,which(cum_cl < X * (sum(cl) / 100)))) + 1])
      }
    } else {
      for(X in Xs){
        NXs <- c(NXs, cl[max(c(0,which(cum_cl < X * (genomeSize / 100)))) + 1])
      }
    }
    return(NXs)
  }
  
  NXorders <- c()
  if(genomeSize == F){
    for(X in Xs){
      NXorders <- c(NXorders, max(c(0,which(cum_cl < X * (sum(cl) / 100)))) + 1)
    }
  } else {
    for(X in Xs){
      NXorders <- c(NXorders, max(c(0,which(cum_cl < X * (genomeSize / 100)))) + 1)
    }
  }
  return(NXorders)
}