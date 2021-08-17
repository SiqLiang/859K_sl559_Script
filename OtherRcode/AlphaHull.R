set.seed(123)
theta = runif(n <- 300, 0, 2 * pi)
r = sqrt(runif(n, 0.25^2, 0.5^2))
x = cbind(0.5 + r * cos(theta), 0.5 + r * sin(theta))
print(x)

## library(animation)
## saveMovie({
library(alphahull)
par(
  mar = rep(0, 4), xaxt = "n", yaxt = "n", bg = "black",
  col = "white"
)
for (alpha in seq(0.25, 0, -0.01)) {
  plot(ahull(x, alpha = alpha), pch = 20, col = "white",
       panel.last = text(
         0.5, 0.5, sprintf("alpha = %.2f", alpha), cex = 2
       )
  )
}
## }, moviename = "alpha-convex-hull")




## install.packages('gWidgetsRGtk2') first if not installed
install.packages("gWidgetsRGtk2")
library(gWidgetsRGtk2)
options(guiToolkit = "RGtk2")

g = glayout(container = gwindow("alpha-convex hull demo"))
g[1, 1:2, expand = TRUE] = ggraphics(container = g)
g[2, 1] = "alpha"
g[2, 2, expand = TRUE] = gslider(
  from = 0, to = .3, value = .2, by = .01,
  container = g, handler = function(h, ...) {
    par(mar = rep(0, 4), xaxt = "n", yaxt = "n")
    plot(ahull(x, alpha = svalue(h$obj)), pch = 20, ann = FALSE)
  }
)