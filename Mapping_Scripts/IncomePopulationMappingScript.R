
rm(list = ls())

library(ggplot2)
library(tidyr)
library(tidyverse)
library(dplyr)
library(caret)

#Reading Data
incomeData<- read.csv("C://Users//prith//OneDrive//Desktop//440//Datasets//Income_Dataset_SCE.csv")

poplData<- read.csv("C://Users//prith//OneDrive//Desktop//440//Datasets//Population_Dataset_SCE.csv")

income16801<- incomeData %>% filter(ZIP == "16801") %>% ggplot(aes(x=Label, y = EstimatePercent)) + 
  geom_bar(stat = "identity", color="blue", fill=rgb(0.1,0.4,0.5,0.7) ) +
  scale_fill_hue(c = 40)+
  labs(
    title = "Income Density in Pennsylvania Zip Code 16801",
    x = "Income Brackets",
    y = "Frequency"
  ) +
  theme_minimal()


income16803<- incomeData %>% filter(ZIP == "16803") %>% ggplot(aes(x=Label, y = EstimatePercent)) + 
  geom_bar(stat = "identity", color="blue", fill=rgb(0.1,0.4,0.5,0.7) ) +
  scale_fill_hue(c = 40)+
  labs(
    title = "Population Density in Pennsylvania Zip Code 16803",
    x = "Income Brackets",
    y = "Frequency"
  ) +
  theme_minimal()

pop16803<- poplData %>% filter(ZIP == "16803")%>% ggplot(aes(x=Age, y = Estimate)) + 
  geom_bar(stat = "identity", color= "blue", fill=rgb(0.1,0.4,0.5,0.7) ) +
  scale_fill_hue(c = 40)+
  labs(
    title = "Population Density in Pennsylvania Zip Code 16803",
    x = "Age Brackets",
    y = "Frequency"
  ) +
  theme_minimal()



popl16801<- poplData %>% filter(ZIP == "16801")%>% ggplot(aes(x=Age, y = Estimate)) + 
  geom_bar(stat = "identity", color= "blue", fill=rgb(0.1,0.4,0.5,0.7) ) +
  scale_fill_hue(c = 40) +
  labs(
    title = "Population Density in Pennsylvania Zip Code 16801",
    x = "Age Brackets",
    y = "Frequency"
  ) +
  theme_minimal()

ggsave("income16801.png", plot = income16801, width = 10, height = 6)
ggsave("income16803.png", plot = income16803, width = 10, height = 6)
ggsave("pop16801.png", plot = pop16801, width = 10, height = 6)
ggsave("pop16803.png", plot = pop16803, width = 10, height = 6)