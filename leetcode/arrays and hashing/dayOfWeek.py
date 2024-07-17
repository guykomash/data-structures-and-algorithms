'''3. Day of week that is K days later
Given a day of the week, with an integer K representing numbers, find the day of the week after K days.

Example 1:
Input:
day = “Monday”
K = 3
Output: Thursday

Solution


Day of week that is K days later Leetcode

By description we have as input parameters: string with name of day of week and distance in days till another day of week. We have to find name of the second day of week and return a string with it’s name. To solve this task it would be good to convert given day of week from string to a number of day. Let’s count the days from 0. That is Sunday is 0, Monday is 1 … Saturday is 6.

Then we have a distance between two days of week in days. And we need to find out which day of week is the last day on this distance. Or in other words which number of the day inside of week.

Each week contains 7 days so in order to find a number of day of week we need to convert the distance between of these days from days to weeks. It is easy to calculate the distance in weeks if we have integer number of weeks between the given days.

For example if we have S = “Sun” and K = 7, a day of week in 7 days is “Sun” too.

But if the distance is not divided entirely we may use the remainder after division by 7 it order to find a number of day within a week. For example let’s S = “Tue” and K = 10. Tuesday is 2 day of week. We should add to 10 to 2. 10+2=12 and divide 12 by 7. We get remainder = 5.

Thus day of week of the last day is Friday because 5th day of week is Friday and there are 10 days between Tuesday this week and Friday next week.'''


'''
Given current day as day of the week and an integer K, the task is to find the day of the week after K days.

Example 1:
Input:
day = “Monday”

K = 3

Output: Thursday
Example 2:
Input:
day = “Tuesday”

K = 101

Output: Friday


'''

def dayOfWeek(day, K):
    daysArr = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    try:
        cur = daysArr.index(day)
    except Exception:
        return print('not valid day')
    cur = cur + K 
    cur = cur % 7

    return daysArr[cur]



if __name__ == "__main__":
    print(dayOfWeek('Monday',3))
    print(dayOfWeek('Tuesday',101))