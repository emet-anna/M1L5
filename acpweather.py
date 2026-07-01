'''
Shusho is bored wearing heavy jacket and scarves. She wants to wear something light and soft. But she also doesn't want to get a cold by not wearing weather-appropriate clothes. So she will design a program and check what temperature is suitable for wearing light clothes.

Best of luck.
'''
weather =float(input('What is the temperature today?'))
if weather >= 30:
    print('It is sunny today, do put on light clothes and drink planty of water.')
elif weather >= 20:
    print('The weather is warm. Light clothes are suitable.')
else:
    print('It is cold put on warm clothes!')