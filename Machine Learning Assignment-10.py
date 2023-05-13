#!/usr/bin/env python
# coding: utf-8

# # Machine Learning Assignment-10

# 1. Define the Bayesian interpretation of probability.
# Ans: Bayesian probability is the study of subjective probabilities or belief in an outcome, compared to the frequentist approach where probabilities are based purely on the past occurrence of the event. A Bayesian Network captures the joint probabilities of the events represented by the model.

# 2. Define probability of a union of two events with equation.
# Ans: The general probability addition rule for the union of two events states that P(A∪B)=P(A)+P(B)−P(A∩B), where A∩B is the intersection of the two sets.

# 3. What is joint probability? What is its formula?
# Ans: Probabilities are combined using multiplication, therefore the joint probability of independent events is calculated as the probability of event A multiplied by the probability of event B. This can be stated formally as follows:
# 
# Joint Probability: P(A and B) = P(A)*P(B)

# 4. What is chain rule of probability?
# Ans: The chain rule, or general product rule, calculates any component of the joint distribution of a set of random variables using only conditional probabilities. This probability theory is used as a foundation for backpropagation and in creating Bayesian networks.

# 5. What is conditional probability means? What is the formula of it?
# Ans: Conditional probability is defined as the likelihood of an event or outcome occurring, based on the occurrence of a previous event or outcome.
# 
# Conditional probability is calculated by multiplying the probability of the preceding event by the updated probability of the succeeding, or conditional, event.
# 
# Let's take a real-life example. Probability of selling a TV on a given normal day may be only 30%. But if we consider that given day is Diwali, then there are much more chances of selling a TV. The conditional Probability of selling a TV on a day given that Day is Diwali might be 70%.

# 6. What are continuous random variables?
# Ans: A continuous random variable X takes all values in a given interval of numbers. ▪ The probability distribution of a continuous random variable is shown by a density curve. ▪ The probability that X is between an interval of numbers is the area under the density curve between the interval endpoints.

# 7. What are Bernoulli distributions? What is the formula of it?
# Ans: A Bernoulli distribution is a discrete probability distribution for a Bernoulli trial — a random experiment that has only two outcomes (usually called a Succes or a Failure).The expected value for a random variable, X.
# 
# For a Bernoulli distribution is: E[X] = p.For example, if p = 0.04, then E[X] = 0.4

# 8. What is binomial distribution? What is the formula?
# Ans: The binomial is a type of distribution that has two possible outcomes (the prefix “bi” means two, or twice).For example, a coin toss has only two possible outcomes: heads or tails and taking a test could have two possible outcomes: pass or fail.
# 
# A Binomial Distribution shows either (S)uccess or (F)ailure.

# 9. What is Poisson distribution? What is the formula?
# Ans: A Poisson distribution is defined as a discrete frequency distribution that gives the probability of the number of independent events that occur in the fixed time.
# 
# In statistics, a Poisson distribution is a probability distribution that is used to show how many times an event is likely to occur over a specified period. ... The Poisson distribution is a discrete function, meaning that the variable can only take specific values in a (potentially infinite) list.

# 10. Define covariance ?
# Ans: Covariance is a measure of how much two random variables vary together. It's similar to variance, but where variance tells you how a single variable varies, co variance tells you how two variables vary together.

# 11. Define correlation ?
# Ans: Correlation explains how one or more variables are related to each other. These variables can be input data features which have been used to forecast our target variable. It's a bi-variate analysis measure which describes the association between different variables.

# 12. Define sampling with replacement. Give example.
# Ans: If you sample with replacement, you would choose one person's name, put that person's name back in the hat, and then choose another name. The possibilities for your two-name sample are: John, John. John, Jack.

# 13. What is sampling without replacement? Give example.
# Ans: In sampling without replacement, each sample unit of the population has only one chance to be selected in the sample. For example, if one draws a simple random sample such that no unit occurs more than one time in the sample, the sample is drawn without replacement.

# 14.What is hypothesis? Give example.
# Ans: A hypothesis (plural hypotheses) is a proposed explanation for a phenomenon. For a hypothesis to be a scientific hypothesis, the scientific method requires that one can test it. ... Even though the words "hypothesis" and "theory" are often used synonymously, a scientific hypothesis is not the same as a scientific theory.
# 
# Examples of hypothesis statements: If garlic repels fleas, then a dog that is given garlic every day will not get fleas. Bacterial growth may be affected by moisture levels in the air. If sugar causes cavities, then people who eat a lot of candy may be more prone to cavities.
