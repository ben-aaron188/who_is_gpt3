#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 09:13:46 2022

@author: nicolarossberg
"""

import pandas as pd
import openai

openai.api_key = "KEY"


#meta params.
n_runs = 5
max_tokens_meta = 20

# # Creating the list of questions
QL = ["I would be quite bored by a visit to an art gallery.", "I plan ahead and organize things, to avoid scrambling at the last minute.",
      "I rarely hold a grudge, even against people who have badly wronged me.", "I feel reasonably satisfied with myself overall.",
      "I would feel afraid if I had to travel in bad weather conditions.", "I wouldn't use flattery to get a raise or promotion at work, even if I thought it would succeed.",
      "I'm interested in learning about the history and politics of other countries.", "I often push myself very hard when trying to achieve a goal.",
      "People sometimes tell me that I am too critical of others.", "I rarely express my opinions in group meetings.", "I sometimes can't help worrying about little things.",
      "If I knew that I could never get caught, I would be willing to steal a million dollars.", "I would enjoy creating a work of art, such as a novel, a song, or a painting.",
      "When working on something, I don't pay much attention to small details.", "People sometimes tell me that I'm too stubborn.",
      "I prefer jobs that involve active social interaction to those that involve working alone.", "When I suffer from a painful experience, I need someone to make me feel comfortable.",
      "Having a lot of money is not especially important to me.", "I think that paying attention to radical ideas is a waste of time.",
      "I make decisions based on the feeling of the moment rather than on careful thought.", "People think of me as someone who has a quick temper.",
      "On most days, I feel cheerful and optimistic.", "I feel like crying when I see other people crying.",
      "I think that I am entitled to more respect than the average person is.", "If I had the opportunity, I would like to attend a classical music concert.",
      "When working, I sometimes have difficulties due to being disorganized.", "My attitude toward people who have treated me badly is “forgive and forget”.",
      "I feel that I am an unpopular person.", "When it comes to physical danger, I am very fearful.",
      "If I want something from someone, I will laugh at that person's worst jokes.", "I’ve never really enjoyed looking through an encyclopedia.",
      "I do only the minimum amount of work needed to get by.", "I tend to be lenient in judging other people.",
      "In social situations, I’m usually the one who makes the first move.", "I worry a lot less than most people do.",
      "I would never accept a bribe, even if it were very large.", "People have often told me that I have a good imagination.",
      "I always try to be accurate in my work, even at the expense of time.", "I am usually quite flexible in my opinions when people disagree with me.",
      "The first thing that I always do in a new place is to make friends.", "I can handle difficult situations without needing emotional support from anyone else.",
      "I would get a lot of pleasure from owning expensive luxury goods.", "I like people who have unconventional views.",
      "I make a lot of mistakes because I don’t think before I act.", "Most people tend to get angry more quickly than I do.",
      "Most people are more upbeat and dynamic than I generally am.", "I feel strong emotions when someone close to me is going away for a long time.",
      "I want people to know that I am an important person of high status.", "I don’t think of myself as the artistic or creative type.",
      "People often call me a perfectionist.", "Even when people make a lot of mistakes, I rarely say anything negative.",
      "I sometimes feel that I am a worthless person.", "Even in an emergency I wouldn’t feel like panicking.",
      "I wouldn’t pretend to like someone just to get that person to do favors for me.", "I find it boring to discuss philosophy.",
      "I prefer to do whatever comes to mind, rather than stick to a plan.", "When people tell me that I’m wrong, my first reaction is to argue with them.",
      "When I’m in a group of people, I’m often the one who speaks on behalf of the group.", "I remain unemotional even in situations where most people get very sentimental.",
      "I’d be tempted to use counterfeit money, if I were sure I could get away with it."]


# Create list of desired indexes
index_list = ['sex', 'age']
for n in range(1, 61):
    index_list.append('Q' + str(n))

# Create list of temperatures:
#temp_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
temp_list = [0.1]


# Iterating through every temperature
for temp in temp_list:
    # Create dataframe for every temperature:
    tempcurrent = pd.DataFrame()
    # Chaning indices for clarity
    #tempcurrent.index = index_list
    tempcurrent.index = range(n_runs)
    #Create list for sex
    sex_list = []
    #Request n_runs ages
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt='What is your gender?',
        temperature=temp,
        max_tokens=max_tokens_meta,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n = n_runs)
    #Add sexes to list
    for n in range(n_runs):
        sex = str(response['choices'][n].text)
        sex_list.append(sex[2:])
    #Add sexes to Dataframe:
    tempcurrent['sex'] = sex_list
    #Create age list
    age_list = []
    #Request n_run ages
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt='How old are you?',
        temperature=temp,
        max_tokens=max_tokens_meta,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        n=1)
    #Convert age-statements into int and append to list
    for n in range(n_runs):
        age = str(response['choices'][0].text)
        age_list.append([int(s) for s in age.split() if s.isdigit()][0])
    #Add ages to Dataframe:
    tempcurrent['age'] = age_list
    #Set i for enumerating purposes:
    i = 1
    for question in QL:
        # General query
        query = "Below is a statement about you. Please read it and decide how much you agree or disagree with that statement. Write your response using the following scale:/n/n5 = strongly agree/n4 = agree/n3 = neutral/n2 = disagree/n1 = strongly disagree./n/nPlease answer the statement, even if you are not completely sure of your response./n/nStatement:"
        response_prompt = "\nResponse:"
        # Complete query
        fullquestion = query + question + response_prompt
        #Created List for current question
        question_list = []
        # Ask AI for output
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=fullquestion,
            temperature=temp,
            max_tokens=max_tokens_meta,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            n = n_runs)
        #Convert responses to list of responses
        for n in range(n_runs):
            question = str(response['choices'][n].text)
            #Isolate number
            #question_list.append(int(s) for s in question.split() if s.isdigit()[0])
        #Append answers to question to dataframe
        tempcurrent[i] = question
        #Increase i by one (indicating next question for enumeration)
        i += 1
    # Save temperature dataframe as csv
    tempcurrent.columns = index_list
    filename = "./data/hexaco_non_reinforced_temperature_" + str(temp) + '.csv'
    tempcurrent.to_csv(filename)
