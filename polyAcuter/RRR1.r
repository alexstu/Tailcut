p_vector <- read.table("length_end.txt")
png(filename = "End T-tail-cut, step 1.png")
head = "Histogram for T-tail-cut reads length from the end\nStep =  1"
x = "Length"
y = "Amounts"
z =  1

vector = as.matrix(p_vector)
brk <- ((max(vector) - min(vector))/z)
hist(vector, main = head, xlab = x, ylab = y, col.lab = "blue", col = "red", breaks = brk, xlim = c(70, 130), ylim = c(0, 150000))
dev.off()



