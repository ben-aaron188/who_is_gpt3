library(rstatix)
library(car)

hvs_nonreinf <- read.csv('/Users/Marilu/Desktop/NLP/GPT-3/Scripts/data/hvs_plus_values.csv')
hvs <- hvs_nonreinf %>%
  select(temp, Conformity, Tradition, Benevolence, Universalism, Self_Direction, Stimulation,
         Hedonism, Achievement, Power, Security) #%>%
#add_column(id = 1:nrow(hvs_nonreinf), .before = 1)
hvs$temp <- as.factor(hvs$temp)

model <- lm(cbind(Conformity, Tradition, Benevolence, Universalism, Self_Direction, Stimulation,
                  Hedonism, Achievement, Power, Security) ~ temp, hvs)
Manova(model, test.statistic = "Pillai")
#Type II MANOVA Tests: Pillai test statistic
#  Df test stat approx F num Df den    Df      Pr(>F)    
#temp 10   0.78366   7.7207    100   9080 < 2.2e-16 ***

# Group the data by variable
hvs1 <- hvs[-c(1),] 
grouped.data <- hvs1 %>%
  gather(key = "variable", value = "value", Conformity, Tradition, Benevolence, Universalism, Self_Direction, Stimulation,
         Hedonism, Achievement, Power, Security) %>%
  group_by(variable)

# Do Kruskal-Wallis one way anova test
grouped.data %>% kruskal_test(value ~ temp)
# or use aov()
grouped.data %>% anova_test(value ~ temp)

