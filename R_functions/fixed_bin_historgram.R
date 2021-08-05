# function fixed_bin_histogram; arguments:
#   list_of_things_to_display - list of vectors to be plotted
#   pal - pallete; their respective colours; got to have the same length
#   bins - similar like breaks it defines the number of bars in the histogram; but unlike breaks it the number of displayed bars (considering xlim), the number is approximate, used breaks for all the histograms are pretty(xlim, bins)
#   xlim, ylim - by defeault "all data and all hights", by changing xlim breaks get recalculated to keep "bins" relative the displayed number of bars
#   default_legend - by detailt names of elements in the list, can be turned off by setting this value to F
#   main - sets title
#   xlab - sets label of the x axis (default: "Value")
#   ... - all addenitional paramaters will be passed to the "plot" function rendering all the histograms

fixed_bin_histogram <- function(list_of_things_to_display, pal = NA, bins = 50,
                                xlim = NA, ylim = NA, probability = F,
																breaks = NA, border = F,
                                default_legend = T,
																main = '', xlab = 'Value', ylab = NA, ...){

	if ( any(is.na(pal)) ){
		pal <- 1:length(list_of_things_to_display)
	}

	if ( length(xlim) != 2 ){
		xmin <- min(sapply(list_of_things_to_display, min))
		xmax <- max(sapply(list_of_things_to_display, max))
		xlim <- c(xmin, xmax)
	}

	ax <- pretty(xlim, n = bins) # Make a neat vector for the breakpoints
	hist_data <- lapply(list_of_things_to_display, function(x){ x[x > xlim[1] & x < xlim[2]] } )
	histograms <- lapply(hist_data, hist, breaks = ax, plot = F)

	if ( probability ){
		for (i in 1:length(histograms)){
			histograms[[i]]$counts <- histograms[[i]]$density
		}
	}

	if ( any(is.na(ylim)) ){
		bar_size_extremes <- sapply(histograms, function(x){ range(x$counts) } )
		ymin <- min(bar_size_extremes[1,])
		ymax <- max(bar_size_extremes[2,])
		ylim <- c(ymin, ymax)
	}

	if( is.na(ylab) ){
		ylab <- ifelse(probability, 'Density', 'Frequency')
	}

	for (i in 1:length(list_of_things_to_display)){
		add <- ifelse(i == 1, F, T)
		plot(histograms[[i]], col = pal[i], add = add, ylim = ylim, main = main, xlab = xlab, ylab = ylab, border = border, ...)
	}

	if( default_legend ){
		legend('topright', names(list_of_things_to_display), col = pal, pch = 20, bty = 'n')
	}
}
