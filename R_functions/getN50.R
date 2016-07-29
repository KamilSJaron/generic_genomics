getN50 <- function(cl, genomeSize = F, order = F){
  cl <- as.numeric(cl)
  if(genomeSize == F & order == F){
    return(sort(cl, decreasing = T)[max(which(cumsum(sort(cl, decreasing = T)) < (sum(cl) / 2))) + 1])
  }
  if(order == F){
    return(sort(cl, decreasing = T)[max(which(cumsum(sort(cl, decreasing = T, na.last = T)) < (genomeSize / 2)), na.rm = T) + 1])
  }
  return(max(which(cumsum(sort(cl, decreasing = T, na.last = T)) < (sum(cl) / 2)), na.rm = T) + 1)
}