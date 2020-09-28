library(readr)
Q7_data<-read.csv("C:/Users/HP/Desktop/assignments submission/basic stats level 1/Q7.csv")
View(Q7_data)


#Measures of Central Tendency
#Mean of the data
mean(Q7_data$Points)
mean(Q7_data$Score)
mean(Q7_data$Weigh)

#Median of data
median(Q7_data$Points)
median(Q7_data$Score)
median(Q7_data$Weigh)

#Mode of data
library(NCmisc)
Mode(Q7_data$Points)
Mode(Q7_data$Score)
Mode(Q7_data$Weigh)


#Measures of Variance/Dispersion
#Variance of data
var(Q7_data$Points)
var(Q7_data$Score)
var(Q7_data$Weigh)

#Standard deviation of data
sd(Q7_data$Points)
sd(Q7_data$Score)
sd(Q7_data$Weigh)

#Range of data
range(Q7_data$Points)
range(Q7_data$Score)
range(Q7_data$Weigh)

#Skewness
Q9_data<-read.csv("C:/Users/HP/Desktop/assignments submission/basic stats level 1/Q9_a.csv")
View(Q9_data)
library(moments)
skewness(Q9_data$speed)
skewness(Q9_data$dist)
kurtosis(Q9_data$speed)
kurtosis(Q9_data$dist)

#Probability
cars_data<-read.csv("C:/Users/HP/Desktop/assignments submission/basic stats level 1/Cars.csv")
View(cars_data)
attach(cars_data)
mean(MPG)
sd(MPG)
#	P(MPG>38)
1-pnorm(38,34.42208,9.131445)
# P(MPG<40)
pnorm(40,34.42208,9.131445)
#	P (20<MPG<50)
pnorm(50,34.42208,9.131445)-pnorm(20,34.42208,9.131445)

# To check Normal Distribution
hist(cars_data$MPG)
qqnorm(cars_data$MPG)
qqline(cars_data$MPG)
boxplot(cars_data$MPG)

#Z scores of  90% confidence interval,94% confidence interval, 60% confidence interval 
qnorm(0.95)
qnorm(0.97)
qnorm(0.8)

#t scores of 95% confidence interval, 96% confidence interval, 99% confidence interval for sample size of 25
qt(0.975,24)
qt(0.98,24)
qt(0.995,24)

#Confidence Interval
library(nycflights13)
data(flights)
sum(is.na(flights$dep_delay))
flights1<-na.omit(flights)
library(Rmisc)
CI(flights1$dep_delay,ci=0.95)
