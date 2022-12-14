
# Stepik
# Анализ данных в R
# 3.2 Множественная линейная регрессия
# задача 1
test_data <- read.csv("https://stepic.org/media/attachments/course/129/fill_na_test.csv")

fill_na <- function(df){
  df <- cbind(df, df[, 3])
  colnames(df)[4] <- paste(colnames(df)[3], "_full", sep = "")
  lm <- lm(df[, 3] ~ df[, 1] + df[, 2], data = df)
  y_full <- predict(lm, newdata = data.frame(df[, 4]))
  for (i in 1:length(y_full)){
    if (is.na(df[i, 4])){
      df[i, 4] <- y_full[i]
    }
  }
  return(df)
}

fill_na(test_data)

# задача 2
data(mtcars)
df <- mtcars
df <- df[, c(1, 3:6)]

summary(lm(wt ~ mpg + disp + drat + hp, data = df))$adj.r.squared
# R^2 = 0.8374193

summary(lm(wt ~ mpg + disp + hp, data = df))$adj.r.squared
# R^2 = 0.8428136

summary(lm(wt ~ mpg + disp, data = df))$adj.r.squared
# R^2 = 0.8241596
# R^2 became smaller => time to stop
# Answer: model <- lm(wt ~ mpg + disp + hp, data = df)

# задача 3
data(attitude)
df <- attitude

summary(lm(rating ~ complaints*critical, data = df))
# Answer: 0.316

# задача 3
data(mtcars)
df <- mtcars
df$am <- factor(df$am, labels = c('Automatic', 'Manual'))

summary(lm(mpg ~ wt*am, data = df))

library(ggplot2)

ggplot(df, aes(x = wt, y = mpg, col = am))+
  geom_point()+
  geom_smooth(method = "lm")

# задача 4
mtcars$am <- factor(mtcars$am)

ggplot(mtcars, aes(x = wt, y = mpg, col = am))+
  geom_smooth(method = "lm")

# 3.3 Множественная линейная регрессия. Отбор моделей
# exercise 1
data(attitude)

model_full <- lm(rating ~ ., data = attitude)
model_null <- lm(rating ~ 1, data = attitude)

scope <- list(lower = model_null, upper = model_full)

ideal_model <- step(object = model_full, scope = scope, direction = "backward")

# exercise 2
anova <- anova(model_full, ideal_model)

# exercise 3
data(LifeCycleSavings)

# 3.4 Диагностика модели
# exercise 1
my_vector <- c(0.027, 0.079, 0.307, 0.098, 0.021, 0.091, 0.322, 0.211, 0.069, 0.261, 0.241, 0.166, 0.283, 0.041, 0.369, 0.167, 0.001, 0.053, 0.262, 0.033, 0.457, 0.166, 0.344, 0.139, 0.162, 0.152, 0.107, 0.255, 0.037, 0.005, 0.042, 0.220, 0.283, 0.050, 0.194, 0.018, 0.291, 0.037, 0.085, 0.004, 0.265, 0.218, 0.071, 0.213, 0.232, 0.024, 0.049, 0.431, 0.061, 0.523)

shapiro.test(my_vector)
shapiro.test(log(my_vector))
shapiro.test(1 / my_vector)
shapiro.test(sqrt(my_vector))

# exercise 2
beta.coef <- function(df){
  scaled <- scale(as.matrix(df))
  lm <- lm(scaled[, 1] ~ scaled[, 2])
  return(lm[["coefficients"]])
}

# exercise 3
normality.test <- function(df){
  p_value <- c()
  for (name in colnames(df)){
    shapiro <- shapiro.test(df[[name]])
    p_value <- c(p_value, shapiro[["p.value"]])
  }
  names(p_value) <- colnames(df)
  return(p_value)
}

normality.test(mtcars[,1:6])

# 3.5 Диагностика модели. Продолжение
# exercise 1
df <- read.csv("https://stepik.org/media/attachments/lesson/12088/homosc.csv")

install.packages("gvlma")
library(gvlma)

lm <- lm(DV ~ IV, data = df)

summary(gvlma(lm))

# exercise 2
resid.norm <- function(lm){
  fit.residuals <- lm[["residuals"]]
  p_value <- shapiro.test(fit.residuals)$p.value
  if (p_value < 0.05){
    colour = "red"
  } else colour = "green"
  plot <- ggplot(as.data.frame(fit.residuals), aes(x = fit.residuals))+
    geom_histogram(fill = colour)
  return(plot)
}

fit <- lm(mpg ~ disp, mtcars)
resid.norm(fit)

fit <- lm(mpg ~ wt, mtcars)
resid.norm(fit)




